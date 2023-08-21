---
id: Logstash-data
title: Logstash
overview: This integration ships Logstash metrics to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/logstash_temp.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Logstash is a server app that ingests and parses log data.
We recommend using it for shipping to Logz.io only when you have an existing Logstash configuration.

For most other cases, we recommend using [Filebeat]({{site.baseurl}}/shipping/log-sources/filebeat.html).

These instructions apply to Logstash running on MacOS, Linux and Windows.


## Shipping with Logstash over TCP - Encrypted

**Before you begin, you'll need**: JDK, [Logstash](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html)

 


### Download the Logz.io public certificate to your Logstash server

For HTTPS shipping, download the Logz.io public certificate to your certificate authority folder.

* For MacOS and Linux:

```shell
sudo curl https://raw.githubusercontent.com/logzio/public-certificates/master/AAACertificateServices.crt --create-dirs -o /usr/share/logstash/keys/AAACertificateServices.crt
```

* For Windows:

Download the [Logz.io public certificate]({@include: ../../_include/log-shipping/certificate-path.md}) to `C:\ProgramData\ElkStack\logstash-<<YOUR-LOGSTASH-VERSION-NUMBER>>\AAACertificateServices.crt` on your machine.

### Add Logz.io to your configuration file

Add these code blocks to the end of your existing Logstash configuration file.

Make sure the `mutate` block is the last item in the `filters` block.

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html}

* For MacOS and Linux:

```conf
filter {
  # ...
  # ...
  mutate {
    add_field => { "token" => "<<LOG-SHIPPING-TOKEN>>" }
  }
}

output {
  lumberjack {
    hosts => ["<<LISTENER-HOST>>"]
    port => 5006
    ssl_certificate => "/usr/share/logstash/keys/AAACertificateServices.crt"
    codec => "json_lines"
  }
}
```

* For Windows:

```conf
filter {
  # ...
  # ...
  mutate {
    add_field => { "token" => "<<LOG-SHIPPING-TOKEN>>" }
  }
}

output {
  lumberjack {
    hosts => ["<<LISTENER-HOST>>"]
    port => 5006
    ssl_certificate => "/C:\ProgramData\ElkStack\logstash-<<YOUR-LOGSTASH-VERSION-NUMBER>>\AAACertificateServices.crt"
    codec => "json_lines"
  }
}
```

### Start Logstash

Start or restart Logstash for the changes to take effect.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
 
## Ship with Logstash over TCP - Unencrypted

**Before you begin, you'll need**: JDK, [Logstash](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html)

 

### Add Logz.io to your configuration file

Add these code blocks to the end of your existing Logstash configuration file.

Make sure the `mutate` block is the last item in the `filters` block.

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html}

```conf
filter {
  # ...
  # ...
  mutate {
    add_field => { "token" => "<<LOG-SHIPPING-TOKEN>>" }
  }
}

output {
  tcp {
    host => "<<LISTENER-HOST>>"
    port => 5050
    codec => json_lines
  }
}
```

### Start Logstash

Start or restart Logstash for the changes to take effect.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).


  