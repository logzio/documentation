---
sidebar_position: 1
title: Regions
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Find the available regions in Logz.io
keywords: [hosting regions, regions, region]
---

Logz.io maintains clusters worldwide so that it can host your account in a region that is closest to you.

You'll need to know your account's region to configure shippers to send data to Logz.io. It is also important if you're using the Logz.io API.

All services related to your account are hosted in the same region. This means you'll ship logs, sign in, and access the API from the same region as your account. However, note that with respect to the **[AI Agent](https://docs.logz.io/docs/user-guide/observability/faq/)**, if your data is hosted in Canada (Central), then we will use the AI model that is hosted in `us-east-1`, and if your data is hosted in Europe (London), then we will use the AI model that is hosted in `eu-central-1`.

## How to look up your account region

You can find your account's region by selecting [**<i class="li li-gear"></i> > Settings > General**](https://app.logz.io/#/dashboard/settings/general) from the top menu. Your two-letter region code is at the start of the region designation. 

Another option is to sign in to your Logz.io account and look at the URL in the address bar.

If you see `app.logz.io`, your account is hosted in the US East (Northern Virginia).
All other regions have a two-letter region code.
For example, if you see `app-eu.logz.io`, then your account is in the Europe (Frankfurt) region.


## Available regions

:::note
Azure Hosting is now deprecated; however, Azure Shipping and Azure Marketplace remain active and will continue to be supported.
:::

Your listener host and API host will always be in the same region as your account.

| Region | Cloud | Logz.io account host | Listener host | API host | Region code | Region slug |
|---|---|---|---|---|---|---|
|US East (Northern Virginia)|AWS|app.logz.io|listener.logz.io|api.logz.io|us | us-east-1|	 
|Asia Pacific (Sydney)|AWS|app-au.logz.io|listener-au.logz.io|api-au.logz.io|au|ap-southeast-2|
|Canada (Central)	|AWS|app-ca.logz.io|listener-ca.logz.io	|api-ca.logz.io|ca|ca-central-1|
|Europe (Frankfurt)|AWS|app-eu.logz.io|listener-eu.logz.io|api-eu.logz.io|eu|eu-central-1|
|Europe (London)|AWS|app-uk.logz.io|listener-uk.logz.io|api-uk.logz.io|uk|eu-west-2|

## OpenTelemetry Protocol (OTLP) regions


When using the OpenTelemetry Protocol (OTLP) to send **log data** to Logz.io, it’s essential to use the appropriate regional endpoint. This ensures compliance with data residency requirements and enhances performance.

Configure your setup with the correct endpoint URL for your region and include your Logz.io token in the configuration file.


| Region | Logz.io account host | Listener host | Region code | Region slug |
|---|---|---|---|---|
|US East (Northern Virginia)|app.logz.io|otlp-listener.logz.io/v1/logs|us | us-east-1|	 
|Asia Pacific (Sydney)|app-au.logz.io|otlp-listener-au.logz.io/v1/logs|au|ap-southeast-2|
|Canada (Central) |app-ca.logz.io|otlp-listener-ca.logz.io/v1/logs	|ca|ca-central-1|
|Europe (Frankfurt) |app-eu.logz.io|otlp-listener-eu.logz.io/v1/logs|eu|eu-central-1|
|Europe (London) |app-uk.logz.io|otlp-listener-uk.logz.io/v1/logs|uk|eu-west-2|




## Supported regions for Prometheus metrics


Your listener host and API host will always be in the same region as your Prometheus metrics account.

| Region | Cloud | Logz.io account host | Listener host | API host | Region code | Region slug |
|---|---|---|---|---|---|---|
|US East (Northern Virginia)|AWS|app.logz.io|listener.logz.io|api.logz.io| | us-east-1|	 
|Canada (Central)	|AWS|app-ca.logz.io|listener-ca.logz.io	|api-ca.logz.io|ca|ca-central-1|
|Europe (Frankfurt)|AWS|app-eu.logz.io|listener-eu.logz.io|api-eu.logz.io|eu|eu-central-1|
|Europe (London)|AWS|app-uk.logz.io|listener-uk.logz.io|api-uk.logz.io|uk|eu-west-2|




