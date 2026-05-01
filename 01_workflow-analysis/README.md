## 🧪 Microbiology Workflow Analysis (In Progress)

---

### Overview

This project simulates and analyzes microbiology and molecular laboratory workflows across the full **order-to-result lifecycle**, aligned with real-world **Epic Beaker–style laboratory operations**.

Using synthetic but clinically realistic data, the project models how workflow structure, transport dynamics, and operational constraints impact turnaround time (TAT). The goal is to identify bottlenecks and workflow inefficiencies using a structured, analyst-driven approach.

---

### Objectives

- Model end-to-end laboratory workflows (**Order → Collection → Receipt → Result**)  
- Quantify turnaround time (TAT) at both **total and stage levels**  
- Identify bottlenecks across:
  - pre-analytic  
  - transport  
  - analytic phases  
- Simulate event-driven delays affecting **STAT and routine workflows**  
- Develop a **Clarity-style SQL analysis layer** for workflow investigation  

---

### Key Focus Areas

#### Turnaround Time (TAT)

Measurement of workflow performance across:
- collection  
- transport  
- laboratory processing  
- result posting  

---

#### Workflow Bottlenecks

Identification of delay drivers across:
- patient locations (ICU, ED, Med Surg, Primary Care, FSED)  
- testing priorities (STAT vs Routine)  
- workflow stages  

---

#### Event-Driven Delays

Simulation of real-world operational constraints, including:
- courier scheduling differences (outreach vs inpatient)  
- specimen transport variability  
- STAT prioritization breakdowns  

---

#### Operational Segmentation

Analysis of workflow performance by:
- patient location  
- test priority  
- instrument/platform  

---

### 🧠 SQL Analysis Layer (Clarity-Style)

A structured SQL analysis layer was developed to simulate **Epic Clarity–style reporting and workflow investigation**.

The SQL analysis includes:
- dataset validation and schema review  
- TAT segmentation by test, location, and priority  
- expected vs actual TAT modeling  
- delay severity classification  
- workflow bottleneck identification  
- delay flag analysis  
- STAT vs routine performance evaluation  
- outlier detection for extreme delays  

---

### Key Finding

> **Med Surg wound cultures demonstrated the highest total turnaround time, primarily driven by laboratory processing time.**

While elevated lab processing time is expected for culture-based workflows, the magnitude of delay suggests potential operational factors such as batching, bench prioritization, or staffing constraints.

---

### Tools & Technologies

- **Python (pandas)** — synthetic data generation and workflow simulation  
- **SQL (PostgreSQL / DBeaver)** — Clarity-style querying and workflow analysis  
- **Power BI (planned)** — visualization and operational dashboards  

---

### Repository Structure

```text
microbiology_workflow_analysis_generator.py
Synthetic data generation aligned to laboratory workflow behavior

microbiology-workflow-analysis.ipynb
Workflow analysis and TAT exploration

/sql
Clarity-style SQL queries (01–09) for workflow investigation
```

### Status

🚧 **In Progress**

- [x] Workflow simulation and data generation  
- [x] Core TAT and delay analysis  
- [x] SQL-based (Clarity-style) investigation layer  
- [ ] Visualization and dashboard development  

---

### Future Enhancements

- Development of Power BI dashboards for operational monitoring  

- Expansion into additional departments:
  - Chemistry  
  - Hematology  
  - Blood Bank  

- Integration of interface-level analysis:
  - Instrument → Middleware → LIS → Reporting  
