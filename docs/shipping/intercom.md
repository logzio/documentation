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


Intercom is a messaging platform with bots, apps, product tours and oher features. Deploy this integration to ship Intercom events from your Intercom account to Logz.io using webhooks. 

#### Ship events data from your Intercom account to Logz.io

Deploy this integration to ship Intercom events from your Intercom account to Logz.io using webhooks.

**Before you begin, you'll need**: an active account with Intercom.

 

##### Create an Intercom developer app

1. Log in to your Intercom account.

2. Navigate to the [Developer hub](https://app.intercom.com/a/apps/_/developer-hub) and select **New app**.

3. Enter the required app name.

4. Select the required workspace.

5. Select **Internal integration**.

6. Select **Create app**.

7. Navigate to **Configure > Webhooks**.

8. Enter the following into the **Your request endpoint URL** field:

   ```shell
   https://<<LISTENER-HOST>>:8071/?token=<<LOG-SHIPPING-TOKEN>>&type=<<MY-TYPE>>
   ```
      {@include: ../_include//general-shipping/replace-placeholders.md}

9. {@include: ../_include/log-shipping/type.md}

10. Select the required webhook topics for the notification types that will be sent to Logz.io.

11. Select **Save**.


##### Check Logz.io for your data

Give your data some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
