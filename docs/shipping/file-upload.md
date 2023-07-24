---
id: Invoke-RestMethod
title: Invoke RestMethod
sidebar_position: 1
overview: Invoke-RestMethod is a command to interact with REST APIs in PowerShell. Invoke-RestMethod is a quick and easy way to test your configuration or troubleshoot your connectivity to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---


 

Invoke-RestMethod is a command to interact with REST APIs in PowerShell. Invoke-RestMethod is a quick and easy way to test your configuration or troubleshoot your connectivity to Logz.io.

You can upload JSON or plain text files.


###### Limitations

* Max body size is 10 MB (10,485,760 bytes)
* Each log line must be 500,000 bytes or less
* If you include a `type` field in the log, it overrides `type` in the request header

#### Upload a JSON log file

**Before you begin, you'll need**:
[PowerShell](https://docs.microsoft.com/en-us/powershell/)


 

##### Upload the file

If you want to ship logs from your code but don't have a library in place,
you can send them directly to the Logz.io listener as a minified JSON file.

```shell
Invoke-RestMethod -method POST -Uri https://<<LISTENER-HOST>>:8071?token=<<LOG-SHIPPING-TOKEN>>"&"<<LOG-TYPE>> -InFile <<PATH/TO/LOG/FILE.JSON>>
```

{@include: ../_include//general-shipping/replace-placeholders.html}

* {@include: ../_include/log-shipping/type.md} Otherwise, the default `type` is `http-bulk`.
* Replace `<<PATH/TO/LOG/FILE.JSON>>` with the path to your log file.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
 

Invoke-RestMethod is a command to interact with REST APIs in PowerShell. Invoke-RestMethod is a quick and easy way to test your configuration or troubleshoot your connectivity to Logz.io.

You can upload JSON or plain text files.


###### Limitations

* Max body size is 30 MB (31,457,280 bytes)
* If you include a `type` field in the log, it overrides `type` in the request header


#### Upload a plain text log file

**Before you begin, you'll need**:
[PowerShell](https://docs.microsoft.com/en-us/powershell/)

 

##### Upload the file


```shell
Invoke-RestMethod -method POST -Uri https://<<LISTENER-HOST>>:8022/file_upload/<<LOG-SHIPPING-TOKEN>>/<<LOG-TYPE>> -InFile <<PATH/TO/LOG/FILE>>
```
Replace the placeholders to match your specifics. (They are indicated by the double angle brackets `<< >>`):

* Replace `<<LOG-SHIPPING-TOKEN>>` with the token of the account you want to ship to.

* {@include: ../_include/log-shipping/type.md} Otherwise, the default `type` is `http-bulk`.

* Replace `<<PATH/TO/LOG/FILE>>` with the path to your log file.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
 
