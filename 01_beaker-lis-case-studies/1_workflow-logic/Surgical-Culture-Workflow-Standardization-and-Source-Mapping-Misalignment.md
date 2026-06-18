# Surgical Culture Workflow Standardization and Source Mapping Misalignment

## Overview

A workflow design issue was identified involving a newly created surgical culture order within the laboratory information system (LIS).

The surgical culture workflow was intended to consolidate specimen collection workflows for surgical procedures; however, the configured specimen source options included sources with microbiology workflow requirements that did not align with the default culture setup.

Several specimen sources available within the order required unique media selection, processing methods, or workflow pathways that were incompatible with the standardized surgical culture build.

The issue was identified during workflow review and escalated as a recommendation for workflow standardization and source restriction.

---

# Operational Context

Microbiology culture workflows are highly source-dependent.

Different specimen sources require unique:

- Plate setups
- Selective media
- Processing methods
- Incubation workflows
- Organism recovery strategies
- Result interpretation pathways

Because of this, specimen source selection directly impacts downstream laboratory processing and diagnostic accuracy.

Standardized culture orders must therefore maintain close alignment between:

- Specimen source
- Default media setup
- Processing workflow
- Reporting logic

---

# Problem Identified

The newly designed surgical culture order included specimen sources that did not match the configured default workflow.

Examples included:

| Specimen Source | Required Workflow Dependency | Workflow Conflict |
|---|---|---|
| Respiratory | CNA plate required by default | Missing respiratory-specific media |
| Genital | Thayer-Martin media required | Missing selective genital workflow |
| Water | Water culture paddle workflow required | Incompatible with standard surgical culture setup |
| Medical Device | Vortexing in thioglycollate broth required | Processing workflow mismatch |

The order design allowed providers to select sources that required fundamentally different microbiology workflows while still using a generalized surgical culture setup.

---

# Workflow Risk Analysis

This design created several potential operational risks:

- Incorrect default media selection
- Missing organism recovery pathways
- Inconsistent specimen processing
- Increased manual correction by laboratory staff
- Risk of culture setup errors
- Workflow ambiguity during specimen processing
- Reduced standardization across microbiology operations

The issue demonstrated how excessive source flexibility within a single order can create downstream workflow instability.

---

# Root Cause Analysis

The primary issue appeared to be insufficient alignment between:

- Orderable design
- Specimen source mapping
- Microbiology processing workflows

The generalized surgical culture build attempted to support specimen sources that required distinct and highly specialized workflows.

Rather than functioning as a unified workflow, the order effectively contained multiple incompatible microbiology workflow pathways within a single culture configuration.

---

# Recommendation Provided

A recommendation was made to standardize the workflow by restricting specimen sources to those compatible with the configured surgical culture defaults.

Suggested remediation included:

- Removing incompatible specimen sources from the surgical culture order
- Redirecting providers toward dedicated culture workflows designed for those specimen types
- Enforcing predefined workflow pathways tied to validated microbiology processing standards

Examples:

| Source Type | Recommended Workflow |
|---|---|
| Respiratory | Dedicated respiratory culture workflow |
| Genital | Dedicated genital culture workflow |
| Water | Dedicated environmental/water culture workflow |
| Medical Device | Dedicated device-associated culture workflow |

This approach would improve workflow consistency and reduce downstream laboratory intervention.

---

# Actions Taken

## Workflow Review

- Evaluated specimen source options against downstream microbiology workflows
- Compared configured defaults against actual laboratory processing requirements
- Identified workflow incompatibilities tied to specific specimen sources

## Operational Risk Identification

- Identified sources requiring unique media or processing pathways
- Documented workflow conflicts affecting microbiology setup integrity
- Evaluated potential impact on specimen processing standardization

## Standardization Recommendation

- Recommended restricting incompatible specimen sources
- Recommended use of dedicated workflow-specific culture orders
- Supported predefined workflow enforcement rather than generalized workflow flexibility

---

# Technical / Informatics Concepts Demonstrated

- LIS workflow analysis
- Microbiology culture workflow design
- Specimen source mapping
- Media setup dependencies
- Workflow standardization
- Order configuration analysis
- Source-to-workflow coherence validation
- Operational risk reduction
- Clinical workflow governance

---

# Analyst Relevance

This issue reflects a common laboratory informatics challenge:

Balancing provider flexibility with operational workflow integrity.

While broad source selection may appear operationally convenient upstream, excessive flexibility can create major downstream laboratory inconsistencies if workflows are not tightly standardized.

The case demonstrates understanding of:

- Source-dependent microbiology workflows
- Build standardization principles
- Workflow governance
- Operational risk analysis
- LIS order design dependencies

---

# Key Takeaway

Laboratory workflows should prioritize standardized and validated processing pathways over unrestricted order flexibility.

Allowing incompatible specimen sources within a generalized culture workflow increases operational complexity, introduces setup inconsistencies, and creates avoidable downstream laboratory risk.

Effective LIS and Epic Beaker analysts must ensure that:

- Specimen source selection
- Media setup
- Processing workflows
- Order design

all remain operationally coherent across the full order-to-result lifecycle.
