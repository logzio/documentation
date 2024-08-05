---
id: AWS-S3-Bucket
title: AWS S3 Bucket
overview: Amazon S3 stores data within buckets, allowing you to send your AWS logs and metrics to Logz.io. S3 buckets lets you store and access large amounts of data and is often used for big data analytics, root cause analysis, and more.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['AWS', 'Data Store', 'Other', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-s3.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
drop_filter: []
---


## Logs 

Some AWS services can be configured to send their logs to an S3 bucket, where Logz.io can directly retrieve them.


### Shipping logs via S3 Hook

If your data is not alphabetically organized, use the S3 Hook. This requires deploying a Lambda function in your environment to manage the log shipping process.


{@include: ../../_include/log-shipping/stack.md}



### Shipping logs via S3 Fetcher

If your data is organized alphabetically, use S3 Fetcher. Logz.io operates this fetcher, directly accessing your S3 to retrieve the data.

:::note
If your S3 bucket is encrypted, add `kms:Decrypt` to the policy on the ARN of the KMS key used to encrypt the bucket.
:::

**Best practices**

Due to S3 API limitations, Logz.io collects logs in alphabetical order. Keep the following tips in mind when configuring logging:

* **Make the prefix as specific as possible** - 
  The prefix is the part of your log path that remains constant across all logs.
  This includes the folder structure and the beginning of the filename.

* **The log path after the prefix must come in alphabetical order** - 
  Start the object name (after the prefix) with the Unix epoch time, as it always increases, ensuring that incoming logs are fetched correctly.

* **The size of each log file should not exceed 50 MB** - 
  Each log file should be no larger than 50 MB to ensure successful upload.



### Add a New S3 Bucket via Logz.io Wizard


{@include: ../../_include/log-shipping/s3-bucket-snippet.html}


<!-- logzio-inject:aws:s3-buckets -->


1. Click **+ Add a bucket**
2. Select IAM role as your method of authentication.
3. The configuration wizard will open:
    * Select the hosting region from the dropdown list.
    * Enter the **S3 bucket name**
    * _(Optional)_ Add a prefix if desired.
    * Decide whether to include the **source file path** as a field in your log.
4. **Save** your information.


:::note
Logz.io fetches logs generated after the S3 bucket is configured. It cannot fetch logs retroactively.
:::
 

#### Enable Logz.io to access your S3 bucket

Add the following to your IAM policy:

* **s3:ListBucket** - to list the files in your bucket and track which files have been ingested.
* **s3:GetObject** - to download and ingest your files.

Add the following to your IAM policy:


```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket",
        "s3:GetBucketLocation",
        "kms:Decrypt"
      ],
      "Resource": [
        "arn:aws:s3:::<BUCKET_NAME>",
        "arn:aws:s3:::<BUCKET_NAME>/*",
        "<<ARN_OF_THE_KMS_KEY_ROLE>>"
      ]
    }
  ]
}
```

* Replace `<BUCKET_NAME>` with the name of your S3 bucket.
* Replace `<<ARN_OF_THE_KMS_KEY_ROLE>>` with your ARN of the KMS key role.

:::note
Note that the ListBucket permission is set to the entire bucket and the GetObject permission ends with a /* suffix, so we can get files in subdirectories.
:::
 


#### Create a Logz.io-AWS connector

Navigate to Logz.io's [**Integration Hub**](https://app.logz.io/#/dashboard/integrations/collectors) and select the relevant AWS resource. Once inside, click **+ Add a bucket** and select the option to **Authenticate with a role**.

Copy the **Account ID** and **External ID** from the integration page.

Fill out the form to create a new connector, including the **S3 bucket name** and optional **Prefix** where your logs are stored.

Click **Get the role policy** to review and copy the policy. Keep this information handy for use in AWS.

Choose whether you want to include the **source file path**. This saves the path of the file as a field in your log.

#### Create the policy

Navigate to [IAM policies](https://us-east-1.console.aws.amazon.com/iam/home#/policies) and click **Create policy**.

In the **JSON** tab, replace the default JSON with the policy you copied from Logz.io.

Click **Next**, provide a **Name** and optional **Description**, and then click **Create policy**. Remember the policy's name.


#### Create the IAM Role in AWS

Go to your [IAM roles](https://console.aws.amazon.com/iam/home#/roles) page in your AWS admin console and click "Create role."

Click **AWS Account > Another AWS account**.

Paste the **Account ID** you copied from Logz.io.

Paste the Account ID from Logz.io, select **Require external ID**, and paste the **External ID**.

Click **Next: Permissions**, refresh the page, and search for your new policy. Select it and proceed.


#### Finalize the role


Provide a **Name** (e.g., "logzio-...") and optional **Description**.

Click **Create role**.


#### Copy the ARN to Logz.io

In the _IAM roles_ screen, type your new role's name in the search box. Click on it to enter its summary page.

Copy the role ARN (top of the page).

In Logz.io, paste the ARN in the **Role ARN** field, and then click **Save**.


#### Check your logs

Allow some time for data ingestion, then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

For troubleshooting, refer to our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.



### Add buckets directly from Logz.io

You can add your buckets directly from Logz.io by providing your S3 credentials and configuration.

 
#### Add a new S3 bucket using the dedicated Logz.io configuration wizard

{@include: ../../_include/log-shipping/s3-bucket-snippet.html}


<!-- logzio-inject:aws:s3-buckets -->


1. Click **+ Add a bucket**.
2. Select **access keys** as your method of authentication.
3. The configuration wizard will open:
    * Select the hosting region from the dropdown list.
    * Enter the **S3 bucket name**
    * _(Optional)_ Add a prefix if desired.
    * Decide whether to include the **source file path** as a field in your log.
4. **Save** your information.


:::note
Logz.io fetches logs generated after the S3 bucket is configured. It cannot fetch logs retroactively.
:::
 

#### Enable Logz.io to access your S3 bucket

Add the following to your IAM policy:

* **s3:ListBucket** - to list the files in your bucket and track which files have been ingested.
* **s3:GetObject** - to download and ingest your files.

Add the following to your IAM policy:

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
Note that the ListBucket permission is set to the entire bucket and the GetObject permission ends with a `/*` suffix, so we can get files in subdirectories.
:::
 

#### Create the user

Navigate to [IAM users](https://console.aws.amazon.com/iam/home#/users) and click **Create user**.

Assign a **User name**.

Under _Select AWS access type_, select **Programmatic access**.

Click **Next: Permissions** to continue.

#### Create the policy

In the _Set permissions_ section, click **Attach existing policies directly** and then **Create policy**. This opens the _Create policy_ page in a new tab.


Set the following permissions:

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


Click **Review policy**, provide a **Name** and optional **Description**, and click **Create policy**.

Remember the policy's name—you'll need this in the next step.

Close the tab to return to the _Add user_ page.

#### Attach the policy to the user

Refresh the page, search for your new policy, and select its check box.

Click **Next: Tags**, then **Next: Review** to continue to the _Review_ screen.

#### Finalize the user

Give the user a **Name** and optional **Description**, and then click **Create user**.

You're taken to a success page.

#### Add the bucket to Logz.io

Add the **S3 bucket name** and **Prefix**.

Copy the _Access key ID_ and _Secret access key_, or click **Download .csv**.

In Logz.io, paste the **Access key** and **Secret key**,
and then click **Save**.


#### Check your logs

Allow some time for data ingestion, then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

For troubleshooting, refer to our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.



### Troubleshooting

#### Migrating IAM roles to a new external ID

If you previously set up an IAM role with your own external ID, we recommend updating your Logz.io and AWS configurations to use a Logz.io-generated external ID. This enhances the security of your AWS account by removing the predictability of internal naming conventions.

**Before Migration:** Identify where the existing IAM role is used in Logz.io. You'll need to replace any S3 fetcher and [Archive & Restore](https://app.logz.io/#/dashboard/tools/archive-and-restore) configurations that use the current role.


* **If the role is used in a single Logz.io account**:
  Update the external ID and replace current Logz.io configurations. See [_Migrate to the Logz.io external ID in the same role_](https://docs.logz.io/docs/user-guide/admin/give-aws-access-with-iam-roles/#migrate-with-same-role).
* **If the role is used with multiple Logz.io accounts**:
  Create a new role for each account and replace current Logz.io configurations. See
  [_Migrate to new IAM roles_](https://docs.logz.io/docs/user-guide/admin/give-aws-access-with-iam-roles/#migrate-to-new-roles).

#### Migrate to the Logz.io external ID in the same role

In this procedure, you'll:

* Replace Logz.io configurations to use the new external ID.
* Update the external ID in your IAM role's trust policy.

Follow this process only if the IAM role is used in a single Logz.io account.

:::danger Warning
When you update your IAM role to the Logz.io external ID,
all Logz.io configurations relying on that role
will stop working.
Before you begin,
make sure you know everywhere your existing IAM role is used in Logz.io.
:::

**1. Delete an S3 configuration from Logz.io**

Choose an S3 fetcher or [Archive & restore](https://app.logz.io/#/dashboard/tools/archive-and-restore) configuration to replace.

Copy the **S3 bucket name**, **Role ARN**, and note the **Bucket region**. For an S3 fetcher, also copy the path **Prefix** and **Log type**.

Delete the configuration.

**2. Replace the configuration**

For an S3 fetcher, click **Add a bucket** and **Authenticate with a role**.

Recreate your configuration with the values copied earlier, and copy the **External ID** for use in AWS.


**3. Update the external ID in your IAM role**

Go to the [IAM roles](https://console.aws.amazon.com/iam/home#/roles) page and open the role used by the deleted configuration.

In the **Trust relationships** tab, click **Edit trust relationship** to open the policy document JSON.

Replace the value of `sts:ExternalId` with the Logz.io external ID.

For example,
if your account's external ID is
`logzio:aws:extid:example0nktixxe8q`,
you would see this:

```text
"sts:ExternalId": "logzio:aws:extid:example0nktixxe8q"
```

:::caution note
Saving the trust policy at this point
will immediately change your role's external ID.
Any other Logz.io configurations that use this role
will stop working until you update them.
:::

Click **Update Trust Policy** to use the Logz.io external ID for this role.

**4. Save the new S3 configuration in Logz.io**

* **For an S3 fetcher**: Click **Save**
* **For Archive & restore**: Click **Start archiving**

You'll see a success message if Logz.io authenticated and connected to your S3 bucket.

If the connection failed,
double-check your credentials in Logz.io and AWS.

**5. _(If needed)_ Replace other configurations that use this role**

If other configurations use the same role, update them with the new external ID. Logz.io generates one external ID per account, so you won't need to change the role again.



 

#### Migrate to new IAM roles

In this procedure, you'll:

* Create a new IAM role with the new external ID.
* Replace Logz.io configurations to use the new role.

Repeat this procedure for each Logz.io account where you need to fetch or archive logs in an S3 bucket.


 

**1. Delete an S3 configuration from Logz.io**

Choose an S3 fetcher or [Archive & restore](https://app.logz.io/#/dashboard/tools/archive-and-restore)
configuration to replace.

Copy the **S3 bucket name**, **Role ARN**, and note the **Bucket region**. For an S3 fetcher, also copy the path **Prefix** and **Log type**.

Delete the configuration.

**2. Replace the configuration**

For an S3 fetcher, click **Add a bucket** and **Authenticate with a role**.

Recreate your configuration with the values copied earlier, and copy the **External ID** for use in AWS.


**3. Set up your new IAM role**

Follow the steps in _[Grant access to an S3 bucket](https://docs.logz.io/docs/user-guide/admin/give-aws-access-with-access-keys/#grant-access-to-an-s3-bucket)_ using the information you copied earlier.

Complete the setup of the new IAM role.


**4. _(If needed)_ Replace other configurations that use this role**

If there are other S3 fetcher or Archive & Restore configurations in this account using the same role, repeat steps 1 and 2, and use the new role ARN.

For configurations in other Logz.io accounts, repeat the entire procedure from the beginning.  
 

#### Testing IAM Configuration

After setting up `s3:ListBucket` and `s3:GetObject` permissions, you can test the configuration as follows.

**1. Install s3cmd**
  
* **For Linux and Mac:**
  
Download the .zip file from the [master branch](https://github.com/s3tools/s3cmd/archive/master.zip) of the s3cmd GitHub repository.
  
* **For Windows:**
  
Download [s3cmd express](https://www.s3express.com/download.htm).
  

Note: s3cmd will usually prefer your locally-configured S3 credentials over those provided as parameters. Backup your current S3 access settings or use a new instance or Docker container.

**2. Configure s3cmd**
  
Run `s3cmd --configure` and enter your Logz.io IAM user access and secret keys.
  
**3. List a required bucket**
  
Run `s3cmd ls s3://<BUCKET_NAME>/<BUCKET_PREFIX>/`. Replace `<BUCKET_NAME>` with the name of your s3 bucket and `<BUCKET_PREFIX>` with the bucket prefix, if the prefix is required.
  
**4. Get a file from the bucket**
  
Run `s3cmd get s3://<BUCKET_NAME>/<BUCKET_PREFIX>/<OBJECT_NAME>`. Replace `<BUCKET_NAME>` with the name of your s3 bucket, `<BUCKET_PREFIX>` with the bucket prefix and `<OBJECT_NAME>` with the name of the file you want to retrieve.



## Metrics

Deploy this integration to send your Amazon S3 metrics to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.

Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["1Pm3OYbu1MRGoELc2qhxQ1"] -->


{@include: ../../_include/metric-shipping/aws-metrics-new.md}

Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["1Pm3OYbu1MRGoELc2qhxQ1"] -->

