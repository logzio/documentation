---
id: Vercel-data
title: Vercel
overview: Vercel is a Cloud Platform that enables developers to deploy, manage, and scale modern web applications. Use this integration to send logs from your Vercel applications to your Logz.io account.
product: ['logs']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/vercel.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

Vercel is a Cloud Platform that enables developers to deploy, manage, and scale modern web applications. Use this integration to send logs from your Vercel applications to your Logz.io account.


## Configure Log Drain

1. In your Vercel account go to **Settings** tab
2. Select **Log Drains** from the list
3. Add a new Log Drain
    - Choose which Projects and Sources you would like to send logs from
    - Choose **Delivery Format** as **NDJSON**
    - (Optional) Set **Custom Name** to `Logz.io Output`
    - Choose the Environments to send logs from
    - (Optional) Change the sampling rate if you don't want 100% of the logs to be sent
    - Set Endpoint to `https://listener.logz.io:8071?token=<<LOG-SHIPPING-TOKEN>>&type=vercel`

:::note
- `<<LOG-SHIPPING-TOKEN>>` can be found [here](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs).
- You can change the type from vercel at the endpoint URL to any type name that you prefer (`&type=<<LOG-TYPE>>`).
:::


4. Click **Test Log Drain** to make sure everything is setup properly.
5. If you got message **Test log drain sent successfully**, click **Add Log Drain**.


## Check Logz.io for your logs

Give your logs some time to get ingested, then open your [Logz.io Account Explore](https://app.logz.io/#/dashboard/explore) to view them.