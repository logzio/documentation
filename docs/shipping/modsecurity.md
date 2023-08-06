---
id: ModSecurity
title: ModSecurity
overview: ModSecurity, sometimes called Modsec, is an open-source web application firewall. This integration allows you to send ModSecurity logs to your Logz.io SIEM account.
product: ['logs']
os: ['windows', 'linux']
filters: ['Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/modsec.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---

ModSecurity, sometimes called Modsec, is an open-source web application firewall. This integration allows you to send ModSecurity logs to your Logz.io SIEM account.


**Before you begin, you'll need**:

* Apache2 Web Server and Terminal access to the instance running it
* [ModSecurity module installed](https://github.com/SpiderLabs/ModSecurity) 
* [OWASP ModSecurity Core Rule Set (CRS) imported](https://github.com/SpiderLabs/owasp-modsecurity-crs)
* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html)

 

 {@include: ../_include/log-shipping/certificate.md}

### Configure Filebeat

Open the Filebeat configuration file (/etc/filebeat/filebeat.yml) with your preferred text editor. Copy and paste the code block below, overwriting the previous content. (You want to replace the file's content with this code block.)

{@include: ../_include/log-shipping/filebeat-input-extension.md}


```yml
### Filebeat ###
filebeat.inputs:

- type: filestream
  paths:
    - /var/log/apache2/error.log
  fields:
    logzio_codec: json
    token: <<LOG-SHIPPING-TOKEN>>
    type: modsecurity
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

### Output ###
output:
  logstash:
    hosts: ["<<LISTENER-HOST>>:5015"]
    ssl:
      certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

If you're running Filebeat 7 to 8.1, paste the code block below instead:


```yml
### Filebeat ###
filebeat.inputs:

- type: log
  paths:
    - /var/log/apache2/error.log
  fields:
    logzio_codec: json
    token: <<LOG-SHIPPING-TOKEN>>
    type: modsecurity
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

#For version 6.x and lower
#filebeat.registry_file: /var/lib/filebeat/registry

# For version 7 and higher
filebeat.registry.path: /var/lib/filebeat

# The following processors are to ensure compatibility with version 7
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

### Output ###
output:
  logstash:
    hosts: ["<<LISTENER-HOST>>:5015"]
    ssl:
      certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```


{@include: ../_include//general-shipping/replace-placeholders.html}


:::note
One last validation - make sure Logz.io is the only output and appears only once.
If the file has other outputs, remove them.
:::
 


### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

  
