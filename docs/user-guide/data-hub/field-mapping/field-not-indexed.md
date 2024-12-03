---
sidebar_position: 2
title: Field Not Indexed
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Troubleshoot Field Not Indexed issue in OpenSearch Dashboards
keywords: [troubleshoot, field, log, mapping, observability, monitoring, issues]
---



Sometimes, it will appear that a field in OpenSearch Dashboards is not mapped. The mapping icon will show a ?<i class="fas fa-question"></i> question mark, indicating that the field is not mapped. 


![field not indexed](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/field-not-indexed_aug2021.png)


Whenever you see the message **Field not indexed**, this is simply an indication that the field is not indexed because nothing in your OpenSearch Dashboards account is dependent on it. It wasn't required for any of your account's alerts, filters, saved searches, visualizations, dashboards, or any other objects.

### If a field is not indexed

If a field is not mapped in your logs, there are a few actions you won't be able to perform on it:

1. You can't visualize it.
2. You can't filter on it. It simply won’t appear in the drop-down filter list.

### Add a field to OpenSearch Dashboards' default mapping

You can always add a field to the list of required fields.

In OpenSearch Dashboards, on the left preview menu, identify the unmapped field. Click on the unmapped field to select it and click on the button **Field not indexed**.

The field will now be added to your default OpenSearch Dashboards mapping.

