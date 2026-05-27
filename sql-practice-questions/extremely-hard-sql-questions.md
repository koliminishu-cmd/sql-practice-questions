# Extremely Hard SQL Questions for Data Engineering Interviews

These questions are designed for senior-level data engineering interviews. They focus on temporal logic, recursive queries, incremental data processing, data quality, warehouse observability, slowly changing dimensions, graph-style analysis, and production-grade edge cases.

## Extremely Hard Questions

1. Given `etl_lineage(upstream_table, downstream_table)`, write a recursive query to return every downstream table impacted by a source table, including dependency depth and full dependency path.
2. Given `etl_lineage`, detect dependency cycles and return the exact cycle path for each detected cycle.
3. Given `job_dependencies(job_id, depends_on_job_id)` and `job_runs(job_id, run_id, run_date, status)`, find jobs that should not have run because at least one transitive dependency failed on the same run date.
4. Given `job_dependencies` and `job_runs`, calculate the longest critical path duration for each daily pipeline run.
5. Given `job_runs(job_id, started_at, finished_at)`, calculate the maximum number of concurrently running jobs at any point in time.
6. Given `job_runs`, identify the exact time windows when concurrency exceeded a warehouse limit of 50 jobs.
7. Given `slow_query_log(query_id, user_id, warehouse, started_at, finished_at, bytes_scanned)`, calculate overlapping query runtime per warehouse and attribute shared compute time proportionally to each query.
8. Given `slow_query_log`, find users responsible for the top 80% of compute cost by warehouse and day using cumulative contribution.
9. Given `table_access_log(user_id, table_name, accessed_at)` and `table_metadata(table_name, owner, sensitivity_level)`, find sensitive tables accessed by users who had no prior access history to that sensitivity level.
10. Given `schema_snapshots(table_name, column_name, data_type, ordinal_position, snapshot_date)`, detect added, removed, reordered, and type-changed columns between two snapshots.
11. Given `schema_snapshots`, find tables whose schema changed more than once within any rolling 7-day period.
12. Given `partition_metadata(table_name, partition_date, row_count, updated_at)`, detect missing partitions, stale partitions, and partitions with abnormal row-count deviation from a 14-day moving average.
13. Given `partition_metadata`, classify each partition as `healthy`, `missing`, `late`, `partial`, or `duplicate_load`.
14. Given `raw_events(event_id, source_system, event_time, ingested_at, payload_hash)`, deduplicate events while preserving the latest payload and flagging conflicting payloads for the same event ID.
15. Given `raw_events`, calculate daily event counts by event date and ingestion date, then identify dates where late-arriving data changed historical counts by more than 5%.
16. Given `raw_events`, design a query to identify records that should be reprocessed in an incremental pipeline with a 3-day lookback window and late-arrival tolerance.
17. Given `cdc_events(table_name, primary_key, operation, before_hash, after_hash, event_time, sequence_number)`, reconstruct the current table state.
18. Given `cdc_events`, identify invalid CDC sequences, such as update before insert, delete before insert, duplicate sequence numbers, and updates after delete.
19. Given `cdc_events`, reconstruct the row state as of any requested timestamp.
20. Given `customer_dim(customer_key, customer_id, effective_start, effective_end, is_current, row_hash)`, validate SCD Type 2 integrity for overlaps, gaps, multiple current rows, and unchanged duplicate versions.
21. Given `customer_dim`, produce a corrected SCD Type 2 timeline by merging adjacent records with identical attributes.
22. Given `customer_staging(customer_id, row_hash, extracted_at)` and `customer_dim`, classify staging rows into inserts, updates, unchanged rows, late-arriving historical corrections, and duplicate extracts.
23. Given `product_price_history(product_id, effective_start, effective_end, price)`, find all orders whose applied price does not match the price valid at the order timestamp.
24. Given `exchange_rates(currency, rate_date, usd_rate)`, fill missing rates using the most recent prior rate, but flag currencies with more than 3 consecutive missing business days.
25. Given `orders(order_id, currency, amount, order_time)` and `exchange_rates`, calculate USD revenue using the most recent prior exchange rate and identify orders where no valid prior rate exists.
26. Given `balances(account_id, balance_time, balance)`, derive daily opening balance, closing balance, minimum balance, maximum balance, and time-weighted average balance.
27. Given `inventory_movements(product_id, warehouse_id, movement_time, quantity_delta)`, reconstruct inventory quantity after every movement and find the first timestamp inventory became negative.
28. Given `inventory_movements`, calculate daily stockout minutes per product and warehouse.
29. Given `warehouse_events(order_id, event_type, event_time)`, validate that each order follows the required sequence `received -> picked -> packed -> shipped` without skipping, repeating, or reversing steps.
30. Given `warehouse_events`, calculate stage-level SLA breaches where each stage has a different allowed duration.
31. Given `web_events(user_id, event_time, page_url, event_name)`, sessionize events using a 30-minute inactivity rule and assign stable session numbers per user.
32. Given `web_events`, calculate conversion funnels where steps must occur in order within the same session, allowing optional intermediate events.
33. Given `web_events`, calculate the most common page path of length 5 before purchase.
34. Given `web_events`, find users whose session boundaries change if the inactivity threshold changes from 30 minutes to 15 minutes.
35. Given `app_events(user_id, event_name, event_time)` and `users(user_id, signup_time)`, calculate retention on day 1, day 7, day 30, and rolling 7-day retention by signup cohort.
36. Given `app_events`, calculate the longest active-day streak per user and return ties by earliest streak start.
37. Given `app_events`, identify users with three or more active streaks of at least 5 consecutive days.
38. Given `orders(customer_id, order_time, amount)`, classify customers each month as `new`, `retained`, `resurrected`, `churned`, or `inactive`.
39. Given `orders`, calculate customer lifetime value at 30, 60, 90, 180, and 365 days after first purchase for each acquisition cohort.
40. Given `orders`, calculate cohort revenue retention where each cohort month is indexed by months since first purchase.
41. Given `orders`, find customers whose monthly spend is above the 95th percentile of their acquisition cohort for at least 3 consecutive months.
42. Given `subscriptions(user_id, plan_id, started_at, ended_at, monthly_price)`, calculate daily MRR while handling overlapping subscriptions, upgrades, downgrades, cancellations, and reactivations.
43. Given `subscription_events(user_id, event_type, event_time, plan_price)`, reconstruct subscription intervals and calculate expansion, contraction, churn, and reactivation MRR by month.
44. Given `subscription_events`, calculate net revenue retention and gross revenue retention by customer cohort.
45. Given `invoices(invoice_id, customer_id, invoice_date, due_date, amount)` and `payments(invoice_id, payment_time, amount)`, calculate invoice aging buckets using remaining unpaid balance.
46. Given `invoices` and `payments`, allocate partial payments to oldest outstanding invoices by customer using SQL.
47. Given `loans(loan_id, principal, issued_at)` and `loan_payments(loan_id, paid_at, principal_amount, interest_amount)`, calculate outstanding principal and delinquency status by day.
48. Given `loan_payments`, detect loans that became delinquent, cured, and became delinquent again within a 90-day period.
49. Given `api_logs(request_id, endpoint, status_code, latency_ms, request_time)`, calculate rolling p50, p95, and p99 latency per endpoint over 5-minute windows.
50. Given `api_logs`, calculate error-budget burn rates over rolling 1-hour, 6-hour, and 24-hour windows.
51. Given `api_logs`, detect endpoints where p95 latency increased for 4 consecutive windows while request volume stayed within 10% of normal.
52. Given `data_quality_results(check_id, table_name, column_name, run_time, metric_name, metric_value)`, detect metric anomalies using rolling mean and standard deviation by check.
53. Given `data_quality_results`, find checks that are flaky, meaning they fail and pass alternately at least 3 times in the last 10 runs.
54. Given `table_row_counts(table_name, snapshot_time, row_count)`, detect silent data loss where row count gradually declines over multiple snapshots without a single large drop.
55. Given `table_column_profile(table_name, column_name, snapshot_date, distinct_count, null_count, total_count)`, detect columns with suspicious cardinality collapse.
56. Given `file_arrivals(source_name, file_name, expected_date, arrived_at, size_bytes)`, find sources with late, missing, duplicate, or unusually small files.
57. Given `file_arrivals`, calculate source reliability score based on timeliness, completeness, size anomaly, and duplicate rate.
58. Given `batch_loads(batch_id, source_name, started_at, finished_at, rows_read, rows_written, rows_rejected)`, identify batches where rejection rate exceeds both an absolute threshold and historical baseline.
59. Given `batch_loads`, calculate end-to-end pipeline latency from source file arrival to target table availability.
60. Given `table_refreshes(table_name, refresh_started_at, refresh_finished_at, status)`, identify downstream tables that are stale because an upstream refresh failed.
61. Given `experiment_assignments(user_id, experiment_id, variant, assigned_at)` and `events`, calculate conversion by variant while excluding users assigned to multiple variants or exposed before assignment.
62. Given `experiment_assignments`, detect sample ratio mismatch for experiments with arbitrary expected allocation ratios.
63. Given `experiment_assignments` and `orders`, calculate revenue lift by variant using winsorized revenue at the 99th percentile.
64. Given `feature_flags(user_id, flag_name, enabled_at, disabled_at)` and `events`, calculate user-level metric changes before and after feature exposure with matched pre/post windows.
65. Given `login_events(user_id, login_time, ip_country, device_id)`, detect impossible travel where the implied speed between countries exceeds a realistic threshold.
66. Given `login_events`, identify accounts with high-risk behavior based on new device, new country, failed login burst, and successful login after failures.
67. Given `payments(payment_id, user_id, card_id, status, amount, payment_time)`, find cards used across many users and users using many cards within rolling 24-hour windows.
68. Given `payments`, detect payment retry storms where repeated failed payments occur before success across multiple cards.
69. Given `marketplace_orders(order_id, buyer_id, seller_id, order_time, amount)`, detect circular trading patterns among groups of 3 users.
70. Given `marketplace_orders`, calculate repeat buyer-seller rate and separate organic repeats from repeats after refunds.
71. Given `graph_edges(src_id, dst_id)`, find connected components using recursive SQL.
72. Given `graph_edges`, find the shortest path between two users up to 6 degrees of separation.
73. Given `graph_edges`, find second-degree connections excluding direct connections and already-blocked users.
74. Given `messages(sender_id, receiver_id, sent_at)`, reconstruct conversation threads and calculate response-time percentiles by participant pair.
75. Given `messages`, detect spam senders based on burst volume, low reply rate, and repeated message templates.
76. Given `employee_shifts(employee_id, shift_start, shift_end)`, merge overlapping shifts and calculate total paid hours per employee per week.
77. Given `employee_shifts`, detect employees scheduled for overlapping shifts across different locations.
78. Given `calendar(date, is_business_day, holiday_name)` and `tickets(created_at, resolved_at)`, calculate business-hour resolution time excluding weekends and holidays.
79. Given `calendar` and `orders(order_time, shipped_time)`, calculate SLA compliance in business hours for multiple region-specific calendars.
80. Given `ride_events(ride_id, event_type, event_time, actor_id)`, reconstruct ride lifecycle and detect rides with invalid event order.
81. Given `ride_events`, calculate driver idle time between completed rides while excluding time spent on cancelled rides.
82. Given `location_pings(entity_id, ping_time, latitude, longitude)`, identify missing ping intervals during active trips and calculate total missing minutes.
83. Given `location_pings`, detect unrealistic movement based on distance and time between consecutive pings.
84. Given `sensor_readings(sensor_id, reading_time, value)`, fill missing 1-minute readings using forward fill and flag gaps longer than 10 minutes.
85. Given `sensor_readings`, detect sustained anomalies where readings exceed dynamic thresholds for at least 5 consecutive minutes.
86. Given `ad_clicks(user_id, campaign_id, clicked_at)` and `purchases(user_id, purchased_at, amount)`, implement last-touch attribution within a 7-day window.
87. Given `ad_clicks` and `purchases`, implement multi-touch attribution where credit is split across all eligible clicks within 7 days.
88. Given `ad_impressions(user_id, campaign_id, impression_time)` and `ad_clicks`, calculate view-through and click-through conversions while avoiding double counting.
89. Given `searches(user_id, query, searched_at)` and `clicks(user_id, query, clicked_at)`, calculate query CTR and zero-result abandonment rate.
90. Given `searches`, normalize queries by lowercasing, trimming whitespace, removing punctuation, and grouping near-duplicates using a provided canonical mapping table.
91. Given `bids(auction_id, bidder_id, bid_time, bid_amount)`, determine the winning bid with tie-breaking by earliest bid time and detect auctions with invalid decreasing bids.
92. Given `bids`, detect coordinated bidding where the same group of bidders repeatedly appears in the final 3 bids across many auctions.
93. Given `fact_orders(order_id, customer_key, product_key, order_date_key, amount)` and dimensions, find orphaned foreign keys, duplicate dimension natural keys, and facts mapped to expired dimension rows.
94. Given `fact_orders` and `dim_customer(customer_key, customer_id, effective_start, effective_end)`, validate that each fact joins to exactly one customer dimension row based on order date.
95. Given `fact_events(event_key, user_key, session_key, event_time)` and dimensions, identify fact rows whose dimension keys were unknown at load time but can now be repaired.
96. Given `audit_log(table_name, batch_id, rows_inserted, rows_updated, rows_deleted, load_time)`, reconcile expected row-count changes against actual target table snapshots.
97. Given `audit_log`, find batches that were loaded out of order for the same source and may have overwritten newer data.
98. Given `merge_log(target_table, business_key, operation, batch_id, operation_time)`, detect duplicate merge operations for the same business key in a single batch.
99. Given `raw_json_events(event_id, payload, ingested_at)`, extract nested fields, count missing required fields, and identify payload schema versions with the highest error rate.
100. Given `raw_json_events`, detect payload schema evolution by comparing the set of JSON keys seen per day.

