---
sidebar_position: 1
title: Intro to Explore
description: Getting started with Logz.io's Explore dashboard
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, dashboard, explore, logs, metrics, traces, analytics, log analysis, observability]
---



Logz.io's Explore improves log search by enhancing performance, optimizing user experience, and reducing time to resolution. Navigate and analyze logs efficiently for issue resolution and troubleshooting.


It is optimized for debugging and troubleshooting issues as quickly and effectively as possible.

Explore lets you view logs, metrics, and traces in one unified dashboard. 

[image]


## Explore Dashboards Overview

Explore is designed to investigate and analyze massive volumes of data quickly and easily. Use filters or use the auto complete syntax tool to find the logs that you need, and drill into them using the quick view panel.

1.
2.
3.
List of elements on the page...


Take actions following your results - create an alert, save view, share it, export, etc...

///

What is changing?
Auto query - Auto-complete easy to use interface for building queries using tags, based on Lucene
Quick filters - Predefined fields to quickly drill down into the most common fields
Improved table - Resizable columns, taking quick actions directly from the table without losing context
Improved graph - Group-by a field and quickly visualize stacked or line charts
Detailed view - Drill down into your logs and find new insights and other observability contextual data
Observability - Query traces and metrics along with logs directly from the new Explore page



///

### 1. Select Account

First, decide which accounts you want to search. Managing your accounts is the first step to successful logging. You can create sub accounts to separate data by environment, microservice, team, and more. [Learn more about account management and sub accounts](/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts).

### 2. Apply Filters

OpenSearch Dashboards filters offer the most convenient, powerful, and flexible method for querying logs.

Filters can be used on any mapped fields and can take any number of forms: filter for field exists or does not exist, filter for a field with an exact value match or a field that contains a value among the results, and more. [Learn more about OSD mapping](/docs/user-guide/data-hub/field-mapping/).

One advantage of OpenSearch filters is that they provide guidance that is specific to your dataset.
When OpenSearch maps your data to fields, it also determines which filtering options are relevant. When you add filters, only relevant options appear in the dropdown menus.

Another advantage is that filters can be inverted, temporarily disabled, edited, and more using the filter menu.

### 3. Use the search bar

You can type a search query in Lucene syntax or DQL. It is an alternative to filtering that requires a little familiarity with the search syntax. Almost anything that can be defined in the Search bar can be accomplished using filters as well.

You can also save your search query in case you want to use them again in the future. Save or load search queries by clicking on the **Save** icon located next to the search bar. 

![Save search query](https://dytvr9ot2sszz.cloudfront.net/logz-docs/osd-discover/save-search-query.png)

### 4. Change your time frame and date

The default time frame in OpenSearch Dashboards is always the last 15 minutes.

You can select the time frame in any number of ways, including relative times such as the last hour, today so far, or the day before yesterday, or use absolute times by calendar dates and timestamps.

### 5. View log results

The logs returned by your search are your results - aka "hits". Depending on the time frame you've selected, the results can be set to continuously auto-refresh and can be quite dynamic.

* **Histogram** -  The Histogram shows the distribution of logs over time. It is often easier to see when logs were sent when graphed directly on the timeline. You can also select a time range directly from the histogram using a drag-and-drop motion or by clicking a data bar.

* **Logs** - The log document table displays a preview of your top results, arranged with the most recent results at the top. The default fields are **time** and **message**, but you can toggle the fields that interest you in and out. 

  To expand a log, click it and review the complete log mapped into field:value pairs. You can also switch to the raw JSON.

* **Patterns** - Logz.io groups your logs using advanced clustering techniques to help you identify similar logs by groups, reducing the amount of logs to review. Patterns also help to surface issues and errors that might otherwise go unnoticed. [Learn more](/docs/user-guide/log-management/opensearch-dashboards/opensearch-patterns/).

* **Exceptions** - Logz.io Insights Engine scans your logs for application errors and warnings to help you identify issues that require your attention. [Learn more](/docs/user-guide/log-management/insights/exceptions/).

### 6. Take action following your results

The number of hits shows you the number of results returned by your query. This is the count of the total number of log documents that answer the query criteria.

If you click the **Inspect** function, you can view the query as sent to OpenSearch. This is useful if you are using the [Logz.io API](/api/), for example.

Once you've refined a query to the point that it returns exactly what you are looking for, you can be proactive in any number of ways:

* Create an **alert** to trigger automatically and send out notifications to your preferred endpoints. [Learn how to configure an alert](/docs/user-guide/log-management/log-alerts/configure-alert/).
* **Save** the search to display it in visualizations and dashboards or to load it in the future.
* **Share** results with colleagues or external stakeholders.
* **Export** results to a spreadsheet.


###### Additional resources

* [OpenSearch Dashboards best practices](/docs/user-guide/log-management/opensearch-dashboards/opensearch-best-practices)
* [Create and run advanced searches in OpenSearch Dashboards](https://logz.io/blog/kibana-advanced/)