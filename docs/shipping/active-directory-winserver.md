---
id: Active-Directory
title: Active Directory
sidebar_position: 1
overview: Active Directory is a directory service developed by Microsoft for Windows domain networks. This integration allows you to send Active Directory logs to your Logz.io SIEM account.
product: ['siem']
os: ['windows', 'linux']
filters: ['firewall']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/windows.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---
Active Directory is a directory service developed by Microsoft for Windows domain networks. This integration allows you to send Active Directory logs to your Logz.io SIEM account.

#### Configuration

**Before you begin, you'll need**:
[Winlogbeat 8](https://www.elastic.co/guide/en/beats/winlogbeat/8.7/winlogbeat-installation-configuration.html#installation), [Winlogbeat 7.0.0](https://www.elastic.co/downloads/past-releases/winlogbeat-7-0-0) or
[Winlogbeat 6](https://www.elastic.co/guide/en/beats/winlogbeat/6.8/winlogbeat-installation.html).


##### Download the Logz.io public certificate

Download the
[Logz.io public certificate]({@include: ../_include/log-shipping/certificate-path.md})
to `C:\ProgramData\Winlogbeat\COMODORSADomainValidationSecureServerCA.crt`
on your machine.

##### Configure Windows applications as an input

If you're working with the default configuration file,
(`C:\Program Files\Winlogbeat\winlogbeat.yml`)
clear the content and start with a fresh file.

Paste this code block.

{@include: ../_include/log-shipping/log-shipping-token.html}

```yaml
# ...
winlogbeat.event_logs:
  - name: Application
    ignore_older: 72h
  - name: Security
  - name: System

fields:
  logzio_codec: json

  # Your Logz.io account token. You can find your token at
  #  https://app.logz.io/#/dashboard/settings/manage-accounts
  token: <<LOG-SHIPPING-TOKEN>>
  type: wineventlog
fields_under_root: true
```

If you're running Winlogbeat 7 or 8, paste this code block.
Otherwise, you can leave it out.

```yaml
# ... For Winlogbeat 7 or 8 only ...
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

##### Set Logz.io as the output

If Logz.io isn't the output, set it now.

Winlogbeat can have one output only, so remove any other `output` entries.

{@include: ../_include/log-shipping/listener-var.html} 

```yaml
# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['C:\ProgramData\Winlogbeat\COMODORSADomainValidationSecureServerCA.crt']
```

##### Restart Winlogbeat

```powershell
Restart-Service winlogbeat
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).
