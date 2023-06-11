---
sidebar_position: 1
---
# Optimize Your Logz.io Data



Logz.io Data Optimization helps you manage and optimize your Logz.io products by offering tailored recommendations and a quick and easy way to drop your logs and metrics.

:::note
You will receive tailored recommendations based on Log data from the last 24 hours and based on Metrics data from the previous 1 hour.
:::

To get started, navigate to **[Data hub > Optimize](https://app.logz.io/#/dashboard/cost)**.



## Explore Metrics and Logs

You can switch between your **Logs** and **Metrics** overview.


The **Metrics** table includes the following details:

* **Name** - Metric's name and its related labels. Click on the labels to view the complete list included in this metric.
* **UTS** - Amount of unique time series used by this metric and a percentage representation of how much it's using.
* **Account** - The accounts that are using this metric.
* **Used** - An indication of how you're using this metric in the account you are signed in to.
* **Actions** - Hover over each metric to reveal the **Drop** button. 
* **Explore** - Clicking on the three dots <i class="li li-ellipsis-v"></i> lets you Rollup or explore this in the Metrics dashboard.

![Optimization hub overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/optimization-hub/optimization-hub-overview.png)

The **Logs** table includes the following details:

* **Type** - The type of the log.
* **Structure** - An overview of the log's build. Click on it to open a side menu with the complete log and its items.
* **Usage** - Amount of GB used by this log and a percentage representation of how much it's using.
* **# of logs** - A numeric value of how many logs exist inside this specific type. The number is updated every 24 hours.
* **Actions** - Hover over each line to reveal the **Drop** button. 
* **Explore** - Clicking on the three dots <i class="li li-ellipsis-v"></i> lets you explore this in OpenSearch Dashboards.

![Optimization hub logs overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/optimization-hub/log-overview.png)


## Filter your Metrics view


The Metrics overview includes two primary filters you can apply: **Account** and **Used**.

The **Account** filter includes all of the accounts associated with your user, and the **Used** filter helps you understand how the data is being used.

You can apply these filters quickly from within the table by clicking on the desired values.

:::tip
To identify which metrics can be optimized, apply the **Not used** filter. The results will include all metrics not used by any dashboard or alert, which you can drop.
:::


![Filter your metrics](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/optimization-hub/click-to-apply-filters.gif)


### Drop and optimize

After viewing and analyzing your data, it's time to optimize your usage by using the drop action.


### Metrics optimization

You can drop individual metrics or logs or perform a bulk-drop action by selecting several metrics or logs.

By clicking on the checkbox next to each metric, you can select it. To select all metrics on the page, click on the checkbox at the top of the table. To select all metrics that match your filter, click on the link at the top of the table. 

![Choose all matches](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/optimization-hub/select-all-metrics.png)

Once selected, a new **Drop** button will appear at the top of the table. Click on it to review all metrics that will be dropped and to get a percentage estimation of how much you'll save.

![Drop all metrics](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/optimization-hub/drop-metrics-bundle.png)

Manage your dropped metrics by navigating to **[Data Hub > Drop filters > Metrics](https://app.logz.io/#/dashboard/tools/metrics-drop-filters)**.

## Logs optimization

You can drop different types of logs by hovering over its line and clicking on the **Drop** button.

![Hover to drop](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/optimization-hub/hover-to-drop.png)

The button opens a dialog where you can customize your drop filter. Select the log type, field, and value you'd like to include in your drop filter, check the acknowledgment button and click **Apply filter**. 

![drop log dialog](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/optimization-hub/new-drop-filter.png)

Manage your dropped logs by navigating to **[Data Hub > Drop filters > Logs](https://app.logz.io/#/dashboard/tools/logs-drop-filters)**.
