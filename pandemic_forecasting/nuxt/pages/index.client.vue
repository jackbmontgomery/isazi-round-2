<script>
export default {
    data() {
        return {
            options: {
                animationEnabled: true,
                theme: "light2",
                title: {
                    text: "South Africa COVID-19 Daily Cases"
                },
                axisX: {
                    valueFormatString: "DD MMM",
                    interval: 1,
                    intervalType: "day"
                },
                axisY: {
                    title: "Daily Cases"
                },
                toolTip: {
                    shared: true,
                },
                data: [
                    {
                        // Actual Data Line
                        type: "line",
                        name: "Daily Cases",
                        showInLegend: true,
                        yValueFormatString: "#.##",
                        xValueFormatString: "DD MMM YYYY",
                        dataPoints: [
                            { x: new Date(2020, 0, 1), y: 100 },
                            { x: new Date(2020, 0, 2), y: 66.537003 },
                            { x: new Date(2020, 0, 3), y: 60.4095 },
                            { x: new Date(2020, 0, 4), y: 58.0075 },
                            { x: new Date(2020, 0, 5), y: 65.255501 },
                            { x: new Date(2020, 0, 6), y: 70.789497 },
                        ]
                    },
                    {
                        // Prediction Mean Line
                        type: "line",
                        name: "Projection",
                        showInLegend: true,
                        yValueFormatString: "$#,##0.#",
                        xValueFormatString: "DD MMM YYYY",
                        dataPoints: [
                            { x: new Date(2020, 0, 7), y: 72.352501 },
                            { x: new Date(2020, 0, 8), y: 75.639503 },
                            { x: new Date(2020, 0, 9), y: 78.305 },
                            { x: new Date(2020, 0, 10), y: 80.066002 },
                            { x: new Date(2020, 0, 11), y: 85.844498 },
                            { x: new Date(2020, 0, 12), y: 88.191498 }
                        ]
                    },
                    {
                        // Confidence Interval (Shaded Area)
                        type: "rangeArea",
                        name: "95% Confidence Interval",
                        showInLegend: true,
                        yValueFormatString: "$#,##0.#",
                        xValueFormatString: "DD MMM YYYY",
                        toolTipContent: "<b><span style='\"'color: {color};'\"'>{x}</span></b><br/>High: {y[0]}<br/>Low: {y[1]}",
                        dataPoints: [
                            { x: new Date(2020, 0, 7), y: [70.709, 79.352501] },
                            { x: new Date(2020, 0, 8), y: [73.2015, 82.639503] },
                            { x: new Date(2020, 0, 9), y: [70.107498, 86.305] },
                            { x: new Date(2020, 0, 10), y: [71.661499, 84.066002] },
                            { x: new Date(2020, 0, 11), y: [80.605499, 90.844498] },
                            { x: new Date(2020, 0, 12), y: [84.699997, 92.191498] }
                        ]
                    }
                ]
            },
            styleOptions: {
                width: "100%",
                height: "360px"
            }
        }
    }
}
</script>

<template>
    <CanvasJSChart :options="options" :style="styleOptions" />
</template>
