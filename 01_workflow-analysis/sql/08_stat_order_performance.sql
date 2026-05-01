-- ============================================
-- 08_stat_order_performance.sql
-- Purpose: Compare turnaround time performance by order priority
-- Context: Evaluates whether STAT workflows perform differently from routine workflows
-- ============================================

SELECT
    priority,

    COUNT(*) AS order_count,

    ROUND(AVG(tat_collection_min)::numeric, 1) AS avg_collection_min,
    ROUND(AVG(tat_transport_min)::numeric, 1) AS avg_transport_min,
    ROUND(AVG(tat_lab_min)::numeric, 1) AS avg_lab_min,
    ROUND(AVG(tat_result_post_min)::numeric, 1) AS avg_result_post_min,

    ROUND(AVG(tat_total_hours)::numeric, 2) AS avg_total_tat_hours,

    SUM(CASE WHEN stat_delay_flag = 'Y' THEN 1 ELSE 0 END) AS stat_delay_count

FROM microbiology_orders
GROUP BY
    priority
ORDER BY
    avg_total_tat_hours DESC;
