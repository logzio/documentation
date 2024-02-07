---
sidebar_position: 2
title: Configure SSO access for main and sub accounts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Configure Single Sign On for main and sub accounts at Logz.io
keywords: [single sign=on, sso, sso setup, sso configuration, secured login, integration]
---



SSO (Single sign-on) simplifies access management for your Logz.io account by allowing you to use a single user and identity management tool. Now, you can use your SSO groups to easily manage access for both main and sub accounts within Logz.io, and share data, objects, and more.

:::note
To enable group SSO for your main and sub accounts, contact your account manager or [Logz.io's support team](mailto:help@logz.io).
:::

## Prerequisite

* Admin privileges in your main Logz.io account

* Existing SSO groups created within your SSO provider

![main sso](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/sso-groups-view-all.png)

## Manage main account SSO groups

Admin users can easily create SSO groups for the main account within Logz.io.

To add and assign SSO groups, navigate to [Settings > Manage users](https://app.logz.io/#/dashboard/settings/manage-users) and click the **SSO Groups** tab.

Next, click on **+ New SSO group** button, paste the name of the relevant SSO group created in your SSO provider, and choose the appropriate permissions from the dropdown list. View the detailed list of available permissions and what they include, [here](https://docs.logz.io/docs/user-guide/admin/users/#access-level-per-role).


:::caution Important
To ensure the correct permissions are transferred, use the **exact SSO group name** as declared in your SSO provider.
:::

![roles sso](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/main-sso-configure.png)

These SSO groups will have access to all accounts connected to your main Logz.io account. Users within these groups will enjoy the following abilities:

* Access to all connected accounts
* Search capabilities across all sub accounts
* Sharing of objects between main and sub accounts

For example, in the image below, the **Management-Admins** SSO group has Admin access, enabling search capabilities, and asset sharing on all accounts to its members.

The **Management-Users** SSO group has User access, enabling search capabilities and asset sharing on all accounts.

![example main sso](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/main-sso-all-accounts.png)

:::caution Important
When setting SSO group permissions, you must ensure you didn’t set user permissions. If a user has both SSO group permissions and user permissions, the user permissions **may override** those of the SSO group permissions.
:::

## Manage sub account SSO groups:

Admin users can create SSO groups for sub accounts in Logz.io.

To add and assign SSO groups, navigate to [Settings > Manage users](https://app.logz.io/#/dashboard/settings/manage-users) and click on the **SSO Groups** tab.

Scroll down to the second part of the page, **Sub accounts SSO groups**, and click on **+ New SSO group** button. Next, paste the name of the relevant SSO group created in your SSO provider, choose the [appropriate permissions](https://docs.logz.io/docs/user-guide/admin/users/#access-level-per-role) from the dropdown list, and click the dropdown list to view and choose which sub accounts these users will be able to access.

:::tip
To ensure the correct permissions are transferred, use the **exact SSO group name** as declared in your SSO provider.
:::

![sub account accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/sub-account-sso.png)

Users within these sub account SSO groups will have access to the following abilities:

* Access to connected sub accounts
* Search capabilities across those sub accounts
* Sharing of objects between the sub accounts


For example, in the image below, the **AppDevAdmins** SSO group has Admin access, enabling search capabilities, and asset sharing on the  Dev-App and Prod-App accounts.

The **AppDevUsers** SSO group has User access, enabling search capabilities, and asset sharing on the same accounts.

However, the **SecurityAdmins** SSO group has Admin access, enabling search capabilities, and asset sharing - but only for the **Security** account.


![sub account sso](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/sub-account-detailed-view.png)

## Asset and objects across main and sub accounts

It's important to note that assets created within the main Logz.io account **will be accessible to all sub accounts**. However, sub account users will only see data corresponding to their access logs. 

For example, if a dashboard is created at the main account level analyzing all alerts sent to the account, users with access to sub-account-1 can view the dashboard. However, these users will only see the data that's shared to their specific sub account.

## Edit or delete SSO groups

You can edit some of the elements in your existing SSO groups.

For SSO groups associated with your **main account**, you can change the name and permissions by hovering over the relevant group and clicking the pencil icon on the right. Click Save to apply your changes.

You can change the name, permissions, and account access for SSO groups associated with your **sub accounts**. Hover over the relevant group and click the pencil icon on the right. Click Save to apply your changes.

To delete one or more SSO groups, click the trash can icon. Note that this action can't be undone, and once deleted, all SSO group members will lose access to the relevant accounts and data.

![edit delete sso](https://dytvr9ot2sszz.cloudfront.net/logz-docs/sso-providers/edit-delete-sso.png)