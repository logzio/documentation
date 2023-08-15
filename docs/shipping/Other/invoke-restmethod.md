---
id: invoke-restmethod
title: Invoke RestMethod
overview: Invoke-RestMethod is a command to interact with REST APIs in PowerShell. Invoke-RestMethod is a quick and easy way to test your configuration or troubleshoot your connectivity to Logz.io.
product: ['logs']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/Invoke-RestMethod.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


 

Invoke-RestMethod is a command to interact with REST APIs in PowerShell. Invoke-RestMethod is a quick and easy way to test your configuration or troubleshoot your connectivity to Logz.io.

You can upload JSON or plain text files.


### Limitations

* Max body size is 10 MB (10,485,760 bytes)
* Each log line must be 500,000 bytes or less
* If you include a `type` field in the log, it overrides `type` in the request header

### Upload a JSON log file

**Before you begin, you'll need**:
[PowerShell](https://docs.microsoft.com/en-us/powershell/)


 

### Upload the file

If you want to ship logs from your code but don't have a library in place,
you can send them directly to the Logz.io listener as a minified JSON file.

```shell
Invoke-RestMethod -method POST -Uri https://<<LISTENER-HOST>>:8071?token=<<LOG-SHIPPING-TOKEN>>"&"<<LOG-TYPE>> -InFile <<PATH/TO/LOG/FILE.JSON>>
```

{@include: ../_include//general-shipping/replace-placeholders.html}

* {@include: ../_include/log-shipping/type.md} Otherwise, the default `type` is `http-bulk`.
* Replace `<<PATH/TO/LOG/FILE.JSON>>` with the path to your log file.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).