---
sidebar_position: 3
title: Drop Metric Filters
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Keep unneeded metrics out of your account with drop filters.
keywords: [Data hub, data optimization, optimization, drop filters, rollups, metrics, recommendations]
---



Drop filters offer a great way to filter out metrics from an account to help manage your account volume and lower costs.

Drop filters check if incoming metrics match certain conditions exactly, based on account and metric name. If a metric matches an active drop filter in your account, it won’t be indexed, it can't be searched, it won't trigger alerts, and it won't show up in dashboards.

To get started with Drop Metrics Filters, navigate to [Data Hub > Drop Filters > Metrics](https://app.logz.io/#/dashboard/tools/metrics-drop-filters).

![Drop filters metrics overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/drop-filters/metric-drop-filter-main.png)

The drop filters table lists all your filters, whether they are active or not. Use the filters at the top of the table to view drop filters for specific accounts or metric names.

You can see the condition and state of each filter. You can easily switch any filter on or off whenever you like, and the changes will take effect in about a minute. Hover over a filter to open additional options: **Edit** and **Delete**.

## Add a new Drop Metric Filter

:::tip note
You can add up to 1,000 Drop Metric Filters.
:::

Click on **+ Add metric drop filter**.

Select the metric account you want to use for this filter and the metric name you wish to filter.

You can add one or more labels and values to your filter criteria to pinpoint specific metrics you want to drop. Note that the label:value pairs match exactly as **drop filters are case-sensitive**.


Click **Apply filter** to create the filter.


<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/drop-filters/drop-metrics-filter-add.png" alt="drawing" width="500"/>


You can create and manage up to 10 drop filters per account.