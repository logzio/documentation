---
sidebar_position: 1
title: Single Sign-On


---

Single sign-on (SSO) lets you manage access to your Logz.io account
from a single user and identity management tool.

## What is SSO?

SSO is a way to authenticate and sign in to different services
with the same credentials.
With SSO, users don't need to remember
different usernames and passwords for each service,
and you can manage access to all your services from one source.
Enabling SSO on your account is more convenient for your users
and more secure for your company.

## How is access managed with SSO? {#how-is-access-managed-with-sso}

:::note
To use the 'Sign in with SSO' button on Logz.io's login page, **your initial login** should be done via the SSO identity service provider.
:::

When you enable SSO on your account,
you're configuring Logz.io to hand off authentication
to your identity provider.
You'll be able to expand or restrict a user's access to Logz.io,
but not add or remove users from within Logz.io.

All authenticated users will have access to your account, and existing users will retain the permission levels they had before SSO was enabled, unless you configure groups.

**Once a user logs via your portal they can use SSO to log to Logz.io using their email domain, even if their email hasn't been added to Logz.io's account.**


## How SSO groups work

SSO groups help you map, monitor, and edit access levels across multiple users in your organization. You can apply **User**, **Admin**, or **Read only** level permissions to all users in the group with a single set up, and change permission levels quickly and easily.


* Create a group in your SSO provider and add the users to the groups. 
* Add the group in your Logz.io account from **<i class="li li-gear"></i> Settings > [Manage users > Groups tab](https://app.logz.io/#/dashboard/settings/manage-users)**.
* Set the permission level for the group to **Read only**, **User**, or **Admin**.

### If you don't have any groups

If you don't configure any groups,
all users who authenticate with your identity provider
will be able to access your Logz.io account.

The first time a new user logs in,
they get **User** access.
Existing admins can edit each user and change their access type to **Admin** or **Read only** access.

Existing users will retain their current level of access.

### If you have groups

As soon as you configure your first group,
only users who are part of that SSO group will be able to log in to this account.

Each group can have **Admin**, **User**, **Read only**, or **Configured per user** permissions.

Permissions are set at the group level unless a group setting is **Configured per user**.
Users who are part of multiple groups will get the highest permissions set.

For example, if someone is a member of both a **User** group and an **Admin** group,
they'll receive **Admin** permissions.

:::note
Multiple accounts can use the same group, but **the group needs to be added to each account separately**.  So, for example, if you have created a group on your main account, you'll need to re-create it on your sub accounts to provide its users the relevant permissions. 
**Otherwise, you won't be able to switch between the accounts.**
:::


## Available identity providers

Logz.io can integrate with a number of SSO providers.
To get started, follow the instructions for your provider:

* [Single sign-on (SSO) for Auth0](https://docs.logz.io/user-guide/users/single-sign-on/auth0-sso-guide.html)
* [Single sign-on for Azure pay-as-you-go Portal integration](https://docs.logz.io/user-guide/users/single-sign-on/azure_marketplace_liftr.html)
* [Single sign-on with AWS](https://docs.logz.io/user-guide/users/single-sign-on/aws-sso.html)
* [Single sign-on with Azure](https://docs.logz.io/user-guide/users/single-sign-on/azure-sso.html)
* [Single sign-on with Google Workspace](https://docs.logz.io/user-guide/users/single-sign-on/google-workspace-sso.html)
* [Single sign-on with Okta](https://docs.logz.io/user-guide/users/single-sign-on/okta-sso.html)
* [Single sign-on with OneLogin](https://docs.logz.io/user-guide/users/single-sign-on/onelogin-sso.html)



Logz.io can integrate with other SSO providers.
If you don't see your provider on the list,
send an email to [help@logz.io](mailto:help@logz.io).
Write that you want to set up SSO for Logz.io,
and include your Logz.io account ID in the message.
