---
id: OneLogin
title: OneLogin
overview: OneLogin is a cloud-based identity and access management (IAM) provider. This integration allows you to ship logs from your OneLogin account to your Logz.io account.
product: ['logs', 'siem']
os: ['windows', 'linux']
filters: ['Access Management']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/onelogin.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


OneLogin is a cloud-based identity and access management (IAM) provider. This integration allows you to ship logs from your OneLogin account to your Logz.io account.

**Before you begin, you'll need**: 

* An active account with OneLogin
* An actie account with Logz.io

 

### Login to your OneLogin account

Log in to your OneLogin account as admin.

### Open the **New broadcaster** dialog

Navigate to **Developers > Webhooks > New broadcaster**.

### Fill out the **New broadcaster** dialog
  
![New-broadcaster](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/New-broadcaster.png)

* In the **Title** field, enter **logzio**.

* In the **Format** field, select **SIEM (NDJSON)**.

* In the **Listener URL** field, enter `https://<<LISTENER-HOST>>:8071/?token=<<LOG-SHIPPING-TOKEN>>&type=onelogin`. {@include: ../../_include/log-shipping/listener-var.html} 
{@include: ../../_include/log-shipping/log-shipping-token.md}


### Save changes

When everything is filled out, click **Save**.


### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can search for `type:onelogin` to filter for your OneLogin logs.
  
If you still don’t see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

 

