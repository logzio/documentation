---
sidebar_position: 3
title: Advanced Logz.io Optimization Features
---

After setting up your account and having your data flowing into Logz.io, it’s time to utilize features and strategies to filter out the noise and analyze the data that is most valuable to you.

The following guide will help you understand how to do just that through Logz.io’s capabilities and products.

## Manage your workspaces - Divide and conquer your quota

Logz.io offers a centralized solution, including all the tools and elements needed to gain observability into your data. You can create a **[Sub account](/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts/#main-vs-sub-account)** to help manage usage, volume, and access to the data.

If your account has **[Flexible volume](/user-guide/accounts/flexible-volume.html)**, use it to control how to allocate GB between your main and sub accounts, ensuring you don’t exceed your volume quota.

Shared volume can help cover your indexing needs across accounts instead of reserving capacity in advance, optimizing data distribution, and minimizing the risk of running out of space.

To manage access and permissions, define which data is accessible through the sub account, limiting or granting access to logs, dashboards, visualizations, and saved searches.

In addition, if you have a flexible account, apply **[Utilization metrics](/docs/user-guide/admin/account-volume-optimization/manage-account-usage/#what-are-account-utilization-metrics)** to optimize it. You'll need to apply Utilization metrics per account, by clicking on **Settings > [Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts)** > choosing the relevant account and checking the **Save access utilization metrics** option.

![Utilization metrics](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/utilization--save-account-utilization-metrics.png)

Enabling this option lets you save utilization metrics on a set schedule (every 10, 30, or 60 mins). These metrics include the used data volume for the account and the expected data volume for the current indexing rate.

## Optimize log data with Drop filters & Archive and restore

**[Drop filters](https://docs.logz.io/user-guide/accounts/drop-filters/)** offer a great and easy way to filter out logs you don’t regularly need from your account, which can help reduce the account’s volume and costs.

Once you set up your drop filters, incoming logs that match your account’s active drop filters will not be indexed and will not appear in your OpenSource Dashboards account. 

Dropped logs are not searchable, cannot trigger alerts, and will not appear in dashboards, reports, or anything else. However, if the Archive and restore option is enabled on your account, it will also include the dropped logs.

That’s why we recommend pairing Drop filters with the **[Archive and restore](/user-guide/archive-and-restore/)** feature. Once you set up [Archiving](/user-guide/archive-and-restore/configure-archiving.html) on an S3 or Azure storage container, a carbon copy that holds all of your logs will be sent to the storage of your choice. This copy also includes dropped logs, allowing you to restore all of your logs to easily investigate when issues occur.

Reasons to love Archive and restore:

* Compliance. Archiving to cold storage ensures you have a copy of all logs for years to come.
* If you want to look back at logs outside your retention period with Logz.io, you can [reingest that data](/user-guide/archive-and-restore/restore-archived-logs.html) into the platform for deeper analysis. 
* Cost-effective. Data you reingest to Logz.io from your archive does not count against your daily quota. 

We know that sometimes you just need to have logs searchable for more extended periods of time, which is why we created **[Smart tiering](/user-guide/accounts/smart-tier/)**, which allows you to reduce storage costs as data ages. 

* [Learn how to set up your Drop filters.](https://docs.logz.io/user-guide/accounts/drop-filters/)
* [Learn how to set up your Archive and restore.](https://docs.logz.io/user-guide/archive-and-restore/)

### Import data volume dashboard

Logz.io uses [**ingestion** log measurements](/user-guide/log-usage-measurement/) on your logs. The ingested data is measured as your logs are received after data parsing has been applied and before data indexing. This measurement does not change and provides a more accurate value for data usage. In addition, each Logz.io plan has the **On Demand** expansion, allowing you to ingest and analyze data past your daily volume limit. Using On Demand helps ensure you have access to your logs, metrics, and traces when you need them. [Learn more about On Demand](/user-guide/accounts/on-demand.html).

You can use metrics to monitor and alert when a certain threshold is exceeded, create a dashboard monitoring your data volumes, and more. For example, import and use our [pre-built dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/data-volume-dashboard.ndjson) to monitor your metric data volume.

To import the dashboard to your account, navigate to [Logs](https://app.logz.io/#/dashboard/osd/discover/) > [Stack Management > Saved objects](https://app.logz.io/#/dashboard/osd/visualize/) and click on the Import button. Next, import the [data-volume-dashboard.ndjson](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/data-volume-dashboard.ndjson) file you've downloaded.

![Upload saved JSON](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/data-optimization/indexedobjects.gif)

After uploading the file, you might be asked to choose a new index pattern. Select **logzioCustomerIndex** from the drop-down menu.

![Choose index pattern](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/data-optimization/import-saved-object.png)

Once you import the file, navigate to [Visualize](https://app.logz.io/#/dashboard/osd/visualize/) to view the newly added dashboard.

![View dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/data-optimization/dashboard-visualization.png)


## Optimize metrics data 

Your Infrastructure Monitoring (metrics) account can help you visualize the status of your services and operations. The account usage is [calculated based on Unique Time Series (UTS)](/docs/user-guide/infrastructure-monitoring/introduction-to-prometheus/explore-metrics-prometheus/#calculating-infrastructure-monitoring-usage), a collection of pairs, each including a timestamp and value. Time series is uniquely identified by its metric name and a set of labels.


To gain quick insights into your metrics account, navigate to your **[Metrics](https://app.logz.io/#/dashboard/metrics)** account and run the following query to view the total unique metrics in the query’s timeframe:

`sum(count by (__name__) ({__name__ != ""}))`

Use the following query to view the top cardinality contributors:

`topk(10, count by (__name__) ({__name__ != ""}))`

## Data analytics - Find the needle in the haystack

Once your Logz.io account is up and running, it's time to focus on getting the data that matters most. Logz.io offers several features and capabilities that you can use to filter through the noise, including:

### Alerting

**[Log alerts](/user-guide/alerts/)** can ensure that you’re notified of critical events. Configuring the right alerts is the foundation of any proactive development, DevOps, and validation practice.

Logz.io alerts use an OpenSearch Dashboards search query to continuously scan your logs and alert you when certain conditions are met. The simplest alerts can use a simple search query or a particular filter, but others can be quite complex and involve several conditions with varying thresholds.

For example, activate an alert when an error occurs, when a particular action is being performed, or even when your account usage crosses a threshold set by yourself.

* **[Configure an alert](https://docs.logz.io/user-guide/alerts/configure-an-alert.html)**


Some incidents are best detected by a sequence of logs, which may involve different log types, log fields, or even accounts.

For example, deployment on a particular microservice coincides with an error in another environment. In this case, the alert can correlate 2 separate events as the trigger.

For those cases, you can create a [**Correlated alert**](https://docs.logz.io/user-guide/alerts/correlated-alert/). These alerts are instrumental in reducing false positives. In addition, by defining a more specific use case that contains 2 scenarios, the trigger can be more sensitive and reduce unwanted noise.

* **[Configure a correlated alert](https://docs.logz.io/user-guide/alerts/correlated-alert/#configuring-a-correlated-alert)**

### Patterns Engine

To help declutter the noise, Logz.io [**Patterns Engine**](https://docs.logz.io/user-guide/logs/log-patterns.html) runs advanced clustering algorithms to automatically group logs with similar message fields by their frequency of occurrence.

As you’re troubleshooting in OpenSearch Dashboards, you can easily see the number of Patterns identified in your log results for every query you run. The list is always in-context and specific to the log results returned by your search.

Patterns can help you isolate unusual events from a mass of repetitive events, identify frequent errors, and spot bulky uninteresting logs that can be dropped.

### Usage Calculation

Navigate to your Logz.io [account > Settings > Plan and Usage](https://app.logz.io/#/dashboard/settings/plan-and-billing/usage) and click on the **Usage & Info** tab. 

![Usage and info dashboards](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/usage-hover-multiple.png)

The dashboard is a visual representation of your account, divided into the different products you use. These dashboards include your account’s daily data plan, how much you’ve used, and your overall usage pattern. [Read more on how to optimize your Usage & Info overview](/user-guide/accounts/plan-and-usage.html). 

###### If you have additional questions about optimizing your Logz.io data, [contact the Support team](mailto:help@logz.io).