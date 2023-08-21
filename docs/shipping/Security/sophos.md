---
id: Sophos-security
title: Sophos
overview: Sophos Endpoint is an endpoint protection product that combines antimalware, web and application control, device control and much more. This integration allows you to send logs from your Linux-based Sophos applications to your Logz.io SIEM account.
product: ['logs', 'siem']
os: ['windows', 'linux']
filters: ['Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/sophos-shield.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Sophos Endpoint is an endpoint protection product that combines antimalware, web and application control, device control and much more. This integration allows you to send logs from your Linux-based Sophos applications to your Logz.io SIEM account.

**Before you begin, you'll need**:

* Sophos Intercept X Endpoint installed
* Access to the [Sophos Central Cloud console](https://central.sophos.com/)
* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html)
* Terminal access to the instance running Filebeat. It is recommended to run the Sophos API script from the same instance running your Filebeat.



 

##### Configure Sophos to collect the Central Cloud logs

Follow the official instructions provided by Sophos for [collecting Sophos Central Cloud logs from all machines](https://support.sophos.com/support/s/article/KB-000036372?language=en_US).

The procedure involves using the Sophos API. Make sure that the `config.ini` used in the Sophos siem.py script is under `format = json` (this is the default setting).

{@include: ../../_include/log-shipping/certificate.md}

##### Configure Filebeat

Open the Filebeat configuration file (`/etc/filebeat/filebeat.yml`) with your preferred text editor.

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


Copy and paste the code block below, overwriting the previous content, to replace the general configuration with the following settings:

```yaml
#... Filebeat
filebeat.inputs:
- type: filestream
  paths:
    - <<FILE_PATH>>
  fields:
    token: <<LOG-SHIPPING-TOKEN>>
  fields_under_root: true
  json.keys_under_root: true
  encoding: utf-8
  ignore_older: 3h

#... Output
output:
  logstash:
    hosts: ["<<LISTENER-HOST>>"]
    ssl:
      certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

If you're running Filebeat 7 to 8.1, paste the code block below instead:

```yaml
#... Filebeat
filebeat.inputs:
- type: log
  paths:
    - <<FILE_PATH>>
  fields:
    token: <<LOG-SHIPPING-TOKEN>>
  fields_under_root: true
  json.keys_under_root: true
  encoding: utf-8
  ignore_older: 3h

#For version 7 and higher
filebeat.registry.path: /var/lib/filebeat
#The following processors are to ensure compatibility with version 7
processors:
- rename:
    fields:
     - from: "type"
       to: "event_type"
    ignore_missing: true
- add_fields:
    target: ''
    fields:
      type: "sophos-ep"
- rename:
    fields:
     - from: "log.file.path"
       to: "source"
    ignore_missing: true
- drop_event:
    when:
      regexp:
        message: "^\\s*$"
#... Output
output:
  logstash:
    hosts: ["<<LISTENER-HOST>>"]
    ssl:
      certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```




{@include: ../../_include/log-shipping/listener-var.html} 

{@include: ../../_include/log-shipping/log-shipping-token.html}

Change `<<FILE_PATH>>` to the output TXT file retrieved from the Sophos siem.py script.


One last validation - make sure Logz.io is the only output and appears only once.
If the file has other outputs, remove them.

##### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can search or filter for Sophos logs, under `type:sophos-ep`.

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

##### Contact support to request custom parsing assistance

The logs will require customized parsing so they can be effectively mapped in Open Search Dashboards.

[Email our support](mailto:help@logz.io?subject=Requesting%20parsing%20assistance%20for%20Sophos%20security%20logs&body=Hi!%20Please%20be%20in%20touch%20with%20further%20instructions%20for%20parsing%20Sophos%20security%20logs.%20Thanks!) to request custom parsing assistance.


 

Sophos Endpoint is an endpoint protection product that combines antimalware, web and application control, device control and much more. This integration allows you to send logs from your Windows-based Sophos applications to your Logz.io SIEM account.

**Before you begin, you'll need**:

* Sophos Intercept X Endpoint installed
* Access to the [Sophos Central Cloud console](https://central.sophos.com/)
* [Filebeat 7 installed](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html)
* Terminal access to the instance running Filebeat. It is recommended to run the Sophos API script from the same instance running your Filebeat.



 

##### Configure Sophos to collect the Central Cloud logs

Follow the official instructions provided by Sophos for [collecting Sophos Central Cloud logs from all machines](https://support.sophos.com/support/s/article/KB-000036372?language=en_US).

The procedure involves using the Sophos API. Make sure that the `config.ini` used in the Sophos siem.py script is under `format = json` (this is the default setting).

##### Download the Logz.io public certificate

For HTTPS shipping, download the Logz.io public certificate to your certificate authority folder.

Download the
[Logz.io public certificate]({@include: ../../_include/log-shipping/certificate-path.md})
to `C:\ProgramData\Filebeat\Logzio.crt`
on your machine.


##### Configure Filebeat

Open the Filebeat configuration file (`C:\Program Files\Filebeat\filebeat.yml`) with your preferred text editor.

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


Copy and paste the code block below, overwriting the previous content, to replace the general configuration with the following settings:

```yaml
#... Filebeat
filebeat.inputs:
- type: log
  paths:
    - <<FILE_PATH>>
  fields:
    token: <<LOG-SHIPPING-TOKEN>>
  fields_under_root: true
  json.keys_under_root: true
  encoding: utf-8
  ignore_older: 3h

#For version 7 and higher
filebeat.registry.path: 'C:\ProgramData\Filebeat'
#The following processors are to ensure compatibility with version 7
processors:
- rename:
    fields:
     - from: "type"
       to: "event_type"
    ignore_missing: true
- add_fields:
    target: ''
    fields:
      type: "sophos-ep"
- rename:
    fields:
     - from: "log.file.path"
       to: "source"
    ignore_missing: true
- drop_event:
    when:
      regexp:
        message: "^\\s*$"
#... Output
output:
  logstash:
    hosts: ["<<LISTENER-HOST>>"]
    ssl:
      certificate_authorities: ['C:\ProgramData\Filebeat\COMODORSADomainValidationSecureServerCA.crt']
```

{@include: ../../_include/log-shipping/listener-var.html} 

{@include: ../../_include/log-shipping/log-shipping-token.html}

Change `<<FILE_PATH>>` to the output TXT file retrieved from the Sophos siem.py script.


One last validation - make sure Logz.io is the only output and appears only once.
If the file has other outputs, remove them.

##### Start Filebeat

Start or restart Filebeat for the changes to take effect.


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can search or filter for Sophos logs, under `type:sophos-ep`.

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

##### Contact support to request custom parsing assistance

The logs will require customized parsing so they can be effectively mapped in Open Search Dashboards.

[Email our support](mailto:help@logz.io?subject=Requesting%20parsing%20assistance%20for%20Sophos%20security%20logs&body=Hi!%20Please%20be%20in%20touch%20with%20further%20instructions%20for%20parsing%20Sophos%20security%20logs.%20Thanks!) to request custom parsing assistance.

