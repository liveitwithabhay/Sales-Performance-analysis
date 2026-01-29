WITH yearly_revenue AS (
    SELECT
        EXTRACT(YEAR FROM order_date) AS year,
        SUM(revenue) AS total_revenue
    FROM sales_data
    GROUP BY year
),
yoy_calc AS (
    SELECT
        year,
        total_revenue,
        LAG(total_revenue) OVER (ORDER BY year) AS prev_year_revenue
    FROM yearly_revenue
)
SELECT
    year,
    total_revenue,
    ROUND(
        ((total_revenue - prev_year_revenue) / prev_year_revenue) * 100, 2
    ) AS yoy_growth_percentage
FROM yoy_calc;
