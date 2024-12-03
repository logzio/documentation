---
id: Windows
title: Windows Operating System
overview: Send your Windows machine logs and metrics to Logz.io to monitor and manage your Windows data, allowing you to identify anomalies, investigate incidents, get to the root cause of any issue, and quickly resolve it.
product: ['logs']
os: ['windows']
filters: ['Operating Systems', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/windows.svg
logs_dashboards: ['7xaHadrh2fJ8dJ5liH4g2S']
logs_alerts: ['72Yry8pK5OfiGdPOV2y9RZ', '4Mkw0OICZz7xnZZjlGWX9x']
logs2metrics: []
metrics_dashboards: ['7vydxtpnlKLILHIGK4puX5']
metrics_alerts: ['4GVNTAqeH4lSRQBfN7dCXQ']
drop_filter: []
---

 
## Send Windows logs and metrics with OpenTelemetry

:::note
For a simpler and more efficient way to collect and send metrics, use the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).
:::


**1. Create a Logz.io directory:**

```shell
New-Item -Path $env:APPDATA\LogzioAgent -ItemType Directory -Force
```

**2. Download OpenTelemetry tar.gz:**

```shell
Invoke-WebRequest -Uri "https://github.com/logzio/otel-collector-distro/releases/download/v0.95.0/otelcol-logzio-windows_amd64.zip" -OutFile C:\Users\<<USERNAME>>\Downloads\otelcol-logzio.zip
```
 
**3. Extract the OpenTelemetry binary:**

```shell
Expand-Archive -LiteralPath C:\Users\<<USERNAME>>\Downloads\otelcol-logzio.zip -DestinationPath $env:APPDATA\LogzioAgent -Force
```
 

**4. Create the OpenTelemetry config file:**

```shell
New-Item -Path $env:APPDATA\LogzioAgent\otel_config.yaml -ItemType File -Force
```
 
**5. Copy the following into the config file:**

Replace `<<LOG-SHIPPING-TOKEN>>`, `<<LISTENER-HOST>>`, and `<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>` with the relevant parameters from your Logz.io account.


 
```yaml
receivers:
  windowseventlog/application/localhost_windows_system:
    channel: Application
    exclude_providers:
      - LogzioOTELCollector
    attributes:
      type: agent-windows
  windowseventlog/security/localhost_windows_system:
    channel: Security
    attributes:
      type: agent-windows
  windowseventlog/system/localhost_windows_system:
    channel: System
    attributes:
      type: agent-windows
  hostmetrics/localhost_windows_system:
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
  logging:
  logzio/logs:
    account_token: <<LOG-SHIPPING-TOKEN>>
    region: <<LOGZIO_ACCOUNT_REGION_CODE>> # Default is US
    headers:
      user-agent: logzio-windows-logs
  prometheusremotewrite:
    endpoint: https://<<LISTENER-HOST>>:8053
    headers:
      Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
      user-agent: logzio-windows-metrics
    resource_to_telemetry_conversion:
      enabled: true
    target_info:
        enabled: false
service:
  pipelines:
    logs:
      receivers:
        - windowseventlog/application/localhost_windows_system
        - windowseventlog/security/localhost_windows_system
        - windowseventlog/system/localhost_windows_system
      processors:
        - resourcedetection/system
      exporters: [logzio/logs]
    metrics:
      receivers:
        - hostmetrics/localhost_windows_system
      processors:
        - resourcedetection/system
        - filter
      exporters: [prometheusremotewrite]
  telemetry:
    logs:
      level: "debug"
    metrics:
      address: localhost:8888
```

 
:::caution Important
If OpenTelemetry metrics are already running on port 8888, edit the `address` field in the config file.
:::
 

**6. Create the service file:**

```shell
New-Service -Name LogzioOTELCollector -BinaryPathName "$env:APPDATA\LogzioAgent\otelcol-logzio-windows_amd64.exe --config $env:APPDATA\LogzioAgent\otel_config.yaml" -Description "Collects localhost logs/metrics and sends them to Logz.io."
```

## Manage your OpenTelemetry on Localhost

Manage OpenTelemetry on your machine using the following commands:

|Description|Command|
|--|--|
|Start service|`Start-Service -Name LogzioOTELCollector`|
|Stop service|`Stop-Service -Name LogzioOTELCollector`|
|Service logs|`eventvwr.msc`|
|Delete service|`Stop-Service -Name LogzioOTELCollector` `sc.exe DELETE LogzioOTELCollector`|

