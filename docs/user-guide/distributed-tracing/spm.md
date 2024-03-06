---
sidebar_position: 5
title: Getting Started with Service Performance Monitoring
description: Get a high-level monitoring dashboard with Service Performance Monitoring 
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, traces, tracing, spm, service performance monitoring, observability, distributed tracing]
---



Distributed tracing assists users by highlighting and analyzing the journey of specific requests, making it easier to track application requests across distributed platforms and microservices architecture.

However, most users have millions of traces at hand, and trying to find a bottleneck or pinpoint a specific incident is difficult and time-consuming.

That’s where Service Performance Monitoring comes in. It's a high-level monitoring dashboard that offers a better way to monitor your services and operations, providing a bird’s eye view into your systems’ health.

Service Performance Monitoring helps cut down the time to identify and resolve anomalies, spikes and issues. It does that by aggregating Request, Error and Duration (R.E.D) metrics from span data, pointing and isolating incidents in your systems.

## Service Performance Monitoring dashboard

The Service Performance Monitoring dashboard is part of your [Tracing account](https://app.logz.io/#/dashboard/jaeger/monitoring), located under the **Monitor** tab. You can generate a dashboard view for each of your services, and adjust the time span between 1 hour to 2 days ago.

![Service Performance Monitoring](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/jaeger-spm-dashboard.png)

The dashboard includes the following data:

* Request rate - Number of requests made per second
* Error rate - The total percentage of errors in this service
* Latency - The duration it took to complete the operations, indicating the 95th, 75th and 50th percentile latency

In addition, the dashboard includes a breakdown of R.E.D data based on the operations running inside the chosen service. Each one has an impact score based on an average of R.E.D data points. To sort the data, click on the arrows next to the title of your preferred data point.

![Operations metrics chart](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/spm-error-rate-highlight.png)

To get a deeper view into the traces of each operation, click on the **View traces** button located at the end of every row. This will display all related traces, which you can investigate more thoroughly and get to the root cause of the issue. 

![View all traces](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/spm-view-traces-highlight.png)

###### Additional Tracing resources: 

* [Configure your Service Performance Monitoring dashboard](/docs/user-guide/distributed-tracing/setup-spm/)
* [What is Distributed Tracing](/docs/user-guide/distributed-tracing/tracing-overview/what-tracing/)
