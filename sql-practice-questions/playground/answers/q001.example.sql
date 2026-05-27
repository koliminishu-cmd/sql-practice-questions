SELECT
  c.customer_id,
  c.customer_name,
  SUM(o.amount) AS total_revenue
FROM customers c
JOIN orders o
  ON c.customer_id = o.customer_id
WHERE o.status = 'completed'
GROUP BY c.customer_id, c.customer_name
ORDER BY c.customer_id;

