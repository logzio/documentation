
#### Before you begin


##### Set up your IAM user

You'll need an [IAM user](https://console.aws.amazon.com/iam/home)
with the following permissions:

* `cloudwatch:ListMetrics`
* `cloudwatch:GetMetricStatistics`
* `tag:GetResources`

If you don't have one, set that up now.

Create an **Access key ID** and **Secret access key** for the IAM user,
and paste them in your text editor.

##### Get your metrics region

You'll need to specify the AWS region you're collecting metrics from.

![AWS region menu](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/region-menu.png)

Find your region's slug in the region menu
(in the top menu, on the right side).

For example:
The slug for US East (N. Virginia)
is "us-east-1"
and the slug for Canada (Central) is "ca-central-1".