# Microbiology Workflow Issue – Missing Thayer-Martin Media for Genital Cultures

## Problem
Genital-source wound culture workflows did not include Thayer-Martin agar as an available or default media option, despite its clinical relevance for recovery of *Neisseria gonorrhoeae*.

---

## Environment
- Domain: Microbiology  
- Workflow: Culture setup / media selection  
- System Context: LIS / Epic Beaker-aligned order and setup configuration  

---

## Investigation
- Initial validation performed using a non-genital source → no selective media issues identified  
- Workflow re-tested using a genital (vulva) source to evaluate source-dependent behavior  

Observed behavior:
- Thayer-Martin agar was not available for selection during culture setup  
- Media option remained unavailable even when specimen source was clinically appropriate  

---

## Expected Behavior
For genital-source cultures:
- Thayer-Martin agar should be:
  - Available as a selectable media option  
  - Or automatically included in default culture setup  

This ensures appropriate recovery of fastidious organisms such as *Neisseria gonorrhoeae*.

---

## Root Cause (Hypothesis)
Likely gap in source-based configuration logic, including:
- Missing conditional mapping between genital specimen sources and appropriate selective media  
- Incorrect or incomplete test-to-media mapping within build configuration  
- Use of a generalized wound culture workflow without source-specific specialization  

---

## Action Taken
- Reproduced issue across multiple workflow paths  
- Validated absence of expected media under appropriate clinical conditions  
- Submitted ticket with:
  - Reproduction steps  
  - Clinical justification  
  - Recommendation for source-based media mapping  

---

## Impact
- Risk of missed recovery of clinically significant organisms  
- Incomplete or inappropriate culture setup  
- Potential downstream impact on:
  - Diagnosis  
  - Treatment decisions  
- Indicates gap in configuration rather than obvious system failure  

---

## Outcome
- Issue escalated with clear clinical and workflow justification  
- Enabled targeted review of source-to-media mapping within build configuration  

---

## Analyst Insight
This case highlights a critical principle in LIS and Epic Beaker design:

> **Specimen source must drive workflow configuration**

Failure to correctly map:
- Specimen source → Media selection → Organism recovery  

…can result in **silent clinical failures**, not just operational inefficiencies.

This also demonstrates:
- The importance of end-to-end workflow validation  
- The role of domain expertise in identifying configuration gaps  
- How build decisions directly impact clinical accuracy  

From a Beaker perspective, this aligns with:
- Source-based logic and conditional workflows  
- Rule-driven configuration of downstream laboratory processes  
- Ensuring system behavior reflects real-world clinical practice  
