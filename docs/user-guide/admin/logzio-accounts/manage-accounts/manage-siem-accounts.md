---
sidebar_position: 4
title: Manage SIEM accounts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn more on managing your SIEM accounts in Logz.io
keywords: [account, manage account, optimization, admin controls, admin, user permissions, permissions, access control, siem, security, security account]
---


Logz.io SIEM (Security Information and Event Management) helps security teams detect threats, investigate incidents, and respond faster—all within the same observability platform.

If you're an admin of your Logz.io main account, you can manage your SIEM setup from the Manage Accounts page under **Settings > Manage Accounts**, then switch to the Security tab.


## Manage your account

Security account usage is based on the volume of data scanned. At the top of the page, you'll see an overview of your account, including:


* Daily scan – The maximum daily indexing capacity (in GB) allocated for threat detection
* Accounts – The number of active and available accounts for this telemetry type

![manage accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/security-account-main.png)

If you've configured a **Repository** account, it serves as a shared resource for SIEM content. Other Security accounts can automatically pull dashboards, visualizations, saved searches, and feeds from this central Repository. This helps streamline content management across accounts.

By default, new Security accounts automatically pull from the Repository account. You can manually disable this access for individual accounts if needed.

At the bottom of the page, you’ll find a breakdown of all related accounts for this telemetry type. Each row includes:

* Account name – The name of the main or sub-account
* Account ID – The unique identifier for the account
* Enable for – The number of accounts this Security account is monitoring

## Create an account

You can add up to 5 Security accounts by default. If you need the ability to add more accounts, contact your account manager or reach out to [Logz.io Sales team](mailto:sales@logz.io).

To create a new Security account, click **Create new account**, and enter a name. Logs are not shipped directly to Security accounts. Instead, Security accounts scan the logs from linked log accounts through granted read permissions.

Under **Read permission**, add the log accounts this Security account should monitor. When selected, the Security account is granted read access to these log accounts for the purpose of threat detection and anomaly scanning.

You can assign the same log account to multiple Security accounts—they’ll be monitored independently.

Click **Create** to complete setup and add the account. The account will be visible in the table with all of the relevant data. 

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/new-security-account.png" alt="new-account" width="700"/>

## Edit accounts

To modify an existing Security account, click the **⋮** icon next to it and select **Edit**. You can update the account name and adjust which log accounts it can access.

Click **Save changes** to apply your updates.

## Delete an account 

To delete a Security account, click the **⋮** icon and select **Remove account**. This will permanently delete all associated data.

This action cannot be undone.