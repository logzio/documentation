---
id: docker-otel
title: Sending traces from instrumented Docker containers using OpenTelemetry
sidebar_position: 1380
overview: test
product: ['tracing', 'docker']
os: ['windows', 'linux']
filters: ['docker', 'existing-instrumentation']
logo: docker-logo.png
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


<Tabs>

<!-- tab:start -->

<TabItem value="overview" label="Overview" default>


## Overview

This integration enables you to send traces from your instrumented applications running in Docker. This is achieved by using a dedicated Logz.io OpenTelemetry collector deployed in the same Docker network as your application. This collector configuration can collect traces from:

* OpenTelemetry
* Zipkin
* Jaeger
* OpenCensus 


</TabItem>

<!-- tab:end -->


<!-- tab:start -->

<TabItem value="setup" label="Setup">


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


</TabItem>

<!-- tab:end -->

<!-- tab:start -->

<TabItem value="troubleshooting" label="Troubleshooting">

{@include: ../../_include/tracing-shipping/otel-troubleshooting.md}

</TabItem>

<!-- tab:end -->

</Tabs>

<!-- tabContainer:end -->