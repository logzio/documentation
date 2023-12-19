---
id: Sysmon-data
title: Sysmon (System Monitor) via Winlogbeat
overview: Sysmon (System Monitor) is a Windows system service that monitors and logs system activity of the Windows event log. It tracks process creations, network connections, and changes to file creation time.
product: ['logs']
os: ['windows']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/windows.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Sysmon (System Monitor) is a Windows system service that monitors and logs system activity of the Windows event log. It tracks process creations, network connections, and changes to file creation time.


**Before you begin, you'll need**:

* [Winlogbeat 7](https://www.elastic.co/downloads/past-releases/winlogbeat-7-0-0) installed.

* [Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon) installed and configured according to the [SwiftOnSecurity configuration](https://github.com/SwiftOnSecurity/sysmon-config).

 

### Download the Logz.io public certificate

Download the
[Logz.io public certificate]({@include: ../../_include/log-shipping/certificate-path.md})
to `C:\ProgramData\Winlogbeat\COMODORSADomainValidationSecureServerCA.crt`
on your machine.

### Configure Windows applications as an input

If you're working with the default configuration file, clear the content and start with a fresh file. (The location may be `C:\ProgramData\Elastic\Beats\winlogbeat\winlogbeat.yml` or `C:\Program Files\Winlogbeat\winlogbeat.yml`, depending on where you installed it.)


Paste this code block:

```yaml
File Content:
winlogbeat.event_logs:
  - name: Microsoft-windows-sysmon/Operational
    ignore_older: 72h
fields:
  logzio_codec: json
  token: <<LOG-SHIPPING-TOKEN>>
  type: wineventlog
fields_under_root: true
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
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['C:\ProgramData\Winlogbeat\COMODORSADomainValidationSecureServerCA.crt']
```



{@include: ../../_include/general-shipping/replace-placeholders.html}


:::note
One last validation - make sure Logz.io is the only output and appears only once.
If the file has other outputs, remove them.
:::
 


### Restart Winlogbeat

Open PowerShell as an admin and run this command:

```powershell
Restart-Service winlogbeat
```

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-filebeat/).

 
