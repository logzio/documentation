---
sidebar_position: 7
title: Audit Trail
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Track activity data in your Logz.io accounts
keywords: [account, manage account, user management, admin controls, admin, user permissions, permissions, access control]
---

The Audit trail page offers account activity data tracking for account admins. You can view various actions in the table- including logging, saving a search, creating alerts, adding users, updating dashboards, and more.

Each action includes information about the user who performed it, such as user ID, name, server IP, geolocation, and the time and date in which the action took place.

![Audit trail screen](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/audit-trail-dashboard.png)

To access the page, navigate to **Settings > [Audit trail](https://app.logz.io/#/dashboard/settings/general/audit-trail)**.

![Audit trail location](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/audit-trail.png)

## View and filter Audit trail

The Audit trail table lets you focus on specific **actions** or **users** in a certain timeframe. 

The **User Name** dropdown menu includes all users connected to the account, and the **Actions** menu shows all of the actions done inside the account. These actions include:

**Admin actions**|**User actions**|
|--|--|
Login info|User saved an object (visualization/dashboard/search)|
Failed login info|User deleted an object|
Changed password|User installed an ELK app|
Reset password|User created a token|
Logz.io Customer Success made authorized changes in the account|User updated a token|
Added user|User deleted a token|
Updated user role|User created a token filter|
Deleted user|User updated a token filter|
Admin changed permissions for Logz.io support access|User deleted a token filter|
Admin created a sub account|User created an alert|
Admin updated a sub account|User updated an alert|
Admin deleted a sub account|User deleted an alert|
||User created an endpoint|
||User updated an endpoint|
||User deleted an endpoint|
||User created a bucket|
||User updated a bucket|
||User deleted a bucket|
||User created S3 archiving|
||User updated S3 archiving|
||User deleted S3 archiving|
||User created a sawmill configuration with Data Parsing|
||User updated a sawmill configuration with Data Parsing|
||User updated field mapping|


:::note
Currently, you can only choose one user and/or one action when filtering.
:::


In addition, you can change your view based on a particular time range to optimize your view. You can also edit the table by adding/removing different columns - click the Columns button and choose the relevant fields.

![Audit trail location](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/edit-audit-trail-view.png)

To export the data, click on the CSV button. The file would include all available fields, including those filtered out in your current view.