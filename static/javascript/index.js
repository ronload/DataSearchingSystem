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
            title="CATEGORY", 
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
                type: 'line'
            }
        ]
    };
    chart.setOption(option)
}

function renderPieChart(containerID, title, renderData) {
    var chart = echarts.init(document.getElementById(containerID))
    option = {
        title: {
            text: title,
            left: 'center'
        },
        tooltip: {
            trigger: 'item'
        },
        legend: {
            orient: 'vertical',
            left: 'left'
        },
        series: [{
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: renderData,
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }]
    };
    chart.setOption(option)
}