# Specimen Source Standardization Gap in Catheter-Related Cultures

## Case Study Type
Epic Beaker / LIS Workflow Validation  
Microbiology | Specimen Source Mapping | Data Integrity

## Summary
During Epic Beaker test build validation, a specimen source standardization gap was identified in catheter-related culture workflows.

The available build options appeared to represent catheter-related specimens too broadly, with limited differentiation between catheter types or other tubing/device-associated sources. In the collection label workflow, the source appeared to default to “catheter tip,” which may not accurately represent the full range of device-associated specimens handled by microbiology.

This case study evaluates how a seemingly small source-selection issue can affect clinical workflow clarity, specimen labeling, downstream reporting, and infection control data quality.

---

## Clinical Context
Microbiology receives cultures associated with multiple device or tubing-related sources, not simply urinary catheters or generic catheter tips.

Examples may include:

- Urinary catheter / Foley-related specimens
- Central line catheter tips
- Drain tubing
- Other device-associated tubing or catheter-related specimens

Accurate source capture matters because specimen source is not just a label. It affects bench interpretation, reporting consistency, infection surveillance, and downstream analytics.

---

## Observed Build Issue
During validation, the catheter-related culture workflow appeared limited to broad source options such as:

- Catheter
- Catheter tip

In the collection label workflow, the source type appeared to print or map as:

- Catheter tip

This creates a potential mismatch between the real-world specimen source and the source value represented in the system.

---

## Expected Workflow
A catheter-related or tubing-associated culture workflow should allow the ordering or collection process to accurately represent the actual specimen source.

Expected behavior:

1. User selects the most accurate source or device category.
2. The selected source maps consistently to the order.
3. The same source carries forward to collection labels.
4. The microbiology bench receives clear source context.
5. Downstream reports and infection control workflows retain meaningful source data.

---

## Actual Workflow Observed
The workflow appeared to collapse multiple possible catheter/device/tubing sources into a narrow source structure.

Potential actual behavior:

1. User selects a broad catheter-related source.
2. Label output displays “catheter tip.”
3. Bench receives limited source context.
4. Downstream reporting treats cases as the same source category even when the clinical context differs.

---

## Why This Matters
This issue is important because specimen source standardization affects multiple downstream workflows.

### Clinical Workflow Impact
Ambiguous source values can create uncertainty for microbiology staff reviewing or processing the specimen.

### Labeling Impact
If the label does not reflect the true source, the receiving bench may lack important context at the point of processing.

### Infection Control Impact
Catheter-related cultures may have different surveillance implications depending on the device type involved.

Examples:

- Urinary catheter-associated workflows may relate to CAUTI surveillance.
- Central line catheter tip workflows may relate to CLABSI surveillance.
- Drain or device-associated tubing may require separate categorization.

### Reporting Impact
If different clinical sources are grouped under the same source value, analytics can become less reliable.

Potential reporting problems:

- Over-grouping catheter-related cultures
- Inability to distinguish catheter type trends
- Reduced value of source-based dashboards
- Lower confidence in downstream quality metrics

---

## Root Cause Hypothesis
The issue may be caused by incomplete or overly broad source dictionary build.

Possible contributing factors:

- Catheter-related source values were simplified during build.
- Source dictionary does not include enough clinically meaningful device categories.
- Orderable-to-source mapping may not fully reflect microbiology workflows.
- Label print logic may be using a generic or default source value.
- Infection control/reporting requirements may not have been fully considered during source design.

---

## Recommended Build Review
Recommended review areas:

### 1. Specimen Source Dictionary
Review whether catheter-related and tubing-associated source values are specific enough for microbiology workflows.

Possible source additions or clarifications:

- Urinary catheter
- Foley catheter
- Central line catheter tip
- Drain tubing
- Device-associated tubing
- Other catheter/device source

### 2. Orderable-to-Source Mapping
Confirm that catheter-related culture orderables map to appropriate allowed source values.

### 3. Collection Label Logic
Validate that the source printed on the label matches the selected source and does not default to an inaccurate value.

### 4. Downstream Reporting Mapping
Confirm how these source values flow into reporting tables, dashboards, infection control workflows, and quality metrics.

### 5. Infection Control Review
Coordinate with infection prevention stakeholders if catheter-related source values support surveillance definitions or internal review workflows.

---

## Analyst Recommendation
Do not treat this as only a missing dropdown option.

This should be reviewed as a source standardization and downstream data integrity issue.

Recommended analyst framing:

> The current catheter-related source configuration may not provide enough specificity to support accurate specimen labeling, microbiology workflow context, infection control classification, and downstream reporting.

---

## Validation Questions
Key questions for follow-up validation:

1. Which catheter-related culture orderables allow “catheter” or “catheter tip” as source values?
2. Does the selected source always print correctly on collection labels?
3. Are urinary catheter, central line, and drain tubing sources intentionally grouped?
4. Where do these source values flow in downstream reporting?
5. Are infection prevention teams using these source values for surveillance or review?
6. Should device-associated sources be standardized into controlled categories?
7. Are there existing legacy LIS source values that need to be mapped into Beaker?

---

## Portfolio Takeaway
This case demonstrates how source dictionary design affects more than order entry.

A limited source configuration can create ambiguity across:

- Collection
- Labeling
- Bench workflow
- Infection control
- Analytics
- Data governance

For Epic Beaker and LIS analysts, accurate source standardization is a core part of maintaining clinical and operational data integrity.

---
## Follow-Up

Following review, the concern was escalated for broader discussion regarding standardized capture of catheter source information across workflows.

This reinforced the importance of structured anatomical context within microbiology order entry and downstream reporting workflows.
