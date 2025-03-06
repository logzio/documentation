---
id: localhost-mac
title: Mac Operating System
overview: Send your Mac machine logs and metrics to Logz.io to monitor and manage your Mac data, allowing you to identify anomalies, investigate incidents, get to the root cause of any issue, and quickly resolve it.
product: ['logs','metrics']
os: ['mac']
filters: ['Operating Systems', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/mac-os.svg
logs_dashboards: ['2c8z6DVvPatBZMgZ7qpfff']
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['2gsQP2xRef7dkwt8pxWieo']
metrics_alerts: ['hWld33IEO6gZMpp2e4vs0']
drop_filter: []
---



## Send Mac logs and metrics using Opentelemetry service

:::note
For a simpler and more efficient way to collect and send metrics, use the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).
:::

**1. Create a Logz.io directory:**

```shell
sudo mkdir /opt/logzio-agent
```

**2. Download OpenTelemetry tar.gz:**

```shell
curl -fsSL "https://github.com/logzio/otel-collector-distro/releases/download/v0.111.0/otelcol-logzio-darwin_amd64.tar.gz" >./otelcol-logzio.tar.gz
```

**3. Extract the OpenTelemetry binary:**

```shell
sudo tar -zxf ./otelcol-logzio.tar.gz --directory /opt/logzio-agent
```
 
**4. Create the OpenTelemetry config file:**

```shell
sudo touch /opt/logzio-agent/otel_config.yaml
```

**5. Copy the following OpenTelemetry config content into the config file:**

Replace  `<<LOG-SHIPPING-TOKEN>>`,  `<<LISTENER-HOST>>`, and `<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` with the relevant parameters from your Logz.io account.
 

```yaml
receivers:
  filelog/localhost_mac_system:
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
      type: agent-mac
  hostmetrics/localhost_mac_system:
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
      user-agent: logzio-mac-logs
  prometheusremotewrite:
    endpoint: https://<<LISTENER-HOST>>:8053
    headers:
      Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
      user-agent: logzio-mac-metrics
    resource_to_telemetry_conversion:
      enabled: true
    target_info:
        enabled: false
service:
  pipelines:
    logs:
      receivers:
        - filelog/localhost_mac_system
      processors:
        - resourcedetection/system
      exporters: [logzio/logs]
    metrics:
      receivers:
        - hostmetrics/localhost_mac_system
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

**6. Create plist file:**

```shell
sudo touch /Library/LaunchDaemons/com.logzio.OTELCollector.plist
```

Copy the plist file's content:

```shell
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.logzio.OTELCollector</string>
        <key>RunAtLoad</key>
        <true/>
        <key>StandardErrorPath</key>
        <string>/opt/logzio-agent/logzio_otel_collector.log</string>
        <key>ProgramArguments</key>
        <array>
            <string>/opt/logzio-agent/otelcol-logzio-darwin_amd64</string>
            <string>--config</string>
            <string>/opt/logzio-agent/otel_config.yaml</string>
        </array>
    </dict>
</plist>
```

{@include: ../../_include/log-shipping/otel-filter.md} 

## Manage your OpenTelemetry on Mac

Manage OpenTelemetry on your machine using the following commands:

Description|Command
|--|--|
|Start service|`sudo launchctl load /Library/LaunchDaemons/com.logzio.OTELCollector.plist`|
|Stop service|`sudo launchctl stop com.logzio.OTELCollector`|
|Service logs|`sudo tail -F /opt/logzio-agent/logzio_otel_collector.log`|
|Delete service|`sudo launchctl remove com.logzio.OTELCollector` `sudo rm /Library/LaunchDaemons/com.logzio.OTELCollector.plist`|
