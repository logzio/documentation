---
sidebar_position: 4
title: Dashboard Variables
description: Configuring Metrics drilldown links
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [metrics, infrastructure monitoring, drilldown, Prometheus, monitoring, dashboard, observability, logz.io]
---

Dashboard variables allow you to apply filters and drill-down links to your dashboards.

**Prerequisites**:
You need to enable [Metrics](https://app.logz.io/#/dashboard/metrics/) in your Logz.io account.


## Add a new dashboard and variable

Navigate to your [Metrics dashboard](https://app.logz.io/#/dashboard/metrics), click the cogwheel icon in the upper right corner of the dashboard toolbar, and select **Variables > New**.

![Add Metrics interface variables](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/metrics-cogwheel.png)

<h3 id="define"> Define the variable</h3>

In this example, we'll focus on the most common variable type — `query` variable. Other variable types are available in the [official documentation](https://grafana.com/docs/grafana/latest/variables/variable-types/).

<h3 id="general"> General settings: </h3>

* **Name**: Provide a short placeholder value for the variable
* **Label**: Set a human-readable label for the filter control at the top of your dashboard
* **Type**: Choose `Query`
* We recommend leaving **Hide** empty checked

_Enabling the Hide option for a variable in Grafana removes it from the dashboard's variable dropdown menu, streamlining the user interface while still allowing the variable to function in queries and dashboard settings. This keeps the dashboard clean and focused by concealing unnecessary variables from users without affecting their underlying functionality. [Read more about variables in Grafana](https://grafana.com/docs/grafana/latest/dashboards/variables/)._


//![Variable general settings](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/variables-edit-containername.png)

<h3 id="query"> Query options: </h3>

* **Data Source**: Select your Metrics account. (You can look it up [here](https://app.logz.io/#/dashboard/settings/manage-accounts))
* **Refresh**: The recommended setting is to automatically occur **On Time Range Change**
* **Query Field**: Enter your query. The full list is available in Grafana's [official documentation](https://grafana.com/docs/grafana/latest/datasources/prometheus/#query-variable). Here are some common examples:

    * Getting label values with no specified conditions. For example, `label_values(container)`
    * Getting label values for a specific metric. The metric will come first, then the label's name, separated by a comma. For example: `label_values(container_cpu_usage_total,container)`
    * Getting label values for a specific metric and previous variable. The metric will come first, followed by the previous variable in curly brackets, then the label's name, separated by a comma. For example: `label_values(container_cpu_usage_total{cluster_name=~”$cluster”},container)`



//![Query field preview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/metricspreview-of-variables.png)



<h3 id="selection"> Query field preview: </h3>

Configure the remaining options as needed for your metrics.

When finished, scroll to the bottom of the page and click **Update**. 

You are now ready to use the variable in your new dashboard.


<h3 id="addons"> Additional resources: </h3>

* To learn more about Prometheus and PromQL, check out our [examples and best practices guide](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/introduction-to-prometheus/promql-query/). 
* Looking to configure drilldown links? [Read our guide](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/log-correlations/explore-in-logs-drilldown-links/).
