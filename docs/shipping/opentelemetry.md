---
id: OpenTelemetry
title: OpenTelemetry
overview: Deploy this integration to send traces from your OpenTelemetry installation to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


<Tabs>


<!-- tab:start -->

<TabItem value="overview" label="Overview" default>


Deploy this integration to send traces from your OpenTelemetry installation to Logz.io.

## Architecture overview

This integration includes:

* Configuring the OpenTelemetry collector to receive traces from your OpenTelemetry installation and send them to Logz.io

On deployment, your OpenTelemetry instrumentation captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.

</TabItem>

<!-- tab:end -->


<!-- tab:start -->

<TabItem value="local-host" label="Local host">



## Set up your locally hosted OpenTelemetry installation to send traces to Logz.io

**Before you begin, you'll need**:

* An active account with Logz.io

<!-- info-box-start:info -->
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
<!-- info-box-end -->


### Download and configure OpenTelemetry collector

Create a dedicated directory on the host of your application and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.70.0) that is relevant to the operating system of your host.

After downloading the collector, create a configuration file `config.yaml` with the following parameters:

{@include: ../_include/tracing-shipping/collector-config.md}

{@include: ../_include/tracing-shipping/replace-tracing-token.html}

{@include: ../_include/tracing-shipping/tail-sampling.md}


If you already have an OpenTelemetry installation, add the following parameters to the configuration file of your existing OpenTelemetry collector:

* Under the `exporters` list

```yaml
  logzio/traces:
    account_token: <<TRACING-SHIPPING-TOKEN>>
    region: <<LOGZIO_ACCOUNT_REGION_CODE>>
```

* Under the `service` list:

```yaml
  extensions: [health_check, pprof, zpages]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [tail_sampling, batch]
      exporters: [logzio/traces]
```

{@include: ../_include/tracing-shipping/replace-tracing-token.html}

An example configuration file looks as follows:

{@include: ../_include/tracing-shipping/collector-config.md}

### Instrument the application

If your application is not yet instrumented, instrument the code as described in our [tracing documents](https://docs.logz.io/shipping/#tracing-sources).


### Start the collector

Run the following command:

```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the path to the directory where you downloaded the collector.
* Replace `<VERSION-NAME>` with the version name of the collector applicable to your system, e.g. `otelcontribcol_darwin_amd64`.

### Run the application

Run the application to generate traces.


### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).

</TabItem>

<!-- tab:end -->

<!-- tab:start -->

<TabItem value="docker" label="Docker">


## Set up your OpenTelemetry installation using containerized collector to send traces to Logz.io

**Before you begin, you'll need**:

* An active account with Logz.io


### Instrument the application

If your application is not yet instrumented, instrument the code as described in our [tracing documents](https://docs.logz.io/shipping/#tracing-sources).


{@include: ../_include/tracing-shipping/docker.md}

{@include: ../_include/tracing-shipping/replace-tracing-token.html}

### Run the application

{@include: ../_include/tracing-shipping/collector-run-note.md}


Run the application to generate traces.


### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).


</TabItem>

<!-- tab:end -->

<!-- tab:start -->

<TabItem value="kubernetes" label="Kubernetes">

## Overview

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


### Deploy the Helm chart
 
Add `logzio-helm` repo as follows:
 
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```

### Run the Helm deployment code

```
helm install  \
--set config.exporters.logzio.region=<<LOGZIO_ACCOUNT_REGION_CODE>> \
--set config.exporters.logzio.account_token=<<TRACING-SHIPPING-TOKEN>> \
--set traces.enabled=true \ 
logzio-k8s-telemetry logzio-helm/logzio-k8s-telemetry
```

{@include: ../_include/tracing-shipping/replace-tracing-token.html}
`<<LOGZIO_ACCOUNT_REGION_CODE>>` - Your Logz.io account region code. [Available regions](https://docs.logz.io/user-guide/accounts/account-region.html#available-regions).

### Check Logz.io for your traces

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

#### Example

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

{@include: ../_include/tracing-shipping/replace-tracing-token.html}





## Uninstalling the Chart

The uninstall command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-k8s-telemetry` deployment, use the following command:

```shell
helm uninstall logzio-k8s-telemetry
```

</TabItem>

<!-- tab:end -->

<!-- tab:start -->

<TabItem value="troubleshooting" label="Troubleshooting">

{@include: ../_include/tracing-shipping/otel-troubleshooting.md}

</TabItem>

<!-- tab:end -->

</Tabs>

<!-- tabContainer:end -->
