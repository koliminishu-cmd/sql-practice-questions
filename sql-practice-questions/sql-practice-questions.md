# 150 SQL Practice Questions for Data Engineer Interviews

## Medium Questions

1. Given `orders(order_id, customer_id, order_date, amount)`, find the total revenue per customer for the last 90 days.
2. Given `orders` and `customers(customer_id, country)`, find revenue by country and month.
3. Given `employees(employee_id, manager_id, salary)`, find employees who earn more than their manager.
4. Given `transactions(txn_id, user_id, txn_date, amount)`, find each user's first transaction date.
5. Given `transactions`, return users whose first transaction amount was greater than 100.
6. Given `events(user_id, event_name, event_time)`, count daily active users.
7. Given `events`, find users who performed both `signup` and `purchase`.
8. Given `orders(order_id, customer_id, order_date)`, find customers with at least 3 orders in any calendar month.
9. Given `products(product_id, category)` and `order_items(order_id, product_id, quantity, price)`, calculate category revenue.
10. Given `order_items`, find the top 5 products by revenue.
11. Given `order_items`, find products that were never purchased.
12. Given `users(user_id, signup_date)` and `orders`, calculate conversion rate by signup month.
13. Given `web_sessions(session_id, user_id, started_at, ended_at)`, calculate average session duration per day.
14. Given `page_views(user_id, page_url, viewed_at)`, find the most viewed page each day.
15. Given `payments(payment_id, order_id, status, paid_at)`, find orders with no successful payment.
16. Given `orders(order_id, order_date, status)`, count orders by status for each week.
17. Given `inventory(product_id, snapshot_date, quantity)`, find products that went out of stock on each date.
18. Given `inventory`, calculate day-over-day quantity change per product.
19. Given `customer_support(ticket_id, customer_id, created_at, resolved_at)`, calculate average resolution time by week.
20. Given `tickets(ticket_id, priority, status)`, find the percentage of open tickets by priority.
21. Given `logins(user_id, login_time)`, find users who logged in on consecutive days.
22. Given `logins`, calculate each user's latest login and previous login.
23. Given `sales(rep_id, sale_date, amount)`, calculate monthly sales and month-over-month growth.
24. Given `sales`, find each sales rep's best sales month.
25. Given `subscriptions(user_id, start_date, end_date)`, count active subscribers on a given date.
26. Given `subscriptions`, calculate monthly active subscribers.
27. Given `subscriptions`, find users whose subscription lasted more than 365 days.
28. Given `ad_clicks(user_id, campaign_id, clicked_at)` and `purchases(user_id, purchased_at, amount)`, attribute purchases within 7 days of a click.
29. Given `campaign_spend(campaign_id, spend_date, spend)` and attributed purchases, calculate ROAS by campaign.
30. Given `reviews(product_id, user_id, rating, review_date)`, find average rating per product.
31. Given `reviews`, find products with an average rating above 4 and at least 20 reviews.
32. Given `reviews`, find users who reviewed the same product more than once.
33. Given `shipments(order_id, shipped_at, delivered_at)`, calculate average delivery time by carrier.
34. Given `orders(order_id, promised_delivery_date)` and `shipments`, calculate on-time delivery rate.
35. Given `refunds(order_id, refund_amount, refund_date)`, find refund rate by month.
36. Given `orders` and `refunds`, find customers with refund amount greater than 50% of their total spend.
37. Given `accounts(account_id, created_at)` and `transactions`, find accounts with no transactions in the first 30 days.
38. Given `transactions`, calculate running transaction total per user.
39. Given `transactions`, find the highest transaction per user and include ties.
40. Given `transactions`, find the second highest transaction amount per user.
41. Given `orders`, remove duplicate rows where duplicates share `customer_id`, `order_date`, and `amount`, keeping the lowest `order_id`.
42. Given `users(user_id, email)`, find duplicate emails ignoring case.
43. Given `users(user_id, phone_number)`, normalize phone numbers and find duplicates.
44. Given `employee_history(employee_id, department, start_date, end_date)`, find each employee's current department.
45. Given `employee_history`, find employees who changed departments more than twice.
46. Given `product_prices(product_id, price, effective_date)`, find the current price per product.
47. Given `product_prices`, find the price in effect for each order item at order time.
48. Given `exchange_rates(currency, rate_date, usd_rate)` and `orders(currency, amount, order_date)`, convert order amount to USD using the latest available rate on or before the order date.
49. Given `sensor_readings(sensor_id, reading_time, value)`, calculate hourly average reading per sensor.
50. Given `sensor_readings`, find readings that are greater than 3 standard deviations from the sensor's average.
51. Given `job_runs(job_id, started_at, finished_at, status)`, calculate success rate per job per day.
52. Given `job_runs`, find jobs whose latest run failed.
53. Given `job_runs`, find jobs with runtime increasing for 3 consecutive runs.
54. Given `data_quality_checks(check_id, table_name, run_time, status)`, find tables with failed checks in the last 24 hours.
55. Given `file_ingestions(file_id, source_name, received_at, processed_at)`, calculate average processing delay by source.
56. Given `file_ingestions`, find sources that missed an expected daily file.
57. Given `orders(order_id, updated_at)` and `order_events(order_id, event_time, event_type)`, find orders updated after their last event.
58. Given `clickstream(user_id, event_time, url)`, find the first page visited in each session, assuming a session breaks after 30 minutes of inactivity.
59. Given `clickstream`, count sessions per user per day using the 30-minute inactivity rule.
60. Given `clickstream`, find bounce sessions with only one page view.
61. Given `cart_events(user_id, product_id, event_name, event_time)`, find users who added to cart but did not purchase.
62. Given `cart_events`, calculate cart abandonment rate by product.
63. Given `orders(customer_id, order_date)`, calculate days between consecutive orders for each customer.
64. Given `orders`, find customers whose order frequency improved month over month.
65. Given `users(user_id, signup_date, acquisition_channel)`, calculate 7-day retention by acquisition channel.
66. Given `app_events(user_id, event_name, event_time)`, find users active on day 1, day 7, and day 30 after signup.
67. Given `balances(account_id, balance_date, balance)`, calculate average daily balance per account per month.
68. Given `balances`, find accounts with negative balance for 5 consecutive days.
69. Given `loans(loan_id, customer_id, issued_at, principal)` and `payments(loan_id, paid_at, amount)`, calculate outstanding principal.
70. Given `loans` and `payments`, find loans with no payment within 30 days of issue.
71. Given `messages(sender_id, receiver_id, sent_at)`, count unique conversations per day.
72. Given `messages`, find pairs of users who exchanged messages both ways.
73. Given `friendships(user_id, friend_id)`, find mutual friends for each user pair.
74. Given `searches(user_id, query, searched_at)` and `clicks(user_id, query, clicked_at)`, calculate click-through rate by query.
75. Given `searches`, find each user's most frequent search query.

## Hard Questions

76. Given `orders(order_id, customer_id, order_date, amount)`, calculate cohort retention by first order month and months since first order.
77. Given `events(user_id, event_name, event_time)`, build a funnel showing users who completed `view_product`, `add_to_cart`, `checkout`, and `purchase` in order within 24 hours.
78. Given `events`, calculate the median time between `signup` and `first_purchase` by signup week.
79. Given `subscriptions(user_id, start_date, end_date, plan_id)`, calculate monthly recurring revenue while handling mid-month upgrades and cancellations.
80. Given `subscription_events(user_id, event_type, event_time, plan_price)`, reconstruct each user's subscription periods.
81. Given `subscription_events`, calculate net revenue retention by customer cohort.
82. Given `invoices(invoice_id, customer_id, invoice_date, amount)` and `payments(invoice_id, paid_at, amount)`, calculate aging buckets for unpaid invoice balances.
83. Given `orders` and `order_status_history(order_id, status, changed_at)`, find the longest time each order spent in any status.
84. Given `order_status_history`, identify invalid status transitions based on a valid transition table.
85. Given `inventory_movements(product_id, warehouse_id, movement_time, quantity_delta)`, reconstruct daily ending inventory by product and warehouse.
86. Given `inventory_movements`, find products that had negative inventory at any point during a day.
87. Given `product_prices(product_id, effective_start, effective_end, price)`, detect overlapping effective-date ranges.
88. Given `customer_dim(customer_id, effective_start, effective_end, is_current)`, validate that each customer has exactly one current SCD Type 2 record.
89. Given `customer_dim`, find gaps in effective-date coverage for each customer.
90. Given a staging table and target dimension table, write SQL logic to identify new, changed, and unchanged dimension records for an SCD Type 2 load.
91. Given `raw_events(event_id, user_id, event_time, ingested_at)`, deduplicate events by `event_id`, keeping the latest ingested version.
92. Given `raw_events`, detect late-arriving events where `event_time` is more than 2 days before `ingested_at`.
93. Given `raw_events`, compute event counts by event date and ingestion date to monitor pipeline delay.
94. Given `job_dependencies(job_id, depends_on_job_id)` and `job_runs(job_id, run_date, status)`, find jobs that ran successfully even though a dependency failed.
95. Given `job_dependencies`, produce the transitive dependency list for each job using a recursive CTE.
96. Given `job_runs`, identify the first failed run after a streak of at least 5 successful runs.
97. Given `job_runs`, calculate rolling 7-run success rate per job.
98. Given `table_row_counts(table_name, snapshot_time, row_count)`, detect tables whose row count changed by more than 30% from the previous snapshot.
99. Given `table_column_stats(table_name, column_name, snapshot_date, null_count, total_count)`, detect columns with a sudden null-rate increase.
100. Given `schema_columns(table_name, column_name, data_type, snapshot_date)`, detect schema drift between two snapshots.
101. Given `api_logs(request_id, endpoint, status_code, latency_ms, request_time)`, calculate p95 latency per endpoint per hour.
102. Given `api_logs`, find endpoints whose p95 latency increased for 3 consecutive hours.
103. Given `api_logs`, calculate error budget burn rate using 5xx responses over rolling 1-hour and 6-hour windows.
104. Given `web_events(user_id, event_time, page, referrer)`, sessionize events and calculate landing page conversion rate.
105. Given `web_events`, find the top conversion path of pages before purchase.
106. Given `web_events`, calculate average number of sessions before first purchase.
107. Given `orders`, calculate customer lifetime value after 30, 60, 90, and 180 days from first order.
108. Given `orders`, find customers whose 90-day spend is in the top 10% of their cohort.
109. Given `orders`, calculate rolling 12-month revenue and compare it with the previous rolling 12-month period.
110. Given `orders`, classify customers as new, retained, resurrected, or churned for each month.
111. Given `user_activity(user_id, activity_date)`, calculate rolling 7-day active users and rolling 30-day active users.
112. Given `user_activity`, calculate stickiness as DAU divided by MAU for each day.
113. Given `user_activity`, identify users with exactly 3 activity streaks of at least 5 days.
114. Given `login_events(user_id, login_time, device_id)`, detect account sharing based on logins from more than 3 devices in a 24-hour window.
115. Given `login_events(user_id, login_time, ip_address)`, detect impossible travel using IP-to-country mappings and timestamps.
116. Given `payments(payment_id, user_id, amount, payment_time, card_id)`, detect users with more than 5 failed payments followed by a successful payment within 1 hour.
117. Given `payments`, find suspicious cards used by more than 3 users in a day.
118. Given `orders` and `fraud_flags(order_id, flag_reason, flagged_at)`, calculate fraud rate by acquisition channel and order month.
119. Given `ride_requests(request_id, rider_id, driver_id, requested_at, accepted_at, completed_at, status)`, calculate driver acceptance rate by hour.
120. Given `ride_requests`, calculate cancellation rate split by rider cancellation and driver cancellation.
121. Given `ride_requests`, match each rider's first completed ride to their signup cohort and calculate cohort activation rate.
122. Given `deliveries(delivery_id, courier_id, accepted_at, picked_up_at, delivered_at)`, calculate courier idle time between deliveries.
123. Given `deliveries`, identify couriers with overlapping deliveries.
124. Given `location_pings(entity_id, ping_time, latitude, longitude)`, find entities with missing pings for more than 15 minutes during an active shift.
125. Given `warehouse_events(order_id, event_type, event_time, station_id)`, calculate average time between pick, pack, and ship stages by station.
126. Given `warehouse_events`, identify orders that skipped a required warehouse stage.
127. Given `employee_shifts(employee_id, shift_start, shift_end)`, find overlapping shifts for the same employee.
128. Given `employee_shifts`, calculate total paid hours per employee per week while merging overlapping shifts.
129. Given `calendar(date, is_business_day)` and `tickets(created_at, resolved_at)`, calculate resolution time in business hours only.
130. Given `calendar` and `orders(order_date, shipped_date)`, calculate shipping SLA compliance in business days.
131. Given `exchange_rates(currency, rate_date, usd_rate)`, fill missing daily rates using the most recent prior available rate.
132. Given `exchange_rates` and `orders`, calculate daily revenue in USD and show the percentage caused by currency-rate movement versus local-currency sales movement.
133. Given `bids(auction_id, bidder_id, bid_time, bid_amount)`, find the winning bid per auction and handle tied bids by earliest bid time.
134. Given `bids`, detect bid sniping where a bidder places the winning bid in the last 10 seconds.
135. Given `marketplace_orders(order_id, buyer_id, seller_id, order_time, amount)`, calculate buyer-seller repeat transaction rate.
136. Given `marketplace_orders`, identify circular trading patterns where users buy and sell among the same small group.
137. Given `graph_edges(src_user_id, dst_user_id)`, find second-degree connections for each user without returning direct connections.
138. Given `graph_edges`, find connected components using recursive SQL.
139. Given `experiment_assignments(user_id, experiment_id, variant, assigned_at)` and `events`, calculate conversion rate by variant while excluding users assigned to multiple variants.
140. Given `experiment_assignments` and `orders`, calculate average revenue per user by variant using only orders after assignment.
141. Given `experiment_assignments`, detect sample ratio mismatch by comparing actual variant counts against expected allocation.
142. Given `feature_flags(user_id, flag_name, enabled_at, disabled_at)` and `events`, calculate metric changes before and after flag enablement.
143. Given `slow_query_log(query_id, warehouse, started_at, finished_at, bytes_scanned)`, find queries responsible for the top 80% of scanned bytes.
144. Given `slow_query_log`, calculate concurrent query count per warehouse over time.
145. Given `table_access_log(user_id, table_name, accessed_at)`, find unused tables not accessed in the last 90 days.
146. Given `table_access_log`, find users who accessed sensitive tables outside business hours.
147. Given `etl_lineage(upstream_table, downstream_table)`, find all downstream tables impacted by a change to a given source table.
148. Given `etl_lineage`, detect cycles in table dependencies.
149. Given `partition_metadata(table_name, partition_date, row_count, last_updated_at)`, find missing or stale partitions for the last 30 days.
150. Given `fact_orders(order_id, customer_key, product_key, order_date_key, amount)` and dimension tables, write validation queries to find orphaned foreign keys and duplicate dimension business keys.

