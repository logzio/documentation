---
sidebar_position: 1
---


There are two types of rules in Cloud SIEM:

* A protected rule is a rule defined by Logz.io. These rules appear in the **Rule definitions** list with a **Logz.io rule** tag. You cannot edit the name or logic of a protected rule unless you duplicate the rule as described in this document. You can, however, define what accounts to apply the rule to, edit the trigger conditions, tags and recipient endpoints of a protected rule.

* A regular rule is a rule defined by the user. These rules appear in the **Rule definitions** list without a tag. You can edit the name and logic of a regular rule, as well as define what accounts to apply the rule to, edit the trigger conditions, tags and recipient endpoints of the rule.


To edit a regular rule:

1. Sign in to Logz.io.

2. Go to **SIEM > Rules**.

   ![Edit_rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/rule-1.png)

3. Select the three dots menu on the right side of a rule that you need to edit.

   ![Edit_rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/edit_rule.png)


4. Select **Edit**.

5. Edit the rule.

6. Select **Save**.

If you need to customize a protected rule, you can clone it, adjust the cloned rule to your needs and then disable the original protected rule. To do tis:

To edit a rule:

1. Sign in to Logz.io.

2. Go to **SIEM > Rules**.

   ![Edit_rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/rule-1.png)

3. Select the three dots menu on the right side of a rule that you need to clone.

4. Select **Duplicate**.

5. Edit the rule.

6. Select **Save**.

7. In the **State** column of the original protected rule, set the state selector to the disabled mode.

