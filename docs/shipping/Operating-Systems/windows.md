---
id: localhost-windows
title: Windows Operating System
overview: Send your Windows machine logs and metrics to Logz.io to monitor and manage your Windows data, allowing you to identify anomalies, investigate incidents, get to the root cause of any issue, and quickly resolve it.
product: ['logs','metrics']
os: ['windows']
filters: ['Compute']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/mac-os.svg
logs_dashboards: []
logs_alerts: ['72Yry8pK5OfiGdPOV2y9RZ','4Mkw0OICZz7xnZZjlGWX9x']
logs2metrics: []
metrics_dashboards: ['7vydxtpnlKLILHIGK4puX5']
metrics_alerts: ['4GVNTAqeH4lSRQBfN7dCXQ']
drop_filter: []
---


## Send your Windows machine logs and metrics using Opentelemetry service

:::note
For a much easier and more efficient way to collect and send logs and metrics from your Windows, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/send-your-data/agent/new).
:::

Follow these steps to manually configure OpenTelemetry on your Windows machine

Create a Logz.io directory:
```shell
New-Item -Path $env:APPDATA\LogzioAgent -ItemType Directory -Force
```

Download OTEL tar.gz:
```shell 
Invoke-WebRequest -Uri "https://github.com/logzio/otel-collector-distro/releases/download/v0.82.0/otelcol-logzio-windows_amd64.zip" -OutFile C:\Users\<<USERNAME>>\Downloads\otelcol-logzio.zip
```

Extract OTEL binary:
```shell 
Expand-Archive -LiteralPath C:\Users\<<USERNAME>>\Downloads\otelcol-logzio.zip -DestinationPath $env:APPDATA\LogzioAgent -Force
```

Create OTEL config:
```shell 
New-Item -Path $env:APPDATA\LogzioAgent\otel_config.yaml -ItemType File -Force
```

Copy OTEL config content to the config: ( replace `<<LOGS_TOKEN>>`,  `<<LISTENER>>`, `<<metrics_token>>`)

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
    account_token: <<LOGS_TOKEN>>
    region: us
  prometheusremotewrite:
    endpoint: https://<<LISTENER>>:8053
    headers:
      Authorization: Bearer <<METRICS_TOKEN>>
    resource_to_telemetry_conversion:
      enabled: true
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
If you already running OpenTelemetry metrics on port 8888, you will need to edit the `address` field in the config file.
:::

Create service:
```shell
New-Service -Name LogzioOTELCollector -BinaryPathName "$env:APPDATA\LogzioAgent\otelcol-logzio-windows_amd64.exe --config $env:APPDATA\LogzioAgent\otel_config.yaml" -Description "Collects localhost logs/metrics and sends them to Logz.io."
```

Start service:
```shell
Start-Service -Name LogzioOTELCollector
```

Stop Service:
```shell
Stop-Service -Name LogzioOTELCollector
```

Service logs:
```shell
eventvwr.msc
('Windows Logs'->'Application' all logs with source 'LogzioOTELCollector')
```

Delete Service:
```shell
Stop-Service -Name LogzioOTELCollector
sc.exe DELETE LogzioOTELCollector
```

