---
id: Heroku
title: Heroku
overview: Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. This integration allows you to send logs from your Heroku applications to your Logz.io account. 
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/heroku.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
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

 
