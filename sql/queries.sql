-- MLApp: Analytical queries

-- Query 1: Total revenue per customer
SELECT
    c.customer_id,
    c.customer_name,
    SUM(t.amount) AS total_spend,
    COUNT(t.transaction_id) AS transaction_count
FROM customers c
LEFT JOIN transactions t
    ON c.customer_id = t.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spend DESC;


-- Query 2: Top selling products
SELECT
    p.product_id,
    p.product_name,
    p.category,
    COUNT(t.transaction_id) AS units_sold,
    SUM(t.amount) AS revenue
FROM products p
JOIN transactions t
    ON p.product_id = t.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY revenue DESC
LIMIT 10;


-- Query 3: Monthly revenue trend
SELECT
    DATE_TRUNC('month', transaction_date) AS month,
    SUM(amount) AS monthly_revenue,
    COUNT(*) AS transaction_count
FROM transactions
GROUP BY DATE_TRUNC('month', transaction_date)
ORDER BY month;
