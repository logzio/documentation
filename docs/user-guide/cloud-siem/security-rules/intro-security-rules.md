---
sidebar_position: 1
---


# Logz.io Security Rules


Use security rules to ensure you're notified of critical events in your systems and machine. Logz.io offers a set of updated preconfigured rules which you can refine and edit or create custom rules with your desired thresholds and triggers.

To open the **Rules** page, navigate to your **[SIEM account](https://app.logz.io/#/dashboard/security/summary) > [Rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions)**.


![Rules main](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/rule-def-main.png)


You'll see a paginated list of all rules configured for your account.


### Order or filter security rules list

* You can click the column headers or the top filters to sort the list by **severity**, by the user who **created the rule**, by **tags**, or by the **state** of each rule. 

* To filter chronologically by when rules were **created** or **updated**, click on the column you'd like to filter:

![Rules definitions](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/rules-table-sort.png)

### Manage security rules

You can manage each rule individually or act on many rules at once.

Use the search terms and filters to find the rules you want to edit. Then, you can choose them by clicking on the checkbox next to their name or selecting all of the page's visible rules (up to 25 rules) by checking the top box.


![Select rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/check-rules.gif)


If you have more than 25 rules you'd like to edit, you can select all of the results that match your search by clicking on the hypertext located at the top right of the table:


![Rules bulk actions](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/select-all-rules.png)


:::note
There is a limit of 1,000 rules that you can act on simultaneously.
:::

#### Managing individual rules


Each rule has a **State** button you can toggle to enable or disable the rule as needed. 

To edit, duplicate or delete a rule, hover over its line to reveal the **Delete** and **Edit** buttons.

You can click the **Menu button <i class="li li-ellipsis-v"></i>** to open the additional options: **Duplicate** a rule and **View last events**. Select the latter to display the rule's query and the number of hits.

#### Managing multiple rules

Choosing one or more rules opens a top menu with the following actions:
 
* **Delete** - Delete all of the selected rules. Note that you can't delete preconfigured Logz.io rules.
* **Activate** - Turn all selected rules to active
* **Deactivate** - Deactivate all selected rule
* **Recipient** - Add or replace recipients and notification points


![Rules edit menu](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/rules-inner-menu.png)


Clicking on the **Recipient** option presents you with a pop-up with 2 available options:

**Add** - Adds new recipients and notification points on top of the existing ones. You can use this to add Slack channels, email addresses, and more.

**Replace** - Remove the existing notification points and recipients, and replace them with the new settings. Note that you won't be able to review the current notification settings, and you won't be able to revert the action once you save your changes.


![Alert recepients edit](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/add-replace-rule.png)