---
sidebar_position: 10
title: Give AWS access with access keys
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Configure AWS access keys with Logz.io
keywords: [AWS, access keys, aws access keys, Logz.io aws access keys]
---

You can connect Logz.io to your AWS account using an IAM user,
which authenticates with AWS access keys.
This gives Logz.io the appropriate level of access
while keeping your AWS account secure.

## Grant access to an S3 bucket


### Enable Logz.io to access your S3 bucket

Logz.io will need the following permissions to your S3 bucket:

* **s3:ListBucket** - to know which files are in your bucket and to thereby keep track of which files have already been ingested
* **s3:GetObject** - to download your files and ingest them to your account

To do this, add the following to your IAM policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::<BUCKET_NAME>"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::<BUCKET_NAME>/*"
            ]
        }
    ]
}
```

* Replace `<BUCKET_NAME>` with the name of your S3 bucket.

:::note
Note that the ListBucket permission is set to the entire bucket and the GetObject permission ends with a /* suffix, so we can get files in subdirectories.
:::

### Create the user

Browse to the [IAM users](https://console.aws.amazon.com/iam/home#/users)
and click **Add user**.
You're taken to the _Add user_ wizard.

![Create an IAM role for another AWS account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/iam--add-user.png)

Assign a **User name**.

Under _Select AWS access type_, select **Programmatic access**.

Click **Next: Permissions** to continue.

### Create the policy

In the  _Set permissions_ section, click **Attach existing policies directly > Create policy**.
The _Create policy_ page loads in a new tab.

![Create policy](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/create-policy-visual-editor.png)

Set these permissions:

* **Service**:
  Choose **S3**
* **Actions**:
  Select **List > ListBucket** and **Read > GetObject**
* **Resources > bucket**:
  Click **Add ARN** to open the _Add ARN_ dialog.
  Type the intended **Bucket name**, and then click **Add**.
* **Resources > object**:
  Click **Add ARN** to open the _Add ARN(s)_ dialog.
  Add the intended **Bucket name**,
  then select **Object name > Any**.
  Click **Add**.

Click **Review policy** to continue.

Give the policy a **Name** and optional **Description**, and then click **Create policy**.

Remember the policy's name—you'll need this in the next step.

Close the tab to return to the _Add user_ page.

### Attach the policy to the user

Click refresh, and then type your new policy's name in the search box.

Find your policy in the filtered list and select its check box.

Click **Next: Tags**,
and then click **Next: Review** to continue to the _Review_ screen.

### Finalize the user

Give the user a **Name** and optional **Description**,
and then click **Create user**.

You're taken to a success page.

### Add the bucket to Logz.io

Add the **S3 bucket name** and **Prefix**

Copy the _Access key ID_ and _Secret access key_, or click **Download .csv**.

In Logz.io, paste the **Access key** and **Secret key**,
and then click **Save**.
