---
sidebar_position: 7
title: Set Alert Triggers
description: Configure triggers for your alerts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, alerts, triggers, log alerts, log analysis, observability]
---


The same alert can potentially trigger many times over a short period of time. If it is set to send out notifications, it can swamp your channels and get too noisy.

To avoid this problem, you can add a waiting period between alert notifications from anywhere between 5 minutes to 24 hours.

![Recipients and wait between notifications](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/recipients-and-wait.png)

### Alert's escalations and de-escalations configuration

If you add a waiting period between notifications, they do not delay notifications of escalations or de-escalations.

If you have several thresholds with different severities configured for an alert, each is evaluated independently. If the same alert triggers multiple times within the waiting period but for _different thresholds_, a notification for each threshold is sent out without waiting.

![Recipients and wait between notifications](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/multiple-thresholds.png)

### Group alert triggers by fields

If an alert includes group-by fields, it will be evaluated independently per set of results.

When you group results by a field, you take the log results and divide them into groups (i.e., "buckets" in OpenSearch Dashboards terminology) by the values returned for that field. That is, _each value or set of values_ is considered a separate event.

If the same alert triggers multiple times within the waiting period but for _different values_, the notifications will be sent out without delay. In other words, the waiting period will only affect notifications for the exact same set of group-by results.

For example, let's take an alert that groups results by city. This alert will trigger per city or set of cities. If this alert triggers for `Paris and London` and `Paris, London, and Berlin`, both alerts will be sent without waiting because they are triggered for different values.