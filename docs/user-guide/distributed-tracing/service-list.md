---
sidebar_position: 4
---

# Service List

The **Service list** dashboard centralizes all of your running services, allowing you to quickly detect if and when issues occur.  You can use the dashboard to investigate the different services, operations, and logs inside each one.

![Services](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/services-main-dev.png)

## Service list overview

The main Service list table view contains the following details:

* **Name** of each service
* **Impact** level - Determines the severity of each event, calculated based on the latency and request rate
* The **Environment** in which this service is located
* **Request rate** - Number of requests per second, in numeral and graph view
* **Latency** - The duration it takes data to travel in the environment, presented in milliseconds and graph view
* **Error ratio** - Both percentage and graph view

At the top of the chart, you can adjust the view to match your monitoring needs.

You can **compare** your view to a previous time frame and view the differences in the graphs and trends.

![service compare](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/compare-services1.png)

**Change the time frame** to range from 2 hours ago and up to 2 days ago.

![service time](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/services-last1.png)

Choose which **environments and operations** you want to display in the chart.

![service filters](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/services-filters1.png)

Or, if you're looking for a specific service, use the **search** to see all the matching results.

![service search](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/services-search.png)

Clicking on the **Clear filters** will remove all of the filters.

## Dive deeper into your services

Clicking on one of the services opens a new page with additional info, including a visual representation of the service’s current error ratio, request rate, latency, and a breakdown of the service’s operations, infrastructure, and logs. Each data point is compared to the time frame of your choice (last day or last week), helping you understand the trends and know which area you should focus on. 

At the top of the page, you can change the time frame, choose which nodes or pods to focus on, or manually update the data by clicking on the refresh icon. 

![service deeper](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/services-inner-dec.png)

Hovering over the graphs provides additional info for the time point you've chosen:

* The **Request rate** graph shows the number of requests made per minute
* The **Latency** graph provides a milliseconds count of how long it takes for data to travel in your environment
* The **Errors** graph analyzes the percentage of errors that occurred

![graphs](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/hover-graph.png)

### Operations overview

This table includes all of the operations running inside the chosen service with this additional data:

* **Operation** name
* The operation’s **Impact** level, calculated based on the latency and request rate
* **Request rate** - Number of requests per second, in numeral and graph view
* **Latency** - The duration it takes data to travel in the environment, presented in milliseconds and graph view
* **Error ratio** - Both percentage and graph view

Use the search bar to find a specific operation or the arrows at the bottom of the table to navigate the operations.

Click on an operation's name to view its detailed trace. The trace dashboard helps you pinpoint where failures occur and find the leading contributors to slow transaction performance.

![operations view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/operations-overview-dec.png)

### Infrastructure overview

View the CPU and memory consumption inside the service. The graphs represent a breakdown of consumption by the hour.

Hovering over the graphs provides values for the specific time point, allowing you to see how much CPU was used by the deployment at this specific time or how much memory this deployment used.

![hovering graph](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/hover-infra.png)

You can toggle your view between pods and nodes inside the service.

## Track Deployment Data

You can enrich your Service Overview graphs by indicating recent deployments, helping you determine if a deployment has increased response times for end-users, altered your application's memory/CPU footprint, or introduced any other performance-related changes.

To enable deployment tracking ability, run the [**Telemetry Collector**](https://app.logz.io/#/dashboard/send-your-data/agent/new) on your Kubernetes clusters. You can also activate this process **manually** by installing [Logz.io Kubernetes events Helm chart](https://app.logz.io/#/dashboard/integrations/Kubernetes:~:text=user%20guide.-,Send%20your%20deploy%20events%20logs,-This%20integration%20sends) and sending Kubernetes deploy events logs.

Once enabled, navigate to [Services](https://app.logz.io/#/dashboard/spm/service-list/table?timeFrame=2h&compareTo=1d) and choose one of your running services. The deployment marker will appear in your graphs, marked by a vertical line.

![deployment popup](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/deplyment-popup.png)

You can view additional deployment data by clicking on the line. This data includes the deployment time, the associated service and environment, and a quick link to view the commit in your logs.

Click **Go to commit** to access and view your own code related to this deployment, allowing you to probe deeper into the relevant data.

:::caution Important
To activate the **Go to Commit** button, go to **your app or service** and add the following annotation to the metadata of each resource's versioning you want to track: `logzio/commit_url: ""`, and the URL structure should be: "`https://github.com/<account>/<repository>/commit/<commit-hash>`". [Learn more](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-k8s-events#deployment-events-versioning).
:::



<!-- ### Logs overview

All of the logs related to the service are shown at the bottom of the page. This view includes a graph view of the log levels and a table view with the following:

* The **timestamp** of each log
* **Log level** tag 
* The **Message** associated to this log
* Number of **exceptions** found in these logs
* Number of **insights** found in these logs

You can search for specific logs or click on Explore in OSD to open the Log analytics view of the relevant service. -->