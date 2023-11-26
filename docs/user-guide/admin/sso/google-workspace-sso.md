---
sidebar_position: 8
title: Single Sign-On with Google Workspace
---

Logz.io offers a quick integration for SSO with Google Workspace.


### Request SSO access from Logz.io

:::note
Only account admins can request single sign-on access for their accounts.
:::

To set up your Google Workspace SSO, you'll first need to email [help@logz.io](mailto:help@logz.io) and write that you want to set up Google Workspace SAML SSO for Logz.io.

Include these items in the message:

* Your Logz.io [account ID](https://docs.logz.io/user-guide/accounts/finding-your-account-id.html)
* The last six characters of your [account token](https://app.logz.io/#/dashboard/settings/manage-accounts)

The Support team will respond with the connection information needed to set up your Google Workspace SSO.

### Set a custom SAML app in Google Workspace

Log into your [Google Workspace panel](https://admin.google.com/AdminHome).

In the sidebar, navigate to Apps > Web and mobile apps. Click on **Add app** and choose the **Add custom SAML** app option.

![Create SAML app](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/google/google-add-saml-app.png)

Name your application and click **Continue**. In the **Google Identity Provider details** screen, copy the **Entity ID** and download the certificate.

![Download certificate](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/google/download-certificate.png)

Continue to the next screen. Enter the ACS URL and Entity ID given to you by Logz.io support; change the Name ID format to **EMAIL**, and set the Name ID to **Basic Information > Primary email**.

![Set entity ID](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/google/service-provider.png)

Continue to the final screen. Edit the Google Directory attributes to **Basic Information - Primary email**, and set App attributes to **email**.

![Set entity ID](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/google/attribute-mapping.png)

Click on Finish to add the custom SAML app.

### Send your SAML details to Logz.io

Draft a new [email to Support](mailto:help@logz.io), and include these items:

* Your zipped SAML Signing Certificate (from the previous step).
* Your SAML SIGN-IN URL.

When Support has received the information and created your Google Workspace + Logz.io connection, you’re done! You can start logging in to Logz.io through your Google Workspace account.



## Google Workspace SSO groups


When [creating access groups for Google Workspace](https://support.google.com/a/answer/9050643?hl=en), you need to add a custom attribute to connect it to your Logz.io SAML application.

First, **[add a custom attribute](https://support.google.com/a/answer/6208725?hl=en)** and link it to your SAML app.

Open your SAML app, navigate to the **SAML attribute mapping** section, and click **Configure SAML attribute mapping**.

In the **Attributes** section, add the custom attribute you've just created and set the app attribute of your choice.

Next, you can add Group membership information by selecting the relevant groups from your account.

:::note
When using a Custom Attribute, you must update **every user** manually with a string.
:::

![Set group SSO](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/google/google-sso-saml-group.png)

Click **Save** to apply the changes. 

<!-- Next, configure the groups attribute to be sent across as part of the SAML login.

![Set group attribute](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/google/sent-group-sso.png) -->