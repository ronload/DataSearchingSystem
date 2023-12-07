document.addEventListener("DOMContentLoaded", function () {
    fetch("/get_month_order_data")
        .then(response => response.json())
        .then(data => { renderLineChart(
            containerID="month-order-chart",
            title="ORDERS IN THE PAST 30 DAYS", 
            xName=data.xName,
            renderData=data.renderData
        );
    })
    .catch(error => console.error("Error fetching data:", error));
    fetch("/get_category_sale_data")
        .then(response => response.json())
        .then(data => { renderPieChart(
            containerID="category-sale-chart",
            title="CATEGORY SALES", 
            renderData=data
        );
    })
    .catch(error => console.error("Error fetching data:", error));

    fetch("/get_month_sale_data")
        .then(response => response.json())
        .then(data => { renderLineChart(
            containerID="month-sale-chart",
            title="SALES IN THE PAST 30 DAYS", 
            xName=data.xName,
            renderData=data.renderData
        );
    })
    .catch(error => console.error("Error fetching data:", error));
});

function renderLineChart(containerID, title, xName, renderData) {
    var chart = echarts.init(document.getElementById(containerID));
    option = {
        title: {
            text: title,
            left: 'center'
        },
        xAxis: {
            type: 'category',
            data: xName
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                data: renderData,
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
    chart.setOption(option)
}

function renderPieChart(containerID, title, renderData) {
    var chart = echarts.init(document.getElementById(containerID))
    var blueGradient = [
        'rgba(42, 54, 181, 0.8)', 'rgba(63, 85, 239, 0.8)', 'rgba(78, 106, 254, 0.8)',
        'rgba(92, 117, 255, 0.8)', 'rgba(106, 129, 255, 0.8)', 'rgba(121, 140, 255, 0.8)',
        'rgba(135, 152, 255, 0.8)', 'rgba(149, 164, 255, 0.8)', 'rgba(164, 175, 255, 0.8)',
        'rgba(178, 187, 255, 0.8)', 'rgba(192, 198, 255, 0.8)', 'rgba(207, 210, 255, 0.8)',
        'rgba(221, 222, 255, 0.8)', 'rgba(235, 234, 255, 0.8)', 'rgba(249, 245, 255, 0.8)'
    ];
    

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
            data: renderData,
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            },
            color: blueGradient,
        }]
    };
    chart.setOption(option);
}
