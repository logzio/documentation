---
sidebar_position: 5
title: Throttling in Your Metrics Account
---

Logz.io provides a throttling mechanism to assist you in effectively managing the volume of data in your Metrics account. This mechanism comes into play when your account exceeds the predefined hourly limit for Unique Time Metrics (UTS) sent.

## How Throttling Works

Your account has an hourly limit for UTS data ingestion. Even after reaching this limit, you can continue to ingest data based on your [On Demand](/docs/user-guide/admin/logzio-accounts/on-demand/) settings. Throttling only activates when you exceed both your hourly limit and On Demand limit.


Throttling, when triggered, temporarily restricts the ingestion of new Unique Time Metrics until the start of the next hour.

Account administrators will receive an email notification when the account is approaching its hourly UTS limit, indicating that throttling is about to begin.

Another email notification will be sent when the account surpasses its On Demand limit.

This throttling mechanism ensures system stability while allowing flexibility in data ingestion based on your On Demand settings.




<!-- ![Edit a panel](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/metric-alert-edit.png)-->


