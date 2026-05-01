## 04 – Expected vs Actual TAT

### Objective
To compare actual turnaround time against modeled expected turnaround time by test, location, and priority.

### Approach
This query builds on the expected TAT model and calculates the average difference between actual and expected TAT. The result identifies where workflows are exceeding expected performance targets.

### Key Metrics
- **avg_actual_tat_hours**: observed average turnaround time
- **avg_expected_tat_hours**: modeled expected turnaround time
- **avg_tat_delta_hours**: difference between actual and expected TAT

### Analyst Interpretation
A positive TAT delta indicates that actual turnaround time exceeded the expected target. This helps distinguish normal long-running workflows from workflows that may require operational review.

### Operational Relevance
For Epic Beaker, LIS, or Clarity-style reporting, expected-vs-actual analysis supports targeted performance review, escalation, and workflow optimization.
