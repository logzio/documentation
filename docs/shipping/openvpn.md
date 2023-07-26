---
id: OpenVPN
title: OpenVPN
overview: OpenVPN  is a virtual private network system for secure point-to-point or site-to-site connections.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/openvpn.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---

[OpenVPN](https://openvpn.net) is a virtual private network system for secure point-to-point or site-to-site connections.

These instructions only apply to Linux and MacOS systems.


**Before you begin, you'll need**: 

* An active account with Logz.io
* OpenVPN Access Server installed
* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html) installed on the same machine as OpenVPN Access Server
* Root priveleges on your machines 

 
  

{@include: ../_include/log-shipping/certificate.md}


##### Configure Filebeat

{@include: ../_include/log-shipping/filebeat-input-extension.md}


Paste the following into the inputs section of the Filebeat configuration file:

   ```yaml
   filebeat.inputs:
   - type: filestream
     paths:
       - /var/log/openvpnas.log
       - /var/log/openvpnas.log.*
     fields:
       logzio_codec: json
       # Your Logz.io account token. You can find your token at
       #  https://app.logz.io/#/dashboard/settings/manage-accounts
       token: <<LOG-SHIPPING-TOKEN>>
       type: openvpn
     fields_under_root: true
     encoding: utf-8
     ignore_older: 3h
     multiline.type: pattern
     multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{4} \[\S+\]( {2,}| \})'
     multiline.negate: false
     multiline.match: after
   filebeat.registry.path: /var/lib/filebeat
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
   output.logstash:
     hosts: ["<<LISTENER-HOST>>:5015"]
     ssl:
       certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
   ```

If you're running Filebeat 7 to 8.1, paste the code block below instead:

   ```yaml
   filebeat.inputs:
   - type: log
     paths:
       - /var/log/openvpnas.log
       - /var/log/openvpnas.log.*
     fields:
       logzio_codec: json
       # Your Logz.io account token. You can find your token at
       #  https://app.logz.io/#/dashboard/settings/manage-accounts
       token: <<LOG-SHIPPING-TOKEN>>
       type: openvpn
     fields_under_root: true
     encoding: utf-8
     ignore_older: 3h
     multiline.type: pattern
     multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+[0-9]{4} \[\S+\]( {2,}| \})'
     multiline.negate: false
     multiline.match: after
   filebeat.registry.path: /var/lib/filebeat
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
   output.logstash:
     hosts: ["<<LISTENER-HOST>>:5015"]
     ssl:
       certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
   ```


  
   * Your Logz.io log shipping token directs the data securely to your Logz.io Log Management account. [Manage your tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/shared).
   * {@include: ../_include/log-shipping/listener-var.md}

##### Restart Filebeat to run it with the new configuration.
  
```shell
service filebeat restart
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for data of type `openvpn` to see the incoming OpenVPN logs.
  
If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

  
