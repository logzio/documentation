---
id: Linux-data
title: Linux Operating System
overview: Send your Linux machine logs and metrics to Logz.io to monitor and manage your Linux data, allowing you to identify anomalies, investigate incidents, get to the root cause of any issue, and quickly resolve it.
product: ['logs','metrics']
os: ['linux']
filters: ['Operating Systems', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/linux.svg
logs_dashboards: ['6AJEM9FdpE5HqXem42edp']
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['6hb5Nww0ar4SXoF92QxMx']
metrics_alerts: ['6y7xNsm1RXlXAFUAXLyOpZ']
drop_filter: []
---


**Before you begin, you'll need**:

* Root access

## Send Linux logs and metrics with OpenTelemetry

:::note
For a simpler and more efficient way to collect and send metrics, use the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).
:::

**1. Create a Logz.io directory:**

```shell
sudo mkdir /opt/logzio-agent
```

**2. Download OpenTelemetry tar.gz:**

```shell
curl -fsSL "https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.111.0/otelcol-contrib_0.111.0_linux_amd64.tar.gz" >./otelcol-contrib.tar.gz
```
 
**3. Extract the OpenTelemetry binary:**

```shell
sudo tar -zxf ./otelcol-contrib.tar.gz --directory /opt/logzio-agent otelcol-contrib
```
 

**4. Create the OpenTelemetry config file:**

```shell
sudo touch /opt/logzio-agent/otel_config.yaml
```
 
**5. Copy the following into the config file:**

Replace `<<LOG-SHIPPING-TOKEN>>`, `<<LISTENER-HOST>>`, and `<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` with the relevant parameters from your Logz.io account.


 
```yaml
receivers:
  filelog/localhost_linux_system:
    include:
      - /var/log/*.log
    include_file_path: true
    operators:
      - type: move
        from: attributes["log.file.name"]
        to: attributes["log_file_name"]
      - type: move
        from: attributes["log.file.path"]
        to: attributes["log_file_path"]
    attributes:
      type: agent-linux
  hostmetrics/localhost_linux_system:
    collection_interval: 15s
    scrapers:
      cpu:
        metrics:
          system.cpu.utilization:
            enabled: true
      disk:
      load:
      filesystem:
      memory:
        metrics:
          system.memory.utilization:
            enabled: true
      network:
      paging:
      process:
        mute_process_name_error: true
        mute_process_exe_error: true
        mute_process_io_error: true
processors:
  resourcedetection/system:
    detectors: ["system"]
    system:
      hostname_sources: ["os"]
  filter:
    metrics:
      include:
        match_type: strict
        metric_names: ["system.cpu.time", "system.cpu.load_average.1m", "system.cpu.load_average.5m", "system.cpu.load_average.15m", "system.cpu.utilization", "system.memory.usage", "system.memory.utilization", "system.filesystem.usage", "system.disk.io", "system.disk.io_time", "system.disk.operation_time", "system.network.connections", "system.network.io", "system.network.packets", "system.network.errors", "process.cpu.time", "process.memory.usage", "process.disk.io", "process.memory.usage", "process.memory.virtual"]
exporters:
  debug:
  logzio/logs:
    account_token: <<LOG-SHIPPING-TOKEN>>
    region: <<LOGZIO_ACCOUNT_REGION_CODE>> # Default is US
    headers:
      user-agent: logzio-linux-logs
  prometheusremotewrite:
    endpoint: https://<<LISTENER-HOST>>:8053
    headers:
      Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
      user-agent: logzio-linux-metrics
    resource_to_telemetry_conversion:
      enabled: true
    target_info:
      enabled: false
service:
  pipelines:
    logs:
      receivers:
        - filelog/localhost_linux_system
      processors:
        - resourcedetection/system
      exporters: [logzio/logs]
    metrics:
      receivers:
        - hostmetrics/localhost_linux_system
      processors:
        - resourcedetection/system
        - filter
      exporters: [prometheusremotewrite]
  telemetry:
    logs:
      level: "info"
    metrics:
      address: localhost:8888
```
:::note 
Ensure that your service pipeline includes the `debug` exporter in the `exporters` section.
See the OpenTelemetry [Debug Exporter documentation](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.111.0/exporter/debugexporter/README.md) for more details.
:::

:::caution Important
If OpenTelemetry metrics are already running on port 8888, edit the `address` field in the config file.
:::
 

**6. Create the service file:**

```shell
sudo touch /etc/systemd/system/logzioOTELCollector.service
```

And copy the service file's content:
 
```shell
[Unit]

Description=OTEL collector for collecting logs/metrics and exporting them to Logz.io.

[Service]

ExecStart=/opt/logzio-agent/otelcol-contrib --config /opt/logzio-agent/otel_config.yaml

[Install]

WantedBy=multi-user.target

```

{@include: ../../_include/log-shipping/otel-filter.md} 

## Manage your OpenTelemetry on Localhost

Manage OpenTelemetry on your machine using the following commands:

|Description|Command|
|--|--|
|Start service|`sudo systemctl start logzioOTELCollector`|
|Stop service|`sudo systemctl stop logzioOTELCollector`|
|Service logs|`sudo systemctl status -l logzioOTELCollector`|
|Delete service|`sudo systemctl stop logzioOTELCollector` `sudo systemctl reset-failed logzioOTELCollector 2>/dev/null` `sudo rm /etc/systemd/system/logzioOTELCollector.service 2>/dev/null` `sudo rm /usr/lib/systemd/system/logzioOTELCollector.service 2>/dev/null` `sudo rm /etc/init.d/logzioOTELCollector 2>/dev/null`|


## Send data through rsyslog 

**Before you begin, you'll need**:

* Root access
* Port 5000 open 

### Run the rsyslog configuration script

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html} 

```shell
curl -sLO https://github.com/logzio/logzio-shipper/raw/master/dist/logzio-rsyslog.tar.gz \
  && tar xzf logzio-rsyslog.tar.gz \
  && sudo rsyslog/install.sh -t linux -a "<<LOG-SHIPPING-TOKEN>>" -l "<<LISTENER-HOST>>"
```


The above assumes the following defaults:

* Log location - `/var/log/`
* Log type - `syslog`

### Check Logz.io for your logs

Allow some time for data ingestion, then open your [metrics dashboard](https://app.logz.io/#/dashboard/metrics).

Encounter an issue? See our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.

 
 

{@include: ../../_include/log-shipping/rsyslog-troubleshooting.md} 

  
