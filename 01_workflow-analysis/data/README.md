# 📊 Microbiology Workflow Analysis Dataset

## Overview

This dataset simulates microbiology and molecular laboratory workflows across the full **order-to-result lifecycle**, aligned with real-world **Epic Beaker–style laboratory operations**.

The dataset is synthetically generated but designed to reflect realistic clinical laboratory behavior, including workflow timing, operational variability, and event-driven delays.

It is used to support workflow analysis, turnaround time (TAT) investigation, and Clarity-style SQL reporting.

---

## Dataset Purpose

The dataset enables analysis of:

- End-to-end laboratory workflow performance  
- Turnaround time (TAT) across workflow stages  
- Bottlenecks in pre-analytic, transport, and analytic processes  
- Differences in workflow behavior by location, priority, and test type  
- Event-driven delays affecting STAT and routine orders  

---

## Workflow Model

Each record represents a laboratory order progressing through:

Time intervals are captured at each stage to allow detailed workflow analysis.

---

## Key Columns

### Identifiers
- `order_id` — unique identifier for each laboratory order  

---

### Workflow Segmentation
- `test_name` — type of microbiology or molecular test  
- `patient_location` — clinical location (ICU, ED, Med Surg, etc.)  
- `priority` — STAT or Routine  
- `instrument` — testing platform used  

---

### Turnaround Time (TAT) Metrics

#### Stage-Level Timing (minutes)
- `tat_collection_min` — order to specimen collection  
- `tat_transport_min` — collection to lab receipt  
- `tat_lab_min` — laboratory processing time  
- `tat_result_post_min` — result verification and release  

#### Total Timing
- `tat_total_min` — total turnaround time in minutes  
- `tat_total_hours` — total turnaround time in hours  

---

### Delay Flags

Boolean-style indicators for workflow delays:

- `collection_delay_flag`  
- `transport_delay_flag`  
- `lab_delay_flag`  
- `result_post_delay_flag`  
- `stat_delay_flag`  

These fields simulate operational flags used in real systems to identify delays.

---

## Data Generation Logic

The dataset was generated using Python (`pandas`) with rules designed to mimic:

- Expected workflow timing by test type  
- Longer lab processing times for culture-based testing  
- Faster workflows for molecular/PCR-based testing  
- Variability across patient locations  
- Courier-based transport delays for outreach locations  
- Event-driven delays affecting STAT prioritization  

---

## Analytical Use Cases

This dataset supports:

- TAT analysis by test, location, and priority  
- Bottleneck detection across workflow stages  
- Expected vs actual TAT modeling  
- Delay classification and severity scoring  
- Outlier detection for extreme workflow delays  
- Clarity-style SQL reporting and workflow investigation  

---

## Limitations

- Data is synthetic and does not represent real patient data  
- Workflow assumptions are simplified representations of real laboratory operations  
- Expected TAT values are modeled rather than sourced from system build tables  

---

## Notes

This dataset is intended for educational and portfolio purposes to simulate real-world healthcare analytics and laboratory informatics workflows.

It is designed to demonstrate:
- SQL-based workflow analysis  
- Clinical systems thinking  
- Epic Beaker / LIS-aligned data modeling  
