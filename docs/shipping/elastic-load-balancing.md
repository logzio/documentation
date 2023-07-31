---
id: Elastic-Load-Balancing
title: Elastic Load Balancing (ELB)
overview: When you set Logz.io to fetch Elastic Load Balancing (ELB) logs, Logz.io will periodically read logs from the configured S3 bucket. Elastic Load Balancing logs are useful for application usage intelligence and monitoring.
product: ['logs']
os: ['windows', 'linux']
filters: ['AWS', 'Load Balancer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-elb.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---



When you set Logz.io to fetch Elastic Load Balancing (ELB) logs, Logz.io will periodically read logs from the configured S3 bucket. Elastic Load Balancing logs are useful for application usage intelligence and monitoring.

{@include: ../_include/log-shipping/s3-bucket.md service="ELB" %}

#### Configuration

**Before you begin, you'll need**:
`s3:ListBucket` and `s3:GetObject` [permissions](https://docs.logz.io/user-guide/give-aws-access-with-iam-roles/) for the required S3 bucket (one bucket per region)

 

##### Send your logs to an S3 bucket

Logz.io fetches your Elastic Load Balancing logs from an S3 bucket.

For help with setting this up, see these docs from AWS:

* For Application Load Balancer,
  see [Access Logs for Your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html).
* For Network Load Balancer,
  see [Monitor Your Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-monitoring.html).
* For Classic Load Balancer,
  see [Enable Access Logs for Your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html).



##### Add a new S3 bucket using the dedicated Logz.io configuration wizard

Log into the app to use the dedicated Logz.io [configuration wizard](https://app.logz.io/#/dashboard/send-your-data/log-sources/elastic-load-balancing) and add a new S3 bucket.


<!-- logzio-inject:aws:elb -->

{@include: ../_include/log-shipping/add-s3-bucket.md}


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
