---
id: Beats
title: Beats
overview: This document describes the way to get logs from your system to Logz.io using any of the Beats shippers.
product: ['logs']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/beats.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


## MacOS or Linux

This document describes the way to get logs from your system to Logz.io using any of the Beats shippers.

### Configure your Beats shipper on macOS or Linux

**Before you begin, you'll need**:

* Any Beats shipper installed on your machine. This includes [Filebeat](https://docs.logz.io/shipping/log-sources/filebeat.html), Auditbeat, Functionbeat, Heartbeat, Journalbeat or Packetbeat. Logz.io recommends that you use the latest stable version.
* Destination port 5015 open to outgoing traffic.


 

{@include: ../../_include/log-shipping/certificate.md}

### Configure your Beats shipper using the configuration file.

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


1. Open the configuration file for your Beats shipper.
2. Add the following to the inputs section:

   ```yml
     fields:
       logzio_codec: <plain> or <json>
       token: <<LOG-SHIPPING-TOKEN>>
       type: <LOGTYPE>
     fields_under_root: true
     encoding: utf-8
     ignore_older: 3h
   ```

3. Specify the log file format in the `logzio_codec` field. It can be `plain` or `json`.
4. Specify your Logz.io log shipping token in the `token` field. You can see the token by navigating to your Logz.io account and selecting **Settings > Manage tokens > Data shipping tokens**.
5. Select the log type from the list or select **Other** and give it a name of your choice to specify a custom log type.
   * If you select a log type from the list, the logs will be automatically parsed and analyzed. [List of types available for parsing by default](https://docs.logz.io/user-guide/log-shipping/built-in-log-types.html).
   * If you select **Other**, contact support to request custom parsing assistance. Don’t be shy, it’s included in your plan!
6. Add the following to the outputs section:

   ```yml
   output:
     logstash:
       hosts: ["<<LISTENER-HOST>>:5015"]  
       ssl:
         certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
   ```
7. {@include: ../../_include/log-shipping/listener-var.html}
8. Save the changes.

### Validate the configuration file

It's a good idea to run the configuration file through a YAML validator to rule out indentation errors, clean up extra characters, and check if your YAML file is valid. [Yamllint.com](http://www.yamllint.com) is a great choice.

### Start your Beats shipper

Start or restart your Beats shipper for the changes to take effect.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

## Windows

This document describes the way to get logs from your system to Logz.io using any of the Beats shippers.

### Configure your Beats shipper on Windows

**Before you begin, you'll need**: 

* Any Beats shipper installed on your machine. This includes [Filebeat](https://docs.logz.io/shipping/log-sources/filebeat.html), Auditbeat, Functionbeat, Heartbeat, Journalbeat, Packetbeat or [Winlogbeat](https://docs.logz.io/shipping/log-sources/windows.html). Logz.io recommends that you use the latest stable version.
* Destination port 5015 open to outgoing traffic.

 

### Download the Logz.io public certificate

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


For HTTPS shipping, download the Logz.io public certificate to your certificate authority folder.

Download the
[Logz.io public certificate]({@include: ../../_include/log-shipping/certificate-path.md})
to `C:\ProgramData\<YOUR SHIPPER NAME>\Logzio.crt`
on your machine.


### Configure your Beats shipper using the dedicated Logz.io configuration wizard

{@include: ../../_include/log-shipping/filebeat-wizard.html}


### Configure your Beats shipper using the configuration file.

1. Open the configuration file for your Beats shipper.
2. Add the following to the inputs section:

   ```yml
     fields:
       logzio_codec: <plain> or <json>
       token: <<LOG-SHIPPING-TOKEN>>
       type: <LOGTYPE>
     fields_under_root: true
     encoding: utf-8
     ignore_older: 3h
   ```

3. Specify the log file format in the `logzio_codec` field. It can be `plain` or `json`.
4. Specify your Logz.io log shipping token in the `token` field. You can see the token by navigating to your Logz.io account and selecting **Settings > Manage tokens > Data shipping tokens**.
5. Select the log type from the list or select **Other** and give it a name of your choice to specify a custom log type.
   * If you select a log type from the list, the logs will be automatically parsed and analyzed. [List of types available for parsing by default](https://docs.logz.io/user-guide/log-shipping/built-in-log-types.html).
   * If you select **Other**, contact support to request custom parsing assistance. Don’t be shy, it’s included in your plan!
6. Add the following to the outputs section:

   ```yml
   output:
     logstash:
       hosts: ["<<LISTENER-HOST>>:5015"]  
       ssl:
         certificate_authorities: ['C:\ProgramData\<YOUR SHIPPER NAME>\Logzio.crt']
   ```


7. {@include: ../../_include/log-shipping/listener-var.html}
8. Save the changes.

### Validate the configuration file

It's a good idea to run the configuration file through a YAML validator to rule out indentation errors, clean up extra characters, and check if your YAML file is valid. [Yamllint.com](http://www.yamllint.com) is a great choice.


### Start your Beats shipper

Start or restart your Beats shipper for the changes to take effect.


### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 


 

Beat shippers make use of modules to ship data from various sources. Refer to the list below to see what modules each of the shippers support.

* [Auditbeat](https://www.elastic.co/guide/en/beats/auditbeat/master/auditbeat-modules.html)

* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-modules.html)

* [Winlogbeat](https://www.elastic.co/guide/en/beats/winlogbeat/current/winlogbeat-modules.html)


 