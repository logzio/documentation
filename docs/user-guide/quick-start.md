---
sidebar_position: 1
title: Getting Started with Logz.io
description: Meet Logz.io's Infrastructure Monitoring solution
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logs, metrics, traces, logz.io, getting started]

---




Logz.io is an end-to-end cloud monitoring service built for scale. It’s the best-of-breed open source monitoring tools on a fully managed cloud service.

One unified SaaS platform to collect and analyze logs, metrics, and traces, combined with human-powered AI/ML features to improve troubleshooting, reduce response time and help you manage costs.


Whether you are a new user or looking for a refresher on Logz.io, you are invited to join one of our engineers for a **[training session on the Logz.io platform](https://docs.logz.io/training/)**!


## Send your data to Logz.io

Once you’ve set up your account, you can start sending your data.

Logz.io provides various tools, integrations, and methods to send data and monitor your Logs, Metrics, Traces, and SIEM.

The fastest and most seamless way to send your data is through our **Telemetry Collector**. It lets you easily configure your data-sending process by executing a single line of code, providing a complete observability platform to monitor and improve your logs, metrics, and traces.

[**Get started with Telemetry Collector**](https://app.logz.io/#/dashboard/send-your-data/agent/new).

If you prefer to send your data manually, Logz.io offers numerous methods to do so, and here are some of the more popular ones based on what you’d like to monitor:

|**Logs**|**Metrics**|**Traces**|**Cloud SIEM**|
| --- | --- | --- | --- |
|[Filebeat](https://app.logz.io/#/dashboard/send-your-data/log-sources/filebeat)|[.NET](https://app.logz.io/#/dashboard/send-your-data/prometheus-sources/dotnet-custom)|[Jaeger installation](https://app.logz.io/#/dashboard/send-your-data/tracing-sources/jaeger_collector)|[Cloudflare](https://app.logz.io/#/dashboard/send-your-data/security-sources/cloudflare)
|[S3 Bucket](https://app.logz.io/#/dashboard/send-your-data/log-sources/s3-bucket)|[Prometheus](https://app.logz.io/#/dashboard/send-your-data/prometheus-sources/prometheus-remote-write_shipping)|[OpenTelemetry installation](https://app.logz.io/#/dashboard/send-your-data/tracing-sources/opentelemetry)|[NGINX](https://app.logz.io/#/dashboard/send-your-data/security-sources/nginx)
|[cURL](https://app.logz.io/#/dashboard/send-your-data/log-sources/curl)|[Azure Kubernetes Service](https://app.logz.io/#/dashboard/send-your-data/prometheus-sources/otel-metrics-aks-helm)|[Docker](https://app.logz.io/#/dashboard/send-your-data/tracing-sources/docker-otel)|[Active directory](https://app.logz.io/#/dashboard/send-your-data/security-sources/active-directory-winserver)
|[JSON uploads](https://app.logz.io/#/dashboard/send-your-data/log-sources/json-uploads)|[Google Kubernetes Engine over OpenTelemetry](https://app.logz.io/#/dashboard/send-your-data/prometheus-sources/otel-metrics-gke-helm)|[Kubernetes](https://app.logz.io/#/dashboard/send-your-data/tracing-sources/otel-traces-helm)|[CloudTrail](https://app.logz.io/#/dashboard/send-your-data/security-sources/cloudtrail)
|[Docker container](https://app.logz.io/#/dashboard/send-your-data/log-sources/docker)|[Amazon EC2](https://app.logz.io/#/dashboard/send-your-data/prometheus-sources/aws-ec2-prometheus)|[Go instrumentation](https://app.logz.io/#/dashboard/send-your-data/tracing-sources/go-otel)|[auditd](https://app.logz.io/#/dashboard/send-your-data/security-sources/auditd) |

Browse the complete list of available shipping methods [here](https://docs.logz.io/shipping/).

To learn more about shipping your data, check out **Shipping Log Data to Logz.io**:


<div style={{position: 'relative', paddingBottom: '56.25%'}}>
  <iframe style={{position: 'absolute', top: '0', left: '0', width: '100%', height: '100%'}} src="https://fast.wistia.com/embed/iframe/oi6qydmyk6" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Parsing your data

Logz.io offers automatic parsing [for over 50 log types](https://docs.logz.io/user-guide/log-shipping/built-in-log-types.html).

If you can't find your log type, or if you're interested in sending custom logs, Logz.io will parse the logs for you. Parsing-as-a-service is included in your Logz.io subscription; just open a chat with our **Support team** with your request, you can also email us at [help@logz.io](mailto:help@logz.io).

If you prefer to parse the logs yourself, you can use our [DIY Data Parsing Editor](https://docs.logz.io/user-guide/mapping-and-parsing/sawmill-parsing.html).

###### Additional resources


Learn more about sending data to Logz.io:

* [Use Logz.io API](https://docs.logz.io/api/)
* [Log shipping FAQ](https://docs.logz.io/user-guide/log-shipping/faqs-logs/)
* [Log shipping troubleshooting](https://docs.logz.io/user-guide/log-shipping/log-shipping-troubleshooting.html)
* [Troubleshooting Filebeat](https://docs.logz.io/user-guide/log-troubleshooting/filebeat-troubleshooting.html)

### Explore your data with Logz.io's Log Management platform

Logz.io’s **[Log Management](https://app.logz.io/#/dashboard/osd)** is where you can search and query log files. You can use it to identify and analyze your code, and the platform is optimized for debugging and troubleshooting issues as quickly and effectively as possible.

![Log management overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/log-analytics-main-sep26.png)

The following list contains some of the common abilities available in Log Management:

* **[Log Management best practices](https://docs.logz.io/user-guide/logs/best-practices.html)**
* **[Configuring an alert](https://app.logz.io/#/dashboard/alerts/v2019/new)**
* Using **[Logz.io's pattern engine](https://docs.logz.io/user-guide/logs/log-patterns.html)** to automatically group logs with similar message fields by their frequency of occurrence
* **[Reviewing your fields' mapping](https://docs.logz.io/user-guide/logs/mapping/)**
* Using **[Optimizers](https://docs.logz.io/user-guide/optimizers/)** to store logs and aggregations to a timeless account
* Predicting exceptions and critical errors with **Insights**


## Create visualizations with Logz.io's Infrastructure Monitoring

Monitor your **[Infrastructure Monitoring](https://app.logz.io/#/dashboard/metrics)** to gain a clear picture of the ongoing status of your distributed cloud services at all times.

Logz.io's Infrastructure Monitoring lets your team curate a handy roster of dashboards to oversee continuous deployment, CI/CD pipelines, prevent outages, manage incidents, and remediate crashes in multi-microservice environments and hybrid infrastructures and complex tech stacks.

![Infrastructure Monitoring overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/metrics-overview-sep26.png)

Once you've sent your metrics to Logz.io, you can:

### Build Metrics visualizations with Logz.io

<div style={{position: 'relative', paddingBottom: '56.25%'}}>
  <iframe style={{position: 'absolute', top: '0', left: '0', width: '100%', height: '100%'}} src="https://fast.wistia.com/embed/iframe/w7lkltrofb" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

You can also:

* Start with a **[pre-build Metrics dashboard](https://docs.logz.io/user-guide/infrastructure-monitoring/metrics-dashboards)** to monitor data
* **Create Metrics related alerts**
* Work with **[Dashboard variable](https://docs.logz.io/user-guide/infrastructure-monitoring/configure-metrics-drilldown-links.html)** to apply filters on your dashboards and drilldown links
* Mark events on your Metrics dashboard based on data from a logging account, with **[Annotations](https://docs.logz.io/user-guide/infrastructure-monitoring/annotations/)**

###### Additional resources

* [Sending Prometheus metrics to Logz.io](https://logz.io/learn/sending-prometheus-metrics-to-logzio/)


## Dive deeper into the code with Logz.io's Distributed Tracing

Use Logz.io’s **[Distributed Tracing](https://app.logz.io/#/dashboard/jaeger)** to look under the hood at how your microservices behave, and access rich information to improve performance, investigate, and troubleshoot issues.

![Distributed Tracing overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/traces-overview-sep26.png)

To help you understand how Distributed Tracing can enhance your data, check out the following guides:

* **[Getting started with Tracing](https://docs.logz.io/user-guide/distributed-tracing/getting-started-tracing/)**
* **[Sending demo traces with HOTROD](https://docs.logz.io/user-guide/distributed-tracing/trace-hotrod-demo)**
* Combine Traces and Metrics with **[Service Performance Monitoring](https://docs.logz.io/user-guide/distributed-tracing/service-performance-monitoring)**
* **[Correlate logs and traces](https://docs.logz.io/user-guide/distributed-tracing/correlate-traces/)**


## Secure your environment with Logz.io's Cloud SIEM

Logz.io **[Cloud SIEM](https://app.logz.io/#/dashboard/security/summary)** (Security Information and Event Management) aggregates security logs and alerts across distributed environments to allow your team to investigate security incidents from a single observability platform.

![Cloud SIEM overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/SIEM-overview-sep26.png)

Here are some popular Cloud SIEM resources to help you get started:

* **[Cloud SIEM quick start guide](https://docs.logz.io/user-guide/cloud-siem/quick-guide.html)**
* **[Investigate security events](https://docs.logz.io/user-guide/cloud-siem/security-events.html)**
* **[Threat Intelligence feeds](https://docs.logz.io/user-guide/cloud-siem/threat-intelligence.html)**
* **[Configure a security rule](https://docs.logz.io/user-guide/cloud-siem/manage-security-rules.html)**
* **[Dashboards and reports](https://docs.logz.io/user-guide/cloud-siem/dashboards/)**

## Manage your Logz.io account

Logz.io's account admins can control and edit different elements inside their accounts. These abilities include setting up SSO access, assigning permissions per user, and sharing and managing data.

The following list explores the more common use cases for Logz.io's account admins:

* **[Setting and editing user permission levels](https://docs.logz.io/user-guide/users/)**
* **[Managing main and sub accounts](https://docs.logz.io/user-guide/accounts/)**
* **[Optimizing account volume usage](https://docs.logz.io/user-guide/accounts/manage-account-usage.html)**
* **[Setting up SSO access](https://docs.logz.io/user-guide/users/single-sign-on/)**
* **[Archiving and restoring data](https://docs.logz.io/user-guide/archive-and-restore/)**



## Home Dashboard 

Home Dashboard includes your account’s data, logs, metrics, traces, alerts, exceptions, and insights. 

You can quickly access the Home Dashboard by clicking on the **Home** icon in the navigation. 

[Learn how to utilize your Home Dashboard](/docs/user-guide/home-dashboard).

![Home dashboard Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/home-dashboard/dashboard-overview-.png)



### 1. Choose elements to view

You can choose which elements you want to view; logs, metrics, traces, number of alerts triggered, and insights gathered within the selected time frame. Click on one of the boxes to add or remove them from your view. The graph and chart will be updated immediately. 

For example, clicking on Insights or Exceptions will remove all of them from the graph and the table, allowing you to shift your focus according to your monitoring needs.

![Add remove elements](https://dytvr9ot2sszz.cloudfront.net/logz-docs/home-dashboard/add-remove-elements.gif)


### 2. Graph overview

This is a visual representation of your account’s data. Hover over the graph to see a breakdown of elements per hour. This view includes the number of overall and unique events.

![Graph hover view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/home-dashboard/graph-hover-view.png)


### 3. Table overview

At the bottom of the page, you can view your account's data as a table. The data is broken down by events, and you can view each event’s type, severity, number of grouped events, and the date on which the event was last triggered. 

When hovering over one of the events you'll see an **Investigate** button, which opens it in OpenSearch Dashboards, allowing you to drill down further into the issue.

![Investigate button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/home-dashboard/investigate-button.png)

### 4. Search and access dashboards

Home Dashboard offers easy access to your logs and metrics dashboards, allowing you to search any available dashboard across your account. Start typing to search throughout your available dashboards, and click on one of the options to open it in a new tab. This view includes which dashboards you've viewed recently, and you can add critical or important dashboards to your favorites for quick access.

### 5. Set your time frame

The top of the page indicates when the data was last updated, helping you keep up to date with the data.

You can change the time range to view data from the last 24 hours and up until from the last 2 hours. Once you choose a different time frame, Home Dashboard will update to reflect the relevant data.

