---
sidebar_position: 10
title: How Logz.io Stores Prometheus Metrics
description: Learn how Logz.io stores Prometheus metrics
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [metrics, infrastructure monitoring, Prometheus, monitoring, observability, logz.io, downsampling, data retention, query performance]
---

Logz.io stores your Prometheus metrics in multiple resolutions to ensure fast performance for long time ranges while keeping the precision needed for troubleshooting.

## Why use multiple resolutions?

Storing every single data point (raw metrics) over a long period can slow down queries and increase storage requirements. To avoid this, Logz.io automatically summarizes older data using aggregation techniques. This provides fast queries for historical views while maintaining accuracy for shorter time ranges.

## What is downsampling?

Downsampling means storing fewer data points over time by summarizing raw metrics. Instead of keeping every scrape, Logz.io keeps statistical summaries like count, sum, min, max, and counter at set intervals.

This process happens in two phases:


| Metric age | Stored resolution | Available aggregations |
|    --    |      --      |        --        |
| 0–40 hours | Raw (scrape rate)	| All raw samples |
| 40h–10 days | 5 minutes | Count, sum, min, max, counter |
| 10 days and up | 1 hour | Count, sum, min, max, counter |

:::note
This process doesn’t save storage space; it actually creates additional summarized datasets. The goal is to improve query speed for large time ranges.
:::

## What does this mean for your queries?

The resolution used depends on your selected time range:

* **Last 40 hours or less** - Uses raw data
* **40 hours to 10 days** - Uses 5-minute summaries
* **10 days or more** - Uses 1-hour summaries

For example, if you view a chart showing 30 days of data, the system will use the 1-hour resolution. If you zoom in to the last 6 hours, it will automatically switch to raw data.

This ensures a balance between detailed insights and high performance.

## Can I disable downsampling?

Downsampling is always enabled in Logz.io. If you want access to raw data from older time ranges (For example, a spike from 30 days ago), make sure your raw metric retention covers that period. Otherwise, only the summarized version will be available.