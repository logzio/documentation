---
sidebar_position: 5
---

# Creating Security Rules


Security rules define events and their execution conditions. A rule can contain one or more queries. You can create a security rule  either from scratch or by using an existing rule.



### Manually create a new rule

The first way is creating a rule from scratch. To do this:

1. Sign in to Logz.io.

2. Go to **SIEM > Rules**.

   ![Rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/rule-1.png)

3. Select **+ New rule**.

   ![Rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/rule-2.png)

4. Fill out the rule details as follows:

   ![Rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/create-a-siem-rule.png)


   * Give the rule a required name.
   
   * Define a query for the rule. You can do it directly in the **Create a rule** window and then preview it in OpenSearch Dashboards. Alternatively, you can define the query in OpenSearch Dashboards and copy it across.
   
   * Define what fields the query needs to be grouped by.
   
   * Define what accounts the query needs to apply to.
   
   * Repeat the previous three steps for another query, if required.
   
   * Define the trigger conditions for the rule.
   
   * If required, add a notification description to the rule. For example, a course of actions required when the rule is executed.
   
   * If required, add tags to the rule.
   
   * If required, add a notification endpoint in the **Recipients** list. This can be an email address or a webhook. See [Adding notification and SOAR endpoints](https://docs.logz.io/user-guide/cloud-siem/select-dashboards.html) for more on this.

4. Select **Save**.


### Clone and modify an existing rule

The other way is creating a rule from an existing rule. In this case, the rule builder will be pre-populated with data from the existing rule, such as the query string. To do this:


1. Sign in to Logz.io.

2. Go to **SIEM**.

3. Scroll down to the **Events** section. 

   ![Rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/events-1.png)


4. Click the **Investigate** tab next to the event that you want to base the new rule on.

5. Select **Create rule**.

   ![Rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/create-rule-from-query.png)

6. Fill out the rule details as follows:

   ![Rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/create-rule-from-query-2.png)

   * Give the rule a required name.
   
   * Define a query for the rule. You can do it directly in the **Create a rule** window and then preview it in OpenSearch Dashboards. Alternatively, you can define the query in OpenSearch Dashboards and copy it across.
   
   * Define what fields the query needs to be grouped by.
   
   * Define what accounts the query needs to apply to.
   
   * Repeat the previous three steps for another query, if required.
   
   * Define the trigger conditions for the rule.
   
   * If required, add a notification description to the rule. For example, a course of actions required when the rule is executed.
   
   * If required, add tags to the rule.
   
   * If required, add a notification endpoint in the **Recipients** list. This can be an email address or a webhook. See [Adding notification and SOAR endpoints](https://docs.logz.io/user-guide/cloud-siem/select-dashboards.html) for more on this.

6. Select **Save**.
