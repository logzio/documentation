---
id: Mailchimp
title: Mailchimp
overview: Mailchimp is the All-In-One integrated marketing platform for small businesses. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/mailchimp.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
drop_filter: []
---


Mailchimp is the All-In-One integrated marketing platform for small businesses. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Mailchimp metrics to Logz.io, you need to add the **inputs.mailchimp** and **outputs.http** plug-ins to your Telegraf configuration file.

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher on a dedicated server

{@include: ../_include/metric-shipping/telegraf-setup.md}
 
#### Add the inputs.mailchimp plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Mailchimp data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.mailchimp]]
  ## MailChimp API key
  ## get from https://admin.mailchimp.com/account/api/
  api_key = "" # required
  
  ## Reports for campaigns sent more than days_old ago will not be collected.
  ## 0 means collect all and is the default value.
  days_old = 0
  
  ## Campaign ID to get, if empty gets all campaigns, this option overrides days_old
  # campaign_id = ""
```

:::note
The database name is only required for instantiating a connection with the server and does not restrict the databases that we collect metrics from. The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/mailchimp/README.md).
:::
 

#### Add the outputs.http plug-in

{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
