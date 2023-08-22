---
sidebar_position: 6
title: Single Sign-On with OneLogin
---


### Request SSO access from Logz.io

:::note
Only account admins can request single sign-on access for their accounts.
:::

To kick off this process, send an email to [help@logz.io](mailto:help@logz.io).
Write that you want to set up OneLogin SAML SSO for Logz.io.
Include these items in the message:

* Your Logz.io [account ID](https://docs.logz.io/user-guide/accounts/finding-your-account-id.html)
* The last six characters of your [account token](https://app.logz.io/#/dashboard/settings/manage-accounts)

The Support team will respond with the connection information you'll need to give in OneLogin.

### Add Logz.io to OneLogin

In the OneLogin top menu, browse to **Apps > Add Apps**.

In the Find Applications page, search for "SAML Test Connector". Select **SAML Test Connector (Advanced)** from the apps list.

On the Configuration page, set the **Display Name** to "Logz.io" and click **Save**.

### Paste the SAML information from Support

Click the **Configuration** tab.
Fill in these details from the Logz.io Support email message:

* In **Audience**, paste _Audience URI_ from the email
* In **Recipient**, paste _Single sign on URL_ from the email
* In **ACS (Consumer) URL Validator**, paste `[a-z]{5}:\/\/[a-z.0]{16}\/[a-z]{5}\/[a-z?=-]*`
* In **ACS (Consumer) URL**, paste _Single sign on URL_ from the email

### Set OneLogin to pass email parameter to Logz.io

![Parameters tab](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/onelogin/parameters-tab-add-parameter.png)

In the Parameters tab, click **Add parameter**. The _New Field_ dialog is displayed.

![New Field dialog](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/onelogin/new-field-modal.png)

Fill in these details:

* In **Field name**, type "email"
* In the Flags section, select **Include SAML assertion**

Click **Save** to continue to the next panel.
Select "Email" from the **Value** list, and click **Save** again to go back to the Parameters page.

Click **Save** (in the upper right corner of the page).

### Zip the SAML certificate

Click the **SSO** tab.

Under X.509 Certificate, click **View Details**. The Standard Strength Certificate page is shown.

![X.509 certficiate details](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/onelogin/x509-certificate-details.png)

Download the file and zip it. You'll attach this zip file to an email to the Support team.

Click <i class="fas fa-long-arrow-alt-left"></i> to return to the SSO tab.

### Get your endpoint information

In the SSO tab, copy the **SAML 2.0 Endpoint (HTTP)**.
Paste this in the email that you'll send to the Support team.

### Send your SAML details to Logz.io

Draft a new [email to Support](mailto:help@logz.io).
Write that you want to set up OneLogin SSO, and include these items in the message:

* Your Logz.io account ID
* Your zipped certificate (from step 4)
* Your SAML 2.0 Endpoint (from step 5)

### _(Optional)_ Restrict Logz.io access to specific user groups

![Add group](https://dytvr9ot2sszz.cloudfront.net/logz-docs/access-and-authentication/sso--manage-groups.png)

By default, all OneLogin users with Logz.io access can sign in to your Logz.io accounts.

You can restrict this access from the [Manage users page](https://app.logz.io/#/dashboard/settings/manage-users) for each of your accounts.
To do this, click **Add group**, and then paste your group's name from OneLogin.
Do this for each group that should have access to this account.

### Receive confirmation from Support

When Support has created your OneLogin + Logz.io connection, you're done!
You can start logging in to Logz.io through your Apps portal.
