---
sidebar_position: 3
title: Manage Tracing accounts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn more on managing your tracing accounts in Logz.io
keywords: [account, manage account, optimization, admin controls, admin, user permissions, permissions, access control, trace, traces]
---


Logz.io Tracing provides powerful tools to search and analyze span data, helping you debug, troubleshoot, and resolve issues more efficiently.

If you're an admin of your Logz.io main account, you can manage your Tracing setup from the Manage Accounts page under **Settings > Manage Accounts**, then switch to the Tracing tab.

![Tracing account overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/tracing-main-account.png)


## Manage your account

Tracing accounts are based on spans: individual units of work in a distributed system. Each span represents a named, timed operation.

At the top of the page, you'll see a summary of your account, including:

* Trial ends in (if applicable) - Remaining time in your tracing trial
* Monthly spans - Total span volume available for the month
* Accounts - Number of active and available Tracing accounts
* Retention - How long span data is stored

Below that, you’ll find a detailed table listing all related accounts for this telemetry type. Each row includes:

* Account name – Name of the account. Special characters such as `<`, `>`, `:`, `\"`, `/`, `\\`, `|`, `?`, `*` are not supported.
* Account ID – A unique identifier for the account
* Spans - Monthly span allocation for the account
* Token – The token used to ship tracing data to this account

## Create an account

You can add up to 3 tracing accounts by default. If you need the ability to add more accounts, contact your account manager or reach out to [Logz.io Sales team](mailto:sales@logz.io).

To create an account, click **Create new account**. Provide a name, the number of monthly spans to allocate, and set a daily limit multiplier—a safeguard that prevents unexpected spikes from consuming your full monthly quota. The multiplier (between x2 and x30) defines your daily cap based on expected usage.

Lastly, define which accounts should have read access to this account’s data.

Click **Create** to complete the setup. The new account will appear in the table.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/tracing-new-account.png" alt="new-account" width="700"/>


## Edit accounts

To update an account, click the **⋮** icon next to it and select **Edit**. You can modify the account name, monthly span allocation, daily limit multiplier, and access permissions.

The daily limit multiplier allows you to set a daily limit to ensure incidents and issues won't consume all of your monthly spans. The number represents a multiplier of your estimated daily span account, ranging between x2 and x30.

Click **Save changes** to apply the updates.

## Delete an account 

To delete an account, click the **⋮** icon and select **Remove account**.

Deleting an account will return its spans allocation to the main account. All data associated with the deleted account will be permanently removed.

This action cannot be undone.

## Additional details

### Configure read access

Each Tracing account can serve as a data source for others. You control access through **read permissions** when creating or editing an account—simply select which accounts can view the data.

### Tracing surge protection

To prevent your span quota from being consumed too quickly, Logz.io offers surge protection through the daily limit multiplier.

Here’s how it works:

* Your estimated daily usage is calculated as:
  monthly span quota / 30
* The daily multiplier (x2–x30) defines the allowed daily cap

If an account exceeds this cap, it will stop ingesting spans for the rest of the day (until midnight UTC). Admins are notified by email when usage hits 80% of the daily limit, giving you time to act before ingestion stops.

To update the multiplier, go to **Manage Accounts > Tracing**, select the account, click Edit, and change the **Daily limit multiplier**.

## Configure your account limits

You can adjust your account’s daily volume and data retention period to fit your current monitoring needs.

To make changes, go to the [Plan and usage](https://app.logz.io/#/dashboard/settings/plan-and-billing/plan) page, select the telemetry type you want to update, and click **Update plan**.

From there, you can modify the Monthly spans (Million Spans) and billing cycle (monthly or yearly). When you're ready, click **Proceed to checkout** to apply the changes.


## Troubleshooting Span Quota Issues

If a Tracing account exceeds its quota, first check whether enough of your overall span quota is allocated to that account.

Navigate to **[Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts)** > Tracing. You'll see how many spans you currently have.

You can add more spans from the overall quota to prevent your Tracing account from getting suspended, increasing your monthly and daily limit multiplier for this account.

If you have several Tracing accounts but no available spans from your monthly quota, you can allocate spans between the different accounts.

If there are no available spans to allocate, you can contact [Logz.io Support team](mailto:help@logz.io) to temporarily increase the quota limit.