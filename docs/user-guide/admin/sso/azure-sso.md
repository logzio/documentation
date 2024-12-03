---
sidebar_position: 3
title: Single Sign-On With Azure
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Configure Single Sign On for Azure and Logz.io
keywords: [single sign=on, sso, sso setup, sso configuration, secured login, integration, azure]
---

Logz.io offers seamless integration for Single Sign-On (SSO) with Azure. Follow these steps to set up SSO for your Logz.io account.



### Request SSO access from Logz.io

:::note
Only account admins can request single sign-on access for their accounts.
:::

To kick off this process, send an email to [help@logz.io](mailto:help@logz.io).
Write that you want to set up Azure SAML SSO for Logz.io and include the following details:

* Your Logz.io [account ID](https://app.logz.io/#/dashboard/settings/general)
* The last six characters of your [account token](https://app.logz.io/#/dashboard/settings/manage-accounts)

The Support team will respond with the connection information you'll need to input in Azure.

### Add Logz.io as a gallery application in Azure

Log into your [Azure Portal](https://portal.azure.com/) and follow the instructions in [Azure's docs](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/logzio-cloud-observability-for-engineers-tutorial) to add the **Logz.io - Microsoft Entra Integration** from the Gallery.






When you get to the step **Set up single sign-on with SAML**, use the SAML information provided by Logz.io Support:

* **Identifier (Entity ID)**.
* **Reply URL (Assertion Consumer Service URL)**.

![information](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/basic-saml-configuration.png)

### Zip the SAML certificate



In your Azure app, navigate to Manage > Single sign-on and select the SAML method. Download the Certificate (Base64) and zip it. Email this zip file to the Logz.io Support team.

In your new Azure app, navigate to **Manage > Single sign-on** and select the SAML method. Download the Certificate (Base64) and zip it. Email this zip file to the [Logz.io Support team](mailto:help@logz.io).


![SAML Certificate](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/download-saml-jul3.png)

Save your configuration and continue.

### Send your SAML details to Logz.io

Draft a new [email to Support](mailto:help@logz.io), and include:

* Your zipped SAML Signing Certificate (from the previous step).
* Your Azure Login URL (SAML-P SIGN-ON ENDPOINT)

![Azure SAML-P SIGN-ON ENDPOINT](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/setup-app-name-jul3.png)


### Configure Azure to send user groups

Go to the App registrations page in your Azure Portal. If Logz.io is not visible, click **View all applications**. Open the App registrations service, choose the relevant application, and click **Manifest**. 

Set `groupMembershipClaims` to `"All"` in the JSON manifest and save your configuration.


![groupMembershipClaims Editor](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/manifest-jul3.png)

### Additional configuration for users who are in over 150 groups

:::note
Azure’s API requires additional configuration for members of 150 groups.
:::

Azure has limitations for users who are members of over 150 groups, which requires additional configuration. To ensure proper data transmission, follow these steps:

Navigate to **[Microsoft Entra ID](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview)** > **[App Registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)** and open the Logz.io app.

Next, navigate to **API Permissions**, and click **Add a permission**.

Add the three following permissions to your account:

  1. Select the **APIs my organization uses** tab on the right side menu, and click on **Windows Azure Active Directory**. Next, choose **Application permissions** > **Directory.Read.All** and add the permission.

  ![Add read all permission](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/add-permission-jul3.png)
  
  2. Click **Add a permission**. Under **Microsoft APIs** select **Microsoft Graph**.
  Choose **Application permissions**, and search for **Group**. Choose **Group:ReadAll**, and click Add permissions.

  ![Add group read all permission](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/add-pemission-2-jul3.png)
  
  3. Click **Add a permission**, select **Microsoft APIs** tab and click on **Microsoft Graph** again.
  Choose **Application permissions**, search for **Application**, choose **Application.Read.All**, and click Add permissions.

  ![Add application read all permission](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/add-permission-group-jul3.png)

Next, navigate to **Certificates & secrets** on the left side menu, and add a **New client secret**. Name the secret, set the expiration date to the farthest option available, 24 months, and click the **Add** button.

Navigate to **Overview**, located on the left side menu, copy the **Application (client) ID** and send it with the Secret you've created to **[Logz.io Support team](mailto:help@logz.io)**.

Once your connection has been updated and approved by Logz.io Support team, you and your team should be able to log in to Logz.io via the SSO connection (found in [Apps dashboard](https://myapplications.microsoft.com/)) regardless of the number of members in a group.


### _(Optional)_ Restrict access to Logz.io to specific user groups

![Add group](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/azure-manage-users-groups.png)

By default, all Azure users with Logz.io access can sign in to your Logz.io accounts.

To restrict access, navigate to the [Manage users page](https://app.logz.io/#/dashboard/settings/manage-users) for each account, click **Add group**, and paste the group's **Object ID**.

Find your **Object ID** in [your Azure app](https://portal.azure.com/) > [Groups](https://portal.azure.com/#blade/Microsoft_AAD_IAM/GroupsManagementMenuBlade/AllGroups). Open the relevant group and copy the Object ID string.

![ObjectID](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/security-jul3.png)



### Receive confirmation from Support

Once the Support team confirms the Azure + Logz.io connection, you can log in to Logz.io through your Azure Apps portal.
