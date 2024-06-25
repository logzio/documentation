---
sidebar_position: 3
title: Log Metrics
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Visualize your log data into insightful graphs and dashboards.
keywords: [Data hub, data optimization, optimization, log metrics, metrics, recommendations]
---


Create graphs and dashboards directly from your log files.

LogMetrics utilizes the full power of PromQL, letting you visualize numeric-based data inside your logs, including latency, request time, volumes of data sent, and more.

By converting log data into metrics, you get a visual representation of your logs which you can monitor in real-time without paying for growing data volumes.


## Which types of metrics can you create?

With LogMetrics, you can create the following types of metrics:

|**Metric**|**Type**|**Example query**|
|----------|--------|-----------------|
|Count|Counter|`rate(metric_name_count{foo=”bar”}[5m])`|
|Sum|Gauge|`sum(metric_name_field_sum{}) by (foo)`|
|Average|Gauge|`avg(metric_name_field_avg{}) by (foo)`|
|Minimum|Gauge|`min(metric_name_field_min{}) by (foo)`|
|Maximum|Gauge|`max(metric_name_field_max{}) by (foo)`|


## Configure LogMetrics

:::warning note
Log Metrics rules should be configured in the account storing the relevant logs.
:::


### 1. Find the relevant logs

You can create a LogMetric from OpenSearch Dashboards by clicking the **Create Metric** button at the top. This button becomes enabled whenever you apply a filter to your search. 

Note that Lucene queries, free text search, "is between" filters, and regular expressions (regex) **are not supported**. Filters must use exact values only.


![OSD to metrics](https://dytvr9ot2sszz.cloudfront.net/logz-docs/logs2metrics/osd-to-metric.png)

You can also create a custom LogMetrics by navigating to [**Data Hub > LogMetrics > New Metric**](https://app.logz.io/#/dashboard/logs-to-metrics/new).


### 2. Name your LogMetric


Give your metric a meaningful name. You can use letters, numbers, and underscores.



### 3. Set the metric


Use the **Group by** option to add dimensions to measure metrics per unique values, based on the fields you're adding. You can bundle up to 6 fields together.

Next, choose how you would like to aggregate your data: by log count, fields, or both. 

### 4. Set the output

Use the dropdown to select which Metrics account will store the metrics output. The metrics are saved in 1-minute granularity and downsampled later for best performance. Retention is based on the settings of the chosen metrics account.


Next, you can add a description. The description is visible on the main LogMetrics page. We recommend making your description helpful so both you and your team members will be able to understand their purpose.

Finally, you can add labels to your metrics. Labels are static values that can be helpful for filtering. For example, you can use labels to create filtered visualizations and dashboards.

Click **Save** to create your LogMetrics. 



## View and manage your LogMetrics

After saving your LogMetrics, you can view and manage it on the main [Log Metrics](https://app.logz.io/#/dashboard/logs-to-metrics/definitions) page. 

![Logs to metrics main page](https://dytvr9ot2sszz.cloudfront.net/logz-docs/logs2metrics/logmetrics-main.png)

Toggle the **Status** button to disable/enable the LogMetrics. In addition, you can hover over the relevant metric to view additional abilities, including:

* **Explore in metrics** - view the dashboard in Grafana.
* **Edit** - Edit the existing metric.
* **Delete** - Delete the metric. This can't be undone. 
* **Duplicate** - You can duplicate an existing metric by clicking on the menu <i class="li li-ellipsis-v"></i> and choosing Duplicate. 


#### Additional information

LogMetrics has the following requirements:

* You can only use field filters. Lucene's free text is not supported.
* The values are case-sensitive. Make sure you’re using the correct values.
* The Group by option can group up to 6 fields.

## Common use cases and solutions

### Avg aggregation discrepancy

The average value in your logs does not match the value in your metrics dashboard.

This can happen if the time interval is too long. In Lucene queries, the average is 10 minutes for all raw data, while Log Metrics presents an average gauge for every small interval.

<h3 id="avg-solution">Solution</h3>

Compare apples to apples and ensure you use the same time interval.

When comparing smaller timeframes (up to 1 hour), using the same interval in both Lucene and Prometheus queries is important. Otherwise, the average will shift over time.

![Comparing logs to metrics](https://dytvr9ot2sszz.cloudfront.net/logz-docs/logs2metrics/apple-to-apple.png)

### Higher values in Log Metrics vs. OpenSearvh Dashboards

Log Metrics (or API) shows higher values than OpenSearch Dashboards aggregation.


This is [a known Prometheus behavior](https://promlabs.com/blog/2020/07/02/selecting-data-in-promql/#lookback-delta) and is not affected by your data.


<h3 id="avg-values">Solution</h3>
 
You can query a shorter timeframe in Grafana (e.g., 12:05 - 13:00 instead of 12:00 - 13:00), or use the `max_over_time` function in Prometheus. The latter will only work for querying metrics grouped by specific dimensions: hostname, method, etc.


`max_over_time(<metric_name>{<dim_1>="value", <dim_2>="<value>"}[15s])`


### Data gaps in dashboard

There's a gap in Log Metrics generated metrics, or metric values are lower than OpenSearch Dashboards queries. 

This happens because every station in the pipeline evaluates some aspect of shipped data, such as validity, latency, and rate limiting. Different components in the infrastructure can drop Log Metrics due to various reasons.

![Data gaps](https://dytvr9ot2sszz.cloudfront.net/logz-docs/logs2metrics/metric-gaps.png)

<h3 id="avg-dropped">Solution</h3>

There are sevaral things you can do to alleviate the dropped data:

* Ensure that all integrations properly configure logs to send with timestamps or refrain from sending any timestamps at all.
* Verify that the target Logz.io metrics plan has enough space to accommodate the required amount of UTS
* Avoid sending big batches of logs at a time. This can hurt the latency and can lead to lost data points
