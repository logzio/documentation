---
sidebar_position: 1
title: Regions
---

Logz.io maintains clusters worldwide so that it can host your account in a region that is closest to you.

You'll need to know your account's region to configure shippers to send data to Logz.io. It is also important if you're using the Logz.io API.

All services related to your account are hosted in the same region. This means you'll ship logs, sign in, and access the API from the same region as your account.


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
|---|---|---|
|US East (Northern Virginia)|AWS|app.logz.io|listener.logz.io|api.logz.io|us | us-east-1|	 
|Asia Pacific (Sydney)|AWS|app-au.logz.io|listener-au.logz.io|api-au.logz.io|au|ap-southeast-2|
|Canada (Central)	|AWS|app-ca.logz.io|listener-ca.logz.io	|api-ca.logz.io|ca|ca-central-1|
|Europe (Frankfurt)|AWS|app-eu.logz.io|listener-eu.logz.io|api-eu.logz.io|eu|eu-central-1|
|Europe (London)|AWS|app-uk.logz.io|listener-uk.logz.io|api-uk.logz.io|uk|eu-west-2|

## Supported regions for Prometheus metrics


Your listener host and API host will always be in the same region as your Prometheus metrics account.

| Region | Cloud | Logz.io account host | Listener host | API host | Region code | Region slug |
|---|---|---|
|US East (Northern Virginia)|AWS|app.logz.io|listener.logz.io|api.logz.io| | us-east-1|	 
|Canada (Central)	|AWS|app-ca.logz.io|listener-ca.logz.io	|api-ca.logz.io|ca|ca-central-1|
|Europe (Frankfurt)|AWS|app-eu.logz.io|listener-eu.logz.io|api-eu.logz.io|eu|eu-central-1|
|Europe (London)|AWS|app-uk.logz.io|listener-uk.logz.io|api-uk.logz.io|uk|eu-west-2|




