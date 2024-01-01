---
sidebar_position: 5
title: Metrics Account Usage and Throttling
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn about Logz.io's Metrics account and Throttling mechanism
keywords: [Metrics, Throttle, Throttling, Metrics account, UTS, Unique Time Series]
---

Your Logz.io Metrics account ingests [**Unique Time Series (UTS)**](/docs/user-guide/infrastructure-monitoring/introduction-to-prometheus/explore-metrics-prometheus/#calculating-infrastructure-monitoring-usage), a collection of pairs, each including a timestamp and value.

## How Metrics are Measured

Metric account usage is measured according to the average hourly ingestion of UTS, allowing you to ingest more data than your daily plan allows without incurring additional charges. 

For example, if the hourly metrics plan allows ingesting 100,000 UTS per hour and you send 50,000 UTS in the first hour, followed by 150,000 UTS in the second hour, the average usage remains within your daily plan limit of 100,000 UTS.

In addition, Logz.io provides a safety net to avoid data surges during infrastructure changes, allowing up to twice your plan's hourly limit (e.g., plan 100,000 = 200,000 UTS/hour) unless your account admin specifies otherwise.

:::info Note
If your hourly average exceeds your account plan for a continuous period of 24 hours, you'll be charged according to your On Demand settings. [Learn more about On Demand](/docs/user-guide/admin/logzio-accounts/on-demand/).
:::

## Logz.io's Throttling Mechanism

However, if you exceed your plan and safety net, a **throttling** mechanism is activated. It briefly limits **new** UTS ingestion until the next hour, ensuring system stability. 

Throttling helps maintain system stability while allowing flexibility in data ingestion.

Account admins receive email alerts when the account ingestion approaches its hourly limit and another email when throttling starts.

To avoid throttling and to ensure new UTS are ingested, account admins can purchase or upgrade the relevant metrics account. If there's additional UTS data available from other metrics accounts, admins can re-allocate it to stop the throttling process from the [Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts?product=Logs) page.
