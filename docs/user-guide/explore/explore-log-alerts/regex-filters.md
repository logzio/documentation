---
sidebar_position: 6
title: Using Regex Filters in Alerts
description: How to use regex filters in your Logz.io alerts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, alerts, regex, filters, log alerts, log analysis, observability]

---


You can refine the data in notifications using regex filters. Adding a regex filter allows you to select specific data to include in the alert output.

There is no danger that a regex filter will disrupt the notification.

* If the regex matches the relevant data, only the desired results will be displayed.
* If the regex _does not_ match, the filter will be ignored, and the alert output will include the full, unaltered value.




## Examples of Regex Filters


:::note
When creating a regex filter, consider **all characters** preceding the one you're trying to filter.
:::


The custom output will display the data matched in the capture group(s) of the regular expression.


| Value | Regex filter | Output |
|---|---|---|
| logzio-support-host-1 | `logzio-(.*)` | support-host-1 |
| logzio-support-host-1 |`(.*)-support(.*)` | logzio-host-1 |
| logzio-support-host-1 | `.*(\d+)` | 1 |


For example, if you have a hostname "logzio-support-host-1", then a regular expression of `logzio-(.*)` will give you **"support-host-1"**.

You can also capture multiple parts of a string. For example, if you run `(.*)-support(.*)` on the previous example, you will get **"logzio-host-1"**. This is because the first capture group matches **"logzio"** and the second capture group matches **"-host-1"** and the results are concatenated in the field.

If you only want to capture the number **"1"** from **"logzio-support-host-1"**, you can use `.*(\d+)`. This pattern matches any character up to the first number and captures that number.