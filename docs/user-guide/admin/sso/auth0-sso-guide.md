---
sidebar_position: 7
title: Single Sign-On (SSO) for Auth0
---

The following guide helps account admins set up a Single sign-on connection for Auth0.

### Prerequisites: 

To get started, you need the following privileges:

* Access to Auth0
* Permissions to create a new native application in Auth0
* Owner role permissions for the account for which you are creating the Logz.io resource 

### Request SSO access from Logz.io

:::note
Only account admins can request single sign-on access for their accounts. 
To access and use the SSO link that is created for a Logz.io Auth0 integration resource, users must be defined in the associated Auth0 account. 
:::

To kick off this process, send an email to [help@logz.io](mailto:help@logz.io).
Write that you want to set up Auth0 SSO for Logz.io.
Include these items in the message:

* Your Logz.io [account ID](https://docs.logz.io/user-guide/accounts/finding-your-account-id.html)
* The last six characters of your [account token](https://app.logz.io/#/dashboard/settings/manage-accounts)

The Support Team will respond with the connection information you'll need to give in Auth0.


### Create a native application in Auth0

Log into your Auth0 account. Navigate to **Applications > Applications** and create a new **Native** application.

![Auth0 create new app](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/auth0/auth0-create-app.png)

Click on **Settings**, scroll down to the bottom of the page, and click **Advance Settings**. Next, click on the **Certificate** tab and download it in a PEM format. In the next step, you’ll need to email this file to the Logz.io Support Team.

![Auth0 certificate download](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/auth0/auth-cert-download.png)

Click on **Endpoints** tab and copy the SAML Protocol URL. 

![Auth0 copy SAML URL](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/auth0/auth0-copy-url.png)

Save your configuration.

### Send your SAML details to Logz.io

Draft a new [email to Support](mailto:help@logz.io), and include these items:

* Your Certificate (from the previous step).
* Your SAML Protocol URL.


### Activate SAML connection in Auth0

Return to your Native app in Auth0 (**Applications > Applications**), click the **Addons** tab, and toggle SAML2 Web App.

![Auth0 toggle SAML app](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/auth0/auth0-saml-web-app.png)

Click on **Settings**, paste the Single Sign-in URL that Logz.io support Team has provided, and click **Enable** at the bottom of the page.

![Auth0 SAML url](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/auth0/auth0-saml-url.png)

When Support has created your Auth0 + Logz.io connection, you're done!
You can start logging in to Logz.io through your Auth0 account.

### Adding New Auth0 SSO users

New users who weren't a part of your account when you first created the SSO configuration, should apply a first login to Logz.io via the Auth0 platform by navigating to Application > SAML2 Web App > Addon settings.

![Add new users](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/auth0/add-auth-logz.png)