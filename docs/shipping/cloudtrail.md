---
id: CloudTrail
title: AWS CloudTrail
sidebar_position: 1
overview: This integration sends CloudTrail logs.
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


{@include: ../_include/log-shipping/s3-bucket.md service="CloudTrail" %}

#### Configuration

**Before you begin**:

* If you plan on using an access key to authenticate your connection, you'll need to set the `s3:ListBucket` and `s3:GetObject` [permissions](https://docs.logz.io/user-guide/give-aws-access-with-iam-roles/) for the required S3 bucket.

* If you plan on using an IAM role to authenticate your connection, you can get the role policy by filling out the bucket information and clicking the "Get the role policy" button.

* {@include: ../_include/log-shipping/s3-bucket-file-order.md}

 

##### Send your logs to an S3 bucket

Logz.io fetches your CloudTrail logs from an S3 bucket.

For help with setting up a new trail, see [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) from AWS.


##### Verify bucket definition on AWS

[Navigate to the location of your trail logs on AWS](https://console.aws.amazon.com/cloudtrail/):

![Trail location](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/trail-location.png)

And verify the definition of the bucket is under the CloudTrail path:

![Trail definition](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/trail-object-library.png)

Region data must be created under the CloudTrain path BEFORE the S3 bucket is defined on Logz.io. Otherwise, you won't be able to proceed with sending CloudTrail data to Logz.io. ![Trail regions](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/trail-regions.png)
:::

Next, note the bucket's name and the way the prefix is constructed, for example:

Bucket name: `aws-cloudtrail-logs-486140753397-9f0d7dbd`.

Prefix name: `AWSLogs/486140753397/CloudTrail/`.

You'll need these values when adding your S3 bucket information.


![prefix](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/prefix-trail.png)


##### Add your S3 bucket information

<!-- logzio-inject:aws:cloudtrail -->

{@include: ../_include/log-shipping/S3-fetcher.html}

1. Click **+ Add a bucket**
2. Select your preferred method of authentication - an IAM role or access keys.

The configuration wizard will open.

3. Provide the **S3 bucket name**
4. Provide your **Prefix**. That is your CloudTrail path. See further details below.
5. There is no **Region** selection box because it is not needed. Logz.io will pull data from all regions in AWS for the specified bucket and account.
6. Choose whether you want to include the **source file path**. This saves the path of the file as a field in your log.
7. **Save** your information.

![S3 bucket configuration wizard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/iam-role-configuration.png)


###### Getting the information from your CloudTrail AWS path

You may need to fill in 2 parameters when creating the bucket - {BUCKET_NAME} and {PREFIX}. You can find them in your CloudTrail AWS path. The AWS path structure for CloudTrail looks like the examle below:

```
{BUCKET_NAME}/{PREFIX_IF_EXISTS}/cloudtrail/AWSLogs/{AWS_ACCOUNT_ID}/CloudTrail/
```

* {BUCKET_NAME} is your **S3 bucket name**.

* {PREFIX} is your CloudTrail path. The prefix is generate by default and represents the complete path inside the bucket up until the regions section. It should look like this: `AWSLogs/{AWS_ACCOUNT_ID}/CloudTrail/`.

:::note
Logz.io fetches logs that are generated after configuring an S3 bucket.
Logz.io cannot fetch past logs retroactively.
:::
 

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 

#### Troubleshooting

##### Problem: Failed to save bucket configuration 

The following error appears when you're trying to create a bucket:

```shell
AWS failed to create cloudtrail bucket. Exception AWS bucket is empty: 403.
```

##### Possible cause

The bucket's location is incorrect or might be missing the correct prefix.

##### Suggested remedy


1. Head to CloudTrail console on AWS and check the relevant trail:
![Dashboard trail](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/dashboard-trail.png)

2. Verify that the location of the trail is correct:
![Trail location](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/trail-location.png)

And verify that the prefix contains all parts:

![Prefix trail](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/prefix-trail.png)

In this case, the cause of the error is that the location is empty or that the prefix is wrong. 

The bucket should be `aws-cloudtrail-logs-486140753397-9f0d7dbd`, and the prefix should be `AWSLogs/486140753397/CloudTrail/` (You can click on the prefix to verify that it is empty).

Once you fix these issues, you can return to Logz.io to create the CloudTrail bucket.