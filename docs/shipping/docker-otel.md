---
id: Docker traces
title: Docker traces
overview: This integration enables you to send traces from your instrumented applications running in Docker. This is achieved by using a dedicated Logz.io OpenTelemetry collector deployed in the same Docker network as your application. 
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/docker.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---



## Overview

This integration enables you to send traces from your instrumented applications running in Docker. This is achieved by using a dedicated Logz.io OpenTelemetry collector deployed in the same Docker network as your application. This collector configuration can collect traces from:

* OpenTelemetry
* Zipkin
* Jaeger
* OpenCensus 


**Before you begin, you'll need**:

* An instrumented application running in a Docker network
* An active account with Logz.io
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.


## In the same Docker network as your application:

{@include: ../../_include/tracing-shipping/docker.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


### Run the application

{@include: ../../_include/tracing-shipping/collector-run-note.md}

Run the application to generate traces.


### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).



{@include: ../../_include/tracing-shipping/otel-troubleshooting.md}
