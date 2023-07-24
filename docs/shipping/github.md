---
id: GitHub
title: GitHub
sidebar_position: 1
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
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



Capture GitHub events to:

* Track issues and PRs opened by your customers
* Track new features from code changes
* Identify when new code changes lead to system alerts or build failures

#### Ship Github Events to Logz.io

**Before you begin, you'll need**: Admin permissions to the GitHub project

 

##### Add a webhook to your GitHub project

Open your GitHub project. On your project page, go to **Setting** > **Webhooks** and select **Add webhook**.

![How to add a GitHub webhook](https://dytvr9ot2sszz.cloudfront.net/logz-docs/integrations/github-webhooks.png)

##### Add your payload url


For the **Payload url**, use either of the following formats. You can send your data encrypted via HTTPS, or unencrypted, via HTTP:

###### For HTTPS shipping

```
https://<<LISTENER-HOST>>:8071/?token=<<LOG-SHIPPING-TOKEN>>&type=github
```

###### For HTTP shipping

```
http://<<LISTENER-HOST>>:8070/?token=<<LOG-SHIPPING-TOKEN>>&type=github
```

{@include: ../_include//log-shipping/log-shipping-token.html}

{@include: ../_include/log-shipping/listener-var.html}

##### Configure your webhook

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

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). Search for `type:github` in Open Search Dashboards Discover to filter for your GitHub events. Your logs should be already parsed thanks to the Logz.io preconfigured parsing pipeline.

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
