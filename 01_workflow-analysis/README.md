# 🧪 Workflow Analysis (In Progress)

## Overview
This module simulates and analyzes microbiology and molecular laboratory workflows across the full **order-to-result lifecycle**, modeled after Epic Beaker-aligned operations.

The project focuses on identifying operational inefficiencies, turnaround time (TAT) variability, and workflow bottlenecks using synthetic but clinically realistic data.

---

## Objectives
- Model end-to-end laboratory workflows (Order → Collection → Receipt → Result)
- Quantify turnaround time (TAT) across workflow stages
- Identify bottlenecks in pre-analytic, transport, and analytic phases
- Simulate event-driven delays affecting STAT and routine testing
- Establish a foundation for Clarity-style SQL analysis

---

## Key Focus Areas

### Turnaround Time (TAT)
Total and stage-level performance across:
- Collection
- Transport
- Laboratory processing

### Workflow Bottlenecks
Identification of delay drivers across:
- Patient locations (ICU, ED, MedSurg, Primary Care, FSED)
- Testing priorities (STAT vs Routine)

### Event-Driven Delays
Simulation of real-world constraints such as:
- Courier schedules (outreach vs inpatient)
- Specimen transport variability
- STAT prioritization breakdowns

### Operational Segmentation
Analysis of workflow performance by:
- Patient location
- Test priority
- Instrument/platform

---

## Tools & Technologies
- **Python** — Synthetic data generation and workflow modeling  
- **SQL (Planned)** — Clarity-style querying and operational investigation  
- **Power BI (Planned)** — Visualization and dashboarding  

---

## Repository Structure

- microbiology_workflow_analysis_generator.py  
  Synthetic data generation (Beaker-aligned workflow simulation)

- microbiology-workflow-analysis.ipynb  
  Workflow analysis, TAT metrics, and bottleneck identification
  
---

## Status
🚧 In Progress  

- [x] Workflow simulation and data generation  
- [x] Core TAT and delay analysis  
- [ ] SQL-based (Clarity-style) investigation layer  
- [ ] Visualization and dashboard development  

---

## Future Enhancements
- Implementation of SQL-based analysis layer to simulate Epic Clarity reporting
- Development of Power BI dashboards for operational monitoring
- Expansion into cross-departmental workflows (Chemistry, Hematology, Blood Bank)
