<template>
    <div>
        <line-chart :chart-data="chartData" :options="chartOptions"></line-chart>
    </div>
</template>

<script>
import { Line } from 'vue-chartjs/legacy';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement);

export default {
    components: {
        LineChart: Line
    },
    props: {
        dates: {
            type: Array,
            required: true
        },
        cases: {
            type: Array,
            required: true
        }
    },
    computed: {
        chartData() {
            return {
                labels: this.dates,
                datasets: [
                    {
                        label: 'Daily Cases',
                        backgroundColor: '#f87979',
                        borderColor: '#f87979',
                        data: this.cases,
                        fill: false,
                    }
                ]
            };
        },
        chartOptions() {
            return {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        type: 'time',
                        time: {
                            unit: 'day',
                            tooltipFormat: 'MMM DD',
                            displayFormats: {
                                day: 'MMM DD'
                            }
                        },
                        title: {
                            display: true,
                            text: 'Date'
                        }
                    },
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Cases'
                        }
                    }
                }
            };
        }
    }
};
</script>

<style scoped>
.chart-container {
    position: relative;
    margin: auto;
    height: 60vh;
    width: 80vw;
}
</style>
