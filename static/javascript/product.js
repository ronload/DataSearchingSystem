// static/javascript/product.js

document.addEventListener("DOMContentLoaded", async function() {
    const chartRenderer = new ChartRenderer();
    await chartRenderer.render(
        "product-rank-chart", "PRODUCT RANK",
        renderType="pie", route="/get_product_rank_data"
    );
    await chartRenderer.render(
        "category-rank-chart", "CATEGORY RANK",
        renderType="pie", route="/get_category_rank_data"
    );
});