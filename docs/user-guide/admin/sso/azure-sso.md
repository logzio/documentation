---
sidebar_position: 3
title: Single Sign-On With Azure
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Configure Single Sign On for Azure and Logz.io
keywords: [single sign=on, sso, sso setup, sso configuration, secured login, integration, azure]
---

Logz.io offers a quick integration for SSO with Azure.


### Request SSO access from Logz.io

:::note
Only account admins can request single sign-on access for their accounts.
:::


To kick off this process, send an email to [help@logz.io](mailto:help@logz.io).
Write that you want to set up Azure SAML SSO for Logz.io.
Include these items in the message:

* Your Logz.io [account ID](https://app.logz.io/#/dashboard/settings/general)
* The last six characters of your [account token](https://app.logz.io/#/dashboard/settings/manage-accounts)

The Support team will respond with the connection information you'll need to give in Azure.

### Add Logz.io as a gallery application in Azure

Log into your [Azure Portal](https://portal.azure.com/) and follow the instructions in [Azure's docs](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/logzio-cloud-observability-for-engineers-tutorial) for adding the **Logz.io-Microsoft Entra Integration** from the  Gallery.

When you get to the step **Set up single sign-on with SAML**, you'll need the SAML information you received from Logz.io Support's email.

* **Identifier (Entity ID)**.
* **Reply URL (Assertion Consumer Service URL)**.

![information](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/single-sign-in-jul.png)

### Zip the SAML certificate

In your new Azure app, navigate to **Manage > Single sign-on** and select the SAML method. In the SAML Signing Certificate section, find Certificate (Base64), download and zip it.

In the next step, you'll need to email this zip file to the [Logz.io Support team](mailto:help@logz.io).

![SAML Certificate](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/azure-saml-download.png)

Save your configuration.

### Send your SAML details to Logz.io

Draft a new [email to Support](mailto:help@logz.io), and include these items:

* Your zipped SAML Signing Certificate (from the previous step).
* Your SAML-P SIGN-ON ENDPOINT.
  This is your Azure **Login URL**.

  ![Azure SAML-P SIGN-ON ENDPOINT](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/setup-azure-mar24.png)


### Configure Azure to send user groups

Return to the App registrations page in your [Azure Portal](https://portal.azure.com/).
If you don't see Logz.io, click **View all applications**.

Open the **App registrations** service, choose the relevant application from the list, and click **Manifest**.
In the manifest JSON, set groupMembershipClaims to `"All"`.
Click **Save** (at the top of the page).

![groupMembershipClaims Editor](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/azure-sso-app-json-mar.png)

### Additional configuration for users who are in over 150 groups

:::note
Azure’s API requires additional configuration for members of 150 groups.
:::

Azure has some limitations for users who are members of over 150 groups, and requires additional configuration to send the relevant data to Logz.io. To make sure your groups are sent appropriately, follow these steps:

In your Azure Portal, navigate to **[Microsoft Entra ID](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview)** > **[App Registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)**, and open Logz.io's app you've created to sign in with SSO.

Next, navigate to **API Permissions**, and click **Add a permission**.

![Add permission](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/add-permission-mar.png)

Add the three following permissions to your account:

  1. Select the **APIs my organization uses** tab on the right side menu, and click on **Windows Azure Active Directory**. Next, choose **Application permissions** > **Directory.Read.All** and add the permission.

  ![Add read all permission](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/directory-read-all-mar.png)
  
  2. Click **Add a permission**. Under **Microsoft APIs** select **Microsoft Graph**.
  Choose **Application permissions**, and search for **Group**. Choose **Group:ReadAll**, and click Add permissions.

  ![Add group read all permission](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/group-read-all-mar.png)
  
  3. Click **Add a permission**, select **Microsoft APIs** tab and click on **Microsoft Graph** again.
  Choose **Application permissions**, search for **Application**, choose **Application.Read.All**, and click Add permissions.

  ![Add application read all permission](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/application-read-all-mar.png)

Next, navigate to **Certificates & secrets** on the left side menu, and add a **New client secret**. Name the secret, for example, Logz.io Group Access, set the expiration date to the farthest option available, 24 months, and click the **Add** button.

Navigate to **Overview**, located on the left side menu, copy the Application (client) ID and send it with the Secret you've created to **[Logz.io Support team](mailto:help@logz.io)**.

Once your connection has been updated and approved by Logz.io Support team, you and your team should be able to log in to Logz.io via the SSO connection (found in https://myapplications.microsoft.com/) regardless of the number of members in a group.


### _(Optional)_ Restrict access to Logz.io to specific user groups

![Add group](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/azure-manage-users-groups.png)

By default, all Azure users with Logz.io access can sign in to your Logz.io accounts.

You can restrict this access from the [Manage users page](https://app.logz.io/#/dashboard/settings/manage-users) for each of your accounts.

Click **Add group**, and paste the group's **Object ID** for each group that should have access to the account in Logz.io.

To find your **Object ID**, navigate to [your Azure app](https://portal.azure.com/) > [Groups](https://portal.azure.com/#blade/Microsoft_AAD_IAM/GroupsManagementMenuBlade/AllGroups). Open the relevant group and copy the Object ID string.

![ObjectID](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/group-object-id.png)


### Receive confirmation from Support

When Support has created your Azure + Logz.io connection, you're done!
You can start logging in to Logz.io through your Azure Apps portal.
