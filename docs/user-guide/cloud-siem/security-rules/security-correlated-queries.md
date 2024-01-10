---
sidebar_position: 3
title: Correlated Rules
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Investigating correlated rules in Logz.io's Cloud SIEM
keywords: [SIEM, rules, correlated rules, managing threats, Security information]
---


Some security incidents are best detected by a sequence of logs originating from different products, i.e. log types.

For example: an email attachment followed by a malware infection.
In this example, the first event is detected by an email security product and the second event is detected by an endpoint security product. In this case 2 separate events can be defined using a correlated rule.

Correlated events are instrumental for reducing false-positives. By defining a more specific use case that contains 2 scenarios, the trigger can be more sensitive and reduce unwanted noise.


## Investigate correlated rules

You can view all recently triggered rules from your [Summary](https://app.logz.io/#/dashboard/security/summary) dashboard.

When a correlated rule triggers, it writes 2 event logs - 1 per query. The event logs will be numbered 1/2 and 2/2, respectively. Each event log will have its own **Investigate** drilldown link.

![Investigate correlated events](https://dytvr9ot2sszz.cloudfront.net/logz-docs/correlated-alerts/2-event-logs.png)

The best way to begin investigating a correlated event is to filter for the matching join values to narrow the list. Hover over the field `logzio-alert-join-values` and click **<i class="fas fa-search-plus"></i>** to filter for its value. Then click the **Investigate** link to dive into the details.
