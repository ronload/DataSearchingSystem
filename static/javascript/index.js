// static/javascript/index.js

document.addEventListener("DOMContentLoaded", async function () {
    const chartRenderer = new ChartRenderer();
    // index
    await chartRenderer.render(
        "month-order-chart", "ORDERS IN THE PAST 30 DAYS",
        "line", "/get_month_order_data"
    );
    await chartRenderer.render(
        "month-sale-chart", "SALES IN THE PAST 30 DAYS", 
        "line", "/get_month_sale_data"
    );
    await chartRenderer.render(
        "category-sale-chart", "CATEGORY SALES", 
        "pie", "/get_category_sale_data"
    );
});