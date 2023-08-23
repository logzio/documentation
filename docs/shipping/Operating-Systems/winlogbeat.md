---
id: Winlogbeat
title: Windows Operating System
overview: Follow these steps to integrate and forward your Windows system's logs to the Logz.io platform.
product: ['logs']
os: ['windows']
filters: ['Other', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/windows.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
drop_filter: []
---

## Default configuration

**Before you begin, you'll need**:
[Winlogbeat 8](https://www.elastic.co/guide/en/beats/winlogbeat/8.7/winlogbeat-installation-configuration.html#installation), [Winlogbeat 7](https://www.elastic.co/guide/en/beats/winlogbeat/7.x/winlogbeat-installation-configuration.html#installation), or [Winlogbeat 6](https://www.elastic.co/guide/en/beats/winlogbeat/6.8/winlogbeat-installation.html).

 
## Manually configure OpenTelemetry on Localhost

:::note
For a much easier and more efficient way to collect and send metrics, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/send-your-data/agent/new).
:::

Create a Logz.io directory: 

```shell
sudo mkdir /opt/logzio-agent
```

Download OpenTelemetry tar.gz: 

```shell
curl -fsSL "https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.82.0/otelcol-contrib_0.82.0_linux_amd64.tar.gz" >./otelcol-contrib.tar.gz
```
 
Extract the OpenTelemetry binary:

```shell
sudo tar -zxf ./otelcol-contrib.tar.gz --directory /opt/logzio-agent otelcol-contrib
```
 

Create the OpenTelemetry config file:

```shell
sudo touch /opt/logzio-agent/otel_config.yaml
```
 
And copy the following OpenTelemetry content into the config file. 

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
  logging:
  logzio/logs:
    account_token: <<LOG-SHIPPING-TOKEN>>
    region: us
  prometheusremotewrite:
    endpoint: https:<<LISTENER-HOST>>:8053
    headers:
      Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
    resource_to_telemetry_conversion:
      enabled: true
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

 
:::caution Important
If you already running OpenTelemetry metrics on port 8888, you will need to edit the `address` field in the config file.
:::
 

Next, create the service file:

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

### Manage your OpenTelemetry on Localhost

|Description|Command|
|--|--|
|Start service|`sudo systemctl start logzioOTELCollector`|
|Stop service|`sudo systemctl stop logzioOTELCollector`|
|Service logs|`sudo systemctl status -l logzioOTELCollector`|
|Delete service|`sudo systemctl stop logzioOTELCollector` `sudo systemctl reset-failed logzioOTELCollector 2>/dev/null` `sudo rm /etc/systemd/system/logzioOTELCollector.service 2>/dev/null` `sudo rm /usr/lib/systemd/system/logzioOTELCollector.service 2>/dev/null` `sudo rm /etc/init.d/logzioOTELCollector 2>/dev/null`|


## Send your logs through Winlogbeat
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

 
