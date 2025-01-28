---
sidebar_position: 1
title: Getting Started with Logz.io
description: Meet Logz.io's Infrastructure Monitoring solution
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logs, metrics, traces, logz.io, getting started]

---


Logz.io is a scalable, end-to-end cloud monitoring service that combines the best open-source tools with a fully managed SaaS platform. It provides unified log, metric, and trace collection with AI/ML-enhanced features for improved troubleshooting, faster response times, and cost management.

Whether you’re new to Logz.io or need a refresher, join one us for a **[training session on the Logz.io platform](https://logz.io/training/)**!

## Send your data to Logz.io

After setting up your account, you can start sending your data to Logz.io using various tools, integrations, and methods for monitoring Logs, Metrics, Traces, and SIEM.

The quickest way is through our **Telemetry Collector**, which simplifies data configuration with a single line of code, enabling full observability across your systems.

[**Get started with Telemetry Collector**](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).

If you prefer a manual approach, Logz.io offers multiple methods tailored to different monitoring needs. Here are some popular options:

|**Logs**|**Metrics**|**Traces**|**Cloud SIEM**|
| --- | --- | --- | --- |
|[Filebeat](https://app.logz.io/#/dashboard/integrations/Filebeat-data)|[.NET](https://app.logz.io/#/dashboard/integrations/dotnet)|[Jaeger installation](https://app.logz.io/#/dashboard/integrations/Jaeger-data)|[Cloudflare](https://app.logz.io/#/dashboard/integrations/Cloudflare-network)
|[S3 Bucket](https://app.logz.io/#/dashboard/integrations/AWS-S3-Bucket)|[Prometheus](https://app.logz.io/#/dashboard/integrations/Prometheus-remote-write)|[OpenTelemetry installation](https://app.logz.io/#/dashboard/integrations/OpenTelemetry-data)|[NGINX](https://app.logz.io/#/dashboard/integrations/Nginx-load)
|[cURL](https://app.logz.io/#/dashboard/integrations/cURL-data)|[Java](https://app.logz.io/#/dashboard/integrations/Java)|[Docker](https://app.logz.io/#/dashboard/integrations/Docker)|[Active directory](https://app.logz.io/#/dashboard/integrations/Active-Directory)
|[HTTP uploads](https://app.logz.io/#/dashboard/integrations/HTTP)|[Node.js](https://app.logz.io/#/dashboard/integrations/Node-js)|[Kubernetes](https://app.logz.io/#/dashboard/integrations/Kubernetes)|[CloudTrail](https://app.logz.io/#/dashboard/integrations/AWS-CloudTrail)
|[Python](https://app.logz.io/#/dashboard/integrations/Python)|[Amazon EC2](https://app.logz.io/#/dashboard/integrations/AWS-EC2)|[Go instrumentation](https://app.logz.io/#/dashboard/integrations/GO)|[Auditbeat](https://app.logz.io/#/dashboard/integrations/auditbeat) |

Browse the complete list of available shipping methods [here](https://app.logz.io/#/dashboard/integrations/collectors).

<!-- To learn more about shipping your data, check out **Shipping Log Data to Logz.io**:


<div style={{position: 'relative', paddingBottom: '56.25%'}}>
  <iframe style={{position: 'absolute', top: '0', left: '0', width: '100%', height: '100%'}} src="https://fast.wistia.com/embed/iframe/oi6qydmyk6" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

-->

### Parsing your data

Logz.io automatically parses [over 50 log types](https://docs.logz.io/docs/user-guide/data-hub/log-parsing/default-parsing/). 

If your log type isn't listed, or you want to send custom logs, we offer parsing-as-a-service as part of your subscription. Just reach out to our **Support team** via chat or email us at [help@logz.io](mailto:help@logz.io?subject=Parse%20my%20data) with your request.



<h4 id="logs-resources"> Additional resources </h4>

Learn more about sending data to Logz.io:

* [Use Logz.io API](https://api-docs.logz.io/docs/logz/logz-io-api/)
* [Log shipping FAQ](https://docs.logz.io/docs/user-guide/log-management/faqs-logs/)
* [Log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/)
* [Troubleshooting Filebeat](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-filebeat/)

### Navigate your logs with Logz.io Explore

Logz.io's [Explore](https://app.logz.io/#/dashboard/explore) lets you view, search, and query your data to analyze code, debug issues, and get guidance with its integrated AI Agent.

![Log management overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/explore-ai-agent-oct21.png)

Key capabilities in Explore include:

* **[Explore best practices](https://docs.logz.io/docs/user-guide/explore/best-practices)**
* **[Configuring an alert](https://app.logz.io/#/dashboard/alerts/v2019/new)**
* **[Review and investigate exceptions](https://docs.logz.io/docs/user-guide/explore/exceptions)**

<!-- 
* Using **[Logz.io's pattern engine](https://docs.logz.io/docs/user-guide/log-management/opensearch-dashboards/opensearch-patterns/)** to automatically group logs with similar message fields by their frequency of occurrence
* **[Reviewing your fields' mapping](https://docs.logz.io/docs/user-guide/data-hub/field-mapping/)**
* Using **[Optimizers](https://docs.logz.io/docs/user-guide/log-management/long-term-storage/optimizers/)** to store logs and aggregations to a timeless account
* Predicting exceptions and critical errors with **Insights**
-->


## Create visualizations with Logz.io's Infrastructure Monitoring


Logz.io's **[Infrastructure Monitoring](https://app.logz.io/#/dashboard/metrics)** provides real-time visibility into the status of your distributed cloud services. It enables your team to create custom dashboards to oversee deployments, manage incidents, and prevent outages in complex environments.


![Infrastructure Monitoring overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/metrics-overview-sep26.png)

After sending your metrics to Logz.io, you can:

### Build Metrics visualizations with Logz.io

<div style={{position: 'relative', paddingBottom: '56.25%'}}>
  <iframe style={{position: 'absolute', top: '0', left: '0', width: '100%', height: '100%'}} src="https://fast.wistia.com/embed/iframe/w7lkltrofb" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

You can also:

* **[Create metrics-based alerts](https://docs.logz.io/docs/user-guide/Infrastructure-monitoring/metrics-alert-manager/)**
* Use **[Dashboard variable](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/variables/)** for filtering and drilldowns
* Mark events on your Metrics dashboard based on data from a logging account, with **[Annotations](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/log-correlations/annotations/)**

<h4 id="metrics-resources"> Additional resources </h4>

* [Sending Prometheus metrics to Logz.io](https://logz.io/learn/sending-prometheus-metrics-to-logzio/)


## Dive deeper with Logz.io's Distributed Tracing

Leverage Logz.io’s **[Distributed Tracing](https://app.logz.io/#/dashboard/jaeger)** to gain deep insights into your microservices' behavior, enhancing performance and streamlining investigation and troubleshooting.

![Distributed Tracing overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/traces-overview-sep26.png)

To make the most of Distributed Tracing, check out these guides:

* **[Getting started with Tracing](https://docs.logz.io/docs/user-guide/distributed-tracing/set-up-tracing/get-started-tracing/)**
* **[Sending demo traces with HOTROD](https://docs.logz.io/docs/user-guide/distributed-tracing/set-up-tracing/hotrod/)**
* **[Correlate logs and traces](https://docs.logz.io/docs/user-guide/distributed-tracing/correlate-traces/)**


## Secure your environment with Logz.io's Cloud SIEM

Logz.io **[Cloud SIEM](https://app.logz.io/#/dashboard/security/summary)** (Security Information and Event Management) consolidates security logs and alerts across distributed environments, enabling your team to investigate incidents from a single observability platform.

![Cloud SIEM overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/SIEM-overview-sep26.png)

Get Started with Cloud SIEM:

* **[Quick start guide](https://docs.logz.io/docs/category/cloud-siem-quick-start-guide/)** 
* **[Investigate security events](https://docs.logz.io/docs/user-guide/cloud-siem/investigate-events/security-events/)**
* **[Threat Intelligence feeds](https://docs.logz.io/docs/user-guide/cloud-siem/threat-intelligence/)**
* **[Configure security rules](https://docs.logz.io/docs/user-guide/cloud-siem/security-rules/manage-security-rules/)**
* **[Dashboards and reports](https://docs.logz.io/docs/user-guide/cloud-siem/dashboards/)**

## Manage and optimize your Logz.io account

Admins can control user permissions, manage accounts, set up SSO, and handle data archiving.

The following list explores the more common use cases for Logz.io's account admins:

* **[Setting and editing user permission levels](https://docs.logz.io/docs/user-guide/admin/users/)**
* **[Managing main and sub accounts](https://docs.logz.io/docs/user-guide/admin/logzio-accounts/accounts/)**
* **[Optimizing account volume usage](https://docs.logz.io/docs/user-guide/admin/account-volume-optimization/manage-account-usage/)**
* **[Setting up SSO access](https://docs.logz.io/docs/user-guide/admin/sso/single-sign-on/)**
* **[Archiving and restoring data](https://docs.logz.io/docs/user-guide/data-hub/archive-restore/archive-and-restore/)**

In addition, Logz.io's Data Hub helps you manage and optimize your Logz.io products by offering tailored recommendations and a quick and easy way to control your logs and metrics usage. Account Admins can use Data Hub to:

* **[Analyze and optimize logs and metrics usage](/docs/user-guide/data-hub/cost-optimization/)**
* **[Create graphs and dashboards from your logs](/docs/user-guide/data-hub/logstometrics/)**
* **[Index and monitor your traces](/docs/user-guide/data-hub/sampling-rules/)**
* **[Archive and restore your data](/docs/category/archive--restore/)**

[And more](/docs/category/data-hub/).


## Get a detailed overview with the Home Dashboard 

The [Home Dashboard](https://app.logz.io/#/dashboard/home) provides a comprehensive view of your account's data, including logs, metrics, traces, alerts, and insights. Access it by clicking the Home icon in the navigation.

[Learn how to utilize your Home Dashboard](/docs/user-guide/home-dashboard/).

![Home dashboard Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/home-dashboard/dashboard-overview-.png)



### 1. Customize your view

Select elements like logs, metrics, and traces to display or hide, with immediate graph and table updates. Click on one of the boxes to add or remove them from your view. The graph and chart will be updated immediately. 

For example, clicking on Insights or Exceptions will remove all of them from the graph and the table, allowing you to shift your focus according to your monitoring needs.

![Add remove elements](https://dytvr9ot2sszz.cloudfront.net/logz-docs/home-dashboard/add-remove-elements.gif)


### 2. Graph overview

Visualize data over time and explore detailed event breakdowns.

![Graph hover view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/home-dashboard/graph-hover-view.png)


### 3. Table overview

At the bottom of the page, your data is displayed in a table format, breaking down events by type, severity, grouped count, and the date they were last triggered.

Hover over an event to reveal the **Investigate** button, which opens the event in OpenSearch Dashboards for deeper analysis.

![Investigate button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/home-dashboard/investigate-button.png)

### 4. Search and access dashboards

The Home Dashboard provides quick access to your logs and metrics dashboards, enabling you to search across all available dashboards in your account. Simply start typing to find a specific dashboard, and click to open it in a new tab. The view also shows recently accessed dashboards, and you can mark essential ones as favorites for easy access.

### 5. Set your time frame

The top of the page shows the last data update, helping you stay current.

You can adjust the time range to view data from the last 2 to 24 hours. The Home Dashboard will then refresh to display data for the selected period.
