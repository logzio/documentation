---
id: BUNNY-NET-data
title: BUNNY.NET
overview: BUNNY.NET is a content delivery network offering features and performance with a fast global network. This document describes how to send system logs from your bunny.net pull zones to Logz.io.
product: ['logs']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/bunny.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


[BUNNY.NET](https://bunny.net/) is a content delivery network offering features and performance with a fast global network. This document describes how to send system logs from your bunny.net pull zones to Logz.io. 

**Before you begin, you'll need**:

* An active account with bunny.net
* An active account with Logz.io
* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html) installed on your machine
* Root priveleges on your machines

 


### Configure bunny.net to send syslog notifications to a remote Syslog server running Filebeat

1. Log in to your bunny.net account and navigate to the details page of the Pull Zone that you need to select logs from.
2. On the left side panel, select **Security > Logging**.
3. Make sure the switches for **Enable logging** and **Enable log forwarding** are on.
3. In the **Syslog Endpoint** section, enter the IP address of your remote syslog server into the **Hostname** field. This is the server where you run Filebeat.
4. Enter the port number into the **Port** field.
5. Select **UDP** from the **Log Server Protocol** menu.
6. Select **Plain text** from the **Log Format** menu.
7. Select **Save Forwarding Configuration**.
![Bunny](https://dytvr9ot2sszz.cloudfront.net/logz-docs/bunny-net/bunny-ui.png)
  
:::note
By default, syslog will be forwarded over port 6514. Feel free to adjust this, based on your preference or availability, but be sure to note any change to this port in the Filebeat configuration.
:::
 

### Install the bunny.net certificate on your Filebeat server

Bunny.net sends encrypted data,
so you'll need to create a dedicated bunny.net certificate to decrypt the logs by the Filebeat server.

```shell
sudo mkdir /etc/filebeat/certificates
sudo openssl req -newkey rsa:2048 -nodes \
-keyout /etc/filebeat/certificates/BunnyNet.key -x509 \
-days 365 \
-out /etc/filebeat/certificates/BunnyNet.crt
```

{@include: ../../_include/log-shipping/certificate.md}


### Configure Filebeat

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


1. Paste the following into the inputs section of the Filebeat configuration file:

   ```yaml  
   filebeat.inputs:
   - type: udp
     max_message_size: 10MiB
     host: "<<ADDRESS-OF-YOUR-FILEBEAT-SERVER>>:6514"
     ssl.enabled: true
     ssl.certificate: "/etc/filebeat/certificates/BunnyNet.crt"
     ssl.key: "/etc/filebeat/certificates/BunnyNet.key"
        ssl.verification_mode: none

     fields:
       logzio_codec: json

       # Your Logz.io account token. You can find your token at
       #  https://app.logz.io/#/dashboard/settings/manage-accounts
       token: <<LOG-SHIPPING-TOKEN>>
       type: bunny-net
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
   * {@include: ../../_include/log-shipping/log-shipping-token.md}
   * {@include: ../../_include/log-shipping/listener-var.md}

2. Run Filebeat with the new configuration.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for data of type `bunny-net` to see the incoming Axonius logs.
  
If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-filebeat/).


 
