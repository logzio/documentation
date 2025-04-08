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

![manage accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/manage-accounts-main-apr7.png)

At the bottom of the page, you’ll find a breakdown of all related accounts for this telemetry type. Each row includes:

* Account name – The name of the main or sub-account
* Account ID – The unique identifier for the account
* Vol (GB) – Daily indexing volume allocated to the account
* Optimizers - List of optimizers applied on this account 
* Usage - Percentage of useage from overall available volume


## Create an account

To create a new Timeless account, click **Create new account**, enter a name, select the volume you want to allocate for this account, and select which accounts should have read and write permissions to this account's data.

Click **Create** to complete setup and add the account. The account will be visible in the table with all of the relevant data. 

## Edit accounts

To modify an existing Security account, click the **⋮** icon next to it and select **Edit**. You can update the account name and adjust which log accounts it can access.

Click **Save changes** to apply your updates.

## Delete an account 

To delete a Security account, click the **⋮** icon and select **Remove account**. This will permanently delete all associated data.

This action cannot be undone.

## Create or manage a timeless account


##### Select or add a timeless account

In the **Timeless account plan** panel,
click the timeless account you want to manage,
or click **Add timeless account**.

![Manage a timeless account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/accounts--manage-timeless-account.png)

##### Adjust account volume

If you need to adjust the **Timeless account volume**,
type in the text box
or use <i class="li li-plus"></i> and <i class="li li-minus"></i>.

Your plan allows for a maximum data volume.
Keep this limit in mind when you allocate resources to your timeless accounts—you won't be able to exceed the limits of your plan. \\
\\
Contact your Logz.io account manager if you need to increase your plan limits.


##### Set search permissions

If you want your sub accounts to be able to search this account,
add the intended accounts to the **Read & write permissions** box.

##### Save your changes

Click **Apply** to save your changes.


#### To clean a timeless account



##### Find your timeless account plan

Log into your Logz.io account, navigate to **[Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts)**, and find your timeless account plan.

![Timeless account plan](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/timeless-account-manage.png)

##### Choose the relevant account

Click on the account you'd like to clean. Then, in the dropdown menu, you'll be able to review the account's data usage.

![Timeless account plan expanded](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/timeless-account-in-use.png)

##### Clean the data

Click on the **Clean** button to open a popup with additional options. You can decide what log data to delete from your timeless account in this popup. Select the date range in which you'd like to clean the data. You can also select specific optimizers to clean. Next, click on **Continue**.

![Clean timeless data](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/timeless-date-and-optimizers-msg.png)

##### Confirm the clean

The final confirmation window summarizes how many log messages will be deleted in this process. This process might take a few minutes, depending on the number of log messages, and is irreversible. To confirm, click on the **Yes, please clean my account** button.

![Timeless account plan expanded](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/timeless-confirmation-msg.png)


If you're an admin for the main account, you can manage the main account and sub accounts from the [**Manage Accounts**](https://app.logz.io/#/dashboard/settings/manage-accounts) page (**<i class="li li-gear"></i> > Settings > Manage accounts** in the navigation menu).

The Distributed Tracing Account plan panel is located in the middle of the **[Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts)** page.

You can view your Distributed Tracing account plan and the specific details and options that can be updated for each account within the plan.

If you don't have a Distributed Tracing account yet, start a trial in the Distributed Tracing tab.
