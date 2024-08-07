If you're an admin for the main account, you can manage the main account and sub accounts from the [**Manage Accounts**](https://app.logz.io/#/dashboard/settings/manage-accounts) page (**<i class="li li-gear"></i> > Settings > Manage accounts** in the navigation menu).

The Distributed Tracing Account plan panel is located in the middle of the **[Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts)** page.

You can view your Distributed Tracing account plan and the specific details and options that can be updated for each account within the plan.

:::note
If you don't have a Distributed Tracing account yet, start a trial in the Distributed Tracing tab.
:::


## View the Tracing plan summary and account allocations

Your Tracing account is based on spans: a building block of a trace, a named, timed operation representing a piece of the workflow in distributed systems.

You can view your monthly available spans, your plan's data retention time, and a breakdown of each account's current month's allocations and usage percentages.

![Tracing account summary](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/main-tracing-account-jul.png)

## View details and options for a specific account

To see the detailed information and the configurable options for each account, click the account name in the table or pie chart. 

![View account details](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/tracing-deep-dive-jul.png)

You can view the following details:

* Account name and creation date 
* Account token
* Summary and breakdown of the spans sent to the account over the last 7 days

And change the following account options: 

* Tracing account name
* Which Logz.io main account and sub accounts can access the data in any of the multiple tracing accounts (which are data sources)
* Total spans allocated from the Distributed Tracing plan to this specific data source, which defines how many spans per calendar month can be ingested into this data source
* Remaining portion of the overall Distributed Tracing plan that can still be allocated to additional tracing data sources (accounts) 

## Update the account name

Enter a new **Tracing account name** and **Save** to update your changes, or **Cancel** to discard them.

![Rename a tracing account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/tracing-new-name-jul.png)

## Configure which accounts can access a tracing data source

Each Distributed Tracing account can function as a data source for other Logz.io accounts.
To manage access to your tracing data, you create an access list of the Logz.io main account and sub accounts that can view the span data for each tracing account. You can see the list of all the sub accounts (and main account) in the top right of the application page, in the account selector.

When users are logged in to an account in the access list,
they can choose the tracing account as a data source in the Jaeger interface of the Tracing tab.
![Pick a data source](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/tracing-data-source.gif)

**To grant access to the data in a tracing account**

  1. Click the account name to open its account details. 
  ![Manage tracing account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/click-on-jul.png)


  2. To enable access to a Distributed Tracing data source for other accounts, in the field below the **Tracing account name**, click **Add an account**, and select the relevant accounts. 
  ![Access to tracing account data for other accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/tracing-sub-account.gif)


## Add a tracing account to your plan

:::note
You can configure up to 5 tracing accounts for your Distributed Tracing plan. If you need the ability to add more tracing accounts, reach out to your account manager or [the Sales team](mailto:sales@logz.io).
:::

**To create a new account**

1. Click **Add Tracing account** in the upper left of the Distributed Tracing Account plan panel.
2. Name the new account
3. Set which accounts can use it as a data source in the Tracing tab. 
4. Configure the **Total monthly spans** to allocate to the new account. 
   If you don't have spans available to allocate to the new plan, you'll be prompted to reduce the allocation of another account.
   ![Reduce existing span allocation](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/new-tracing-account-no-spans-jul.png)

5. Click **Save** to apply your changes.

![Adding a new tracing account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/new-tracing-account-flow-jul.gif)

## Delete a tracing account from your plan
 
1. In the account details, click the **Delete** icon next to the account name.
  ![delete](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/delete-tracing-account-jul.png)   

2. Confirm (or **Cancel**) the action. 
  ![Confirm delete](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/confirm-delete-tracingacct2.png)


## Change spans allocation across Distributed Tracing accounts within your plan

Juggle the allocated spans per month of your Distributed Tracing account plan between the different tracing accounts according to each account's current usage details. Each data source has its quota defined in the **Spans** column. 

![overview of allocated spans](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/span-allocation-jul.png)

To change how many spans are allocated to a tracing account, pick the relevant account, increase or decrease the **Total monthly spans** and click **Save** to apply your changes.


By **setting a daily limit**, you can ensure incidents and issues won't consume all of your monthly spans. The number represents a multiplier of your estimated daily span account, ranging between x2 and x30. 

![daily span limit](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/daily-span-limit.png)

In the example below, **New Tracing Account 2**  is not using its allocated spans: It would be reasonable to reduce its monthly allocation and increase the allocation for the **Tracing** account. 
![juggle allocated spans](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/shiftspans-betweenaccts-jul.png)

## Tracing surge protection

Your Distributed Tracing accounts are limited by a monthly quota of a number of spans, representing your Distributed Tracing plan. 

To avoid a situation in which your monthly quota runs out too fast because of unnoticed spikes, Logz.io introduced a **surge protection** mechanism for Tracing accounts.

The surge protection is a span number-based quota, aimed to cover different scenarios in which your accounts run out of quota too fast.

The calculation is estimating your span number:

* Monthly spans quota / 30 = Estimated number of daily spans.
<!-- * 4 X Estimated number of daily spans X 2KB = Estimated daily spans volume. -->


Your account's overhead spans can be configured by changing the daily span multiplier. To configure the daily span multiplier, navigate to the **[Manage account](https://app.logz.io/#/dashboard/settings/manage-accounts)** page, select the relevant Tracing account, and apply the daily span multiplier.

If your Tracing account's overall daily span number exceeds the **estimated daily spans limit** - the Tracing account will stop ingesting spans for this day (ending midnight UTC). 

When an account exceeds 80% of the allowed daily spans, account admins will receive an email alert indicating an unusual traffic event in the Tracing account, providing extra time to examine the issue before the ingestion stops.

## Troubleshooting

If your Tracing account exceeded its quota, the first thing you'll need to do is check that the overall quota is assigned to your account.

Navigate to **[Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts)** and scroll to find your **Distributed Tracing plan**. You'll see how many spans you currently have and their distribution across your account.

![Distributed Tracing account overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/span-usage-2-jul.png)

In this example, the overall quota is 600M monthly spans, when only 450M are allocated to the **Sock Shop Tracing** account.

You can add more spans from the overall quota to prevent your Tracing account from getting suspended, increasing both your monthly and daily limit for this account.

If you have several Tracing accounts but don't have any available spans from your monthly quota, you can allocate spans between the different accounts.

![Distributed Tracing allocation](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/tracing-allocating-spans-jul.png)

In this example, all of the monthly spans quota is divided between 2 Tracing accounts. 

By moving 50M monthly spans to the **Sock Shop Tracing DEV** account, you can prevent the dev account from getting suspended.

![Distributed Tracing reallocation](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/reallocate-spans-jul.png)

If there are no available spans to allocate, you can contact [Logz.io Support team](mailto:help@logz.io) to temporarily increase the quota limit.

