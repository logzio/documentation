---
sidebar_position: 7
title: Set Alert Triggers
description: Configure triggers for your alerts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, alerts, triggers, log alerts, log analysis, observability]
---



An alert can trigger multiple times over a short period, potentially overwhelming your notification channels with noise. To mitigate this, you can set a waiting period between alert notifications, ranging from 5 minutes to 24 hours.


![Recipients and wait between notifications](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/recipients-and-wait.png)

### Alert escalations and de-escalations configuration

If you add a waiting period between notifications, they do not delay notifications of escalations or de-escalations.

If you have multiple thresholds with different severities configured for an alert, each threshold is evaluated independently. If the same alert triggers multiple times within the waiting period but for _different thresholds_, a notification for each threshold is sent out without waiting.



![Recipients and wait between notifications](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/multiple-thresholds.png)

### Grouping alert triggers by fields

When an alert includes group-by fields, it is evaluated independently for each set of results.

Grouping results by a field means dividing the log results into distinct groups (or "buckets") based on the values returned for that field. Each _unique value or set of values_ is considered a separate event.

If the same alert triggers multiple times within the waiting period but for _different values_, notifications will be sent out without delay. The waiting period only affects notifications for the exact same set of group-by results.

For example, consider an alert that groups results by city. This alert will trigger separately for each city or set of cities. If the alert triggers for `Paris and London` and then for `Paris, London, and Berlin`, both alerts will be sent without waiting because they are triggered by different sets of values.