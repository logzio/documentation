---
sidebar_position: 1
title: Single Sign-On
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Configure Single Sign On for Logz.io
keywords: [single sign=on, sso, sso setup, sso configuration, secured login, integration]
---

Single sign-on (SSO) lets you manage access to your Logz.io account from a single user and identity management tool.


## What is SSO?

Single Sign-On (SSO) allows you to manage access to your Logz.io account using a single user and identity management tool. SSO enables users to authenticate and sign in to various services with one set of credentials. This eliminates the need for multiple usernames and passwords for different services, streamlining access management. Implementing SSO on your account not only enhances convenience for your users but also boosts security for your company.


## How is access managed with SSO?

:::caution important
To use the ‘Sign in with SSO’ button on Logz.io’s login page, **your initial login** must be performed through the SSO identity service provider.
:::

When you enable SSO on your Logz.io account, authentication is managed by your identity provider. You can control user access to Logz.io by expanding or restricting permissions, but you cannot add or remove users directly within Logz.io.

All authenticated users will have access to your account. Existing users will maintain their current permission levels unless you configure groups to modify access. 

**Once a user logs in through your portal, they can use SSO to access Logz.io with their email domain, even if their email hasn’t been pre-added to the Logz.io account.**


## How SSO groups work

SSO groups enable you to map, monitor, and manage access levels for multiple users in your organization efficiently. By creating groups, you can assign **User**, **Expert User**, **Admin**, or **Read only** permissions to all members within the group with a single setup, allowing for quick and easy changes to permission levels.

### Setting Up SSO Groups:

1.	Create a group in your SSO provider and add users to the group.
2.	Add the Group in Logz.io. Go to [Settings > Manage Users > Groups](https://app.logz.io/#/dashboard/settings/manage-users) in your Logz.io account and add the group.
3.	Assign the group’s permission level to **Read only**, **User**, **Expert User**, or **Admin**.

### If you don't have any groups:


If you don't configure any groups, all users who authenticate with your identity provider will be able to access your Logz.io account.

The first time a new user logs in, they get **User** access. Existing admins can edit each user and change their access type to **Admin**, **Expert User**, or **Read only** access.

Existing users will retain their current level of access.

### If you have groups:

As soon as you configure your first group, only users who are part of that SSO group will be able to log in to this account.

Each group can have **Admin**, **User**, **Read only**, **Expert User**, or **Configured per user** permissions.

Permissions are set at the group level unless a group setting is **Configured per user**.
Users who are part of multiple groups will get the highest permissions set.

For example, if someone is a member of both a **User** group and an **Admin** group,
they'll receive **Admin** permissions.

:::note
Multiple accounts can use the same group, but **group must be added to each account individually**. For example, if you have created a group on your main account, you'll need to re-create it on your sub accounts to grant its users the relevant permissions. 
**Otherwise, you won't be able to switch between the accounts.**
:::


## Available identity providers

Logz.io can integrate with a number of SSO providers.
To get started, follow the instructions for your provider:

* [Single sign-on (SSO) for Auth0](https://docs.logz.io/docs/user-guide/admin/sso/auth0-sso-guide/)
* [Single sign-on for Azure pay-as-you-go Portal integration](https://docs.logz.io/docs/user-guide/admin/sso/azure_marketplace_liftr/)
* [Single sign-on with AWS](https://docs.logz.io/docs/user-guide/admin/sso/aws-sso/)
* [Single sign-on with Azure](https://docs.logz.io/docs/user-guide/admin/sso/azure-sso/)
* [Single sign-on with Google Workspace](https://docs.logz.io/docs/user-guide/admin/sso/google-workspace-sso/)
* [Single sign-on with Okta](https://docs.logz.io/docs/user-guide/admin/sso/okta-sso/)
* [Single sign-on with OneLogin](https://docs.logz.io/docs/user-guide/admin/sso/onelogin-sso/)



Logz.io can integrate with other SSO providers.
If you don't see your provider on the list,
send an email to [help@logz.io](mailto:help@logz.io).
Write that you want to set up SSO for Logz.io,
and include your Logz.io account ID in the message.
