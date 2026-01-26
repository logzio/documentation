---
id: Logstash-data
title: Logstash
overview: Logstash is an open-source server-side data processing pipeline. This integration can ingest data from multiple  sources. With Logz.io, you can monitor Logstash instances and quickly identify if and when issues arise.
product: ['logs']
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

For most other cases, we recommend using [Filebeat](/docs/shipping/other/filebeat-data/).

These instructions apply to Logstash running on MacOS, Linux and Windows.


## Shipping with Logstash over TCP - Encrypted

**Before you begin, you'll need**: JDK, [Logstash](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html)

### Add Logz.io to your configuration file

Add these code blocks to the end of your existing Logstash configuration file.
 
Make sure the `mutate` block is the last item in the `filters` block.

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-url.html}

```conf
filter {
  # ...
  # ...
  mutate {
    add_field => { "token" => "<<LOG-SHIPPING-TOKEN>>" }
  }
}

output {
  http {
    url => "https://<<LISTENER-HOST>>:8071?token=<<LOG-SHIPPING-TOKEN>>&type=<LOG-TYPE>"
    http_method => "post"
    format => "json"
  }
}
```

### Start Logstash

Start or restart Logstash for the changes to take effect.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

**Limitations**

* Max body size: 10 MB (10,485,760 bytes).
* Max log line size: 500,000 bytes.
* Type field in the log overrides the `type` in the request header.

### Start Logstash

Start or restart Logstash for the changes to take effect.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).


  