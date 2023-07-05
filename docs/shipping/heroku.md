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


Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. This integration allows you to send logs from your Heroku applications to your Logz.io account. 
#### Set up a Heroku log drain

**Before you begin, you'll need**:
[Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

 
  
##### Enable the runtime metrics 

Optional - run the following command to include application run time metrics in your logs (for example, http status code, customer's IP, and more):

```shell
heroku labs:enable log-runtime-metrics -a <<HEROKU-APP-NAME>>
```

##### Set up the log drain in Heroku CLI

Run this command in the command line.

```shell
heroku drains:add "https://<<LISTENER-HOST>>:8081?token=<<LOG-SHIPPING-TOKEN>>" -a <<HEROKU-APP-NAME>>
```

{@include: ../_include/log-shipping/log-shipping-token.html}

{@include: ../_include/log-shipping/listener-var.html}

Replace `<<HEROKU-APP-NAME>>` with the name of the app in Heroku.

You can add custom fields to each log message, allowing you to identify different Heroku apps and filter your data in Logz.io.
To do this, add `&<<KEY>>=<<VALUE>>` to the end of the Logz.io URL.

For example:

```shell
heroku drains:add "https://<<LISTENER-HOST>>:8081?token=<<LOG-SHIPPING-TOKEN>>&<<KEY>>=<<VALUE>>" -a <<HEROKU-APP-NAME>>
```


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd) to confirm you're shipping logs.

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
