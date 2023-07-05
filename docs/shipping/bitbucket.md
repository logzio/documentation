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



Bitbucket is a Git-based source code repository hosting service. This integration allows you to ship logs from your Bitbucket repository to your Logz.io account.

**Before you begin, you'll need**: 

* An active account with Bitbucket and a Bitbucket repository
* An actie account with Logz.io

 

##### Open the Bitbucket repository

Log in to your Bitbucket account and navigate to the repository that you need to send logs from.

##### Open the **Add new webhook** page

Navigate to **Repository Settings > Webhooks > Add webhook**.

##### Fill out the **Add new webhook** page

* In the **Title** field, enter **logzio**.

* In the **URL** field, enter `https://<<LISTENER-HOST>>:8071/?token=<<LOG-SHIPPING-TOKEN>>&&type=bitbucket`. {@include: ../_include/log-shipping/listener-var.html} {@include: ../_include/log-shipping/log-shipping-token.md}

* In the **Status** section, enable **Active**.

* Skip the **SSL/TLS** section.

* In the **Triggers** section, select triggers that you would like to enable.

##### Save changes

When everything is filled out, click **Save**.


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can search for `type:bitbucket` to filter for your BitBucket logs.
  
If you still don’t see your logs, see [log shipping troubleshooting](https://docs.logz.io/user-guide/log-shipping/log-shipping-troubleshooting.html).

 

