SELECT
    region,
    product_category,
    SUM(revenue) AS total_revenue,
    SUM(cost) AS total_cost,
    ROUND(
        (SUM(revenue) - SUM(cost)) / SUM(revenue) * 100, 2
    ) AS contribution_margin_percent
FROM sales_data
GROUP BY region, product_category
ORDER BY contribution_margin_percent DESC;


