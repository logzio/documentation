---
id: Amazon-S3-Bucket
title: Amazon S3
sidebar_position: 1
overview: Some AWS services can be configured to ship their logs to an S3 bucket, where Logz.io can fetch those logs directly.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---



Some AWS services can be configured to ship their logs to an S3 bucket, where Logz.io can fetch those logs directly.


:::note
In case your S3 bucket is encrypted, you need to add `kms:Decrypt` to the policy on the ARN of the KMS key used to encrypt the bucket.
:::
 

## Best practices

The S3 API does not allow retrieval of object timestamps, so Logz.io must collect logs in alphabetical order.
Please keep these notes in mind when configuring logging.

* **Make the prefix as specific as possible** \\
  The prefix is the part of your log path that remains constant across all logs.
  This can include folder structure and the beginning of the filename.

* **The log path after the prefix must come in alphabetical order** \\
  We recommend starting the object name (after the prefix) with the Unix epoch time.
  The Unix epoch time is always increasing, ensuring we can always fetch your incoming logs.

* **The size of each log file should not exceed 50 MB** \\
  To guarantee successful file upload, make sure that the size of each log file does not exceed 50 MB.

  


You can add your buckets directly from Logz.io by providing your S3 credentials and configuration.

#### Configure Logz.io to fetch logs from an S3 bucket

 

##### Add a new S3 bucket using the dedicated Logz.io configuration wizard

{@include: ../_include/log-shipping/s3-bucket-snippet.html}


<!-- logzio-inject:aws:s3-buckets -->


1. Click **+ Add a bucket**
2. Select IAM role as your method of authentication.

The configuration wizard will open.

3. Select the hosting region from the dropdown list.
4. Provide the **S3 bucket name**
5. _Optional_ You have the option to add a prefix.
6. Choose whether you want to include the **source file path**. This saves the path of the file as a field in your log.
7. **Save** your information.

![S3 bucket IAM authentication wizard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/s3-add-bucket.png)

:::note
Logz.io fetches logs that are generated after configuring an S3 bucket.
Logz.io cannot fetch old logs retroactively.
:::
 

##### Enable Logz.io to access your S3 bucket

Logz.io will need the following permissions to your S3 bucket:

* **s3:ListBucket** - to know which files are in your bucket and to thereby keep track of which files have already been ingested
* **s3:GetObject** - to download your files and ingest them to your account

To do this, add the following to your IAM policy:

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
 


##### Create a Logz.io-AWS connector

In your Logz.io app, go to **Send your data**.
Select the relevant AWS resource from the left menu.

Click **+ Add a bucket** and select the option to **Authenticate with a role**

![Connect Logz.io to an AWS resource](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/s3-add-bucket-ids.png)

Copy and paste the **Account ID** and **External ID** in your text editor.

Fill in the form to create a new connector.

Enter the **S3 bucket name** and, if needed,
the **Prefix** where your logs are stored.

Click **Get the role policy**.
You can review the role policy to confirm the permissions that will be needed.
Paste the policy in your text editor.

Keep this information available so you can use it in AWS.

Choose whether you want to include the **source file path**. This saves the path of the file as a field in your log.

##### Create the IAM Role in AWS

Go to your [IAM roles](https://console.aws.amazon.com/iam/home#/roles) page in your AWS admin console.

Click **Create role**.
You're taken to the _Create role_ wizard.

![Create an IAM role for another AWS account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/iam--create-role.png)

Click **Another AWS account**.

Paste the **Account ID** you copied from Logz.io.

Select **Require external ID**,
and then paste the **External ID** from step 1.

Click **Next: Permissions** to continue.

##### Create the policy

In the  _Create role_ screen, click **Create policy**.
The _Create policy_ page loads in a new tab.

In the **JSON** tab,
replace the default JSON with the policy you copied from Logz.io.

Click **Review policy** to continue.

Give the policy a **Name** and optional **Description**,
and then click **Create policy**.

Remember the policy's name—you'll need this in the next step.

Close the tab to return to the _Create role_ page.

##### Attach the policy to the role

Refresh the page,
and then type your new policy's name in the search box.

Find your policy in the filtered list and select its check box.

Click **Next: Tags**,
and then click **Next: Review** to continue to the _Review_ screen.

##### Finalize the role

Give the role a **Name** and optional **Description**.
We recommend beginning the name with "logzio-"
so that it's clear you're using this role with Logz.io.

Click **Create role** when you're done.

##### Copy the ARN to Logz.io

In the _IAM roles_ screen, type your new role's name in the search box.

Find your role in the filtered list and click it to go to its summary page.

Copy the role ARN (top of the page).
In Logz.io, paste the ARN in the **Role ARN** field, and then click **Save**.


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 

You can add your buckets directly from Logz.io by providing your S3 credentials and configuration.

#### Configure Logz.io to fetch logs from an S3 bucket

 

##### Add a new S3 bucket using the dedicated Logz.io configuration wizard

{@include: ../_include/log-shipping/s3-bucket-snippet.html}


<!-- logzio-inject:aws:s3-buckets -->


1. Click **+ Add a bucket**
2. Select **access keys** as the method of authentication.

The configuration wizard will open.

3. Select the hosting region from the dropdown list.
4. Provide the **S3 bucket name**
5. _Optional_ You have the option to add a prefix.
6. Choose whether you want to include the **source file path**. This saves the path of the file as a field in your log.
7. **Save** your information.

![S3 bucket keyaccess authentication wizard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/key-access-config-basic.png)

:::note
Logz.io fetches logs that are generated after configuring an S3 bucket.
Logz.io cannot fetch old logs retroactively.
:::
 

##### Enable Logz.io to access your S3 bucket

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
Note that the ListBucket permission is set to the entire bucket and the GetObject permission ends with a `/*` suffix, so we can get files in subdirectories.
:::
 

##### Create the user

Browse to the [IAM users](https://console.aws.amazon.com/iam/home#/users)
and click **Add user**.
You're taken to the _Add user_ wizard.

![Create an IAM role for another AWS account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/iam--add-user.png)

Assign a **User name**.

Under _Select AWS access type_, select **Programmatic access**.

Click **Next: Permissions** to continue.

##### Create the policy

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

##### Attach the policy to the user

Refresh the page,
and then type your new policy's name in the search box.

Find your policy in the filtered list and select its check box.

Click **Next: Tags**,
and then click **Next: Review** to continue to the _Review_ screen.

##### Finalize the user

Give the user a **Name** and optional **Description**,
and then click **Create user**.

You're taken to a success page.

##### Add the bucket to Logz.io

Add the **S3 bucket name** and **Prefix**

Copy the _Access key ID_ and _Secret access key_, or click **Download .csv**.

In Logz.io, paste the **Access key** and **Secret key**,
and then click **Save**.


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).


  

## Migrating IAM roles to a new external ID {#new-external-id}

If you previously set up an IAM role with your own external ID,
we recommend updating your Logz.io and AWS configurations
to use a Logz.io-generated external ID.
This adds security to your AWS account
by removing the predictability
of any internal naming conventions
your company might have.

Before you migrate,
you'll need to know where the existing IAM role is used in Logz.io.
This is because you'll need to replace any
[S3 fetcher](https://app.logz.io/#/dashboard/send-your-data/log-sources/s3-bucket)
and
[Archive & restore](https://app.logz.io/#/dashboard/tools/archive-and-restore)
configurations that use the existing role.

* **If the role is used in a single Logz.io account**:
  You can update the external ID
  and replace current Logz.io configurations.
  See
  [_Migrate to the Logz.io external ID in the same role_](#migrate-with-same-role)
  (below).
* **If the role is used with multiple Logz.io accounts**:
  You'll need to create a new role for each account
  and replace current Logz.io configurations.
  See
  [_Migrate to new IAM roles_](#migrate-to-new-roles)
  (below).

#### Migrate to the Logz.io external ID in the same role {#migrate-with-same-role}

In this procedure, you'll:

* Replace Logz.io configurations to use the new external ID
* Update the external ID in your IAM role's trust policy

Follow this process only if the IAM role is used in a single Logz.io account.

When you update your IAM role to the Logz.io external ID,
all Logz.io configurations that rely on that role
will stop working.
Before you begin,
make sure you know everywhere your existing IAM role is used in Logz.io.
{:.info-box.warning}

 

##### Delete an S3 configuration from Logz.io

Choose an
[S3 fetcher](https://app.logz.io/#/dashboard/send-your-data/log-sources/s3-bucket)
or
[Archive & restore](https://app.logz.io/#/dashboard/tools/archive-and-restore)
configuration to replace.

Copy the **S3 bucket name** and **Role ARN** to your text editor,
and make a note of the **Bucket region**.
If this is an S3 fetcher, copy the path **Prefix** as well,
and make a note of the **Log type**.

Delete the configuration.

##### Replace the configuration

If this is for an S3 fetcher, click **Add a bucket**,
and click **Authenticate with a role**.

![S3 fetcher and archive configuration screens](https://dytvr9ot2sszz.cloudfront.net/logz-docs/archive-and-restore/s3-fetcher-and-archive-config-external-id.png)

Recreate your configuration with the values you copied in step 1,
and copy the **External ID** (you'll paste it in AWS in the next step).

##### Replace the external ID in your IAM role

Browse to the [IAM roles](https://console.aws.amazon.com/iam/home#/roles) page.
Open the role used by the configuration you deleted in step 1.

![IAM role summary page, trust relationships tab](https://dytvr9ot2sszz.cloudfront.net/logz-docs/aws/iam-role-edit-trust-relationship.png)

Open the **Trust relationships** tab
and click **Edit trust relationship** to open the policy document JSON.

Find the line with the key `sts:ExternalId`,
and replace the value with the Logz.io external ID you copied in step 2.

For example,
if your account's external ID is
`logzio:aws:extid:example0nktixxe8q`,
you would see this:

```text
"sts:ExternalId": "logzio:aws:extid:example0nktixxe8q"
```

Saving the trust policy at this point
will immediately change your role's external ID.
Any other Logz.io configurations that use this role
will stop working until you update them.
:::

Click **Update Trust Policy** to use the Logz.io external ID for this role.

##### Save the new S3 configuration in Logz.io

Save the configuration in Logz.io:

* **For an S3 fetcher**: Click **Save**
* **For Archive & restore**: Click **Start archiving**

You'll see a success message if Logz.io authenticated and connected to your S3 bucket.

If the connection failed,
double-check your credentials in Logz.io and AWS.

##### _(If needed)_ Replace other configurations that use this role

If there are other S3 fetcher or Archive & restore configurations
in this account that use the same role,
replace those configurations with the updated external ID.

Logz.io generates one external ID per account,
so you won't need to change the role again.

 

#### Migrate to new IAM roles {#migrate-to-new-roles}

In this procedure, you'll:

* Create a new IAM role with the new external ID
* Replace Logz.io configurations to use the new role

You'll repeat this procedure for each Logz.io account
where you need to fetch or archive logs in an S3 bucket.

 

##### Delete an S3 configuration from Logz.io

Choose an
[S3 fetcher](https://app.logz.io/#/dashboard/send-your-data/log-sources/s3-bucket)
or
[Archive & restore](https://app.logz.io/#/dashboard/tools/archive-and-restore)
configuration to replace.

Copy the **S3 bucket name** to your text editor,
and make a note of the **Bucket region**.
If this is an S3 fetcher, copy the path **Prefix** as well,
and make a note of the **Log type**.

Delete the configuration.

##### Replace the configuration

If this is for an S3 fetcher, click **Add a bucket**,
and click **Authenticate with a role**.

![S3 fetcher and archive configuration screens](https://dytvr9ot2sszz.cloudfront.net/logz-docs/archive-and-restore/s3-fetcher-and-archive-config-external-id.png)

Recreate your configuration with the values you copied in step 1,
and copy the **External ID** (you'll paste it in AWS later).

##### Set up your new IAM role

Using the information you copied in step 1,
follow the steps in
[_Grant access to an S3 bucket_](#grant-access-to-an-s3-bucket)
(near the top of this page).

Continue with this procedure when you're done.

##### _(If needed)_ Replace other configurations that use this role

If there are other S3 fetcher or Archive & restore configurations
in this account that use the same role,
repeat steps 1 and 2,
and use the role ARN from step 3.

For configurations in other Logz.io accounts,
repeat this procedure from the beginning.
  
 

## Testing IAM Configuration  

After setting up `s3:ListBucket` and `s3:GetObject` permissions, you can test the configuration as follows.
  
 

##### Install s3cmd
  
###### For Linux and Mac:
  
Download the .zip file from the [master branch](https://github.com/s3tools/s3cmd/archive/master.zip) of the s3cmd GitHub repository.
  
###### For Windows:
  
Download [s3cmd express](https://www.s3express.com/download.htm).
  
Note that s3cmd will usually prefer your locally-configured s3 credentials over the ones that you provide as parameters. So, either backup your current s3 access settings, or use a new instance or Docker container.

##### Configure s3cmd
  
Run `s3cmd --configure` and enter your Logz.io IAM user access and secret keys.
  
##### List a required bucket
  
Run `s3cmd ls s3://<BUCKET_NAME>/<BUCKET_PREFIX>/`. Replace `<BUCKET_NAME>` with the name of your s3 bucket and `<BUCKET_PREFIX>` with the bucket prefix, if the prefix is required.
  
##### Get a file from the bucket
  
Run `s3cmd get s3://<BUCKET_NAME>/<BUCKET_PREFIX>/<OBJECT_NAME>`. Replace `<BUCKET_NAME>` with the name of your s3 bucket, `<BUCKET_PREFIX>` with the bucket prefix and `<OBJECT_NAME>` with the name of the file you want to retrieve.
  
  