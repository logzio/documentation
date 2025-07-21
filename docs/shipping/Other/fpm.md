---
id: FPM-data
title: FPM
overview: This integration sends Prometheus-format PHP-FPM metrics to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/phpfpm-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['55uVoiaFwAreNAf7DojQZN']
metrics_alerts: ['1A2NfkQQprZqbtzQOVrcO7']
drop_filter: []
---


FPM (FastCGI Process Manager) is an alternative PHP FastCGI implementation with some additional features (mostly) useful for heavy-loaded sites. 

## Send FPM metrics with Prometheus

### Run the containerized exporter

```shell
git clone git@github.com:hipages/php-fpm_exporter.git
cd php-fpm_exporter/test
docker-compose -p php-fpm_exporter up
```

### Download OpenTelemetry collector

:::note
If you already have OpenTelemetry, proceed to the next step.
:::

Create a dedicated directory on your host and download the OpenTelemetry collector that is relevant to the operating system of your host.

After downloading the collector, create a configuration file `config.yaml`.

### Configure the Receivers

Open the configuration file and ensure it contains the required configuration to collect your metrics:

```yaml
receivers:
 prometheus:
   config:
     scrape_configs:
       - job_name: 'otel-collector-php'
         scrape_interval: 5s
         static_configs:
           - targets: ['localhost:9253']


processors:
 resourcedetection/system:
   detectors: ["system"]
   system:
     hostname_sources: ["os"]
 attributes/agent:
   actions:
     - key: logzio_agent_version
       value: v1.0.36
       action: insert
     - key: cloudservice
       value: _CloudService_
       action: insert
     - key: role
       value: _role_
       action: insert


exporters:
 debug:
 logzio/logs:
   account_token: <<LOG-SHIPPING-TOKEN>>
   region: <<LOGZIO_ACCOUNT_REGION_CODE>> # Default is US
 prometheusremotewrite:
   endpoint: https://<<LISTENER-HOST>>:8053
   headers:
     Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
   resource_to_telemetry_conversion:
     enabled: true


service:
 pipelines:
   metrics:
     receivers:
       - prometheus
     exporters: [prometheusremotewrite]
     processors: [resourcedetection/system]
 telemetry:
   logs:
     level: debug
   metrics:
     address: localhost:8899
```

:::note
Ensure that your service pipeline includes the `debug` exporter in the `exporters` section.
See the OpenTelemetry [Debug Exporter documentation](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.111.0/exporter/debugexporter/README.md) for more details.
:::

@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html}

{@include: ../../_include/p8s-shipping/replace-prometheus-token.html}


### Start the Collector

Run the following command:

```shell
<path/to>/otelcol-contrib --config ./config.yaml
```

* Replace `<path/to>` with the path to the directory where you downloaded the collector. If the name of your configuration file is different to config, adjust the name in the command accordingly.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["55uVoiaFwAreNAf7DojQZN"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}

{@include: ../../_include/log-shipping/otel-filter.md} 


## Send FPM metrics with Telegraf


Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format PHP-FPM metrics to Logz.io, you need to add the **inputs.phpfpm** and **outputs.http** plug-ins to your Telegraf configuration file.

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher

{@include: ../../_include/metric-shipping/telegraf-setup.md}

#### Add the inputs.PHP-FPM plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the PHP-FPM data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.phpfpm]]
  ## An array of addresses to gather stats about. Specify an ip or hostname
  ## with optional port and path
  ##
  ## Plugin can be configured in three modes (either can be used):
  ##   - http: the URL must start with http:// or https://, ie:
  ##       "http://localhost/status"
  ##       "http://192.168.130.1/status?full"
  ##
  ##   - unixsocket: path to fpm socket, ie:
  ##       "/var/run/php5-fpm.sock"
  ##      or using a custom fpm status path:
  ##       "/var/run/php5-fpm.sock:fpm-custom-status-path"
  ##      glob patterns are also supported:
  ##       "/var/run/php*.sock"
  ##
  ##   - fcgi: the URL must start with fcgi:// or cgi://, and port must be present, ie:
  ##       "fcgi://10.0.0.12:9000/status"
  ##       "cgi://10.0.10.12:9001/status"
  ##
  ## Example of multiple gathering from local socket and remote host
  ## urls = ["http://192.168.1.20/status", "/tmp/fpm.sock"]
  urls = ["http://localhost/status"]

  ## Duration allowed to complete HTTP requests.
  # timeout = "5s"

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/phpfpm/README.md)
::: 
 

#### Add the outputs.http plug-in
  
{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}
  
### Start Telegraf

{@include: ../../_include/metric-shipping/telegraf-run.md}

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["55uVoiaFwAreNAf7DojQZN"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}

 
