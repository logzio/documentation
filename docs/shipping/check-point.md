---
id: Check-Point
title: Check Point
overview: Check Point provides hardware and software products for IT security, including network security, endpoint security, cloud security, mobile security, data security and security management. This integration allows you to send Check Point logs to your Logz.io SIEM account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/check-point.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---
 

Check Point provides hardware and software products for IT security, including network security, endpoint security, cloud security, mobile security, data security and security management. This integration allows you to send Check Point logs to your Logz.io SIEM account.

  

#### Configuration on Linux

**Before you begin, you'll need**:

* [Check Point Log Exporter](https://support.checkpoint.com/results/sk/sk122323)
* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html) installed
* Root access

 

##### Configure Check Point Log Exporter

Configure your Check Point Log Exporter to send logs to your Filebeat server.

:::note
For complete details on configuring Log Exporter, see [Check Point Log Export](https://support.checkpoint.com/results/sk/sk122323) from Check Point.
{:.info-box.read}
 


###### Option 1: Export logs for all domains

```shell
cp_log_export add name logzio_filebeat_exporter \
target-server <<FILEBEAT-IP-ADDRESS>> \
target-port 514 \
protocol udp \
format syslog \
--apply-now
```

###### Option 2: Export logs for a specific domain

```shell
cp_log_export add name logzio_filebeat_exporter \
domain-server <<YOUR-DOMAIN>> \
target-server <<FILEBEAT-IP-ADDRESS>> \
target-port 514 \
protocol udp \
format syslog \
--apply-now
```

:::note
If you restart the management server, you'll need to run `cp_log_export` again
to restart the exporter.
:::
 

{@include: ../_include/log-shipping/certificate.md}

##### Add UDP traffic as an input

In the Filebeat configuration file (/etc/filebeat/filebeat.yml), add UDP to the filebeat.inputs section.

{@include: ../_include/log-shipping/log-shipping-token.html}

{@include: ../_include/log-shipping/filebeat-input-extension.md}


```yaml
# ...
filebeat.inputs:
- type: udp
  max_message_size: 10MiB
  host: "0.0.0.0:514"

  fields:
    logzio_codec: plain

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    type: checkpoint
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
```

If you're running Filebeat 7, paste this code block.
Otherwise, you can leave it out.

```yaml
# ... For Filebeat 7 only ...
filebeat.registry.path: /var/lib/filebeat
processors:
- rename:
    fields:
    - from: "agent"
      to: "filebeat_agent"
    ignore_missing: true
- rename:
    fields:
    - from: "log.file.path"
      to: "source"
    ignore_missing: true
```

If you're running Filebeat 6, paste this code block.

```yaml
# ... For Filebeat 6 only ...
registry_file: /var/lib/filebeat/registry
```

##### Set Logz.io as the output

If Logz.io is not an output, add it now.
Remove all other outputs.

{@include: ../_include/log-shipping/listener-var.html} 

```yaml
# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

##### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).


 

  

#### Configuration on Windows

**Before you begin, you'll need**: 

* [Check Point Log Exporter](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk122323)
{@include: ../_include//log-shipping/filebeat-installed-port5015-begin.md} installed as a Windows service{@include: ../_include//log-shipping/filebeat-installed-port5015-end.md}




 

##### Configure Check Point Log Exporter

Configure your Check Point Log Exporter to send logs to your Filebeat server.

:::note
For complete details on configuring Log Exporter, see [Check Point Log Export](https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk122323) from Check Point.
{:.info-box.read}
 


###### Option 1: Export logs for all domains

```shell
cp_log_export add name logzio_filebeat_exporter \
target-server <<FILEBEAT-IP-ADDRESS>> \
target-port 514 \
protocol udp \
format syslog \
--apply-now
```

###### Option 2: Export logs for a specific domain

```shell
cp_log_export add name logzio_filebeat_exporter \
domain-server <<YOUR-DOMAIN>> \
target-server <<FILEBEAT-IP-ADDRESS>> \
target-port 514 \
protocol udp \
format syslog \
--apply-now
```

:::note
If you restart the management server, you'll need to run `cp_log_export` again
to restart the exporter.
:::
 

{@include: ../_include/log-shipping/certificate.md}


##### Download the Logz.io public certificate

For HTTPS shipping, download the Logz.io public certificate to your certificate authority folder.

Download the
[Logz.io public certificate]({@include: ../_include/log-shipping/certificate-path.md})
to `C:\ProgramData\Filebeat\Logzio.crt`
on your machine.


##### Configure Filebeat using the dedicated Logz.io configuration wizard

{@include: ../_include/log-shipping/filebeat-input-extension.md}


{@include: ../_include/log-shipping/filebeat-wizard.html}


<!-- logzio-inject:filebeat-wizard:os-windows -->


{@include: ../_include/log-shipping/filebeat-wizard.md}


{@include: ../_include/log-shipping/validate-yaml.md}

##### Move the configuration file to the Filebeat folder

Move the configuration file to `C:\Program Files\Filebeat\filebeat.yml`.


##### Add UDP traffic as an input

In the Filebeat configuration file (/etc/filebeat/filebeat.yml), add UDP to the filebeat.inputs section.

{@include: ../_include/log-shipping/log-shipping-token.html}

{@include: ../_include/log-shipping/filebeat-input-extension.md}


```yaml
# ...
filebeat.inputs:
- type: udp
  max_message_size: 10MiB
  host: "0.0.0.0:514"

  fields:
    logzio_codec: plain

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    type: checkpoint
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
```

If you're running Filebeat 7, paste this code block.
Otherwise, you can leave it out.

```yaml
# ... For Filebeat 7 only ...
filebeat.registry.path: C:\ProgramData\filebeat\registry
processors:
- rename:
    fields:
    - from: "agent"
      to: "filebeat_agent"
    ignore_missing: true
- rename:
    fields:
    - from: "log.file.path"
      to: "source"
    ignore_missing: true
```

If you're running Filebeat 6, paste this code block.

```yaml
# ... For Filebeat 6 only ...
registry_file: C:\ProgramData\filebeat\registry
```

##### Set Logz.io as the output

If Logz.io is not an output, add it now.
Remove all other outputs.

{@include: ../_include/log-shipping/listener-var.html} 

```yaml
# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['C:\ProgramData\Filebeat\Logzio.crt']
```

##### Restart Filebeat

```powershell
PS C:\Program Files\Filebeat> Restart-Service filebeat
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat's troubleshooting guide](/user-guide/log-troubleshooting/filebeat-troubleshooting.html).

 
 