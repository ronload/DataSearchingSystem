document.addEventListener("DOMContentLoaded", function () {
    fetch("/get_month_order_data")
        .then(response => response.json())
        .then(data => { renderLineChart(
            "month-order-chart",
            "month-order-chart", 
            data.xName,
            data.renderData
        );
    })
    .catch(error => console.error("Error fetching data:", error));

    // renderPieChart(
    //     containerID = "category-sale-chart",
    //     title = "category",
    //     renderData = [
    //         { value: 1048, name: 'Search Engine' },
    //         { value: 735, name: 'Direct' },
    //         { value: 580, name: 'Email' },
    //         { value: 484, name: 'Union Ads' },
    //         { value: 300, name: 'Video Ads' }
    //     ]
    // )
    fetch("/get_month_sale_data")
        .then(response => response.json())
        .then(data => { renderLineChart(
            "month-sale-chart",
            "month-sale-chart", 
            data.xName,
            data.renderData
        );
    })
    .catch(error => console.error("Error fetching data:", error));
});

function renderLineChart(containerID, title, xName, renderData) {
    console.log("containerID:", containerID);
    console.log("title:", title);
    console.log("xName:", xName);
    console.log("renderData:", renderData);
    var element = document.getElementById(containerID)
    var chart = echarts.init(element);
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
    chart.setOption(option);
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