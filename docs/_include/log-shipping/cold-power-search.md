1. Navigate to your AWS account and search for S3.

  ![Select S3](https://dytvr9ot2sszz.cloudfront.net/logz-docs/power-search/select-s3.png)
2. Choose the relevant bucket on which you want to apply these permissions. **It should be the same bucket you've used when setting up your S3 permissions.** Once inside, click on Permissions, scroll down to **Bucket policy** and click on **Edit**.
  ![Select S3](https://dytvr9ot2sszz.cloudfront.net/logz-docs/power-search/permission-policy.png)
3. Paste the following code inside the policy. **Replace the `XXX` with your bucket's name.**

  *If you don't have an existing policy, paste this code inside the editor. Otherwise, add this code to the bottom of the page.*

  ```yaml
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Principal": {
                  "AWS": "arn:aws:iam::406095609952:user/search-archive-restore-user"
              },
              "Action": [
                  "s3:GetObject",
                  "s3:ListBucket"
              ],
              "Resource": [
                  "arn:aws:s3:::XXX", #replace XXX with your bucket's name
                  "arn:aws:s3:::XXX/*" #replace XXX with your bucket's name
              ]
          }
      ]
  }
  ```


  ![Edit bucket policy](https://dytvr9ot2sszz.cloudfront.net/logz-docs/power-search/edit-bucket-policy.png)
4. Click on **Save changes** to apply the new policy. It might take a few minutes for Logz.io to identify the new policy.