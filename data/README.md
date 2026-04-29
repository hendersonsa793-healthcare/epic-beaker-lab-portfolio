# Microbiology Workflow Analysis Dataset

## Overview
This dataset simulates a clinical laboratory workflow aligned with Epic Beaker environments, modeling the order-to-result lifecycle for microbiology and molecular diagnostics.

## Workflow Modeled
- Order → Collection
- Collection → Receipt
- Receipt → Instrument Result
- Instrument Result → Final Result

## Key Features
- Turnaround time (TAT) segmented across workflow stages
- Location-based variability (ED, ICU, FSED, Primary Care)
- Priority-based workflows (STAT vs Routine)
- Event flags for workflow bottlenecks
- Delay reason classification for root cause analysis

## Example Use Cases
- Identifying workflow bottlenecks
- Evaluating STAT order performance
- Analyzing transport delays across locations
- Supporting lab operations optimization initiatives

## Notes
- Dataset is synthetic but designed to reflect realistic laboratory workflows
- Intended for SQL-based analysis and clinical systems portfolio projects
