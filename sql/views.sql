-- Executive Summary View
CREATE VIEW executive_summary AS
SELECT
    (SELECT SUM(mrr)
     FROM subscriptions
     WHERE end_date IS NULL OR end_date > CURRENT_DATE) AS current_mrr,

    (SELECT COUNT(*) FROM users WHERE status='active') AS active_users,

    (SELECT COUNT(*) FILTER (WHERE status='churned')::float /
            COUNT(*) FROM users) AS churn_rate,

    (SELECT SUM(acquisition_cost)::float /
            COUNT(*) FROM customer_acquisition) AS cac,

    (SELECT AVG(mrr) * 12 FROM subscriptions) AS estimated_ltv;


-- Monthly MRR View
CREATE VIEW monthly_mrr AS
SELECT
    DATE_TRUNC('month', start_date) AS month,
    SUM(mrr) AS mrr
FROM subscriptions
GROUP BY month
ORDER BY month;


-- Revenue by Plan View
CREATE VIEW revenue_by_plan AS
SELECT
    plan_type,
    SUM(mrr) AS total_revenue
FROM subscriptions
GROUP BY plan_type;
