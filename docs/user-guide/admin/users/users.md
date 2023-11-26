---
sidebar_position: 1
title: Manage Users and Roles
---

User permissions are determined by their role and the account to which they belong.

Account Admins can manage users and change user access permissions at any time.

![Manage users](https://dytvr9ot2sszz.cloudfront.net/logz-docs/access-and-authentication/manage-users-demo.png)

You can get to this page
by selecting [**<i class="li li-gear"></i> > Settings > Manage users**](https://app.logz.io/#/dashboard/settings/manage-users)
in the top menu.

:::note
Community plans have a maximum of 50 users.
:::

## Access level per role

You can assign **Read Only**, **User**, **SIEM**, or **Admin** roles. Each role has different access that helps you limit the data, visibility, and abilities shared with other users.

Logz.io observability platform offers several features, each with its own set of permission and access levels:

* [View Log Management permissions and access levels](/user-guide/users/#user-role-permissions-for-log-management)
* [View Metrics permissions and access levels](/user-guide/users/#user-role-permissions-for-metrics-instrastructe-monitoring)
* [View Tracing permissions and access levels](/user-guide/users/#user-role-permissions-for-tracing)
* [View Cloud SIEM permissions and access levels](/user-guide/users/#user-role-permissions-for-cloud-siem)
* [View General settings permissions and access levels](/user-guide/users/#user-role-permissions-for-general-account-settings)

### User role permissions for Log Management

Log Management lets you search and query logs, create alerts, investigate issues, identify patterns, surface errors, and more. This table contains all Log Management features and which user roles can access and use them.


| **Main features**                       | Read Only | User | SIEM | Admin |
|-----------------------------------------|-----------|------|-------|-------|
| View dashboards                         | ✓         | ✓    | ✓     | ✓     |
| View alerts                             | ✓         | ✓    | ✓     | ✓     |
| Create an alert                         |           | ✓    | ✓     | ✓     |
| View alerts Event Management            | ✓         | ✓    | ✓     | ✓     |
| Live tail                               | ✓         | ✓    | ✓     | ✓     |
| Optimizers                              |           | ✓    | ✓     | ✓     |
| Insights                                |           | ✓    | ✓     | ✓     |
| Reports                                 |           | ✓    | ✓     | ✓     |
| Data parsing                            |           |      |       | ✓     |
| Field mapping                           |           |      |       | ✓     |
| Archive and restore                     |           |      |       | ✓     |
| Drop filters                            |           |      |       | ✓     |
| Incident reports                        |           | ✓    | ✓     | ✓     |

###### Additional restrictions

* **Read Only** roles can't create, delete or update visualizations, dashboards, and save searches.
* **Read Only** and **User** roles can't create optimizers.


### User role permissions for Metrics (Instrastructe Monitoring)

Use Infrastructure Monitoring to create and curate dashboards that monitor your system's health and status. This table contains Metrics features, and which user roles can access and use them.


| **Main features**                       | Read Only | User | SIEM | Admin |
|-----------------------------------------|-----------|------|-------|------|
| View dashboards                         | ✓         | ✓    | ✓     |  ✓   |
| Manage tokens                           |           |      |       | ✓    |

###### Additional restrictions

* **Read Only** roles can only view dashboards. They can't create or duplicate them. They can, however, edit existing user-made dashboards.

### User role permissions for Tracing

Logz.io’s Tracing feature gives you the ability to look under the hood at how your microservices interact, and lets you access rich information to help improve performance, investigate, and troubleshoot issues. This table contains all Tracing features, and which user roles can access and use them.


| **Main features**                       | Read Only | User | SIEM | Admin |
|-----------------------------------------|-----------|------|-------|-----|
| View dashboards                         | ✓         | ✓    | ✓     | ✓   |
| Manage tokens                           |           |      |       | ✓   |

### User role permissions for Cloud SIEM

Cloud SIEM (*Security Information and Event Management*) aggregates security logs and alerts across distributed environments to allow your team to investigate security incidents from a single observability platform. This table contains all Cloud SIEM features, and which user roles can access and use them.


| **Main features**                       | Read Only | User | SIEM | Admin |
|-----------------------------------------|-----------|------|-------|------|
| View summary                            | ✓         | ✓    | ✓     | ✓     |
| Event management                        | ✓         | ✓    | ✓     | ✓     |
| View rules                              | ✓         | ✓    |       | ✓     |
| Create rules                            |           | ✓    | ✓     | ✓     |
| Dashboards                              | ✓         | ✓    | ✓     | ✓     |
| Threats overview                        | ✓         | ✓    | ✓     | ✓     |
| Threats intelligent field               | ✓         | ✓    | ✓     | ✓     |
| OpenSearch Dashboards                   | ✓         | ✓    | ✓     | ✓     |
| Reports                                 |           | ✓    | ✓     | ✓     |
| Drilldowns                              |           |      |       | ✓     |
| Lookups                                 |           | ✓    | ✓     | ✓     |
| Incident reports                        |           | ✓    | ✓     | ✓     |


## User role permissions for general account settings

Logz.io general settings allow users to control elements relevant to their accounts, such as passwords, tokens, system status, unified variables, and more. This table contains all general settings, and which user roles can access and use them.

| **Main features**                       | Read Only | User | SIEM | Admin |
|-----------------------------------------|-----------|------|-------|-------|
| Change personal password                | ✓         | ✓    | ✓     | ✓     |
| Change dark/light theme                 | ✓         | ✓    | ✓     | ✓     |
| View token                              |           |      |       | ✓     |
| Manage tokens                           |           |      |       | ✓     |
| View region                             |           |      |       | ✓     |
| Toggle support access                   |           |      |       | ✓     |
| Refresh OpenSearch Dashboards mapping   |           | ✓    | ✓     | ✓     |
| View system status                      | ✓         | ✓    | ✓     | ✓     |
| Notification endpoints                  |           | ✓    | ✓     | ✓     |
| ELK apps                                |           | ✓    | ✓     | ✓     |
| View Unified variables                  | ✓         | ✓    | ✓     | ✓     |
| Edit Unified variables                  |           |      |       | ✓     |
| Manage users                            |           |      |       | ✓     |
| Audit trail                             |           |      |       | ✓     |
| Manage accounts                         |           |      |       | ✓     |
| Usage and billing                       |           |      |       | ✓     |


### Sub account
You can add users directly to a sub account and assign them either an Admin or User role.

Users belonging to a sub account do not have access to any other accounts, unless explicitly added to them.

### User management

#### Add or remove a user

* To add a user,
  click the button **+New user** at the top of the page.

* To delete a user, hover over the item and click **delete** <i class="li li-trash"></i> to delete it. You'll be asked to confirm the deletion.

#### Suspend or unsuspend a user

To suspend or unsuspend a user, hover over the user,
click the **Menu button <i class="li li-ellipsis-v"></i>**, and click **Suspend** or **Unsuspend**. The user's status is changed.

#### Edit role or rename a user

* To change the user's role (Admin/User) rename, hover over the user, click **edit** <i class="li li-pencil"></i>, make your changes, and click **Save**.

* To rename a user, hover over the user, click **edit** <i class="li li-pencil"></i>, make your changes, and click **Save**.