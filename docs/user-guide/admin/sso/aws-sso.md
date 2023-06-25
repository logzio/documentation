---
sidebar_position: 8
title: Single Sign-On with AWS
---

Logz.io offers a quick integration for SSO with AWS.


## To set up single sign-on for AWS


### Request SSO access from Logz.io


:::note
Only account admins can request single sign-on access for their accounts.
:::

To set up your AWS SSO, you'll first need to email [help@logz.io](mailto:help@logz.io) and write that you want to set up AWS SAML SSO for Logz.io.

Include these items in the message:

* Your Logz.io [account ID]({{site.baseurl}}/user-guide/accounts/finding-your-account-id.html)
* The last six characters of your [account token](https://app.logz.io/#/dashboard/settings/manage-accounts)

The Support team will respond with the connection information needed to set up your AWS SSO.

### Set a custom SAML app in AWS

Log into your [AWS SSO dashboard](https://us-east-1.console.aws.amazon.com/singlesignon/identity/home).

Click on **Applications** located on the left-hand menu. Then, click on **Add a new application** > **Add a custom SAML application**.

![Create SAML app](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/aws/create-saml-app.gif)

Name your application and give it a short description. Then, download the **AWS SSO certificate**.

![Download certificate](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/aws/export-certificate.png)

Under **Application properties**, enter the **Application start URL** given to you by Logz.io, and set the **Session duration** to 12 hours. 

![Download certificate](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/aws/application-properties-aws.png)

Next, in **Application metadata**, click on the link located underneath the browse button. Enter the ACS URL and Application SAML audience given to you by Logz.io support.

![Set entity ID](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/aws/application-metadata.gif)

Click on **Save changes** to create your app.

### Send your SAML details to Logz.io

Draft a new email to Support, and include these items:

* Your zipped SAML Signing Certificate.
* Your AWS SSO sign-in URL.

![SAML details](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/aws/aws-sso-metadata.png)

When Support has received the information and created your AWS + Logz.io connection, you'll receive confirmation that your AWS SSO is ready to go, and you can start logging in to Logz.io through your AWS account.

### Assign users to Logz.io's SSO connection

In your main SAML application you've just created, navigate to the **Assigned users** tab and click on **Assign users**. Here you can choose and add all relevant users from your organization who can use your new SSO connection.

:::note
Users must also have a Logz.io account to use the new SSO feature.
:::

![Assign users](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/aws/assign-users.png)
