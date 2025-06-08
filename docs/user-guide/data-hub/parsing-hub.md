---
sidebar_position: 4
title: Parsing Rules Hub
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Create and view custom log parsing rules
keywords: [log parsing, parsing rule, parsing, parsing hub, log parser, logz.io parsing]
---

:::tip note
Parsing Rules Hub is currently in **beta**. We're actively improving it based on user feedback, so functionality and abilities may evolve over time.
:::


The Parsing Rules Hub lets you create and manage custom parsing rules to structure your logs as they arrive. This feature supports multiple parsing methods and provides a centralized view of all rules configured in your account.

## Accessing the Parsing Rule Hub

To open the Parsing Rule Hub, go to [Data Hub > Parsing Rule Hub](https://app.logz.io/#/dashboard/parsing-rules-hub).

![Parsing Rules Hub](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-rules/parsing-rule-hub-main.png)


## How Parsing Rules Work

Each **log type** can have **one active rule** at a time.

Use the **Active** toggle to turn rules on or off.

Hover over a rule to reveal the **magnifying glass** icon, then click it to **view rule details**.

At this time, rules can’t be edited or deleted after creation.

## Creating a New Parsing Rule

To create a new rule, click **+ New Rule** in the main Parsing Rules Hub.

* Name your rule. Give it a clear, descriptive title.

* Select the relevant log type for applying the rule. Note: Only **one rule** can be active per log type.

* Paste a log sample (raw text or JSON) to use as a reference while building your rule.

* Define the parsing logic using the rule editor. You can find all supported processors in the [Sawmill Processors Wiki](https://github.com/logzio/sawmill/wiki/Processors). The editor automatically validates your syntax as you type.

* Click **Run** to preview how your rule processes the sample.

Once you're happy with the result, click **Save rule** to apply it.

![Parsing Rules Editor](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-rules/parsing-rule-editor.png)


**Need Help?** If you have questions or need support, contact us at [help@logz.io](mailto:help@logz.io).