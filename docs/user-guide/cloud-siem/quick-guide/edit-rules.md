---
sidebar_position: 8
title: Manage Security Rules
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Manage and edit security rules
keywords: [SIEM, security rule, rules, cloud security, Security information and event management, Security information]
---


There are two types of rules in Cloud SIEM:

* A **protected rule** is a rule defined by Logz.io. These rules appear in the **Rule definitions** list with a **Logz.io rule** tag. You can only edit the name or logic of a protected rule if you duplicate the rule as described in this document. You can, however, define what accounts to apply the rule to and edit the trigger conditions, tags, and recipient endpoints of a protected rule.

* A **custom rule** is a rule defined by the user. These rules appear in the **Rule definitions** list without a tag. You can edit the name and logic of a regular rule, define what accounts to apply the rule to and edit the rule's trigger conditions, tags, and recipient endpoints.

## Manage Custom Rules

Navigate to your Logz.io [SIEM account > Rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions). 

Find a custom rule created by you or your team. These rules include the name of the user who created them.

![custom rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-created-team-member-dec.png)

Click the pencil icon on the right side of the rule you want to edit. 

![edit rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-edit-rule-dec.png)

You can review and edit the rule according to your needs. Click **Save** to apply the changes.


## Manage Protected Rules

Rules that are Preconfigured By Logz.io cannot be edited. However, you **can add** trigger thresholds and notification options.

Navigate to your Logz.io [SIEM account > Rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions).

Choose the rule you want to edit and click the pencil icon on the right side menu.

Edit the trigger thresholds or the notification options, and click **Save** to apply the changes.

![edit preconfigured rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/edit-preconfigured-rule-jan.png)


## Duplicate and Edit Protected Rules

You can edit and change preconfigured Logz.io rules by duplicating them. 

Navigate to your Logz.io [SIEM account > Rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions).

Choose the rule you want to duplicate, click on the three dots next to it, and choose **Duplicate**. 

![duplicate preconfigured rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/duplicate-rule-jan.png)

The rule configuration wizard includes all the settings set by Logz.io, and you can edit, change, or remove elements from each section.

Click **Save** to apply the changes.

Navigate to the main [Rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions) page, find the original preconfigured rule you've duplicated, and change its **State** to disable it.