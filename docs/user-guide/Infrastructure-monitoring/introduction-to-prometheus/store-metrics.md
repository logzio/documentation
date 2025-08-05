---
sidebar_position: 10
title: How Logz.io Stores Prometheus Metrics
description: Learn how Logz.io stores Prometheus metrics
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [metrics, infrastructure monitoring, Prometheus, monitoring, observability, logz.io, downsampling, data retention, query performance]
noindex: true
---

Logz.io stores your Prometheus metrics in multiple resolutions to ensure fast performance for long time ranges while preserving the precision needed for troubleshooting.

## Why use multiple resolutions?

Storing every single data point (raw metrics) over long periods can slow down queries. To avoid this, Logz.io automatically summarizes older data using aggregation techniques. This allows for fast historical queries without compromising accuracy for recent data.

## What is downsampling?

Downsampling means storing fewer data points over time by summarizing raw metrics. Instead of keeping every scrape, Logz.io stores statistical summaries like count, sum, min, max, and counter at set intervals.

This process happens in two phases:

| Metric age | Stored resolution | Available aggregations |
|    --    |      --      |        --        |
| 0–40 hours | Raw (scrape rate)	| All raw samples |
| 40h–10 days | 5 minutes | Count, sum, min, max, counter |
| 10 days and up | 1 hour | Count, sum, min, max, counter |

:::note
Downsampling is automatic and helps improve query performance for large time ranges.
:::

## What does this mean for your queries?

The resolution used depends on your selected time range:

* Last 40 hours or less - Uses raw data
* 40 hours to 10 days - Uses 5-minute summaries
* 10 days or more - Uses 1-hour summaries

For example, if you view a chart showing 30 days of data, the system will use the 1-hour resolution. If you zoom in to the last 6 hours, it will automatically switch to raw data.

This ensures a balance between detailed visibility and high-speed queries.

## Can I disable downsampling?

Downsampling is always enabled in Logz.io to ensure optimal performance across different time ranges. Raw data is retained for 30 days. After that, only the downsampled summaries are available.

If you need to investigate a specific event (like a spike) that occurred more than 30 days ago, the summarized data will provide a high-level view, but raw-level granularity won’t be available.