# TaskFlow SaaS Analytics Dashboard

An end-to-end analytics project simulating a B2B SaaS company.

## Overview
Built a PostgreSQL-backed analytics pipeline to calculate key SaaS business metrics and visualized them in Tableau Public.

## Tech Stack
- PostgreSQL 18
- SQL (Views, Aggregations, Date Truncation)
- Tableau Public
- Python (Data Seeding)

## Key Metrics
- Current MRR: ₹23,128
- Active Users: 375
- Churn Rate: 16.67%
- CAC: ₹102.62
- Estimated LTV: ₹1,273.38

## SQL Logic
Created analytical views:
- `executive_summary`
- `monthly_mrr`
- `revenue_by_plan`

Used:
- Aggregate functions
- Subqueries
- DATE_TRUNC
- FILTER clauses

## 📂 Project Structure
taskflow-analytics/
- 'sql/views.sql'
- 'data_exports'
- 'seed_data.py'
- 'README.md'

## Dashboard
Built an executive-level dashboard with:
- KPI cards
- MRR trend analysis
- Revenue breakdown by plan
