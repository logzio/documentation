---
sidebar_position: 19
title: Release Notes
description: What's new in Logz.io - latest releases, features, enhancements, and updates
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [release notes, logzio, logs, metrics, traces, logz.io, updates, releases, features]
toc_max_heading_level: 2
---

## July 2025

### Logz.io Dashboards

Logz.io Dashboards are now generally available to all customers, providing an interface for visualizing and exploring your observability data. This release includes several additional capabilities:

**New Metrics Builder in Logz.io Dashboards**
Logz.io Dashboards now include a Metrics Builder - a new interface for constructing PromQL queries. Users can browse available metrics, labels, and values, with PromQL expressions generated in real time based on their selections. This helps simplify data exploration and query building, eliminating the need to write PromQL manually.

**Drilldown links**
You can now make any table cell clickable by turning column values into customizable links. To set this up, go to Column Settings, click Link, and enable the Enabling Link option. This allows for quick and easy drilldowns directly from your tables.

**Dashboard Management via API**
You can now manage Logz.io Dashboards using our API - create, update, delete, and retrieve dashboards as needed. This provides a flexible way to access and automate native dashboards, streamlining dashboard operations. For full details, see the API documentation.

**Migrating Dashboards from OpenSearch Dashboards or Grafana**
You can now migrate your existing dashboards from OpenSearch Dashboards or Grafana into Logz.io Dashboards. [Contact our support team](mailto:help@logz.io) to get started with the migration process.

[Try it now in your Logz.io Dashboard](https://app.logz.io/#/dashboard/dashboards-hub).

### Core Updates

**Logz.io Agent Manifest Integration upgraded to v2.0.6**
* Added traces and span metrics pipelines for Linux, Linux EC2, macOS, and Windows
* Upgraded OpenTelemetry version from `v0.82.0` to `v0.109.0`
* Introduced new parameters for localhost types: `samplingLatency`, `samplingProbability`, `isSpanMetrics`
* Added OpenTelemetry templates for traces and span metrics
* Added localhost end-to-end tests for Linux, macOS, and Windows

[View on GitHub](https://github.com/logzio/logzio-agent-manifest)

**Logz.io Monitoring Helm Chart upgraded to v7.3.1**
* Upgraded logzio-k8s-telemetry chart to `v5.2.1`
    * Fixed Pod Disruption Budget selector label for the SPM collector (Contributed by @jod972)
    * Added `PriorityClassName` support for the SPM collector (Contributed by @jod972)
    * Added configurable replica counts for Traces and SPM collectors
* Upgraded `logzio-logs-collector` chart to `v2.1.0`
    * Updated `otel/opentelemetry-collector-contrib` image to `v0.127.0`
        *  Note: The `time` attribute has been removed from the log record. The log timestamp is now only available under `@timestamp` in Logz.io.


[View on GitHub](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-monitoring)


## June 2025

### AI Agent

Use insight cards to create alerts or dashboards.

You can now take action directly from your AI Agent conversations. The AI Agent generates dashboards and visualizations as part of its analysis. Found something useful? Add it to your dashboards with one click, or turn it into an alert to track issues, monitor changes, and move seamlessly from investigation to observability.

To get started, start a conversation with the [AI Agent](https://docs.logz.io/docs/user-guide/observability/assistantiq/) and turn your data into actionable dashboards and alerts.

### Logz.io Dashboards (Beta)

The Dashboards Beta now includes several new capabilities:

* Unified telemetry view - Visualize logs, metrics, and traces together in a single dashboard to maintain full context during investigations.
* Explore integration - Send visualizations from Explore directly to a dashboard with one click.
* Improved tables and filters - Use new column types (e.g., links, gauges) and enhanced filters for more actionable dashboards.

Note: Logz.io Dashboards are in beta. To join, contact your account manager or [Logz.io support](mailto:help@logz.io).

### Core Updates

**docker-logs-collector upgraded to v0.1.2**
* Base image updated to Debian Bookworm for improved `glibc` compatibility.
* Added support for the `LOGZIO_BULK_SIZE_MB` environment variable (1–9MB; default 2MB).
* Output plugin now pulled from the `fluent-bit-logzio-output` GitHub release assets.

[View on GitHub](https://github.com/logzio/docker-logs-collector)

**fluent-bit-logzio-output upgraded to v0.6.3**
* Fixed a critical stack overflow crash under high load.
* Introduced `logzio_bulk_size_mb` parameter (1–9MB; default 2MB) for tuning batch size before compression.
* Plugin binaries now distributed via GitHub release assets. Update your download method as noted in the README.

[View on GitHub](https://github.com/logzio/fluent-bit-logzio-output)


## May 2025

### Data source variables in Logz.io dashboards

You can now define Log Datasource variables in your dashboards, making it easier to switch between data sources at runtime.

This feature brings you one step closer to unified observability — flexible dashboards that adapt to your data context.

[Create a dashboard](https://app.logz.io/#/dashboard/dashboards-hub)

### AI Agent Analysis (Beta)

Introducing AI Agent Analysis, a new feature that helps accelerate incident response by automatically investigating alerts in your Logz.io environment.

When an alert is triggered, the AI Agent analyzes related logs, metrics, and patterns to uncover root causes and surface key findings. Insights are sent directly to a designated Slack channel and stored in the AI Agent chat for future reference.

*Note: AI Agent Analysis is currently in beta. Functionality and results may change as we continue to gather user feedback and improve the experience. To get early access, contact your account manager or reach out to Support.*

[Create an alert](https://app.logz.io/#/dashboard/alerts/v2019/new)

### Core Updates

**Logz.io Monitoring Integration upgraded to v7.1.1**

This release includes subchart upgrades and expanded configuration options:

All subcharts now support `global.tolerations`
`logzio-fluentd` upgraded to v1.0.2
`logzio-k8s-telemetry` upgraded to v5.0.4
`logzio-logs-collector` upgraded to v2.0.1
`logzio-apm-collector` upgraded to v1.2.1
`logzio-trivy` upgraded to v1.0.1
`logzio-k8s-events` updated to v1.0.1, now with support for `tolerations` and `global.tolerations`

**Logz.io Agent Manifest Integration upgraded to v2.0.2**

This release adds support for the OTLP receiver on:
* `localhost` for Windows, macOS, and Linux
* EC2 Linux instances

**New: Logz.io Logback Appender v2.3.0**
Introduced the `<executor>` configuration option to allow specifying a custom `ScheduledExecutorService` for background log-sending tasks.

**Logz.io Monitoring Chart Integration upgraded to v7.3.0**

* `logzio-apm-collector` upgraded to v1.2.3
    Added support for automatic resource detection using the `distribution` and `resourceDetection.enabled` flags.
* `logzio-logs-collector` upgraded to v2.0.2
    Now also supports automatic resource detection via `distribution` and `resourceDetection.enabled`
* `logzio-k8s-telemetry` upgraded to v5.2.0
    * Exposes the collector metrics port by default
    * Adds support for `podDisruptionBudget` and `topologySpreadConstraints`
    * Includes automatic resource detection support using `distribution` and `resourceDetection.enabled`
* Operator await job Now dynamically determines the webhook path based on the release namespace and chart name
* `opentelemetry-operator` chart upgraded to ~0.86.2


## April 2025

### Logz.io Dashboards (Beta)

Over the next few weeks we’re rolling out Logz.io Dashboards, an intuitive hub for visualizing and exploring your observability data in one centralized view.

Designed for monitoring, investigations, and collaborative troubleshooting, Logz.io Dashboards bring together logs and metrics in a unified experience.

_Note: Logz.io Dashboards are currently in beta. Contact your account manager or [support](mailto:help@logz.io) to request access._

### Log Parsing API

The new Parsing Rules API allows you to manage your Sawmill pipelines programmatically—giving you greater flexibility and automation for your log processing workflows.

Use the API to create, update, and manage parsing rule, streamlining how you handle custom log transformations across environments.

_Note: The Parsing Rules API requires enablement. Contact your [account manager](mailto:sales@logz.io) to request access._

### Core Updates:

**Updated Logzio API Fetcher version 2.0.0:**

* Added Google Workspace support
* Added option to configure multiple Logz.io outputs

[View on GitHub](https://github.com/logzio/logzio-api-fetcher/tree/2.0.0).

**Updated the logzio-monitoring Chart integration with version v7.1.2:**

* Upgrade opentelemetry-operator chart to ~0.82.0
* Upgrade logzio-fluentd chart to 1.0.1
* Upgrade ARM and AMD fluentd image version to v1.18.0-debian-logzio-amd64-1.3 and v1.18.0-debian-logzio-arm64-1.3

[View on GitHub](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-monitoring).

**Released the Prometheus Alerts Migrator Helm Chart integration with version v3.0.0**

:::tip note
Only upgrade to v3.0.0 if you're using Grafana 10 in Logz.io. This version is **not compatible** with earlier Grafana versions.
:::

* Upgrade logzio/prometheus-alerts-migrator image v1.2.1-> v1.3.0:
* Upgrade GoLang version to 1.24

Upgrade dependencies:
* `logzio_terraform_client: 1.22.0 -> v1.23.2`
* `prometheus/alertmanager: v0.28.0 -> v0.28.1`
* `prometheus/common: v0.61.0 -> v0.62.0`
* `prometheus/prometheus: v0.301.0 -> v0.302.1`
* `k8s.io/api: v0.32.0 -> v0.32.2`
* `k8s.io/apimachinery: v0.32.0 -> v0.32.2`
* `k8s.io/client-go: v0.32.0 -> v0.32.2`

[View on GitHub](https://github.com/logzio/logzio-helm/tree/master/charts/prometheus-alerts-migrator).

**Released the Logzio Terraform provider integration with version v1.17.1:**

* Upgrade logzio_client_terraform to 1.23.2

Upgrade Grafana API for compatibility with Grafana 10

:::tip note
Only relevant if you're using **Grafana 10** in Logz.io. If you're on an earlier version, no upgrade is needed.
:::

Breaking changes:
* Grafana Alerts API `exec_err_state` field is no longer configurable, always defaults to `OK`
* Grafana Contact Point `teams` now refers to Microsoft Teams Workflows Contact Point. The old `teams` endpoint was deprecated
* Default notification policy contact point changed from `default-email` to `grafana-default-email`
* Webhook Contact Point now supports `authorization_credentials`

[View on GitHub](https://github.com/logzio/terraform-provider-logzio).












## March 2025

### Explore improvements:

**Enhanced Lucene Query Editor** - Syntax highlighting and auto suggestions to streamline query building and troubleshooting.

**Date Picker Updates** - Now located next to the query line, the date picker features an improved timestamp for better readability.

**Trace Tab Indicator** - An indicator now appears on the Traces tab whenever trace data is linked to the log you're viewing, making it easy to spot available traces.

### Core updates:

**Logzio-Monitoring Helm Chart:**

Added support for enabling the OpenTelemetry Operator to auto-instrument cluster applications.

Integrated opentelemetry-operator chart (v0.79.0).

Secret values have been centralized under global:

* `secrets.MetricsToken >> global.logzioMetricsToken`
* `secrets.TracesToken >> global.logzioTracesToken`
* `secrets.SpmToken >> global.logzioSpmToken`
* `secrets.k8sObjectsLogsToken >> global.logzioLogsToken`
* `secrets.env_id >> global.env_id`
* `secrets.LogzioRegion >> global.logzioRegion`
* `secrets.CustomTracingEndpoint >> global.customTracesEndpoint`
* Deprecate `secrets.p8s_logzio_name and secrets.ListenerHost`

Added customization options for propagators, samplers, data collection types, and enabled libraries.

Added OTLP receivers to the metrics pipeline for improved telemetry collection. [Read more](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-monitoring).


Added support for [migrating to logzio-monitoring 7.x.x](https://docs.logz.io/docs/shipping/containers/kubernetes/#migrating-to-logzio-monitoring-7xx) in Kubernetes.

**Logzio Collector Agent Integration:**

* Updated the generated Helm command to align with the logzio-monitoring Helm Chart v7.0.0 structure.
* Added updates to the Agent script to support the new Helm version.
* Updated the UI to reflect the new Helm deployment structure.

[Read more](https://github.com/logzio/logzio-agent-manifest).


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
