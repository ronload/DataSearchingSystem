// index.js

document.addEventListener("DOMContentLoaded", function () {
    const chartRenderer = new ChartRenderer();
    // index
    chartRenderer.renderByFetching(
        "month-order-chart", "ORDERS IN THE PAST 30 DAYS",
        "line", "/get_month_order_data"
    )
    chartRenderer.renderByFetching(
        "category-sale-chart", "CATEGORY SALES", 
        "pie", "/get_category_sale_data"
    )
    chartRenderer.renderByFetching(
        "month-sale-chart", "SALES IN THE PAST 30 DAYS", 
        "line", "/get_month_sale_data"
    )

    // customer
    chartRenderer.renderByFetching(
        "customer-number-chart", "CUSTOMERS IN THE PAST 30 DAYS",
        "line", "/get_customer_number_data"
    )
    chartRenderer.renderByFetching(
        "customer-rank-chart", "CUSTOMER RANK",
        "pie", "/get_customer_rank_data"
    )

    // product
    chartRenderer.renderByFetching(
        "product-rank-chart", "PRODUCT RANK",
        renderType="pie", route="/get_product_rank_data"
    )
    chartRenderer.renderByFetching(
        "category-rank-chart", "CATEGORY RANK",
        renderType="pie", route="/get_category_rank_data"
    )
});