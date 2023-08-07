---
sidebar_position: 4
title: Dashboard Variables
---

Variables will allow you to apply filters on your dashboards and drilldown links.


**Before you begin, you'll need**:
[Metrics](https://app.logz.io/#/dashboard/metrics/) in your Logz.io metrics account.


### Add a new dashboard and variable

* In the Metrics left menu, click <i class="fas fa-plus"></i>.
* Click <i class="fas fa-cog"></i> in the dashboard toolbar (upper right corner).
* Select **Variables** > **Add variable**.

![Add Metrics interface variables](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/metrics-variables.png)

### Define the variable

In this example, we will be focusing on the most common variable type - `query` variable. However, there are other variable types - you can see the complete list in the [official documentation](https://grafana.com/docs/grafana/latest/variables/variable-types/).


Fill in the form, starting with the **General** section.

* Give a short variable **Name**. This is the placeholder value this variable will use.
* Set a human-readable **Label**. This is the filter control at the top of your dashboard.
* In the **Type** list, choose **Query**.
* We recommend leaving **Hide** empty.

![Variable general settings](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/variables-edit-containername.png)


Next, fill in the query options.

For the **Data source**, select your Metrics account. (You can look it up [here](https://app.logz.io/#/dashboard/settings/manage-accounts).)

We recommend setting **Refresh** to automatically occur **On Time Range change**.

The **Query** field is where things get really fun. There are several options here, we will be focusing on the main ones (you can see the full list in the [official documentation](https://grafana.com/docs/grafana/latest/datasources/prometheus/#query-variable)):

* Getting label values with no specified conditions. For example: `label_values(container)`.
* Getting label values specified to a metric. The metric will come first, then the label's name, separated by a comma. For example: `label_values(container_cpu_usage_total,container)`.
* Getting label values specified to a metric and a previous variable. The metric will come first, followed by the previous variable in curly brackets, then the label's name, separated by a comma. For example: `label_values(container_cpu_usage_total{cluster_name=~”$cluster”},container)`.

![Query field preview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/metricspreview-of-variables.png)


### Configure the remaining options and save

You can set the remaining options to whatever makes the most sense for your metrics.

When finished, scroll to the bottom of the page and click **Update**.

You're now ready to use the variable in your new dashboard.

###### Additional resources

* To learn more about Prometheus and PromQL, check out our [examples and best practices guide](https://docs.logz.io/user-guide/infrastructure-monitoring/prometheus-promql-queries.html). 
* Looking to configure **Explore in OpenSearch Dashboards** drilldown links? [Read our guide](/user-guide/infrastructure-monitoring/explore-in-logs-drilldown-links.html).
