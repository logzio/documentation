---
sidebar_position: 5
title: Manage Timeless accounts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn more on managing your timeless accounts in Logz.io
keywords: [account, manage account, optimization, admin controls, admin, user permissions, permissions, access control, timeless]
---

Logz.io Timeless accounts allow you to aggregate critical logs or metrics into dedicated accounts with endless retention—ensuring long-term visibility into the data that matters most.

If you're an admin of your Logz.io main account, you can manage your Timeless setup from the Manage Accounts page under **Settings > Manage Accounts**, then switch to the Timeless tab.

## Manage your account

Your Timeless account usage is based on the volume of data ingested. Timeless accounts work with optimizers, allowing you to save a subset of your logs for as long as you need them. You can store key metrics that you want to track in your timeless accounts. Each timeless account contains its own index, which you can search from your main account.

At the top of the page, you'll see an overview of your account, including:

* Volume – The maximum daily indexing capacity (in GB) allocated to the account
* Available volume – The maximum overall capacity (in GB) allocated to the account
* Accounts – The number of active and available accounts for this telemetry type

![manage accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/timeless-account-main.png)

At the bottom of the page, you’ll find a breakdown of all related accounts for this telemetry type. Each row includes:

* Account name – The name of the main or sub-account
* Account ID – The unique identifier for the account
* Vol (GB) – Daily indexing volume allocated to the account
* Optimizers - List of optimizers applied on this account 
* Usage - Percentage of useage from overall available volume


## Create an account

To create a new Timeless account, click **Create new account**, enter a name, select the volume you want to allocate for this account, and select which accounts should have read and write permissions to this account's data.

Click **Create** to complete setup and add the account. The account will be visible in the table with all of the relevant data. 

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/new-timeless-account.png" alt="new-account" width="700"/>

## Edit accounts

To modify an existing account, click the **⋮** icon next to it.

Select **Edit** to modify the account's name, volume, and read and write permissions. You'll be redirected to the Optimizers page where you can configure and manage all optimizers. 

Select **Connect an optimizer** to add an additional optimizer to the account.

Select **Clean the account** to delete log data from your timeless. A popup will open asking you to select the date range in which you'd like to clean the data. You can also select specific optimizers to clean. Click on **Clean** to confirm and start the process. It can take a few minutes, depending on the number of log messages. This process is irreversible.

![Clean timeless data](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/clean-timeless.png)


## Delete an account 

To delete a Timeless account, click the **⋮** icon and select **Remove account**. This will permanently delete all associated data.

This action cannot be undone.