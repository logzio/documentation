---
id: GitHub
title: GitHub
overview: This integration enable you to collect logs and metrics from github
product: ['logs','  metrics']
os: ['windows', 'linux']
filters: ['CI/CD']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/github.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


## Logs

Capture GitHub events to:

* Track issues and PRs opened by your customers
* Track new features from code changes
* Identify when new code changes lead to system alerts or build failures

**Before you begin, you'll need**: Admin permissions to the GitHub project

 

### Add a webhook to your GitHub project

Open your GitHub project. On your project page, go to **Setting** > **Webhooks** and select **Add webhook**.

![How to add a GitHub webhook](https://dytvr9ot2sszz.cloudfront.net/logz-docs/integrations/github-webhooks.png)

### Add your payload url


For the **Payload url**, use either of the following formats. You can send your data encrypted via HTTPS, or unencrypted, via HTTP:

#### For HTTPS shipping

```
https://<<LISTENER-HOST>>:8071/?token=<<LOG-SHIPPING-TOKEN>>&type=github
```

#### For HTTP shipping

```
http://<<LISTENER-HOST>>:8070/?token=<<LOG-SHIPPING-TOKEN>>&type=github
```

{@include: ../../_include//log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html}

### Configure your webhook

Complete filling in the form:

2. **Content Type**: Select **application/json**.
3. **Secret**: Leave it blank. Your Logz.io account token is used to securely route your logs to your account.
4. **SSL verification**: We recommend enabling SSL verification.
5. Select your event triggers. The options available are:
    * **Just the push event**
    * **Send me everything**
    * **Let me select individual events**. A checklist will appear for you to make your selections.
6. **Active**. Make sure this checkbox is enabled.
7. Click **Add webhook** to save your webhook.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). Search for `type:github` in Open Search Dashboards Discover to filter for your GitHub events. Your logs should be already parsed thanks to the Logz.io preconfigured parsing pipeline.

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).


## Metrics

GitHub is a Git repository hosting service. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Github metrics to Logz.io, you need to add the **inputs.github** and **outputs.http** plug-ins to your Telegraf configuration file.

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher

{@include: ../../_include/metric-shipping/telegraf-setup.md}
 
#### Add the inputs.github plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Github data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.github]]
  ## List of repositories to monitor
  repositories = [
      "influxdata/telegraf",
      "influxdata/influxdb"
  ]

  ## Github API access token.  Unauthenticated requests are limited to 60 per hour.
  # access_token = ""

  ## Github API enterprise url. Github Enterprise accounts must specify their base url.
  # enterprise_base_url = ""

  ## Timeout for HTTP requests.
  # http_timeout = "5s"

  ## List of additional fields to query.
    ## NOTE: Getting those fields might involve issuing additional API-calls, so please
    ##       make sure you do not exceed the rate-limit of GitHub.
    ##
    ## Available fields are:
    ##  - pull-requests         -- number of open and closed pull requests (2 API-calls per repository)
  # additional_fields = []
```

:::note
The database name is only required for instantiating a connection with the server and does not restrict the databases that we collect metrics from. The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/github/README.md).
:::
 

#### Add the outputs.http plug-in

{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
 
