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

![Parsing Rules Hub](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-rules/parsing-rules-jun26.png)


## How Parsing Rules Work

Each log type supports only **one active parsing rule** at a time.

To change a rule’s status, hover over it and open the **⋮** menu to activate, deactivate, or delete it.

Rules marked as **Pending** are view-only and can’t be modified until approved.

## Creating a New Parsing Rule

To create a new rule, click **+ New Rule** in the main Parsing Rules Hub.

* Name your rule. Give it a clear, descriptive title.

* Choose a log type to apply the rule to. Note: **Only one rule** is allowed per log type.

* Paste a log sample (raw text or JSON) to use as a reference while building your rule.

* Build your parsing logic using the editor. Need help? The [Sawmill Processors Wiki](https://github.com/logzio/sawmill/wiki/Processors) has all the supported processors you can use. In addition, the editor checks your syntax in real time.

* Click **Run** to preview how your rule processes the sample.

If everything looks good, click **Save rule** to apply it.

:::tip note
Some processors may take a bit longer to apply and will appear as Pending until they're ready.
:::

![Parsing Rules Editor](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-rules/parsing-rule-editor.png)


**Need Help?** If you have questions or need support, contact us at [help@logz.io](mailto:help@logz.io).