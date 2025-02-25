---
sidebar_position: 19
title: Release Notes
description: What's new in Logz.io - latest releases, features, enhancements, and updates
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [release notes, logzio, logs, metrics, traces, logz.io, updates, releases, features]
toc_max_heading_level: 2
---

## February 2025

### Explore Upgrades and Improvements

Enhanced Explore with new account visibility features. Users can now view their selected accounts directly within Explore and add an accounts column to the table for improved clarity and organization.

**[Trace view](https://docs.logz.io/docs/user-guide/explore/trace-view/)** is now available to all users, who can add multi-telemetry insights to your logs, making it easier to find bottlenecks and identify errors in your environment.

**Visualization** features are now available to all users, allowing you to switch between linear and logarithmic scales, add deployment markers, and compare data across time periods.

### Core Updates

Added support for [**OpenTelemetry Lambda Layers**](https://github.com/logzio/opentelemetry-lambda), enabling the use of tail_sampling and metricstransformprocessor processors. Additionally, connectors are now supported, allowing the integration of the spanmetrics connector.

Enhanced the **[Prometheus Alert Migrator](https://github.com/logzio/prometheus-alerts-migrator)** for streamlined monitoring and alert management in Logz.io environments. Updates include support for MS Teams contact points and upgrade dependencies.

Enhanced the **[Logz.io Node.js Logger](https://github.com/logzio/logzio-nodejs)** integration with addOtelContext configuration option, adding trace_id, span_id, and service_name fields to logs when OpenTelemetry context is available.

**[Java log appenders](https://github.com/logzio/logzio-java-sender)** (Logback and Log4j2) now support OpenTelemetry context injection. When OpenTelemetry context is available, logs can include trace_id, span_id, and service_name fields for improved traceability and observability.



## January 2025

### Introducing Our New Support Help Center
We’re thrilled to launch our brand-new and improved Support Help Center, designed to streamline how you interact with our support team and access the resources you need. This enhanced platform empowers users to:

* Submit and track support tickets, ensuring full visibility into your requests and their progress.
* Find answers to integration-related questions.
* Submit feature requests, helping us better understand and prioritize your needs.
* Report bugs directly, enabling faster resolutions and improved product reliability.
* This is more than just a support portal—it’s a centralized hub to enhance your experience, provide solutions faster, and keep your feedback front and center in our development process.

Explore our new [Support Help Center](https://logzio-support.atlassian.net/servicedesk/customer/user/login?destination=portals) for answers and assistance!


### Trace Context Support for .NET and Python

We’ve introduced Trace Context support for .NET and Python integrations, enabling better correlation between your logs and traces.

With this feature, you can now seamlessly connect logs to their associated traces, gaining deeper insights into the full execution flow of your applications.

To get started, install the OpenTelemetry logging instrumentation dependency for .NET or Python. This enhancement simplifies troubleshooting and improves observability across your system.

Learn more about [Trace Context](https://docs.logz.io/docs/user-guide/explore/trace-view/). 

### Enhanced API Capabilities in Event Manager

We’ve expanded the functionality of the Event Manager API to give you greater control over your security events. With this update, you can now:

* Close incidents directly via the API, reducing time spent on manual tasks and streamlining incident management workflows.
* Edit security events to reflect the latest updates and changes as investigations progress.
* Add comments to incidents via the API, ensuring key context and updates are documented and shared programmatically.

These enhancements are designed to simplify incident handling and help you and your team manage your security events seamlessly. [Read more](https://api-docs.logz.io/docs/logz/edit-security-rules-events/).

## December 2024

### Explore Upgrades and Improvements

#### New Visualization Features

We’re rolling out new visualization capabilities in the [Explore](https://logz.io/blog/explore-log-management/) log management interface that are available now in some accounts and will be added to all in the coming weeks and months. With these updates you can:

* Switch between linear and logarithmic scales 
* Add deployment markers 
* Compare data across time periods 

#### Warm Tier:
There is now a new option for log storage and access that bridges the gap between high-performance Hot storage and the low-cost Cold Tier. [Reach out to your customer success team](https://logz.io/customer-request/) for more information.

#### Trace View:
Traces add multi-telemetry insights to your logs, making it easier to find bottlenecks and identify errors in your environment. Our goal is to bring all telemetry data together in one place. The feature is slowly rolling out to all users, [reach out to your customer success team](https://logz.io/customer-request/) for more information.

### AI-Powered Observability

#### Root Cause Analysis:

We’ve added RCA on alerts set up in the platform by users. You can now get to the root causes of system issues with a trigger process through your alerting.

#### AI Agent:

We’ve also improved the “out of the box” questions user experience in the AI Agent (see example below).

Additionally we’ve added new default capabilities for the AI Agent in the US and EU within Explore. These include enhanced search capabilities and dynamic context, allowing you to tackle complex questions with greater precision over the original beta release of the agent. [Learn more](https://docs.logz.io/docs/user-guide/observability/assistantiq/).

### Retirement of Office 365 connectors within Microsoft Teams
Starting August 15, 2024, new Microsoft Teams endpoints must be configured using the Workflows app. [Read more on Microsoft’s blog](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/). As such we are retiring Office 365 connectors within Microsoft Teams. [Learn how to configure an endpoint for Microsoft Teams](https://docs.logz.io/docs/user-guide/integrations/notification-endpoints/ms-teams/).

## November 2024

### Explore Upgrades and Improvements

We’ve improved the filter pane to include:

* Log table and filters that update instantly as you type, showing results that match your search criteria.
* A new **Favorites** section for quick access to your most useful fields. 
* An improved **Available Fields** section with results from visible logs, and a percentage indication of field value frequencies.
* A new **Other Fields** section, where you can now view fields that aren’t marked as favorites or currently displayed in the logs, providing you a more comprehensive overview of your log data.

A new time-picker option lets you mix absolute and relative times and manually set the date and time to the second. Additionally, you can view your data in either UTC or your local time zone.

**Saved searches** from Explore can now be used to create visualizations and dashboards in OpenSearch Dashboards, streamlining data analysis.

You can now **edit Lucene filters** for more control and flexibility over searches.


### AI Agent: Smarter Responses and a Smoother Experience

* **Enhanced context** for more accurate responses.
* UI improvements for a smoother user interaction experience. Learn more here.

### Enhanced API Management and Usage Insights

* Improved handling of **API shared tokens**.
* You now have an indication of when a shared API was last used.

## October 2024

### Explore Logs and Data Features

* **Surrounding Logs** added to the log view, allowing users to view the surrounding logs or a single log for better context.
* An **improved log view** lets you filter, add to the table, group by fields, and ask the AI Agent questions about specific fields.
* Share and view individual logs from the **expanded log view**.
* **A column filtering**: An option to filter in and out directly from each column in the log table.

### Kubernetes 360 improvements

* Added **YAML configuration** for Kubernetes resources to improve troubleshooting and investigation
