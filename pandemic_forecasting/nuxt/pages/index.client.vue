<template>
    <CanvasJSChart :options="options" :style="styleOptions" />
</template>

<script setup>
import { ref } from 'vue';

const response = await fetch("http://localhost:8000/");
const data = await response.json();

// Transform the API response into the format required by the chart
const dataPoints = Object.keys(data).map(date => ({
    x: new Date(date),
    y: data[date].cases
}));

// Define reactive references for chart options and style
const options = ref({
    animationEnabled: true,
    theme: "light2",
    title: {
        text: "South Africa COVID-19 Daily Cases"
    },
    axisX: {
        valueFormatString: "MMM YY",
        interval: 3,
        intervalType: "month"
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
            dataPoints: dataPoints  // Initialize as an empty array
        }
    ]
});

const styleOptions = {
    width: "100%",
    height: "360px"
};

</script>
