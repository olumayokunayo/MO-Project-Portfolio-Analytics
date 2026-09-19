# PMO Project Portfolio Analytics

## Overview

A PMO analytics project designed to analyse project delivery, financial performance, risks, issues, and resource utilisation across a simulated project portfolio.

The project demonstrates an end-to-end workflow using **Python, MySQL, SQL, and Power BI** to transform project data into actionable PMO insights.

## Tools

- Python — Synthetic data generation
- MySQL — Data storage and analysis
- SQL — Portfolio, risk, schedule and resource analysis
- Power BI — Interactive dashboard
- Git/GitHub — Version control

## Portfolio

- 120 projects
- 10 project managers
- 316 risks
- 308 issues
- 851 resource assignments

## Key Metrics

| Metric | Result |
| Total Budget | £118.07M |
| Total Actual Cost | £96.40M |
| Projects Over Budget | 38 |
| High/Critical Issues | 94 |
| Resource Utilisation | 97.49% |
| Over-Allocated Projects | 44 |

## Power BI Dashboard

The dashboard contains four pages:

1. Executive Overview — Portfolio KPIs, project status and financial overview
2. Financial & Delivery — Cost variance, budget performance and schedule issues
3. Risk & Issues Analysis — Risk exposure and issue severity
4. Resource & Project Manager Performance — Resource utilisation and PM portfolio performance

## SQL Analysis

The project demonstrates:

- Joins and aggregations
- CTEs
- Subqueries
- `CASE` statements
- Window functions
- `RANK()` and `ROW_NUMBER()`
- Conditional aggregation
- Date analysis
- Data quality validation

## Key Insights

- 38 projects are currently over budget.
- 38 projects are classified as Delayed, At Risk or On Hold.
- 94 issues are High or Critical severity.
- 44 projects have resource utilisation above 100%.
- Portfolio performance varies across project managers and departments.

## Recommendations

- Strengthen schedule monitoring and recovery planning.
- Prioritise high-risk projects and critical issues.
- Investigate project-level cost overruns.
- Review resource over-allocation.
- Use cost, schedule, risk, issues and resources together for PMO governance.

## Project Structure

```
PMO-Project-Portfolio-Analytics/
├── data/
├── data_generation/
├── sql/
├── insights/
├── powerbi/
└── README.md
