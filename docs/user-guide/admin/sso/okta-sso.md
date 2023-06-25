---
sidebar_position: 4
title: Single Sign-On with Okta
---

## To set up single sign-on for Okta


### Request SSO access from Logz.io

:::note
Only account admins can request single sign-on access for their accounts.
:::


To kick off this process, send an email to [help@logz.io](mailto:help@logz.io).
Write that you want to set up Okta SAML SSO for Logz.io.
Include these items in the message:

* Your Logz.io [account ID](https://docs.logz.io/user-guide/accounts/finding-your-account-id.html)
* The last six characters of your [account token](https://app.logz.io/#/dashboard/settings/manage-accounts)

The Support team will respond with the connection information you'll need to give in Okta.

### Add Logz.io to Okta

In Okta, click **Admin**.

In the Shortcuts panel (on the right), click **Add Applications**.

On the left side of the window, click **Create New App**.
The "Create a New Application Integration" panel is displayed.

![Create a New Application Integration panel](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/okta/create-a-new-application-integration.png)

Select **Web** from the Platform list, click **SAML 2.0** option, and click **Create**.
The Create SAML Integration page is displayed.

Set your **App name** to "Logz.io". Click **Next** to continue to the Configure SAML tab.

### Paste the SAML information from Support

![SAML settings](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/okta/saml-settings.png)

Paste **Single sign on URL** and **Audience URI** from the Logz.io Support email message.

Don't change **Default RelayState**, **Name ID format**, or **Application username**.

![Attribute Statements](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/okta/attribute-statements.png)

In the Attribute Statements section:

* Set **Name** to "email"
* Select "Unspecified" from **Name format**
* Set **Value** to "${user.email}"

### Configure Okta to send user groups

![Group Attribute Statements](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/okta/group-attribute-statements.png)

In the Group Attribute Statements section:

* Set **Name** to "groups"
* Select "Unspecified" from **Name format**
* Type an expression for the groups that you want to have access to Logz.io in **Filter value**.
This field can't be blank.

### Zip the SAML certificate

On the right side of the page, click **Download Okta Certificate**.

Download the certificate file and zip it.
You'll attach this zip file to your next email to the Support team.

Click **Next**, select **I'm an Okta customer adding an internal app**, and then click **Finish**.

### Get your endpoint information

![SAML setup instructions](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/okta/view-setup-instructions.png)

Browse to the Sign On tab, and then click **View Setup Instructions**.

Copy the **Identity Provider Single Sign-On URL**, and paste this in the email that you'll send to the Support team.

### Send your SAML details to Logz.io

Draft a new [email to Support](mailto:help@logz.io), and include these items:

* Your zipped certificate (from step 5)
* Your Identity Provider Single Sign-On URL (from step 6)

### _(Optional)_ Restrict Logz.io access to specific user groups

![Add group](https://dytvr9ot2sszz.cloudfront.net/logz-docs/access-and-authentication/sso--manage-groups.png)

By default, all Okta users with Logz.io access can sign in to your Logz.io accounts.

You can restrict this access from the [Manage users page](https://app.logz.io/#/dashboard/settings/manage-users) for each of your accounts.
To do this, click **Add group**, and then paste your group's name from Okta.
Do this for each group that should have access to this account.

### Receive confirmation from Support

When Support has created your Okta + Logz.io connection, you're done!
You can start logging in to Logz.io through your Apps portal.
