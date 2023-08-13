---
id: Windows-Defender
title: Windows Defender
overview: This integration enable you to send Windows Defender events to Logz.io using winlogbeat
product: ['logs','siem']
os: ['windows']
filters: ['Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/windows-defender.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---

Windows Defender is an anti-malware component of Microsoft Windows. This integration allows you to send Windows Defender logs to your Logz.io SIEM account.

**Before you begin, you'll need**:
[Winlogbeat 8](https://www.elastic.co/guide/en/beats/winlogbeat/8.7/winlogbeat-installation-configuration.html#installation), [Winlogbeat 7](https://www.elastic.co/downloads/beats/winlogbeat) or
[Winlogbeat 6](https://www.elastic.co/guide/en/beats/winlogbeat/6.8/winlogbeat-installation.html).

 

### Configure Windows Defender audit permissions

In the Windows taskbar search box, type "gpedit"
and click **Edit group policy**.
You'll see the _Local Group Policy Editor_.

![Local Group Policy Editor](https://dytvr9ot2sszz.cloudfront.net/logz-docs/windows/local-group-policy-editor.png)

In the left pane, select **Windows Settings > Security Settings > Local Policies > Audit Policy**.
In the right pane, open **Audit object access**.

![Audit object access Properties](https://dytvr9ot2sszz.cloudfront.net/logz-docs/windows/audit-object-access-properties.png)

Select **Success** and **Failure**, and click **OK**.

Back in the Windows taskbar search box, type "regedit"
and click **Registry Editor**.

![Windows Registry Editor](https://dytvr9ot2sszz.cloudfront.net/logz-docs/windows/registry-editor-windows-defender-context-menu.png)

In the search bar at the top of the window, paste
"Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender".

In the left pane, right-click the _Windows Defender_ folder,
then click **Permissions...** to show _Permissions for Windows Defender_.
Click **Advanced** to show _Advanced Security Settings for Windows Defender_.

![Advanced Security Settings for Windows Defender](https://dytvr9ot2sszz.cloudfront.net/logz-docs/windows/advanced-security-settings-for-windows-defender.png)

In the _Auditing_ tab, click **Add** to show the _Auditing Entry for Windows Defender_ dialog.

Click **Select a principal** to show the _Select User or Group_ dialog.

![Select User or Group](https://dytvr9ot2sszz.cloudfront.net/logz-docs/windows/select-user-or-group.png)

Type "Administrators" in the text box and click **Check Names**.

Now click **OK** to exit all those dialogs you just opened. 😬

### Download the Logz.io public certificate

Download the
[Logz.io public certificate]({@include: ../_include/log-shipping/certificate-path.md})
to `C:\ProgramData\Winlogbeat\COMODORSADomainValidationSecureServerCA.crt`
on your machine.

### Configure Windows input

If you're working with the default configuration file,
(`C:\Program Files\Winlogbeat\winlogbeat.yml`)
clear the content and start with a fresh file.

Paste this code block.

{@include: ../_include/log-shipping/log-shipping-token.html}

```yaml
winlogbeat.event_logs:
  - name: Application
    ignore_older: 72h
  - name: System
  - name: Microsoft-Windows-Sysmon/Operational
  - name: Microsoft-Windows-Windows Defender/Operational
  - name: Microsoft-Windows-Windows Firewall With Advanced Security/Firewall

fields:
  logzio_codec: json
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

### Add Logz.io as an output

If Logz.io isn't the output, set it now.

Winlogbeat can have one output only, so remove any other `output` entries.

{@include: ../_include/log-shipping/listener-var.html} 

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

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

 
