// static/javascript/customer.js

document.addEventListener("DOMContentLoaded", async function() {
    const chartRenderer = new ChartRenderer();
    await chartRenderer.render(
        "customer-number-chart", "CUSTOMERS IN THE PAST 30 DAYS",
        "line", "/get_customer_number_data"
    );
    await chartRenderer.render(
        "customer-rank-chart", "CUSTOMER RANK",
        "pie", "/get_customer_rank_data"
    );
});