---
sidebar_position: 1
title: Logz.io Security Rules
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Intro to Logz.io's security rules
keywords: [SIEM, Security, Security rules, security rule, Security information]
---


Set up security rules to notify you when critical events occur on your machines and systems. Logz.io offers a set of updated pre-configured rules you can refine and edit or create custom rules with your desired thresholds and triggers. 

To open the **Rules** page, navigate to **[SIEM account](https://app.logz.io/#/dashboard/security/summary) > [Rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions)**.


![Rules main](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/rule-def-main.png)


There are two types of rules in Cloud SIEM:

* A protected rule is a rule defined by Logz.io. These rules appear in the Rule definitions list with a **Logz.io rule** tag. You cannot edit the name or logic of a protected rule unless you duplicate the rule as described in this document. You can, however, define what accounts to apply the rule to, edit the trigger conditions, tags and recipient endpoints of a protected rule.

* A regular rule is a rule defined by the user. These rules appear in the Rule definitions list **without a tag**. You can edit the name and logic of a regular rule, as well as define what accounts to apply the rule to, edit the trigger conditions, tags and recipient endpoints of the rule.

The list includes all of the rules configured to your account. 

## Rule defenition list overview

Click the column headers or the top filters to sort the list by **severity**, by the user who **created the rule**, by **tags**, or by the **state** of each rule.

To filter the list chronologically by when rules were **created** or **updated**, click on the column you'd like to filter:

![Rules definitions](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/rules-table-sort.png)

You can manage each rule individually or act on many rules at once.

Use the search terms and filters to find the rules you want to edit. Then, you can choose multiple rules by clicking on the checkbox next to their name. You can also select all of the visible rules (up to 25 rules) by checking the top box. 


![Select rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/check-rules.gif)


If you have more than 25 rules you'd like to edit, you can select all of the results that match your search by clicking on the hypertext located at the top right of the table:


![Rules bulk actions](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/select-all-rules.png)


:::note
There is a limit of 1,000 rules that you can act on simultaneously.
:::

## Manage individual rules

Each rule has a **State** button you can toggle to enable or disable the rule as needed. 

To edit, duplicate or delete a rule, hover over its line to reveal the **Edit** button. Custom rules will allow feature a **Delete** button.

Click the **Menu button** to open the additional options: **Duplicate** a rule and **View last events**. Select the latter to display the rule's query and the number of hits.

## Managing multiple rules

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

## Manage pre-configured rules

If you need to customize a protected rule, you can clone it, adjust the cloned rule to your needs and then disable the original protected rule.

Navigate to  **[SIEM account](https://app.logz.io/#/dashboard/security/summary) > [Rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions)** and select the rule you want to duplicate. 

Click the **Menu button** to open the additional **Duplicate** option and choose it. Edit the rule according to your needs, give it a unique name, and **Save** it.

In the Rule defenition dashboard, locate the original rule you've duplicated and set the state selector to the **disabled** mode.


