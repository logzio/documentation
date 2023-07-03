---
id: Java Otel
title: Sending traces from Java applications via auto instrumentation with OpenTelemetry
sidebar_position: 1380
overview: test
product: ['tracing', 'java']
os: ['windows', 'linux']
filters: ['aws']
logo: java.svg
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


<Tabs
  defaultValue="overview"
  values={[
    {label: 'Overview', value: 'overview'},
    {label: 'Local host', value: 'local-host'},
    {label: 'Docker', value: 'docker'},
    {label: 'Kubernetes', value: 'kubernetes'},
    {label: 'Troubleshooting', value: 'troubleshooting'},
  ]}>
  

<!-- tab:start -->

<TabItem value="overview">


Deploy this integration to enable automatic instrumentation of your Java application using OpenTelemetry.

## Architecture overview

This integration includes:

* Downloading the OpenTelemetry Java agent to your application host
* Installing the OpenTelemetry collector with Logz.io exporter
* Establishing communication between the agent and collector

On deployment, the Java agent automatically captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.

</TabItem>

<!-- tab:end -->


<!-- tab:start -->

<TabItem value="local-host">

## Setup auto-instrumentation for your locally hosted Java application and send traces to Logz.io

**Before you begin, you'll need**:

* A Java application without instrumentation
* An active account with Logz.io
* Port `4317` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.

<!-- info-box-start:info -->
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
<!-- info-box-end -->


### 1. Download Java agent

Download the latest version of the [OpenTelemetry Java agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar) to the host of your Java application.

### 2. Download and configure OpenTelemetry collector

Create a dedicated directory on the host of your Java application and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.70.0) that is relevant to the operating system of your host.


After downloading the collector, create a configuration file `config.yaml` with the following parameters:

{@include: ./tracing-shipping/collector-config.md}

{@include: ./tracing-shipping/replace-tracing-token.html}


### 3. Start the collector

Run the following command:

```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the path to the directory where you downloaded the collector.
* Replace `<VERSION-NAME>` with the version name of the collector applicable to your system, e.g. `otelcontribcol_darwin_amd64`.

### 4. Attach the agent to the collector and run it

Run the following command from the directory of your Java application:

```shell
java -javaagent:<path/to>/opentelemetry-javaagent-all.jar \
     -Dotel.traces.exporter=otlp \
     -Dotel.metrics.exporter=none \
     -Dotel.resource.attributes=service.name=<YOUR-SERVICE-NAME> \
     -Dotel.exporter.otlp.endpoint=http://localhost:4317 \
     -jar target/*.jar
```

* Replace `<path/to>` with the path to the directory where you downloaded the agent.
* Replace `<YOUR-SERVICE-NAME>` with the name of your tracing service defined earlier.


### 5. Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).


## Controlling the number of spans

To limit the number of outgoing spans, you can use the sampling option in the Java agent.

The sampler configures whether spans will be recorded for any call to `SpanBuilder.startSpan`.

| System property                 | Environment variable            | Description                                                  |
|---------------------------------|---------------------------------|--------------------------------------------------------------|
| otel.traces.sampler              | OTEL_TRACES_SAMPLER              | The sampler to use for tracing. Defaults to `parentbased_always_on` |
| otel.traces.sampler.arg          | OTEL_TRACES_SAMPLER_ARG          | An argument to the configured tracer if supported, for example a ratio. |

Supported values for `otel.traces.sampler` are

- "always_on": AlwaysOnSampler
- "always_off": AlwaysOffSampler
- "traceidratio": TraceIdRatioBased. `otel.traces.sampler.arg` sets the ratio.
- "parentbased_always_on": ParentBased(root=AlwaysOnSampler)
- "parentbased_always_off": ParentBased(root=AlwaysOffSampler)
- "parentbased_traceidratio": ParentBased(root=TraceIdRatioBased). `otel.traces.sampler.arg` sets the ratio.


</TabItem>

<!-- tab:end -->

<!-- tab:start -->
<TabItem value="docker">


## Setup auto-instrumentation for your Java application using Docker and send traces to Logz.io

This integration enables you to auto-instrument your Java application and run a containerized OpenTelemetry collector to send your traces to Logz.io. If your application also runs in a Docker container, make sure that both the application and collector containers are on the same network.

**Before you begin, you'll need**:

* A Java application without instrumentation
* An active account with Logz.io
* Port `4317` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.


### 1. Download Java agent

Download the latest version of the [OpenTelemetry Java agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar) to the host of your Java application.


{@include: ./tracing-shipping/docker.md}

{@include: ./tracing-shipping/replace-tracing-token.html}



### 2. Attach the agent to the collector and run it

{@include: ./tracing-shipping/collector-run-note.md}


Run the following command from the directory of your Java application:

```shell
java -javaagent:<path/to>/opentelemetry-javaagent-all.jar \
     -Dotel.traces.exporter=otlp \
     -Dotel.metrics.exporter=none \
     -Dotel.resource.attributes=service.name=<YOUR-SERVICE-NAME> \
     -Dotel.exporter.otlp.endpoint=http://localhost:4317 \
     -jar target/*.jar
```

* Replace `<path/to>` with the path to the directory where you downloaded the agent.
* Replace `<YOUR-SERVICE-NAME>` with the name of your tracing service defined earlier.


### 3. Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).


## Controlling the number of spans

To limit the number of outgoing spans, you can use the sampling option in the Java agent.

The sampler configures whether spans will be recorded for any call to `SpanBuilder.startSpan`.

| System property                 | Environment variable            | Description                                                  |
|---------------------------------|---------------------------------|--------------------------------------------------------------|
| otel.traces.sampler              | OTEL_TRACES_SAMPLER              | The sampler to use for tracing. Defaults to `parentbased_always_on` |
| otel.traces.sampler.arg          | OTEL_TRACES_SAMPLER_ARG          | An argument to the configured tracer if supported, for example a ratio. |

Supported values for `otel.traces.sampler` are

- "always_on": AlwaysOnSampler
- "always_off": AlwaysOffSampler
- "traceidratio": TraceIdRatioBased. `otel.traces.sampler.arg` sets the ratio.
- "parentbased_always_on": ParentBased(root=AlwaysOnSampler)
- "parentbased_always_off": ParentBased(root=AlwaysOffSampler)
- "parentbased_traceidratio": ParentBased(root=TraceIdRatioBased). `otel.traces.sampler.arg` sets the ratio.


</TabItem>

<!-- tab:end -->



<TabItem value="kubernetes">


## Kubernetes overview

You can use a Helm chart to ship Traces to Logz.io via the OpenTelemetry collector. The Helm tool is used to manage packages of pre-configured Kubernetes resources that use charts.

**logzio-k8s-telemetry** allows you to ship traces from your Kubernetes cluster to Logz.io with the OpenTelemetry collector.

<!-- info-box-start:info -->
:::note
This chart is a fork of the [opentelemtry-collector](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-collector) Helm chart. The main repository for Logz.io helm charts are [logzio-helm](https://github.com/logzio/logzio-helm).
:::
<!-- info-box-end -->

<!-- info-box-start:info -->
:::caution Important
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
<!-- info-box-end -->

## Standard configuration

### 1. Deploy the Helm chart
 
Add `logzio-helm` repo as follows:
 
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```

### 2. Run the Helm deployment code

```
helm install  \
--set config.exporters.logzio.region=<<LOGZIO_ACCOUNT_REGION_CODE>> \
--set config.exporters.logzio.account_token=<<TRACING-SHIPPING-TOKEN>> \
logzio-k8s-telemetry logzio-helm/logzio-k8s-telemetry
```

{@include: ./tracing-shipping/replace-tracing-token.html}

`<<LOGZIO_ACCOUNT_REGION_CODE>>` - (Optional): Your logz.io account region code. Defaults to "us". Required only if your logz.io region is [different than US East](https://docs.logz.io/user-guide/accounts/account-region.html#available-regions).


### 3. Define the logzio-k8s-telemetry dns name

In most cases, the dns name will be `logzio-k8s-telemetry.default.svc.cluster.local`, where `default` is the namespace where you deployed the helm chart and `svc.cluster.name` is your cluster domain name.
  
If you are not sure what your cluster domain name is, you can run the following command to look it up: 
  
```shell
kubectl run -it --image=k8s.gcr.io/e2e-test-images/jessie-dnsutils:1.3 --restart=Never shell -- \
sh -c 'nslookup kubernetes.default | grep Name | sed "s/Name:\skubernetes.default//"'
```
  
It will deploy a small pod that extracts your cluster domain name from your Kubernetes environment. You can remove this pod after it has returned the cluster domain name.

### 4. Download Java agent

Download the latest version of the [OpenTelemetry Java agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar) to the host of your Java application.

### 5. Attach the agent to your java application 

Add the following command to your Java application Dockerfile or equivalent:

```shell
java -javaagent:<path/to>/opentelemetry-javaagent-all.jar \
     -Dotel.traces.exporter=otlp \
     -Dotel.metrics.exporter=none \
     -Dotel.resource.attributes=service.name=<<YOUR-SERVICE-NAME>> \
     -Dotel.exporter.otlp.endpoint=http://<<logzio-k8s-telemetry-service-dns>>:4317 \
     -jar target/*.jar
```

* Replace `<<path/to>>` with the path to the directory where you downloaded the agent.
* Replace `<<YOUR-SERVICE-NAME>>` with a name for your service under which it will appear in Logz.io Jaeger UI.
* Replace `<<logzio-k8s-telemetry-service-dns>>` with the OpenTelemetry collector service dns obtained previously (service IP is also allowed here).

### 6. Check Logz.io for your traces

Give your traces some time to get from your system to ours, then open [Logz.io](https://app.logz.io/).



##  Customizing Helm chart parameters

### Configure customization options

You can use the following options to update the Helm chart parameters: 

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install`.

* Edit the `values.yaml`.

* Overide default values with your own `my_values.yaml` and apply it in the `helm install` command. 

If required, you can add the following optional parameters as environment variables:
  
| Parameter | Description | 
|---|---|
| secrets.SamplingLatency | Threshold for the spand latency - all traces slower than the threshold value will be filtered in. Default 500. | 
| secrets.SamplingProbability | Sampling percentage for the probabilistic policy. Default 10. | 

### Example

You can run the logzio-k8s-telemetry chart with your custom configuration file that takes precedence over the `values.yaml` of the chart.

For example:

<!-- info-box-start:info -->
:::note
The collector will sample **ALL traces** where is some span with error with this example configuration. 
:::
<!-- info-box-end -->

```yaml
baseCollectorConfig:
  processors:
    tail_sampling:
      policies:
        [
          {
            name: error-in-policy,
            type: status_code,
            status_code: {status_codes: [ERROR]}
          },
          {
            name: slow-traces-policy,
            type: latency,
            latency: {threshold_ms: 400}
          },
          {
            name: health-traces,
            type: and,
            and: {
              and_sub_policy:
              [
                {
                  name: ping-operation,
                  type: string_attribute,
                  string_attribute: { key: http.url, values: [ /health ] }
                },
                {
                  name: main-service,
                  type: string_attribute,
                  string_attribute: { key: service.name, values: [ main-service ] }
                },
                {
                  name: probability-policy-1,
                  type: probabilistic,
                  probabilistic: {sampling_percentage: 1}
                }
              ]
            }
          },
          {
            name: probability-policy,
            type: probabilistic,
            probabilistic: {sampling_percentage: 20}
          }
        ] 
```

```
helm install -f <PATH-TO>/my_values.yaml \
--set logzio.region=<<LOGZIO_ACCOUNT_REGION_CODE>> \
--set logzio.tracing_token=<<TRACING-SHIPPING-TOKEN>> \
--set traces.enabled=true \
logzio-k8s-telemetry logzio-helm/logzio-k8s-telemetry
```

Replace `<PATH-TO>` with the path to your custom `values.yaml` file.

{@include: ./tracing-shipping/replace-tracing-token.html}




## Uninstalling the Chart

The uninstall command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-k8s-telemetry` deployment, use the following command:

```shell
helm uninstall logzio-k8s-telemetry
```

</TabItem>


<!-- tab:end -->

<!-- tab:start -->

<TabItem value="troubleshooting">

{@include: ../../_include/tracing-shipping/otel-troubleshooting.md}

</TabItem>

<!-- tab:end -->

</Tabs>

<!-- tabContainer:end -->
