1. Click **+ Add a bucket**
2. Select your preferred method of authentication - an IAM role or access keys.

The configuration wizard will open.

3. Select the hosting region from the dropdown list.
4. Provide the **S3 bucket name**
5. _Optional_ You have the option to add a prefix.
6. Choose whether you want to include the **source file path**. This saves the path of the file as a field in your log.
7. **Save** your information.

![S3 bucket IAM authentication wizard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/s3-add-bucket.png)
![S3 bucket keyaccess authentication wizard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/key-access-config-basic.png)

:::note
Logz.io fetches logs that are generated after configuring an S3 bucket.
Logz.io cannot fetch old logs retroactively.
:::

