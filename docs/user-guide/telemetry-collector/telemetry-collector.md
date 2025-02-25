---
sidebar_position: 1
title: Getting Started with Logz.io's Telemetry Collector
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Send your data with Logz.io's Telemetry Collector
keywords: [Telemetry Collector, Telemetry, ship data, collectors, metrics, tracing, logs]
slug: /telemetry-collector/
---


Logz.io’s Telemetry Collector lets you quickly send your data based on the configuration that fits your needs. For example, you can use it to send logs, metrics, and tracing data back to Logz.io’s observability platform.

:::note
Telemetry Collector is currently **available in all regions** except for Japan. If you're located in this region, you can use **[Logz.io’s integrations hub](https://app.logz.io/#/dashboard/integrations/collectors)** to send your data.
:::


## Why should you use Telemetry Collector?

Configuring and running Logz.io’s Telemetry Collector provides several advantages, including:

* **Easy installation process** - Logz.io’s Telemetry Collector lets you easily configure your data sending process by executing a single line of code.
* **Full coverage** - The Telemetry Collector collects logs, metrics, and tracing data from your end, providing a complete observability platform to monitor and improve your data.

## Supported platforms

Logz.io’s Telemetry Collector supports **Kubernetes**, **AWS**, **GCP**, **Azure** and **localhost** servers for logs, metrics, traces, and SIEM.

If you're interested in sending your data through a different source, you can browse Logz.io's **[Integration hub](https://app.logz.io/#/dashboard/integrations/collectors)**, which includes over 300 shipping methods.


## Getting started with the Telemetry Collector:

* [Send **AWS** data with Telemetry Collector](https://docs.logz.io/docs/telemetry-collector/telemetry-collector-aws/)
  * [Manage an AWS Telemetry Collector](https://docs.logz.io/docs/telemetry-collector/telemetry-collector-aws/#manage-your-ec2-telemetry-collector)
* [Send **Kubernetes** data with Telemetry Collector](https://docs.logz.io/docs/telemetry-collector/telemetry-collector-k8s/)
  * [Manage a Kubernetes Telemetry Collector](https://docs.logz.io/docs/telemetry-collector/telemetry-collector-k8s/#manage-your-telemetry-collector)
* [Send **Localhost** data with Telemetry Collector](https://docs.logz.io/docs/telemetry-collector/telemetry-collector-localhost/)
  * [Manage a Localhost Telemetry Collector](https://docs.logz.io/docs/telemetry-collector/telemetry-collector-localhost/#manage-and-remove-a-telemetry-collector)

###### Additional resources

* [View Telemetry Collector on GitHub](https://github.com/logzio/logzio-agent-manifest)