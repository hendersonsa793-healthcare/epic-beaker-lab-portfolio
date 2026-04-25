# LIS Interface Issue – Order Retrieval Failure (Hologic Panther)

## Problem
The Hologic Panther molecular platform was unable to retrieve test orders from the LIS under specific accession conditions, preventing specimen processing.

---

## Environment
- Instrument: Hologic Panther  
- LIS: Sunquest  
- Workflow: Molecular diagnostics  
- Interface Type: Bidirectional (order query + result transmission)  

---

## Investigation
Initial troubleshooting steps restored baseline connectivity but revealed intermittent order retrieval failures.

Analysis of LIS protocol output identified inconsistent message patterns. Comparison of accession-level structure across working and failing scenarios revealed a clear dependency on order composition.

### Key Observations
- Orders failed when the accession contained a single standalone test  
- Orders succeeded when:
  - Multiple tests were present on the accession  
  - The test was part of a panel/combination order  

---

## Root Cause (Hypothesis)
Interface behavior appears dependent on accession-level order structure.

When only a single test is present:
- Order retrieval or message parsing fails  
- Required fields may not be consistently populated in the interface message  

### Likely Contributing Factors
- Configuration or mapping inconsistency following system changes  
- Dependency on multi-order or panel-based formatting within interface logic  

---

## Action Taken
- Documented reproducible failure pattern  
- Captured LIS protocol output demonstrating inconsistent field population (e.g., pipe-delimited empty fields `|||||`)  
- Escalated findings to LIS and vendor teams for further investigation  

---

## Outcome
- Isolated a specific, reproducible failure condition  
- Enabled targeted escalation with clear technical criteria  
- Reduced repeated troubleshooting cycles and ambiguity  

---

## Analyst Insight
This case demonstrates how accession structure and order configuration directly impact LIS–instrument interface behavior.

### Key Takeaways
- Interface logic may behave differently based on single vs multi-order accessions  
- Structurally valid messages can still fail if required fields are not populated  
- Post-change validation of interface behavior is critical  

From an Epic Beaker perspective, this reinforces the importance of:
- Order build design (standalone vs panel-based orders)  
- Interface validation across edge cases  
- Ensuring consistent data structure throughout the order-to-result lifecycle  
