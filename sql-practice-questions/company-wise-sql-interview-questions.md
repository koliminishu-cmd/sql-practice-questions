# Company-Wise SQL Interview Practice Questions

These are company-style SQL questions inspired by common data engineering interview patterns. They are not guaranteed to be exact questions from any company. Use them to practice the kind of thinking commonly tested by product, marketplace, fintech, SaaS, streaming, logistics, and cloud data teams.

## How to Use This File

For each question:

- Mark status: `[ ]`, `[~]`, or `[x]`
- Write the output grain before writing SQL
- List edge cases before finalizing the query
- Explain the query in 2-3 minutes as interview practice

## Amazon-Style Questions

1. [ ] Given `orders(order_id, customer_id, order_time, status, amount)` and `order_items(order_id, product_id, quantity, item_price)`, find the top 3 products by revenue in each product category for every month.
   - Topic: window functions, ranking, joins
   - Think about: ties, cancelled orders, revenue grain

2. [ ] Given `shipments(order_id, promised_date, shipped_at, delivered_at, carrier)`, calculate on-time delivery rate by carrier and week.
   - Topic: date logic, aggregation
   - Think about: null delivery dates, partial weeks

3. [ ] Given `inventory_movements(product_id, warehouse_id, movement_time, quantity_delta)`, calculate daily ending inventory per product and warehouse.
   - Topic: running totals
   - Think about: missing days, negative inventory

4. [ ] Given `returns(order_id, return_time, refund_amount)` and `orders`, find customers whose return value is more than 40% of their order value in the last 6 months.
   - Topic: joins, ratio metrics
   - Think about: customers with zero spend, partial refunds

5. [ ] Given `warehouse_events(order_id, event_type, event_time)`, find orders that skipped any required step from `received`, `picked`, `packed`, and `shipped`.
   - Topic: event sequencing
   - Think about: repeated events, out-of-order events

## Google-Style Questions

6. [ ] Given `searches(user_id, query, search_time)` and `clicks(user_id, query, click_time)`, calculate click-through rate by query for the last 30 days.
   - Topic: joins, aggregation
   - Think about: multiple clicks per search, zero-click queries

7. [ ] Given `web_events(user_id, event_time, page_url, event_name)`, sessionize events using a 30-minute inactivity rule.
   - Topic: sessionization, window functions
   - Think about: first event per user, exact 30-minute boundary

8. [ ] Given `experiments(user_id, experiment_id, variant, assigned_at)` and `events`, calculate conversion rate by variant after assignment.
   - Topic: A/B testing SQL
   - Think about: users assigned to multiple variants

9. [ ] Given `api_logs(endpoint, request_time, latency_ms, status_code)`, calculate p95 latency by endpoint and hour.
   - Topic: percentile analytics
   - Think about: low-volume endpoints, failed requests

10. [ ] Given `query_logs(query_id, user_id, started_at, finished_at, bytes_scanned)`, find users responsible for the top 80% of scanned bytes.
   - Topic: cumulative distribution
   - Think about: tied usage, daily versus total usage

## Meta/Facebook-Style Questions

11. [ ] Given `friendships(user_id, friend_id)` and `messages(sender_id, receiver_id, sent_at)`, find users who messaged a non-friend.
   - Topic: graph joins, anti-join
   - Think about: friendship direction, duplicate edges

12. [ ] Given `posts(post_id, user_id, created_at)` and `reactions(post_id, user_id, reaction_type, reacted_at)`, calculate engagement rate per post within 24 hours of creation.
   - Topic: time-window joins
   - Think about: multiple reactions by same user

13. [ ] Given `events(user_id, event_name, event_time)`, find users who performed `view_ad`, `click_ad`, and `purchase` in order within 1 day.
   - Topic: funnel analysis
   - Think about: repeated steps, first valid funnel

14. [ ] Given `login_events(user_id, login_time, device_id, country)`, detect users logging in from more than 3 countries in a 24-hour window.
   - Topic: fraud/risk analytics
   - Think about: rolling windows, distinct count

15. [ ] Given `user_activity(user_id, activity_date)`, calculate daily active users, weekly active users, and monthly active users.
   - Topic: active user metrics
   - Think about: distinct users, date spine

## Netflix-Style Questions

16. [ ] Given `watch_events(user_id, title_id, started_at, seconds_watched)` and `titles(title_id, genre)`, find the top genre by watch time for each user.
   - Topic: aggregation, ranking
   - Think about: tied genres, incomplete sessions

17. [ ] Given `subscriptions(user_id, started_at, ended_at, plan_id)`, calculate monthly active subscribers.
   - Topic: date ranges
   - Think about: users active for partial months

18. [ ] Given `watch_events`, calculate 7-day retention after a user's first watch.
   - Topic: cohort retention
   - Think about: first watch date, timezone

19. [ ] Given `ratings(user_id, title_id, rating, rated_at)`, find titles with at least 100 ratings and an average rating above 4.5.
   - Topic: filtering aggregates
   - Think about: duplicate ratings from same user

20. [ ] Given `watch_events`, find users who watched at least 3 episodes of the same series on the same day.
   - Topic: grouping, product behavior
   - Think about: episode metadata joins

## Uber/Lyft-Style Questions

21. [ ] Given `ride_requests(request_id, rider_id, driver_id, requested_at, accepted_at, completed_at, status)`, calculate driver acceptance rate by hour.
   - Topic: event metrics
   - Think about: null accepted time, cancelled rides

22. [ ] Given `ride_requests`, calculate cancellation rate by rider, driver, and city.
   - Topic: conditional aggregation
   - Think about: status definitions

23. [ ] Given `driver_locations(driver_id, ping_time, lat, lon)`, detect missing location pings longer than 10 minutes during active rides.
   - Topic: time gaps
   - Think about: active ride windows

24. [ ] Given `rides(driver_id, completed_at, fare_amount)`, calculate each driver's rolling 7-day earnings.
   - Topic: rolling windows
   - Think about: days with no rides

25. [ ] Given `rides(rider_id, completed_at)`, find riders whose first 3 completed rides happened within 7 days of signup.
   - Topic: activation metrics
   - Think about: ranking rides per rider

## Airbnb-Style Questions

26. [ ] Given `bookings(booking_id, listing_id, guest_id, host_id, checkin_date, checkout_date, status)`, calculate occupancy rate by listing and month.
   - Topic: date expansion, aggregation
   - Think about: cancelled bookings, overlapping bookings

27. [ ] Given `listing_prices(listing_id, effective_date, nightly_price)`, find the price active for each booking date.
   - Topic: temporal joins
   - Think about: missing price records

28. [ ] Given `reviews(listing_id, guest_id, rating, review_date)`, find hosts with an average rating above 4.8 across at least 20 reviews.
   - Topic: joins, aggregate filters
   - Think about: review duplicates

29. [ ] Given `search_results(search_id, listing_id, rank_position)` and `bookings`, calculate booking conversion by search rank bucket.
   - Topic: funnel analysis
   - Think about: repeated listings in search results

30. [ ] Given `messages(sender_id, receiver_id, sent_at)`, calculate median host response time to guest messages.
   - Topic: pairing events
   - Think about: multiple guest messages before host reply

## Stripe/Fintech-Style Questions

31. [ ] Given `payments(payment_id, merchant_id, user_id, amount, status, payment_time)`, calculate payment success rate by merchant and day.
   - Topic: conditional aggregation
   - Think about: retries and duplicate payment attempts

32. [ ] Given `payments`, detect users with 5 failed payments followed by a successful payment within 1 hour.
   - Topic: sequence detection
   - Think about: rolling windows

33. [ ] Given `transactions(account_id, transaction_time, amount)` and `balances(account_id, balance_time, balance)`, reconcile transaction sums against balance changes.
   - Topic: reconciliation
   - Think about: missing transactions, pending transactions

34. [ ] Given `invoices(invoice_id, customer_id, due_date, amount)` and `payments(invoice_id, paid_at, amount)`, calculate unpaid invoice aging buckets.
   - Topic: finance analytics
   - Think about: partial payments

35. [ ] Given `cards(card_id, user_id)` and `payments(card_id, user_id, payment_time)`, find cards used by more than 3 users in a day.
   - Topic: fraud detection
   - Think about: shared family cards versus suspicious cards

## Snowflake/Databricks-Style Questions

36. [ ] Given `table_lineage(upstream_table, downstream_table)`, return all downstream tables impacted by a source table.
   - Topic: recursive SQL
   - Think about: dependency depth, cycles

37. [ ] Given `query_history(query_id, warehouse_id, started_at, ended_at, credits_used)`, calculate cost by user and warehouse per day.
   - Topic: warehouse observability
   - Think about: overlapping queries

38. [ ] Given `table_storage(table_name, snapshot_date, bytes)` and `table_access(table_name, accessed_at)`, find large tables unused in the last 90 days.
   - Topic: cost optimization
   - Think about: recently created tables

39. [ ] Given `data_quality_results(table_name, check_name, run_time, status)`, find tables with 3 consecutive failed checks.
   - Topic: pipeline quality
   - Think about: check order and missing runs

40. [ ] Given `schema_snapshots(table_name, column_name, data_type, snapshot_date)`, detect schema drift between yesterday and today.
   - Topic: metadata SQL
   - Think about: renamed columns versus dropped and added columns

## LinkedIn-Style Questions

41. [ ] Given `connections(user_id, connected_user_id)` and `profile_views(viewer_id, profile_id, viewed_at)`, find profile views from second-degree connections.
   - Topic: graph joins
   - Think about: excluding first-degree connections

42. [ ] Given `job_applications(user_id, job_id, applied_at)` and `job_views(user_id, job_id, viewed_at)`, calculate apply rate by job category.
   - Topic: conversion metrics
   - Think about: views after application

43. [ ] Given `messages(sender_id, receiver_id, sent_at)`, calculate response rate within 48 hours by sender seniority.
   - Topic: event pairing
   - Think about: many messages before one reply

44. [ ] Given `user_skills(user_id, skill)` and `job_skills(job_id, skill)`, calculate skill match percentage for each user-job pair.
   - Topic: many-to-many joins
   - Think about: duplicate skills

45. [ ] Given `feed_impressions(user_id, post_id, impression_time)` and `post_clicks(user_id, post_id, click_time)`, calculate feed CTR by user cohort.
   - Topic: attribution joins
   - Think about: multiple impressions before click

## DoorDash/Instacart-Style Questions

46. [ ] Given `deliveries(delivery_id, courier_id, accepted_at, picked_up_at, delivered_at)`, calculate courier idle time between deliveries.
   - Topic: lag, time intervals
   - Think about: overlapping deliveries

47. [ ] Given `orders(order_id, store_id, placed_at, delivered_at, promised_delivery_at)`, calculate SLA breach rate by store.
   - Topic: operational analytics
   - Think about: cancelled orders

48. [ ] Given `order_items(order_id, item_id, requested_qty, fulfilled_qty)`, calculate item substitution and out-of-stock rate.
   - Topic: fulfillment metrics
   - Think about: partial fulfillment

49. [ ] Given `courier_events(courier_id, event_type, event_time)`, calculate active courier hours per day.
   - Topic: event intervals
   - Think about: missing offline events

50. [ ] Given `orders(customer_id, order_time)`, calculate reorder rate within 14 days of first order.
   - Topic: retention
   - Think about: first order definition

## General Company-Style Hard Questions

51. [ ] Given `raw_events(event_id, event_time, ingested_at)`, find late-arriving events and quantify how much they changed historical daily counts.
   - Topic: late data
   - Think about: event date versus ingestion date

52. [ ] Given `customer_dim(customer_id, effective_start, effective_end, is_current)`, find SCD Type 2 overlaps, gaps, and multiple current records.
   - Topic: dimensional modeling
   - Think about: inclusive versus exclusive end dates

53. [ ] Given `cdc_events(primary_key, operation, event_time, sequence_number)`, reconstruct the latest state of each row.
   - Topic: CDC
   - Think about: deletes, duplicate sequence numbers

54. [ ] Given `job_runs(job_id, started_at, finished_at, status)`, identify jobs whose runtime increased for 5 consecutive runs.
   - Topic: observability
   - Think about: failed runs and missing durations

55. [ ] Given `file_arrivals(source_name, expected_date, arrived_at, file_size)`, detect missing, late, duplicate, and unusually small files.
   - Topic: ingestion monitoring
   - Think about: expected schedule table

56. [ ] Given `table_row_counts(table_name, snapshot_time, row_count)`, find tables with gradual row-count decline over 7 snapshots.
   - Topic: anomaly detection
   - Think about: seasonality

57. [ ] Given `api_logs(endpoint, request_time, status_code)`, calculate rolling 5xx error rate over 1-hour windows.
   - Topic: rolling windows
   - Think about: low request volume

58. [ ] Given `orders` and `refunds`, calculate net revenue by customer cohort and month since first order.
   - Topic: cohort revenue
   - Think about: refunds after cohort month

59. [ ] Given `events(user_id, event_name, event_time)`, find the first valid funnel completion where steps happen in order but can have other events between them.
   - Topic: ordered funnels
   - Think about: repeated funnel starts

60. [ ] Given `employee_shifts(employee_id, shift_start, shift_end)`, merge overlapping shifts before calculating total hours.
   - Topic: interval merging
   - Think about: adjacent shifts

