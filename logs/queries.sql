-- logs/queries.sql
-- Example queries in BigQuery-style SQL (adapt COUNTIF/SAFE_DIVIDE if needed)
--
-- Assumed table schema:
--   api_logs(
--     request_id  STRING,
--     timestamp   TIMESTAMP,
--     endpoint    STRING,
--     method      STRING,
--     region      STRING,
--     status_code INT64,
--     latency_ms  INT64,
--     error_type  STRING,
--     plan_tier   STRING
--   );

------------------------------------------------------------
-- 1) Error breakdown
--    Total errors by status_code and error_type
------------------------------------------------------------
SELECT
  status_code,
  COALESCE(NULLIF(error_type, ''), 'unknown') AS error_type,
  COUNT(*) AS error_count
FROM api_logs
WHERE status_code >= 400
GROUP BY status_code, error_type
ORDER BY error_count DESC;

------------------------------------------------------------
-- 2) Latency distribution
--    Bucket requests by latency range
------------------------------------------------------------
SELECT
  CASE
    WHEN latency_ms < 200 THEN '<200ms'
    WHEN latency_ms < 500 THEN '200-499ms'
    WHEN latency_ms < 1000 THEN '500-999ms'
    ELSE '>=1000ms'
  END AS latency_bucket,
  COUNT(*) AS request_count
FROM api_logs
GROUP BY latency_bucket
ORDER BY
  CASE latency_bucket
    WHEN '<200ms' THEN 1
    WHEN '200-499ms' THEN 2
    WHEN '500-999ms' THEN 3
    ELSE 4
  END;

------------------------------------------------------------
-- 3) Daily error trend
--    Errors per day + error rate
------------------------------------------------------------
SELECT
  DATE(timestamp) AS event_date,
  COUNTIF(status_code >= 400) AS error_count,
  COUNT(*) AS total_requests,
  SAFE_DIVIDE(COUNTIF(status_code >= 400), COUNT(*)) AS error_rate
FROM api_logs
GROUP BY event_date
ORDER BY event_date;

------------------------------------------------------------
-- 4) Region comparisons
--    Error rate + average latency per region
------------------------------------------------------------
SELECT
  region,
  COUNT(*) AS total_requests,
  COUNTIF(status_code >= 400) AS total_errors,
  SAFE_DIVIDE(COUNTIF(status_code >= 400), COUNT(*)) AS error_rate,
  AVG(latency_ms) AS avg_latency_ms
FROM api_logs
GROUP BY region
ORDER BY error_rate DESC;

------------------------------------------------------------
-- 5) 4xx vs 5xx totals
------------------------------------------------------------
SELECT
  CASE
    WHEN status_code BETWEEN 400 AND 499 THEN '4xx'
    WHEN status_code BETWEEN 500 AND 599 THEN '5xx'
    ELSE 'other'
  END AS status_family,
  COUNT(*) AS total
FROM api_logs
WHERE status_code >= 400
GROUP BY status_family
ORDER BY status_family;

