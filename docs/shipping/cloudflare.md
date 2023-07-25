---
id: Cloudflare
title: Cloudflare
overview: The Cloudflare web application firewall (WAF) protects your internet property against malicious attacks that aim to exploit vulnerabilities such as SQL injection attacks, cross-site scripting, and cross-site forgery requests.
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


The Cloudflare web application firewall (WAF) protects your internet property against malicious attacks that aim to exploit vulnerabilities such as SQL injection attacks, cross-site scripting, and cross-site forgery requests.

For an overview of Cloudflare logs, and the related S3 and Logpush configuration procedures, click [here](https://developers.cloudflare.com/logs/).

#### Setup

To send firewall event logs to Logz.io Cloud SIEM, you'll first configure a Logpush job to send your Cloudflare data to a dedicated S3 bucket, then configure Logz.io to collect and ingest that data from the S3 bucket. 

##### Prerequisites

Before you begin, ensure that you have: 

+ Admin access to Cloudflare.
+ Enterprise account with Cloudflare.
+ Admin access to your AWS environment.
+ Configured an S3 bucket for your Cloudflare logs.
  To create an S3 bucket, see the [instructions from Amazon.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
+ Logs of your HTTP requests uploaded to Amazon S3.
+ [Enabled the Cloudflare Logppush service](https://developers.cloudflare.com/logs/get-started/logpush-dashboard) for the assets you want to monitor in Cloudflare, via **Analytics > Logs > Connect a service**.


 

##### Configure Logpush to send logs to the S3 bucket

To configure Logpush to stream logs of Cloudflare's datasets to your cloud service in batches, follow the [Cloudflare procedure](https://developers.cloudflare.com/logs/get-started/enable-destinations/aws-s3/) to enable the Logpush service to access Amazon S3. <!--  deprecated link (https://developers.cloudflare.com/logs/logpush/aws-s3  -->

For an overview of the Logpush service, [click here](https://developers.cloudflare.com/logs/about)

##### Configure Logz.io to collect logs from the S3 bucket. 

Use [our procedure](https://docs.logz.io/shipping/log-sources/s3-bucket.html#configure-logzio-to-fetch-logs-from-an-s3-bucket) to configure Logz.io to fetch logs from your S3 bucket.


##### Check Logz.io for your logs

Give your Cloudflare data some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your data, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 

