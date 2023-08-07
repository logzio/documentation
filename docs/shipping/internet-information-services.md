---
id: internet-information-services
title: Internet Information Services (IIS)
overview: Internet Information Services (IIS) for Windows® Server is a flexible, secure and manageable Web server for hosting on the Web. This integration allows you to send logs from your IIS services to your Logz.io account. 
product: ['logs']
os: ['windows', 'linux']
filters: ['Compute']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/iis.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---


Internet Information Services (IIS) for Windows® Server is a flexible, secure and manageable Web server for hosting on the Web. This integration allows you to send logs from your IIS services to your Logz.io account. 


**Before you begin, you'll need**:

* [NXLog](http://nxlog.org/products/nxlog-community-edition/download)
* Admin access

 

### Configure NXLog

Copy this code into your configuration file (`C:\Program Files (x86)\nxlog\conf\nxlog.conf` by default).

{@include: ../_include/log-shipping/log-shipping-token.html}

{@include: ../_include/log-shipping/listener-var.html} 

```conf
define ROOT C:\\Program Files (x86)\\nxlog
define ROOT_STRING C:\\Program Files (x86)\\nxlog
define CERTDIR %ROOT%\\cert
Moduledir %ROOT%\\modules
CacheDir %ROOT%\\data
Pidfile %ROOT%\\data\\nxlog.pid
SpoolDir %ROOT%\\data
LogFile %ROOT%\\data\\nxlog.log
<Extension charconv>
    Module xm_charconv
    AutodetectCharsets utf-8, euc-jp, utf-16, utf-32, iso8859-2
</Extension>

#create one for each application
<Input IIS_Site1>
    Module im_file
    File "C:\\inetpub\\logs\\LogFiles\\W3SVC1\\u_ex*.log"
    SavePos TRUE
    Exec if $raw_event =~ /^#/ drop();
    Exec convert_fields("AUTO", "utf-8");
    Exec $raw_event = '[<<LOG-SHIPPING-TOKEN>>][type=iis]' + $raw_event;
</Input>
<Output out>
    Module  om_tcp
    Host    <<LISTENER-HOST>>
    Port    8010
</Output>

<Route IIS>
    Path IIS_Site1 => out
</Route>
```

### Restart NXLog

```powershell
PS C:\Program Files (x86)\nxlog> Restart-Service nxlog
```

### Check Logz.io for your logs

Confirm you're shipping logs by opening an IIS-hosted webpage in your browser. Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
