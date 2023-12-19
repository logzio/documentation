---
sidebar_position: 1
title: Manage Accounts
---


Each Logz.io plan starts with a main account, and you can expand your account to send additional logs, data, metrics, and so on.

The following guide will help you get familiarized with your Logz.io account, understand how to use it, and provide some additional tips and tricks.



## Configuration options

There are several different configurations you can apply to your account, including:

### Access control (Pro and Enterprise plans)

You can control access to different sets of data by shipping your logs to sub accounts, each with its own set of users. You can also use account default permissions to determine who can access and read the data. [Manage sub accounts](https://docs.logz.io/user-guide/accounts/manage-the-main-account-and-sub-accounts.html).

### Flexible volume

You can make the most of your plan’s indexing capacity by switching to flexible volume. Flexible volume makes it easier to ensure that accounts don’t max out their indexing capacity. [Explore flexible volume options](https://docs.logz.io/user-guide/accounts/flexible-volume.html).


:::note
You can include up to 200 sub accounts when flexible volume is enabled. To add more sub accounts, you’ll have to disable the flexible volume option.
:::

### Long-term storage

Optimizers are great for analyzing long-term patterns and trends on aggregated data.

You can use [data optimizers](https://docs.logz.io/user-guide/optimizers/configure-optimizers.html) to copy select data from your logs and store them long-term in a timeless account. Data stored in timeless accounts is easily searched and continuously available without requiring additional steps to restore the data. [Explore timeless accounts](/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts#timeless).

### Archive and restore data

You can connect your Logz.io accounts to an S3 bucket or Azure Blob Storage to archive your logs. [Explore archiving options](https://docs.logz.io/user-guide/archive-and-restore/).

Before searching archived data, you’ll need to restore it to its own temporary account. [Explore data restoring options](https://docs.logz.io/user-guide/archive-and-restore/restore-archived-logs.html).

### Two Factor Authentication

You can add an extra layer of security to your Logz.io account by enabling the Two Factor Authentication (2FA) toggle. 

2FA requires two forms of identification to access the account, and you can choose the method that works for you, whether it's a physical token, SMS verification, phone-call-based authentication, or an authenticating app.

Once you toggle the 2FA option, you'll receive an email guiding you on setting up your two-factor authentication.

![2fa toggle](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/2fa-toggle.png)


## Your account dictionary


| Settings | Description |
|---|---|
| **Token** | The default [token](/user-guide/tokens/) for the account. Each account has a set of different tokens which you can use to configure shippers, send data to your account, allow access, and more. Keep these tokens secure. |
| **Account name** | Your account name. You can edit and update it at any time. |
| **Total daily volume** | The maximum volume of logs/data you can ship per calendar day. The index resets every day at midnight (00:00 UTC). |
| **Retention** | The number of days your data is kept in storage. _Note that retention is measured in days, not hours. Retention of 2 days allows you to view logs from yesterday to today, and it's not the equivalent of 48 hours._  |
| **Save account utilization metrics** | You can enable this option to log [account utilization metrics](/docs/user-guide/admin/account-volume-optimization/manage-account-usage/#what-are-account-utilization-metrics). Depending on the required granularity, metrics can be calculated every 10, 30, or 60 minutes. Utilization data is stored in a separate index as the log type: `logzio_account_utilization`. |
| **Save log size** | Adds a [new field](/docs/user-guide/admin/account-volume-optimization/manage-account-usage/#what-happens-when-i-save-log-size) to incoming logs. This new field is called `LogSize`, and it contains the log size in bytes. |
| **Use objects from the selected accounts** | Gives the account access to OpenSearch Dashboards objects (dashboards, visualizations, saved searches) stored in other accounts under the same plan. |

## Manage your accounts

Account admins have various options when it comes to managing the account. For further information, check out the following guides:

* [Manage your **Log Management** account](/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts#logs)
* [Manage your **Cloud SIEM** account](/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts#siem)
* [Manage your **Infrastructure Monitoring** (Metrics) account](/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts#metrics)
* [Manage your **Distributed Tracing** account](/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts#tracing)
* [Manage your **Timeless** account](/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts#timeless)