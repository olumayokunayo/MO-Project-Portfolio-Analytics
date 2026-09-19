# PMO Project Portfolio Analytics

## Portfolio Profiling

Initial SQL profiling was performed to understand the portfolio's project status, financial performance, risk exposure, issues and resource utilisation.

The portfolio contains 120 projects across Finance, Procurement, Operations, IT, HR and Marketing.

## Portfolio Summary

| Metric | Result |
| Total Projects | 120 |
| Total Budget | £118.07M |
| Actual Cost | £96.40M |
| Cost Variance | -£21.67M |
| Total Risks | 316 |
| Total Issues | 308 |
| Resource Assignments | 851 |
| Resource Utilisation | 97.49% |

## Key Findings

### Project Delivery

- 44 projects are In Progress
- 38 are Completed
- 21 are Delayed
- 10 are At Risk
- 7 are On Hold
- 38 projects (31.7%) are Delayed, At Risk or On Hold.

### Financial Performance

- Portfolio budget: £118.07M
- Actual cost recorded: £96.40M
- Portfolio variance: -£21.67M
- 38 projects are over budget
- The largest over-budget project is PRJ022, with a variance of approximately £380.7K.

> The overall negative variance should not automatically be treated as savings because many projects are still in progress.

### Risk Exposure

- 316 risks were identified.
- Schedule is the largest risk category with 58 risks.
- Operational risks have the highest average risk score at 10.83.

### Issue Severity

| Severity | Issues |
| Medium | 122 |
| Low | 92 |
| High | 79 |
| Critical | 15 |

94 of 308 issues (30.5%) are High or Critical, indicating significant issue-management exposure.

### Resource Utilisation

- 851 resource assignments
- 464,311 allocated hours
- 452,676 actual hours
- Overall utilisation: 97.49%

Several projects exceeded 100% utilisation, including:

- PRJ011 — 115.36%
- PRJ078 — 113.16%
- PRJ084 — 110.66%
- PRJ025 — 110.00%
- PRJ089 — 109.26%

This may indicate resource pressure or additional work beyond initial allocations.

### Schedule Performance

There are 21 delayed projects.

The longest delays include:

| Project | Delay |
| PRJ110 | 151 days |
| PRJ035 | 150 days |
| PRJ091 | 143 days |
| PRJ039 | 140 days |
| PRJ114 | 140 days |

## PMO Recommendations

1. Prioritise the 38 Delayed, At Risk and On Hold projects for enhanced monitoring.
2. Investigate the 38 over-budget projects, particularly completed projects.
3. Strengthen schedule-risk monitoring.
4. Review high-scoring operational risks and mitigation plans.
5. Monitor projects with resource utilisation above 100%.
6. Escalate and track High and Critical issues.
7. Separate completed and ongoing projects when evaluating financial performance.

## Next Analysis Stage

The next stage will move from profiling to advanced  analysis using:

- CTEs
- Subqueries
- Window Functions
- `RANK()`
- `ROW_NUMBER()`
- `COUNT(DISTINCT)`
- Project performance analysis
- Risk analysis
- Resource analysis
- Schedule analysis