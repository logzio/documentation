---
id: Amazon-S3
title: Amazon S3
sidebar_position: 1
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
---

 

#### Configuration

**Before you begin, you'll need**:

* Root access
* Port 5000 open

 

##### Run the rsyslog configuration script

{@include: ../_include/log-shipping/log-shipping-token.html}

{@include: ../_include/log-shipping/listener-var.html} 

```shell
curl -sLO https://github.com/logzio/logzio-shipper/raw/master/dist/logzio-rsyslog.tar.gz \
  && tar xzf logzio-rsyslog.tar.gz \
  && sudo rsyslog/install.sh -t linux -a "<<LOG-SHIPPING-TOKEN>>" -l "<<LISTENER-HOST>>"
```


The above assumes the following defaults:

* Log location - `/var/log/`
* Log type - `syslog`

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then [open Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can search for `type:syslog` to filter for your logs. 

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
 

{@include: ../_include/log-shipping/rsyslog-troubleshooting.md} 

  