-- ============================================
-- 07_delay_flags_analysis.sql
-- Purpose: Summarize delay flag frequency by test type
-- Context: Identifies which workflow stages are most frequently flagged
-- ============================================

SELECT
    test_name,

    COUNT(*) AS total_orders,

    SUM(CASE WHEN collection_delay_flag = 'Y' THEN 1 ELSE 0 END) AS collection_delay_count,
    SUM(CASE WHEN transport_delay_flag = 'Y' THEN 1 ELSE 0 END) AS transport_delay_count,
    SUM(CASE WHEN lab_delay_flag = 'Y' THEN 1 ELSE 0 END) AS lab_delay_count,
    SUM(CASE WHEN result_post_delay_flag = 'Y' THEN 1 ELSE 0 END) AS result_post_delay_count,

    ROUND(AVG(tat_total_hours)::numeric, 2) AS avg_total_tat_hours

FROM microbiology_orders
GROUP BY
    test_name
ORDER BY
    avg_total_tat_hours DESC;
