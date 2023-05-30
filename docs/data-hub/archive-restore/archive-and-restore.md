---
sidebar_position: 5
---


# Archive & Restore



Archiving provides a cost-effective solution for long-term storage of logs that don't need to be instantly searchable. You can configure Logz.io to archive logs to an AWS S3 bucket or a Microsoft Azure Storage account.

When you need to investigate old logs after they have expired from your account, you can restore them to a temporary account with no additional storage costs.

:::note
Restored accounts are complimentary, and do not count against your daily log volume.
:::

To get to the **Archive and restore** page, select **Data Hub > Archive and restore**.

![Navigate to Archive and Restore](https://dytvr9ot2sszz.cloudfront.net/logz-docs/archive-and-restore/archive-and-restore-menu.png)






## Overview


![Archive and restore](https://dytvr9ot2sszz.cloudfront.net/logz-docs/archive-and-restore/azure-aws-archive.png)

Archive configuration
: You can configure Logz.io to archive your logs to either an AWS S3 bucket or a Microsoft Azure Storage container. [Learn more

Restore data
: Re-ingest up to 24 hours of archived logs. Restoring data might require additional permissions. [Learn more

Restored accounts
: Data is restored to a temporary account. The list of Restored accounts includes information about who made the request and its status. [Learn more



### Known limitations

Each account (or sub-account) should archive to a separate S3 bucket.

The maximum amount of data that can be restored is equal to your account’s daily reserved volume and is capped at 100 GB for all accounts (including accounts with a daily reserved volume greater than 100 GB).

If the restore process exceeds this maximum, the process fails.
