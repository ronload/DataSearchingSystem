// static/javascript/ChartRenderer.js

class ChartRenderer {
    async render(containerID, title, type, route) {
        const response = await fetch(route);
        const response_data = await response.json();
        const chart = echarts.init(document.getElementById(containerID));
        let option;
        if(type == "line") {
            option = {
                title: {
                    text: title,
                    left: 'center'
                },
                tooltip: {
                    trigger: 'axis'
                },
                xAxis: {
                    type: 'category',
                    data: response_data.xName
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        data: response_data.renderData,
                        symbol: 'none',
                        areaStyle: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                {
                                    offset: 0,
                                    color: 'rgba(58,77,233,0.8)'
                                },
                                {
                                    offset: 1,
                                    color: 'rgba(58,77,233,0.3)'
                                }
                            ])
                        },
                        type: 'line'
                    }
                ]
            };
        }
        if(type == "pie") {
            option = {
                title: {
                    text: title,
                    left: 'center'
                },
                tooltip: {
                    trigger: 'item'
                },
                series: [{
                    name: 'Access From',
                    type: 'pie',
                    radius: '60%',
                    data: response_data,
                    itemStyle: {
                        emphasis: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    },
                    color: [
                        'rgba(42, 54, 181, 0.8)', 'rgba(63, 85, 239, 0.8)', 'rgba(78, 106, 254, 0.8)',
                        'rgba(92, 117, 255, 0.8)', 'rgba(106, 129, 255, 0.8)', 'rgba(121, 140, 255, 0.8)',
                        'rgba(135, 152, 255, 0.8)', 'rgba(149, 164, 255, 0.8)', 'rgba(164, 175, 255, 0.8)',
                        'rgba(178, 187, 255, 0.8)', 'rgba(192, 198, 255, 0.8)', 'rgba(207, 210, 255, 0.8)',
                        'rgba(221, 222, 255, 0.8)', 'rgba(235, 234, 255, 0.8)', 'rgba(249, 245, 255, 0.8)'
                    ],
                }]
            };
        }
        chart.setOption(option);
    }
}