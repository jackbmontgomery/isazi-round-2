<template>
    <div class="container">
        <CanvasJSChart :options="options" :style="styleOptions" class="chart" />
        <UTable :columns="columns" :rows="tableData" class="table" style="color: black;" />
        <div class="button-container">
            <button @click="downloadCsv" class="download-button">Download Projection CSV</button>
        </div>
    </div>
</template>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 90%;
    margin: 0 auto;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background-color: white;
}

.chart {
    width: 100%;
    margin-bottom: 20px;
}

.button-container {
    margin-bottom: 20px;
}

.download-button {
    background-color: #007BFF;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
    margin: 10px;
}

.download-button:hover {
    background-color: #0056b3;
}

.table {
    width: 100%;
    border-radius: 4px;
}
</style>

<script setup>
import { ref } from 'vue';

// Get thedate two years ago from the current date
const currentDate = new Date();
const twoYearAgo = new Date(currentDate.setFullYear(currentDate.getFullYear() - 2));
const twoYearsAgoFormatted = twoYearAgo.toISOString().split('T')[0];

// Store the API call date to display in the UI
const apiCallDate = ref(twoYearsAgoFormatted);


// Call local FastAPI server to fetch the data
const response = await fetch(`http://localhost:8000/?runDate=${twoYearsAgoFormatted}`);
const data = await response.json();

// Historical data
const casesData = data.data;
const cases = Object.keys(casesData).map(date => ({
    x: new Date(date),
    y: casesData[date].cases
}));

// Forecasted data
const forecastData = data.forecast;
const projectedCases = Object.keys(forecastData).map(date => ({
    x: new Date(date),
    y: forecastData[date].predicted_mean
}));

// Adjust the projected cases to start from the last actual data point for UI continuity
const lastCaseDataPoint = cases[cases.length - 1];
const adjustedProjectedCases = [
    { x: lastCaseDataPoint.x, y: lastCaseDataPoint.y },  // Add the last actual case data point
    ...projectedCases  // Followed by the forecasted data
];

// Define the zoom range to focus on the last 3 months of data
const viewStart = twoYearAgo.setMonth(twoYearAgo.getMonth() - 3);

// Chart options
const options = ref({
    animationEnabled: true,
    theme: "light2",
    title: {
        text: `South Africa COVID-19 Daily Cases - ${apiCallDate.value}`
    },
    exportEnabled: true,
    axisX: {
        valueFormatString: "MMM YY",
        interval: 1,
        intervalType: "month",
        viewportMinimum: viewStart
    },
    axisY: {
        title: "Daily Cases"
    },
    toolTip: {
        shared: true,
    },
    data: [
        {
            type: "line",
            name: "Daily Cases",
            showInLegend: true,
            yValueFormatString: "#.##",
            xValueFormatString: "DD MMM YYYY",
            dataPoints: cases
        },
        {
            type: "line",
            name: "Projected Daily Cases",
            showInLegend: true,
            yValueFormatString: "#.##",
            xValueFormatString: "DD MMM YYYY",
            dataPoints: adjustedProjectedCases,
        }
    ]
});

// Chart style options
const styleOptions = {
    width: "100%",
    height: "300px"
};

// Setting the table headers
const columns = [{
    key: 'x',
    label: 'Date',
    class: 'bg-gray-600'
}, {
    key: 'y',
    label: 'Projected Cases',
    class: 'bg-gray-600'
}];


// Setting the table data
const tableData = Object.keys(forecastData).map(date => ({
    x: new Date(date).toISOString().split('T')[0], // Format: YYYY-MM-DD
    y: forecastData[date].predicted_mean.toFixed(2), // Rounded to 2 decimal places
}));

// Function to download the projected cases as a CSV file
function downloadCsv() {
    const csvData = generateCsv(projectedCases);
    const blob = new Blob([csvData], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');

    const filename = `7_Day_Projection_${twoYearsAgoFormatted}.csv`;

    link.setAttribute('href', url);
    link.setAttribute('download', filename);
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Function to generate CSV data from the projected cases
function generateCsv(data) {
    const header = 'date,new_cases\n';
    const rows = data
        .map(item => `${item.x.toISOString().split('T')[0]},${item.y}`)
        .join('\n');
    return header + rows;
}


function exportChartAsImage() {
    var chart = new Chart("chartContainer", options.value);
    chart.exportChart({ format: "jpg" });
}
</script>