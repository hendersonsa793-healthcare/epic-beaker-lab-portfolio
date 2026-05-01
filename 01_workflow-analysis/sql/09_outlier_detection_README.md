## 09 – Outlier Detection

### Objective
To identify microbiology orders with significantly elevated turnaround times compared to overall workflow performance.

### Approach
This query calculates the average and standard deviation of total turnaround time across all orders. Orders exceeding two standard deviations above the mean are classified as outliers.

### Analyst Interpretation
Outliers represent extreme workflow delays that may not be visible in aggregate metrics. These cases are often associated with:
- workflow breakdowns
- specimen handling issues
- instrument or interface disruptions
- atypical clinical scenarios

### Operational Relevance
For Epic Beaker, LIS, and clinical systems teams, outlier detection supports targeted investigation of high-impact cases. This is especially useful during go-live stabilization and ongoing performance monitoring, where identifying and resolving extreme delays can significantly improve overall system reliability.
