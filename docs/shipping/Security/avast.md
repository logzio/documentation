---
id: Avast
title: Avast
overview: Avast is a family of cross-platform internet security applications. This topic describes how to send system logs from your Avast Antivirus platform to Logz.io. 
product: ['logs', 'siem']
os: ['windows', 'linux']
filters: ['Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/avast.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

[Avast Antivirus](https://www.avast.com/) is a family of cross-platform internet security applications. This topic describes how to send system logs from your Avast Antivirus platform to Logz.io. 

**Before you begin, you'll need**:

* Avast Antivirus installed on your machine
* An active account with Logz.io
* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html) installed on your machine
* Root priveleges on your machines 

## Default configuration

 

{@include: ../../_include/log-shipping/certificate.md}


### Configure Filebeat

1. Paste the following into the inputs section of the Filebeat configuration file:

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


   ```yaml
   filebeat.inputs:
   
   - type: filestream
     paths:
       - C:\ProgramData\Avast Software\Avast\report\FileSystemShield.txt
     fields:
       logzio_codec: plain
       token: <<LOG-SHIPPING-TOKEN>>
       type: avast
     fields_under_root: true
     encoding: utf-8
     ignore_older: 3h
     multiline:
       type: pattern 
       pattern: '(\d\d/\d\d/\d\d\d\d)' 
       negate: true 
       match: after
   - type: filestream
     paths:
       - C:\ProgramData\Avast Software\Avast\report\Full Virus Scan.txt
     fields:
       logzio_codec: plain
       token: <<LOG-SHIPPING-TOKEN>>
       type: avast
     fields_under_root: true
     encoding: utf-8
     ignore_older: 3h
     multiline:
      pattern: '^\* Avast Scan Report'
      negate: true
      match: after
     ignore_older: 3h
   - type: filestream
     paths:
       - C:\ProgramData\Avast Software\Avast\report\aswBoot.txt
     fields:
       logzio_codec: plain
       token: <<LOG-SHIPPING-TOKEN>>
       type: avast
     fields_under_root: true
     encoding: utf-8
     ignore_older: 3h
     multiline:
      pattern: '^\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}\nScan of'
      negate: true
      match: after
     ignore_older: 3h
   - type: filestream
     paths:
       - C:\ProgramData\Avast Software\Avast\report\WebShield.txt
     fields:
       logzio_codec: plain
       token: <<LOG-SHIPPING-TOKEN>>
       type: avast
     fields_under_root: true
     encoding: utf-8
     ignore_older: 3h
     multiline:
      pattern: '^\*\n\* Avast Real-time Shield Scan Report'
      negate: true
      match: after
     ignore_older: 3h
   filebeat.registry.path: 'C:\ProgramData\Filebeat'
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
   output:
     logstash:
       hosts: ["<<LISTENER-HOST>>:5015"]  
       ssl:
         certificate_authorities: ['C:\ProgramData\Elastic\Beats\filebeat\Logzio.crt']

   ```

   If you're running Filebeat 7 to 8.1, paste the code block below instead:


   ```yaml
   filebeat.inputs:
   
   - type: log
     paths:
       - C:\ProgramData\Avast Software\Avast\report\FileSystemShield.txt
     fields:
       logzio_codec: plain
       token: <<LOG-SHIPPING-TOKEN>>
       type: avast
     fields_under_root: true
     encoding: utf-8
     ignore_older: 3h
     multiline:
       type: pattern 
       pattern: '(\d\d/\d\d/\d\d\d\d)' 
       negate: true 
       match: after
   - type: log
     paths:
       - C:\ProgramData\Avast Software\Avast\report\Full Virus Scan.txt
     fields:
       logzio_codec: plain
       token: <<LOG-SHIPPING-TOKEN>>
       type: avast
     fields_under_root: true
     encoding: utf-8
     ignore_older: 3h
     multiline:
      pattern: '^\* Avast Scan Report'
      negate: true
      match: after
     ignore_older: 3h
   - type: log
     paths:
       - C:\ProgramData\Avast Software\Avast\report\aswBoot.txt
     fields:
       logzio_codec: plain
       token: <<LOG-SHIPPING-TOKEN>>
       type: avast
     fields_under_root: true
     encoding: utf-8
     ignore_older: 3h
     multiline:
      pattern: '^\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}\nScan of'
      negate: true
      match: after
     ignore_older: 3h
   - type: log
     paths:
       - C:\ProgramData\Avast Software\Avast\report\WebShield.txt
     fields:
       logzio_codec: plain
       token: <<LOG-SHIPPING-TOKEN>>
       type: avast
     fields_under_root: true
     encoding: utf-8
     ignore_older: 3h
     multiline:
      pattern: '^\*\n\* Avast Real-time Shield Scan Report'
      negate: true
      match: after
     ignore_older: 3h
   filebeat.registry.path: 'C:\ProgramData\Filebeat'
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
   output:
     logstash:
       hosts: ["<<LISTENER-HOST>>:5015"]  
       ssl:
         certificate_authorities: ['C:\ProgramData\Elastic\Beats\filebeat\Logzio.crt']

   ```
  
  
   * {@include: ../../_include/log-shipping/log-shipping-token.md}
   * {@include: ../../_include/log-shipping/listener-var.md}

2. Run Filebeat with the new configuration.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for data of type `avast` to see the incoming Axonius logs.
  
If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).
  
 

## Optional configuration with report files

 


### Configure Avast Antivirus to generate report files for your scans
  
If you want to send data from virus scans together with the logs, you need to enable Avast Antivirus to generate report files for these scans. You do not need to change antything in the Filebeat configuration as it already includes paths to these report files.
  
To enable this:

1. Open Avast Antivirus.
2. Navigate to **Menu > Settings > Protection > Virus Scans > Full Virus Scan**.
3. Check the **Generate report file** checkbox.
4. Navigate to **Targeted Scan**.
5. Check the **Generate report file** checkbox.
6. Navigate to **Explorer Scan**.
7. Check the **Generate report file** checkbox.


 
 
