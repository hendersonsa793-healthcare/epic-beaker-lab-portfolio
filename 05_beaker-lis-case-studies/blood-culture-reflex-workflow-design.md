# Microbiology Workflow Design Issue – Blood Culture Reflex Workflow Misalignment

## Problem
Blood culture workflow configuration required documentation of culture plate setup prior to confirmation of bottle positivity, creating a mismatch between system behavior and real laboratory workflow.

---

## Environment
- Domain: Microbiology  
- Workflow: Blood culture processing and organism workup  
- System Context: LIS / Epic Beaker-aligned workflow configuration  

---

## Observed Behavior
- Workflow required documentation of plate culture setup at initial processing stage  
- Plate setup recorded before instrument-confirmed positivity  

---

## Expected Behavior
Blood culture workflows should be **event-driven**, with downstream processes triggered only after positivity is confirmed.

Correct workflow:
1. Blood culture collection and incubation  
2. Instrument monitoring  
3. Bottle flags positive  
4. Reflex workflow triggered:
   - Gram stain  
   - Plate culture setup  
   - Organism workup  

---

## Root Cause (Hypothesis)
The workflow appears to combine:
- Initial blood culture monitoring  
- Downstream microbiology workup  

…into a single process, rather than separating them into event-triggered phases.

---

## Proposed Solution
Split workflow into two distinct components:

### 1. Initial Order
**Blood Culture Collection + Monitoring**
Tracks:
- Collection  
- Incubation  
- Time to positivity  

### 2. Reflex Workflow (Triggered Event)
Trigger:
- Positive bottle detection  

Automatically generates:
- Gram stain  
- Plate culture setup  
- Organism identification workflow  

---

## Impact
- Prevents premature documentation of work not yet performed  
- Aligns system behavior with real laboratory processes  
- Reduces user confusion and training inconsistency  
- Improves data integrity for:
  - Workflow tracking  
  - Turnaround time analysis  
  - Quality metrics  

---

## Outcome
- Provided workflow redesign recommendation aligned with microbiology best practices  
- Highlighted need for event-driven configuration within LIS/Beaker build  

---

## Analyst Insight
This case demonstrates a core principle in Epic Beaker and LIS design:

> **Workflows should be event-driven, not assumption-driven**

Separating initial testing from reflex workflows:
- Improves data quality and traceability  
- Enables accurate process timing analysis  
- Supports rule-based automation and downstream workflows  

This aligns directly with Epic Beaker capabilities:
- Result-triggered reflex testing  
- Rule-based workflow configuration  
- Segmentation of the order-to-result lifecycle  
