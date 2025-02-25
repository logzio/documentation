---
sidebar_position: 4
title: Drop Filters - Trace Sampling
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: How Sampling rules can improve your monitoring
keywords: [Sampling, data, sampling rules, traces, tracing]
slug: /user-guide/data-hub/sampling-rules
---


Trace Sampling lets you select which traces to index and monitor within your account, helping you focus on real-time events in your systems and services. Applying Drop Filters also optimizes quota usage by indexing only critical and actionable spans or full traces.


## Trace Sampling overview

The Sampling Rules screen includes the following:

* **Account Selection** - Choose the Tracing accounts where you'd like to create and apply Drop Filters. Each account requires a separate set of rules.

* **Main Table** - Displays your sampling rules, including descriptions and the services they apply to. If no services are listed, the rule applies to all spans.


![Sampling rules overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/sampling-rules/sampling-rules.png)

## Create Custom Trace Sampling Rules

:::tip
Creating individual rules for each tracing account allows for more precise span volume control.
:::

To create a rule, click **New Rule** at the top right. Then, select the services where this rule will apply. To manually add services, check **These Services** and choose from the dropdown menu.

### Sampling actions

Each rule can have one of the following actions:

* Keep a percentage of traces (choose a value from 1-100).
* Keep traces slower than a specified duration (must exceed 1 ms).
* Keep all traces with span errors to focus on identifying issues.

![Create a sampling rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/sampling-rules/create-a-rule.png)

While each rule can have only one action, you can create multiple rules for the same services. For example:

* Sample all traces with spans containing errors.
* Sample traces slower than 2000 ms.
* Sample 50% of traces.
* Sample all traces from a critical service.

:::caution Important
To **activate the new set of rules**, navigate to the [YAML Configuration Generator](https://app.logz.io/#/dashboard/settings/tracing-yaml-configuration/) and follow the instructions.
![Yaml configuration](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/sampling-rules/click-on-yaml.png)
:::



## Configure and apply Trace Sampling rules

Start by creating your sampling rules for the chosen account.

Configure them using the OTEL Configuration Generator, which creates a YAML file for your collector to run the rules.

Access the generator by clicking the button at the top right or navigating to **[Tracing > OTEL configuration](https://app.logz.io/#/dashboard/settings/tracing-yaml-configuration/)**. 

Select your configuration method based on your OTEL deployment strategy (currently supports Localhost; Docker and Kubernetes support is coming soon).

After selecting the Tracing account, follow the instructions to apply your rules to the collector.

![Create a sampling rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/sampling-rules/otel-configuration-screen.png)