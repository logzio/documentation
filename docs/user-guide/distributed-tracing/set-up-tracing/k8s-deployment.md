---
sidebar_position: 2
title: Kubernetes Deployment Reference to Send Traces
description: Ship Kubernetes traces to Logz.io with a Helm chart
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, traces, tracing, helm chart, helm, kubernetes, ship data, observability, distributed tracing]
slug: /distributed-tracing/set-up-tracing/k8s-deployment/
---

If you're working with Kubernetes, you can ship your traces to Logz.io using a Helm chart, via the OpenTelemetry collector.

The following guide will walk you through how to get your Tracing account token and how to configure and send your Helm chart to Logz.io.

The main repository for Logz.io helm charts are [logzio-helm](https://github.com/logzio/logzio-helm).

Our Helm chart is designed to automatically set up your tracing environment, simplifying the process of sending traces to Logz.io. This feature ensures a hassle-free setup, allowing you to focus on your Kubernetes deployment without worrying about manual configurations.


#### _Send traces from Kubernetes_


##### Determine which Tracing account you want to use and get your Tracing account token
Look up your Distributed Tracing `ACCOUNT TOKEN`. 

##### Get your region code


##### Ship your traces to Logz.io

Logz.io uses a Helm chart to send traces from your Kubernetes cluster via the OpenTelemetry collector. 

Select **[Send your traces](https://app.logz.io/#/dashboard/integrations/collectors?tags=Tracing) [> Kubernetes](https://app.logz.io/#/dashboard/integrations/Kubernetes)** and follow the steps to deploy the chart and trace your data.

##### Check the Distributed Tracing tab for your traces.

Give your traces some time to get from your system to ours, then check the Distributed Tracing tab in Logz.io to see the traces in the Jaeger UI.
