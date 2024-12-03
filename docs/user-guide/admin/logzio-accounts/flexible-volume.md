---
sidebar_position: 5
title: Flexible volume
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Control how to manage and allocate data between your Logz.io accounts
keywords: [account, manage account, optimization, user management, admin controls, admin, user permissions, permissions, access control]
---

Flexible volume gives you more control over how you allocate space between your accounts.

With flexible volume, accounts can share indexing capacity and use it as needed. Instead of reserving capacity in advance, you can rely on shared volume to cover your indexing needs across accounts. When properly configured, shared volume can help to optimize distribution and minimize the risk of running out of space.




![Enable flexible volume](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/flexy-vol.gif)



Flexible volume is a global setting that applies to your time-based logging accounts. To reach it, go to [**<i class="li li-gear"></i> > Settings > Manage accounts**](https://app.logz.io/#/dashboard/settings/manage-accounts). This page is only available when logged in to the main account as an admin user.


:::note
You can include up to 200 sub accounts when flexible volume is enabled. To add more sub accounts, you’ll have to disable the flexible volume option.
:::c



## Volume settings

* **Reserved volume**

  If you'd like to guarantee indexing capacity to high priority accounts, you can configure their reserved volume. You are not required to allocate reserved volume. If you prefer, you can set reserved volume at zero to add even more flexibility.

  After an account fills its daily reserved volume, it can continue to index data using shared volume until it hits its cap or shared volume is spent for the day.


* **Shared volume**

  With flexible volume enabled, you can leave a portion of your plan volume unallocated. This is your plan's shared volume. Shared volume is available for accounts to use dynamically, as needed.

  Notification emails are sent to account admins to alert them when utilization of shared volume reaches 80% and 100%.


* **Volume cap**

  If you'd like to avoid situations where daily capacity is over-used by certain accounts, you can cap them.

  Notification emails are sent to account admins to alert them when account utilization reaches 80% and 100% of its cap.

* **If reserved volume is zero**

  It is possible for an account to have zero reserved volume. In this case, data capacity is entirely dependent on the availability of shared volume. Keep in mind that this configuration does not guarantee indexing capacity for the account and subsequently could lead to data loss whenever shared volume is not available.

## Account utilization notifications

When flexible volume is enabled, your plan's shared volume helps to protect against data loss. Still, to help prevent surprises and help you avoid data loss, Logz.io sends out notification emails to account admins to alert them of the following:

| Notifications | Low risk  | High risk |
|---|----|---|
| Shared volume | 80% of shared volume is spent for the day. | 100% of shared volume is spent for the day. Only accounts with available reserved volume can continue to index logs. No shared capacity will be available until the index switches at 00:00 UTC tonight. |
| Account cap | Account has reached 80% of its daily cap. | Account has reached 100% of its daily cap. It will no longer accept data until the index switches at 00:00 UTC. |

## Configure flexible capacity accounts


### Enable flexible volume for your plan

Go to [**<i class="li li-gear"></i> > Settings > Manage accounts**](https://app.logz.io/#/dashboard/settings/manage-accounts) to manage your plan. This page is only available when logged in to the main account as an admin user.

To enable flexible volume, toggle the button **Use flexible volume** to turn it on.

### Configure account capacity

Click an account from your list to select it. Or, click **Add sub account** to create a new sub account.

Configure the account's daily capacity:

* **Reserved volume** - This is the volume that is guaranteed for the account per calendar day.

  For the main account, there is a 1 GB minimum. Otherwise, for sub accounts, it can be 0 as well.

* **Cap this account's volume** - This is optional.

    * If you leave this option unchecked, the account has unlimited access to shared volume.

      Once the account exhausts its daily volume, it can continue to receive and index data as long as shared volume is available.

   * If you enable this option, another field will appear:  **Volume cap**.

      This is the maximum volume that the account can index per calendar day. It cannot be greater than the sum of the account's reserved volume and available shared volume.

![Enable flexible storage](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/configure-flexible-volume.png)
