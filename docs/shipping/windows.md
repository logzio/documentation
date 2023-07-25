---
id: Winlogbeat
title: Winlogbeat
overview: Winlogbeat metrics.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
---



#### Configure Winlogbeat

**Before you begin, you'll need**:
[Winlogbeat 8](https://www.elastic.co/guide/en/beats/winlogbeat/8.7/winlogbeat-installation-configuration.html#installation), [Winlogbeat 7](https://www.elastic.co/guide/en/beats/winlogbeat/7.x/winlogbeat-installation-configuration.html#installation), or [Winlogbeat 6](https://www.elastic.co/guide/en/beats/winlogbeat/6.8/winlogbeat-installation.html).

 

##### Download the Logz.io public certificate

Download the
[Logz.io public certificate]({@include: ../_include/log-shipping/certificate-path.md})
to `C:\ProgramData\Winlogbeat\COMODORSADomainValidationSecureServerCA.crt`
on your machine.

##### Configure Windows input

If you're working with the default configuration file,
(`C:\Program Files\Winlogbeat\winlogbeat.yml`)
clear the content and start with a fresh file.

Paste this code block.

{@include: ../_include/log-shipping/log-shipping-token.html}

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


##### Set Logz.io as the output

If Logz.io isn't the output, set it now.

Winlogbeat can have one output only, so remove any other `output` entries.

{@include: ../_include/log-shipping/listener-var.html} 

```yaml
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['C:\ProgramData\Winlogbeat\COMODORSADomainValidationSecureServerCA.crt']
```

##### Restart Winlogbeat

Open PowerShell as an admin and run this command:

```powershell
Restart-Service winlogbeat
```

:::note
If you're starting Winlogbeat, and haven't configured it as a service yet, refer to [Winlogbeat documentation](https://www.elastic.co/guide/en/beats/winlogbeat/current/configuring-howto-winlogbeat.html).
:::
 

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 


#### Configure NXLog

**Before you begin, you'll need**:
[NXLog](https://nxlog.co/products/nxlog-community-edition/download)

 

##### Configure NXLog basics

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
{:.info-box.read}
 

##### Add Windows as an input

Add an `Input` block to append your account token to log records.

{@include: ../_include/log-shipping/log-shipping-token.html}

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

##### Set Logz.io as the output

Add the Logz.io listener in the `Output` block.

{@include: ../_include/log-shipping/listener-var.html} 

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

##### Restart NXLog

Open PowerShell as an admin and run this command:

```powershell
Restart-Service nxlog
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

 
