SELECT
    region,
    product_name,
    SUM(revenue) AS revenue,
    SUM(cost) AS cost,
    SUM(revenue) - SUM(cost) AS profit
FROM sales_data
GROUP BY region, product_name
HAVING SUM(revenue) - SUM(cost) < 0;
