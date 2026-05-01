-- ============================================
-- 02_tat_by_test_location_priority.sql
-- Purpose: Analyze turnaround time by test, location, and priority
-- Context: Microbiology workflow performance analysis
-- ============================================

SELECT
    patient_location,
    priority,
    test_name,

    COUNT(*) AS order_count,

    ROUND(AVG(tat_collection_min)::numeric, 1) AS avg_collection_min,
    ROUND(AVG(tat_transport_min)::numeric, 1) AS avg_transport_min,
    ROUND(AVG(tat_lab_min)::numeric, 1) AS avg_lab_min,
    ROUND(AVG(tat_result_post_min)::numeric, 1) AS avg_result_post_min,

    ROUND(AVG(tat_total_hours)::numeric, 2) AS avg_total_tat_hours

FROM microbiology_orders
GROUP BY
    patient_location,
    priority,
    test_name
ORDER BY
    avg_total_tat_hours DESC;
