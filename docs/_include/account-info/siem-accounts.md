Each Security account is a separate entity, with its own users, rules, and feeds.
Security accounts can only access each other's dashboards, rules, private feeds, or data if you enable and configure how these objects can be shared.

If you're an admin for the main account, you can manage the main account and sub accounts from the [**Manage Accounts**](https://app.logz.io/#/dashboard/settings/manage-accounts) page (**<i class="li li-gear"></i> > Settings > Manage accounts** in the navigation menu).

:::note
If you're interested in adding a Cloud SIEM plan, reach out to your account manager or email [the Sales team](mailto:sales@logz.io).
:::

### Manage your Cloud SIEM account

* [Add a Cloud SIEM account](/user-guide/accounts/manage-the-main-account-and-sub-accounts.html#add-a-cloud-siem-account)
* [Configure or update your Cloud SIEM account](/user-guide/accounts/manage-the-main-account-and-sub-accounts.html#configure-or-update-a-cloud-siem-account)
* [Delete a Cloud SIEM account](/user-guide/accounts/manage-the-main-account-and-sub-accounts.html#delete-a-cloud-siem-account-from-your-plan)
* [Investigate security events](/user-guide/accounts/manage-the-main-account-and-sub-accounts.html#investigate-security-events)


#### Add a Cloud SIEM account

You'll find your Cloud SIEM accounts
in the [Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts) page
of your Operations workspace. Scroll down to the bottom of the page to see them.

Click **Add Security account** to open the form.
The number of accounts you can create is listed.

![Add a Cloud SIEM account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/add-security-account11.png)


#### Configure or update a Cloud SIEM account

![Configure a Cloud SIEM account](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/config-security-account.png)


Fill in the form:

1. **Name** (or rename) the account.
2. **Enable Cloud SIEM on these accounts** - Select the log accounts to be secured. You'll be giving the security account **read permissions** so it can monitor and enrich the logs.

    Logs are not shipped directly to your Cloud SIEM accounts. Instead, you'll grant read-access to log accounts you want a security account to monitor.

    You can add the same log account to multiple Security accounts. It will be monitored by each   Security account independently.
    {:.info-box.note}

3. **Automatically pull dashboards, visualizations, and saved searches from these Security accounts** - Select which security accounts you can automatically pull shared objects from. 

  ![Shared security objects](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/add_new-account.gif)

  The security account you're configuring will automatically be able to access the OpenSearch dashboards, visualizations, and saved searches from the source accounts you add to this list, but will *not* have access to the data in these accounts.  
  
  This is helpful if you have multiple main accounts. 
  
  For example: 

  + Instead of creating the same objects for each account, you can just share them! 
  + You can use this process to keep a local backup copy of these data objects. 
  + Create a library of data objects in your main Security account, and then enable client accounts to use objects from your main account.  

#### Save your changes

Click **Create**/**Apply** to save your changes.

When you first add a new account, give it a few minutes to finish setting up.


#### Delete a Cloud SIEM account from your plan 
 
1. In the account details, click the **Delete** icon next to the account name.
  ![delete](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/delete-SIEM.png)   

2. Confirm (or **Cancel**) the action. 
  ![Confirm delete](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/confirm-delete-siem-acct.png)


### Investigate security events

Cloud SIEM logs a security event every time a rule triggers. The terms **triggered rules** and **security events** have the same meaning and are used interchangeably.


Logs of security events- logs of triggered rules- are kept for 10 years. This ensures that details concerning security incidents are kept on record and can be investigated and re-visited many months and even years after the fact as new findings come to light.

The event log includes details about the security incident and the rule that caused it to trigger. It also offers an **Investigate** link to pull up the logs that triggered the specific event quickly.

![Logz.io Cloud SIEM Summary page](https://dytvr9ot2sszz.cloudfront.net/logz-docs/security-analytics/investigate-600px.png)

Learn more about investigating security events.




