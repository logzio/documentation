---
sidebar_position: 1
title: Getting Started with Logz.io
description: Meet Logz.io's Infrastructure Monitoring solution
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logs, metrics, traces, logz.io, getting started]

---




Logz.io is an end-to-end cloud monitoring service built for scale. It’s the best-of-breed open source monitoring tools on a fully managed cloud service.

One unified SaaS platform to collect and analyze logs, metrics, and traces, combined with human-powered AI/ML features to improve troubleshooting, reduce response time and help you manage costs.


Whether you are a new user or looking for a refresher on Logz.io, you are invited to join one of our engineers for a **[training session on the Logz.io platform](https://logz.io/training/)**!


## Send your data to Logz.io

Once you’ve set up your account, you can start sending your data.

Logz.io provides various tools, integrations, and methods to send data and monitor your Logs, Metrics, Traces, and SIEM.

The fastest and most seamless way to send your data is through our **Telemetry Collector**. It lets you easily configure your data-sending process by executing a single line of code, providing a complete observability platform to monitor and improve your logs, metrics, and traces.

[**Get started with Telemetry Collector**](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).

If you prefer to send your data manually, Logz.io offers numerous methods to do so, and here are some of the more popular ones based on what you’d like to monitor:

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

Logz.io offers automatic parsing [for over 50 log types](https://docs.logz.io/docs/user-guide/data-hub/log-parsing/default-parsing/).

If you can't find your log type, or if you're interested in sending custom logs, Logz.io will parse the logs for you. Parsing-as-a-service is included in your Logz.io subscription; just open a chat with our **Support team** with your request, you can also email us at [help@logz.io](mailto:help@logz.io).

<h4 id="logs-resources"> Additional resources </h4>

Learn more about sending data to Logz.io:

* [Use Logz.io API](https://api-docs.logz.io/docs/logz/logz-io-api/)
* [Log shipping FAQ](https://docs.logz.io/docs/user-guide/log-management/faqs-logs/)
* [Log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/)
* [Troubleshooting Filebeat](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-filebeat/)

### Explore your data with Logz.io's Log Management platform

Logz.io's [Explore](https://app.logz.io/#/dashboard/explore) is where you can view, search, and query your data. Use it to identify and analyze your code, debug and troubleshoot issues, and get recommendations to next steps with its AI Assistant.

![Log management overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/explore-aug27.png)

//The following list contains some of the common abilities available in Log Management:

* **[Log Management best practices](https://docs.logz.io/docs/user-guide/log-management/opensearch-dashboards/opensearch-best-practices/)**
* **[Configuring an alert](https://app.logz.io/#/dashboard/alerts/v2019/new)**
* Using **[Logz.io's pattern engine](https://docs.logz.io/docs/user-guide/log-management/opensearch-dashboards/opensearch-patterns/)** to automatically group logs with similar message fields by their frequency of occurrence
* **[Reviewing your fields' mapping](https://docs.logz.io/docs/user-guide/data-hub/field-mapping/)**
* Using **[Optimizers](https://docs.logz.io/docs/user-guide/log-management/long-term-storage/optimizers/)** to store logs and aggregations to a timeless account
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

* **[Create Metrics related alerts](https://docs.logz.io/docs/user-guide/Infrastructure-monitoring/metrics-alert-manager/)**
* Work with **[Dashboard variable](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/variables/)** to apply filters on your dashboards and drilldown links
* Mark events on your Metrics dashboard based on data from a logging account, with **[Annotations](https://docs.logz.io/docs/user-guide/infrastructure-monitoring/log-correlations/annotations/)**

###### Additional resources

* [Sending Prometheus metrics to Logz.io](https://logz.io/learn/sending-prometheus-metrics-to-logzio/)


## Dive deeper into the code with Logz.io's Distributed Tracing

Use Logz.io’s **[Distributed Tracing](https://app.logz.io/#/dashboard/jaeger)** to look under the hood at how your microservices behave, and access rich information to improve performance, investigate, and troubleshoot issues.

![Distributed Tracing overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/traces-overview-sep26.png)

To help you understand how Distributed Tracing can enhance your data, check out the following guides:

* **[Getting started with Tracing](https://docs.logz.io/docs/user-guide/distributed-tracing/set-up-tracing/get-started-tracing/)**
* **[Sending demo traces with HOTROD](https://docs.logz.io/docs/user-guide/distributed-tracing/set-up-tracing/hotrod/)**
* Combine Traces and Metrics with **[Service Performance Monitoring](https://docs.logz.io/docs/user-guide/distributed-tracing/spm/)**
* **[Correlate logs and traces](https://docs.logz.io/docs/user-guide/distributed-tracing/correlate-traces/)**


## Secure your environment with Logz.io's Cloud SIEM

Logz.io **[Cloud SIEM](https://app.logz.io/#/dashboard/security/summary)** (Security Information and Event Management) aggregates security logs and alerts across distributed environments to allow your team to investigate security incidents from a single observability platform.

![Cloud SIEM overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/SIEM-overview-sep26.png)

Here are some popular Cloud SIEM resources to help you get started:

* **[Cloud SIEM quick start guide](https://docs.logz.io/docs/category/cloud-siem-quick-start-guide/)** 
* **[Investigate security events](https://docs.logz.io/docs/user-guide/cloud-siem/investigate-events/security-events/)**
* **[Threat Intelligence feeds](https://docs.logz.io/docs/user-guide/cloud-siem/threat-intelligence/)**
* **[Configure a security rule](https://docs.logz.io/docs/user-guide/cloud-siem/security-rules/manage-security-rules/)**
* **[Dashboards and reports](https://docs.logz.io/docs/user-guide/cloud-siem/dashboards/)**

## Manage and optimize your Logz.io account

Logz.io's account admins can control and edit different elements inside their accounts. These abilities include setting up SSO access, assigning permissions per user, and sharing and managing data.

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

Home Dashboard includes your account’s data, logs, metrics, traces, alerts, exceptions, and insights. 

You can quickly access the Home Dashboard by clicking on the **Home** icon in the navigation. 

[Learn how to utilize your Home Dashboard](/docs/user-guide/home-dashboard/).

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

