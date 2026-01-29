SELECT
    customer_id,
    COUNT(order_id) AS total_orders,
    SUM(revenue) AS lifetime_revenue,
    ROUND(AVG(revenue), 2) AS avg_order_value
FROM sales_data
GROUP BY customer_id;
