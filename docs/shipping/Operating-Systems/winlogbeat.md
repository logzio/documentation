---
id: Windows
title: Windows Operating System
overview: Follow these steps to integrate and forward your Windows system's logs to the Logz.io platform.
product: ['logs']
os: ['windows']
filters: ['Other', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/windows.svg
logs_dashboards: []
logs_alerts: ['72Yry8pK5OfiGdPOV2y9RZ', '4Mkw0OICZz7xnZZjlGWX9x']
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1','7vydxtpnlKLILHIGK4puX5']
metrics_alerts: ['4GVNTAqeH4lSRQBfN7dCXQ']
drop_filter: []
---

 
## Send your Windows machine logs and metrics using OpenTelemetry service

:::note
For a much easier and more efficient way to collect and send metrics, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/send-your-data/agent/new).
:::

Create a Logz.io directory: 

```shell
New-Item -Path $env:APPDATA\LogzioAgent -ItemType Directory -Force
```

Download OpenTelemetry tar.gz: 

```shell
Invoke-WebRequest -Uri "https://github.com/logzio/otel-collector-distro/releases/download/v0.82.0/otelcol-logzio-windows_amd64.zip" -OutFile C:\Users\<<USERNAME>>\Downloads\otelcol-logzio.zip
```
 
Extract the OpenTelemetry binary:

```shell
Expand-Archive -LiteralPath C:\Users\<<USERNAME>>\Downloads\otelcol-logzio.zip -DestinationPath $env:APPDATA\LogzioAgent -Force
```
 

Create the OpenTelemetry config file:

```shell
New-Item -Path $env:APPDATA\LogzioAgent\otel_config.yaml -ItemType File -Force
```
 
And copy the following OpenTelemetry content into the config file. 

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
    region: us
  prometheusremotewrite:
    endpoint: https://<<LISTENER-HOST>>:8053
    headers:
      Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
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
 

Next, create the service file:

```shell
New-Service -Name LogzioOTELCollector -BinaryPathName "$env:APPDATA\LogzioAgent\otelcol-logzio-windows_amd64.exe --config $env:APPDATA\LogzioAgent\otel_config.yaml" -Description "Collects localhost logs/metrics and sends them to Logz.io."
```

### Manage your OpenTelemetry on Localhost

|Description|Command|
|--|--|
|Start service|`Start-Service -Name LogzioOTELCollector`|
|Stop service|`Stop-Service -Name LogzioOTELCollector`|
|Service logs|`eventvwr.msc`|
|Delete service|`Stop-Service -Name LogzioOTELCollector` `sc.exe DELETE LogzioOTELCollector`|


## Send your logs and metrics using Winlogbeat


**Before you begin, you'll need**:
[Winlogbeat 8](https://www.elastic.co/guide/en/beats/winlogbeat/8.7/winlogbeat-installation-configuration.html#installation), [Winlogbeat 7](https://www.elastic.co/guide/en/beats/winlogbeat/7.x/winlogbeat-installation-configuration.html#installation), or [Winlogbeat 6](https://www.elastic.co/guide/en/beats/winlogbeat/6.8/winlogbeat-installation.html).

### Download the Logz.io public certificate

Download the
[Logz.io public certificate]({@include: ../../_include/log-shipping/certificate-path.md})
to `C:\ProgramData\Winlogbeat\COMODORSADomainValidationSecureServerCA.crt`
on your machine.

### Configure Windows input

If you're working with the default configuration file,
(`C:\Program Files\Winlogbeat\winlogbeat.yml`)
clear the content and start with a fresh file.

Paste this code block.

{@include: ../../_include/log-shipping/log-shipping-token.html}

```yaml
winlogbeat.event_logs:
  - name: Application
    ignore_older: 72h
  - name: Security
  - name: System

fields:
  logzio_codec: json
  token: <<LOG-SHIPPING-TOKEN>>
  type: wineventlog
fields_under_root: true
```

If you're running Winlogbeat 7 or 8, paste this code block.
Otherwise, you can leave it out.

```yaml
# ... For Winlogbeat 7 and 8 only ...
processors:
  - rename:
      fields:
      - from: "agent"
        to: "beat_agent"
      ignore_missing: true
  - rename:
      fields:
      - from: "log.file.path"
        to: "source"
      ignore_missing: true
  - rename:
      fields:
      - from: "log"
        to: "log_information"
      ignore_missing: true
```


### Set Logz.io as the output

If Logz.io isn't the output, set it now.

Winlogbeat can have one output only, so remove any other `output` entries.

{@include: ../../_include/log-shipping/listener-var.html} 

```yaml
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['C:\ProgramData\Winlogbeat\COMODORSADomainValidationSecureServerCA.crt']
```

### Restart Winlogbeat

Open PowerShell as an admin and run this command:

```powershell
Restart-Service winlogbeat
```

:::note
If you're starting Winlogbeat, and haven't configured it as a service yet, refer to [Winlogbeat documentation](https://www.elastic.co/guide/en/beats/winlogbeat/current/configuring-howto-winlogbeat.html).
:::
 

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 


## Configure NXLog

**Before you begin, you'll need**:
[NXLog](https://nxlog.co/products/nxlog-community-edition/download)

 

### Configure NXLog basics

Copy this code into your configuration file (`C:\Program Files (x86)\nxlog\conf\nxlog.conf` by default).

```conf
define ROOT C:\\Program Files (x86)\\nxlog
define ROOT_STRING C:\\Program Files (x86)\\nxlog
define CERTDIR %ROOT%\\cert
Moduledir %ROOT%\\modules
CacheDir %ROOT%\\data
Pidfile %ROOT%\\data\\nxlog.pid
SpoolDir %ROOT%\\data
LogFile %ROOT%\\data\\nxlog.log
<Extension charconv>
    Module xm_charconv
    AutodetectCharsets utf-8, euc-jp, utf-16, utf-32, iso8859-2
</Extension>
```

:::note
For information on parsing multi-line messages, see [this](https://nxlog.co/documentation/nxlog-user-guide/parsing-multiline.html#parsing-multiline) from NXLog.
:::
 

### Add Windows as an input

Add an `Input` block to append your account token to log records.

{@include: ../../_include/log-shipping/log-shipping-token.html}

```conf
<Input eventlog>

# For Windows Vista/2008 and later, set Module to `im_msvistalog`. For
#  Windows XP/2000/2003, set to `im_mseventlog`.
    Module im_msvistalog

    Exec if $raw_event =~ /^#/ drop();
    Exec convert_fields("AUTO", "utf-8");
    Exec    $raw_event = '[<<LOG-SHIPPING-TOKEN>>][type=wineventlog]' + $raw_event;
</Input>
```

### Set Logz.io as the output

Add the Logz.io listener in the `Output` block.

{@include: ../../_include/log-shipping/listener-var.html} 

```conf
<Output out>
    Module  om_tcp
    Host    <<LISTENER-HOST>>
    Port    8010
</Output>
<Route 1>
    Path eventlog => out
</Route>
```

### Restart NXLog

Open PowerShell as an admin and run this command:

```powershell
Restart-Service nxlog
```

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

 
