---
sidebar_position: 4
title: Manage SIEM accounts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn more on managing your SIEM accounts in Logz.io
keywords: [account, manage account, optimization, admin controls, admin, user permissions, permissions, access control, siem, security, security account]
---


## Manage your Cloud SIEM account


#### Add a Cloud SIEM account

You'll find your Cloud SIEM accounts
in the [Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts) page
of your Operations workspace. Scroll down to the bottom of the page to see them.

Click **Add Security account** to open the form.
The number of accounts you can create is listed.

![Add a Cloud SIEM account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/add-security-account11.png)


#### Configure or update a Cloud SIEM account

![Configure a Cloud SIEM account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/config-security-account.png)


Fill in the form:

1. **Name** (or rename) the account.
2. **Enable Cloud SIEM on these accounts** - Select the log accounts to be secured. You'll be giving the security account **read permissions** so it can monitor and enrich the logs.

    Logs are not shipped directly to your Cloud SIEM accounts. Instead, you'll grant read-access to log accounts you want a security account to monitor.

    :::note
    You can add the same log account to multiple Security accounts. It will be monitored by each   Security account independently.
    :::

3. **Automatically pull dashboards, visualizations, and saved searches from these Security accounts** - Select which security accounts you can automatically pull shared objects from. 

  ![Shared security objects](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/add_new-account.gif)

  The security account you're configuring will automatically be able to access the OpenSearch dashboards, visualizations, and saved searches from the source accounts you add to this list, but will *not* have access to the data in these accounts.  
  
  This is helpful if you have multiple main accounts. 
  
  For example: 

  + Instead of creating the same objects for each account, you can just share them! 
  + You can use this process to keep a local backup copy of these data objects. 
  + Create a library of data objects in your main Security account, and then enable client accounts to use objects from your main account.  

#### Save your changes

Click **Create**/**Apply** to save your changes.

When you first add a new account, give it a few minutes to finish setting up.


#### Delete a Cloud SIEM account from your plan 
 
1. In the account details, click the **Delete** icon next to the account name.
  ![delete](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/delete-SIEM.png)   

2. Confirm (or **Cancel**) the action. 
  ![Confirm delete](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/confirm-delete-siem-acct.png)

Logz.io Metrics lets your team curate dashboards to oversee continuous deployment, CI/CD pipelines, prevent outages, manage incidents, and remediate crashes in multi-microservice environments, hybrid infrastructures, and complex tech stacks.

If you're an admin for the main account, you can manage the main account and sub accounts from the [**Manage Accounts**](https://app.logz.io/#/dashboard/settings/manage-accounts) page (**<i class="li li-gear"></i> > Settings > Manage accounts** in the navigation menu).


The Infrastructure Monitoring plan panel is located at the bottom of the **[Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts)** page.

If you don't have an Infrastructure Monitoring account yet,
reach out to your account manager or email [the Sales team](mailto:sales@logz.io).