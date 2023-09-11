---
sidebar_position: 4
---

# Service List

The **Service list** dashboard centralizes all of your running services, allowing you to detect if and when issues occur quickly.  You can use the dashboard to investigate the different services, operations, and logs inside each one.

![Services](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/service-list-overview.png)

## Service list overview

The main Service list table view contains the following details:

* **Name** of each service
* **Impact** level - Determines the severity of each event, calculated based on the latency and request rate
* The **Environment** in which this service is located
* **Request rate** - Number of requests per second, in numeral and graph view
* **Latency** - The duration it takes data to travel in the environment, presented in milliseconds and graph view
* **Error ratio** - Both percentage and graph view

You can change your view by comparing the data to a previous time frame, such as the last day or week. You can also choose a different time frame that ranges from 2 hours ago and up to 24 hours ago.

If you’re looking for a specific service, start typing its name in the search box, and your view will change to display all the matching results.

## Dive deeper into your services

Clicking on one of the services opens a new page with additional info, including a visual representation of the service’s current error ratio, request rate, latency, and a breakdown of the service’s operations, infrastructure, and logs.

![service deeper](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/service-overview.png)

Hovering over the graphs provides additional info for the time point you've chosen:

* The **Request rate** graph shows the number of requests made per minute
* The **Latency** graph provides a milliseconds count of how long it takes for data to travel in your environment
* The **Errors** graph analyzes the percentage of errors that occurred

![graphs](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/hover-graph.png)

### Operations overview

This table includes all of the operations running inside the chosen service, with this additional data:

* **Operation** name
* Operation’s **Impact** level, calculated based on the latency and request rate
* **Request rate** - Number of requests per second, in numeral and graph view
* **Latency** - The duration it takes data to travel in the environment, presented in milliseconds and graph view
* **Error ratio** - Both percentage and graph view

Use the search bar to find a specific operation or the arrows at the bottom of the table to navigate the operations.

Click on an operation's name to view its detailed trace. The trace dashboard helps you pinpoint where failures occur and find the leading contributors to slow transaction performance.

![operations view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/operations-view.png)

### Infrastructure overview

View the CPU and memory consumption inside the service. The graphs represent a breakdown of consumption by the hour.

Hovering over the graphs provides values for the specific time point, allowing you to see how much CPU was used by the deployment at this specific time, or view how much memory this deployment used.

![hovering graph](https://dytvr9ot2sszz.cloudfront.net/logz-docs/services/hover-infra.png)

You can toggle your view between pods and nodes inside the service.

<!-- ### Logs overview

All of the logs related to the service are shown at the bottom of the page. This view includes a graph view of the log levels and a table view with the following:

* The **timestamp** of each log
* **Log level** tag 
* The **Message** associated to this log
* Number of **exceptions** found in these logs
* Number of **insights** found in these logs

You can search for specific logs or click on Explore in OSD to open the Log analytics view of the relevant service. -->