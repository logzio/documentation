---
id: Intercom
title: Intercom
overview: Intercom is a messaging platform with bots, apps, product tours and oher features. Deploy this integration to ship Intercom events from your Intercom account to Logz.io using webhooks. 
product: ['metrics']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/intercom.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
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

 
