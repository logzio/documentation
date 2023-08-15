---
id: Axonius
title: Axonius
overview: This integration sends system logs from your Axonius platform to Logz.io. 
product: ['logs', 'siem']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/axonius.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

[Axonius](https://www.axonius.com/) is a cybersecurity asset management platform. This topic describes how to send system logs from your Axonius platform to Logz.io. 

**Before you begin, you'll need**:

* An active account with Axonius
* An active account with Logz.io
* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html) installed on your machine
* Root priveleges on your machines 

 


### Configure Axonius to send syslog notifications to a remote Syslog server running Filebeat

1. On your Axonius web interface, go to **System Settings > Global Settings > Syslog Settings**.
![Axonius](https://dytvr9ot2sszz.cloudfront.net/logz-docs/axonius/axonius514.png)
2. Select **Use Syslog**.
3. Enter the IP address of your remote syslog server into the **Syslog host** field. This is the server where you run Filebeat.
4. Enter the port number into the **Port** field.
5. Select **UDP** in the **Protocol** menu.

  
:::note
By default, syslog will be forwarded over port 514. Feel free to adjust this, based on your preference or availability, but be sure to note any change to this port in the Filebeat configuration.
:::
 

{@include: ../_include/log-shipping/certificate.md}


### Configure Filebeat

1. Paste the following into the inputs section of the Filebeat configuration file:

{@include: ../_include/log-shipping/filebeat-input-extension.md}


   ```yaml
   filebeat.inputs:
   - type: udp
     max_message_size: 10MiB
     host: "<<ADDRESS-OF-YOUR-FILEBEAT-SERVER>>:514"
     fields:
       logzio_codec: plain
       # Your Logz.io account token. You can find your token at
       #  https://app.logz.io/#/dashboard/settings/manage-accounts
       token: <<LOG-SHIPPING-TOKEN>>
       type: axonius
     fields_under_root: true
     encoding: utf-8
     ignore_older: 3h
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
   output.logstash:
     hosts: ["<<LISTENER-HOST>>:5015"]
     ssl:
       certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
   ```
  
   * Replace `<<ADDRESS-OF-YOUR-FILEBEAT-SERVER>>` with the address of your server running Filebeat.
   * {@include: ../_include/log-shipping/log-shipping-token.md}
   * {@include: ../_include/log-shipping/listener-var.md}

2. Run Filebeat with the new configuration.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for data of type `axonius` to see the incoming Axonius logs.
  
If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).


 
