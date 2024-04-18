---
sidebar_position: 2
title: Drop Log Filters
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Keep unneeded logs out of your account with drop filters.
keywords: [Data hub, data optimization, optimization, drop filters, rollups, metrics, recommendations]
---



Drop filters offer a great way to filter out logs from an account to help manage your account volume and lower costs.

Drop filters check if incoming logs match specific criteria exactly, based on field and value. If a log matches an active drop filter in your account, it won’t be indexed, so you won’t see it in your OpenSearch Dashboards. Such logs can't be searched, won't trigger alerts, and won't show up in dashboards or reports. However, these logs will still be archived if you have log archiving turned on.

To get started with Drop Log Filters, navigate to [Data Hub > Drop Filters > Log](https://app.logz.io/#/dashboard/tools/logs-drop-filters).

![Drop filters logs overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/drop-filters/drop-filter-log-main.png)

The drop filters table lists all your filters, whether they are active or not. You can see the rule, description, and status for each filter. You can easily switch any filter on or off whenever you like, and the changes will take effect in just about a minute.

## Add a new Drop Log Filter

Click on **+ Add drop filter**.

Select a specific log type to filter, or choose **All** to apply the filter across all log types.

Next, set fields and values. You can add up to three field-value pairs per filter. Make sure each pair matches exactly as **drop filters are case-sensitive**.

For example, if logs from a Docker container include the pair:


`{ "docker.container.name": "system-logs" }`


You would set the Field to `docker.container.name` and the **Value** to `system-logs`. Logs will not be filtered if the **Value** is set differently, such as to `system`.

Confirm the settings by checking the acknowledgment box and clicking **Apply filter** to activate.


<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/drop-filters/new-drop-filter-log-1.png" alt="drawing" width="500"/>


You can create and manage up to 10 drop filters per account.

If you are restoring logs from an archive, consider temporarily deactivating some filters. This ensures that all logs are indexed and visible in your OpenSearch Dashboards.