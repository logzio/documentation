---
sidebar_position: 6
title: Using regex filters in alerts

---




You can "clean" the data in the notification using regex filters. If you add a regex filter, it will select for the data you want to include in the alert output.

There is no danger that a regex filter will disrupt the notification.

* If the regex matches the relevant data, you will see only the desired results.
* If the regex _does not_ match, the filter will be disregarded and the alert output will include the full value, unaltered.


### Regex filters examples


:::info
When creating a regex filter, you need to take into account **all of the characters** proceeding the one you're trying to filter.
:::

The custom output will display the data that is matched in the capture group(s) of the regular expression.


| Value | Regex filter | Output |
|---|---|---|
| logzio-support-host-1 | `logzio-(.*)` | support-host-1 |
| logzio-support-host-1 |`(.*)-support(.*)` | logzio-host-1 |
| logzio-support-host-1 | `.*(\d+)` | 1 |


For example, if you have a hostname that is "logzio-support-host-1", then a regular expression of `logzio-(.*)` will give you **"support-host-1"**.

You could also capture multiple parts of a string, for example, if you run `(.*)-support(.*)`  on the previous example, you will get **"logzio-host-1"**.  This is because the first capture group matches the **"logzio"** and the second capture group matches the **"-host-1"** and the results are concatenated in the field.

Let's say you only want to capture the **"1"** from **"logzio-support-host-1"** then you can use `.*(\d+)`, this will match any character up until the first number and will capture that number.