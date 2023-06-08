---
sidebar_position: 4
---

# LogMetrics


Create graphs and dashboards directly from your log files.

LogMetrics utilizes the full power of PromQL, letting you visualize numeric-based data inside your logs, including latency, request time, volumes of data sent, and more.

By converting log data into metrics, you get a visual representation of your logs which you can monitor in real-time without paying for growing data volumes.

###### On this page


#### Which types of metrics can you create?

With LogMetrics, you can create the following types of metrics:

|**Metric**|**Type**|**Example query**|
|----------|--------|-----------------|
|Count|Counter|`rate(metric_name_count{foo=”bar”}[5m])`|
|Sum|Gauge|`sum(metric_name_field_sum{}) by (foo)`|
|Average|Gauge|`avg(metric_name_field_avg{}) by (foo)`|
|Minimum|Gauge|`min(metric_name_field_min{}) by (foo)`|
|Maximum|Gauge|`max(metric_name_field_max{}) by (foo)`|


#### Configure LogMetrics




##### Find the relevant logs


You can create a LogMetric from OpenSearch Dashboards by clicking the **Create Metric** button at the top. This button is enabled whenever you apply a filter to your search, and currently, it does not support Lucene queries, free text search, or "is between" filters.

![OSD to metrics](https://dytvr9ot2sszz.cloudfront.net/logz-docs/logs2metrics/osd-to-metric.png)

You can also create a custom LogMetrics by navigating to [**Data Hub > LogMetrics > New Metric**](https://app.logz.io/#/dashboard/logs-to-metrics/new).


##### Name your LogMetric


Give your metric a meaningful name. You can use letters, numbers, and underscore.



##### Set the metric


Use the **Group by** option to add dimensions to measure metrics per unique values, based on the fields you're adding. You can bundle up to 6 fields together.

Next, choose how you would like to aggregate your data; by log count, fields, or both. 

##### Set the output

Use the dropdown to select which Metrics account will store the metrics output. The metrics are saved in 1-minute granularity and downsampled later for best performance. Retention is based on the settings of the chosen metrics account.


Next, you can add a description. The description is visible on the main LogMetrics page. We recommend making your description helpful so both you and your team members will be able to understand what’s their purpose.

Finally, you can add labels to your metrics. Labels are static values that can be helpful for filtering. For example, you can use labels to create filtered visualizations and dashboards.

Click **Save** to create your LogMetrics. 



#### View and manage your LogMetrics

After saving your LogMetrics, you'll be able to view and manage it on the main [Log Metrics](https://app.logz.io/#/dashboard/logs-to-metrics/definitions) page. 

![Logs to metrics main page](https://dytvr9ot2sszz.cloudfront.net/logz-docs/logs2metrics/logmetrics-main.png)

Toggle the **Status** button to disable/enable the LogMetrics. In addition, you can hover over the relevant metric to view additional abilities, including:

* **Explore in metrics** - view the dashboard in Grafana.
* **Edit** - Edit the existing metric.
* **Delete** - Delete the metric. This can't be undone. 
* **Duplicate** - You can duplicate an existing metric by clicking on the menu <i class="li li-ellipsis-v"></i> and choosing Duplicate. 


### Additional information

LogMetrics has the following requirements:

* You can only use field filters. Lucene's free text is not supported.
* The values are case-sensitive. Make sure you’re using the correct values.
* The Group by option can group up to 6 fields.

