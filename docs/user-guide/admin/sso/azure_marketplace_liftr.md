---
sidebar_position: 3
title: Single Sign-On for Azure Pay-As-You-Go Portal Integration
---

Logz.io offers an integration with Azure Marketplace. 
This topic provides guidance for admins to set up SSO for the Logz.io-Azure Portal integration, which enables an SSO link for users who access Logz.io resources via Microsoft Azure Marketplace.

:::note
This guide is for customers using **Azure pay-as-you-go plan**. If you have a different Azure plan, use our [SSO with Azure](https://docs.logz.io/user-guide/users/single-sign-on/azure-sso.html) guide.
:::


### Benefits
The advantages of providing your users access to the Logz.io Azure resource via SSO: 

+ No need to predefine a unique username and password for each user: Any user who has the SSO link can sign in to the application.
+ Better user control: A user must be defined in the Azure account to be able to use the SSO link.

:::tip
Prepare SSO connectivity before setting up the Azure resource for Logz.io. You'll need the credentials you create in this process to set up the resource. 
:::


## Creating SSO connectivity for your Logz.io resource in Azure Active Directory 

You'll create an Azure Active Directory (AD) Enterprise application to enable using SSO to connect to your Logz.io account from your Azure resource. 

### Prerequisites: 
To get started, you need the following privileges:

* Access to Azure Active Directory (AAD)
* Permissions to create a new Enterprise Application
* Owner role permissions for the Azure subscription for which you are creating the Logz.io resource 


To be able to access and use the SSO link that is created for a Logz.io-Azure integration resource, users must be defined in the associated Azure account. 

## Setting up an SSO link for the Logz.io-Azure Portal resource


### Add the Logz.io-Azure Active Directory Integration from the gallery

To configure SSO for the Logz.io resource in the Azure Portal, you need to add the Logz.io - Azure AD Integration from the gallery to your list of managed SaaS apps.

1. Sign in to the Azure Portal using a Microsoft account.
2. In the Azure Portal, in **Logz.io | Overview**, in the **+ Add** menu, select **Enterprise application**.
   ![Enterprise application option](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/liftr-ovrview_enterprise_apps.png)
3. In the Azure Active Directory Gallery, browse to the **Logz.io - Azure AD Integration** application and select it.
4. Rename the integration with a relevant name and click **Create**. (In the steps that follow, we used the name **AD app for a logz.io resource**)
![Rename the integration](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/liftr-rename_logzio-ad_integration.png)

### Copy the Application ID


In **AD app for a logz.io resource | Overview > Properties**, copy the **Application ID** property.
![Copy Application ID](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/liftr-copy_application_id2.png)

### Configure Azure AD SSO

1. In  **AD app for a logz.io resource | Overview > Getting Started**, in **2. Set up single sign on**, click **Get started** to open **Single sign-on**.
![Set up SSO](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/liftr-set-up_sso.png)
2. In **AD app for a logz.io resource | Single sign-on**, select the **SAML** method.
![Select SAML SSO method](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/liftr-select_saml.png)

### Basic SAML configuration   

1. In **AD app for a logz.io resource | SAML-based Sign-on**, click **Edit** to open the **Basic SAML Configuration** panel.
![Edit basic SAML](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/liftr-edit_basic_saml.png)

2. In the **Identifier (Entity ID)** text box, type a value using the pattern `urn:auth0:logzio:*`: Replace the `*` with the **Application ID** you copied in procedure 2, and click the **Default** option. 

3. In the **Reply URL (Assertion Consumer Service URL)**, text box, type a URL using the pattern `https://logzio.auth0.com/login/callback?connection=`: Replace `CONNECTION_NAME` with the **Application ID** you copied in procedure 2.

4. Click **Save** at the top of the panel.
![Set SML](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/liftr-basic-saml-config.png) 

### Configure the user assignment option    

In **AD app for a logz.io resource|Properties  (Manage > Properties)**, set **User assignment required?** to **No** and click **Save**.  
This step enables users with access to the SSO link to sign in to Logz.io via Microsoft Azure Portal, without requiring that you predefine each user in Active Directory.

This option allows any user who is defined under Active Directory to use the SSO link, instead of requiring that you define specific access rights for each user through the AD app that was just created. 

If you don't want to configure this option, your organization will have to assign specific access rights to Logz.io for each user.

![User assignment not required](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/liftr-user-assignment-required-no.png)


## Enable SSO for your Logz.io resource via Azure Active Directory

When you create a Logz.io account, use the AD app you created for the Logz.io resource to enable single sign-on with Azure Active Directory.  

The Logz.io AAD app resource name is automatically populated as you type.
![Select your Logz AAD app to enable SSO](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/liftr-select-logz-aad-app.png)


The SSO link is displayed when you sign into your Logz.io resource.  
![One click SSO to Logz.io](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/azure/liftr-logzio-sso-link.png)
Click the link to access your account in Logz.io. 

If you don't configure SSO while you are creating the Logz.io resource, you can configure it later via the Single sign-on blade.

You'll have to configure your logs in Azure to ensure they're sent to Logz.io.