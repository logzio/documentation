---
sidebar_position: 6
title: Manage the Shared SIEM Repository
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn about shared SIEM Repository and how to manage it 
keywords: [account, manage account, siem, security, admin controls, admin, user permissions, permissions, access control]
---

## About the shared SIEM Repository 

Build, prepare, and test your security content in a single SIEM account, set it as the shared SIEM Repository, and share the content in the Repository with your other SIEM accounts.

The Repository acts as a centralized resource for all your SIEM content. When you set up a shared Repository, you can configure your other SIEM accounts to pull dashboards, visualizations, saved searches, and [private security feeds from it. 

All new SIEM accounts automatically pull from the shared Repository: You can manually disable access to the shared Repository for any SIEM account.

When you change which account is defined as the Repository, by default, the change creates an automatic dependency for all the existing SIEM accounts. 

If you don't have a Repository set, the Repository status is grayed out, with a link to **Set repository account**. 

![Setting a Repository, starting from 1 account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/repo-setup_start_from_1acct.gif)


## Set a shared Repository account

To define a Repository account, you must have at least two related Cloud SIEM accounts.

To configure the shared Repository, in **Settings > Manage accounts**, navigate to your Cloud SIEM Plan, and **Set repository account**.


![Set a shared SIEM Repository](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/repo_set-account.png)

Select an existing account to be the shared Repository account.
![Pick a designated Repo](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/repo_picklist.gif) 

Configure the accounts that can pull SIEM content from the shared Repository and **Save** or **Cancel** your change. 
![Set a shared SIEM Repository ](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/repo_dependent_accts.png)

After you set the Repository, it's flagged with the Repository icon <!--<i class="li li-repository"></i> -->in the list of Security accounts, and the **Repository account** status changes to display the Repository name.  
![Configured account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/repo_all_set.png)


## Manage Repository dependencies

### View which accounts are associated with the Repository

Do one of the following to check Repository dependencies: 

- Open the account details to check if the account is associated with the SIEM Repository.
- Open the **Repository account setup** screen to view which SIEM accounts pull from the Repository.
    ![View the Repository's dependent accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/repo_view_dependant_accts.gif)

### Set dependent accounts and manage access to the Repository

You can add or remove the Repository dependency for a single account when you view the account's detaild, or you can   open the **Repository account setup** screen to edit which accounts pull from the Repository.

## Reset a Repository account

Use the **Reset** operation to change the shared Repository back to a regular Cloud SIEM account. Dependent accounts will no longer be able to pull content from that account.

When you replace the SIEM Repository, you automatically create dependencies for your other SIEM accounts: They will pull content from the new Repository, unless you manually remove the dependency for the Repository.

In the **Repository account setup** screen, click **Reset**. 

To replace the Repository account, select a different SIEM account to set as the Repository, and **Save** or **Cancel** the change. 



## Delete a Repository 

To delete your current Repository, you must first reset it to remove the dependencies for the other SIEM accounts. Once the Repository status is removed, the account can be deleted.

![Delete the existing Repository account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/repo_reset-delete.gif)

## Private feeds in the shared Security Repository

Define a [private feed](https://docs.logz.io/docs/user-guide/cloud-siem/threat-intelligence/ioc-types/) once in your SIEM Repository and share it with the relevant Security accounts. You can find more information on how to include private feeds in your Repository in [Adding a private feed](https://docs.logz.io/docs/user-guide/cloud-siem/threat-intelligence/private-feeds/).