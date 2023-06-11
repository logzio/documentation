---
sidebar_position: 4
---

# Sampling Rules


Sampling rules let you choose which traces you want to index and monitor inside your account. They help you focus your attention on events that are happening right now inside your systems and services. In addition, applying Sampling rules optimizes your quota management by only indexing critical and actionable spans or full traces.



## Sampling rules overview

The Sampling rules screen has these main components:

* **Choose an account** - Choose the Tracing accounts for which you'd like to create and apply your rules. You’ll need to create a different set of rules for each one of your accounts.

* **Main table** - Your Sampling rules will appear in this table. Each rule includes a description and a list of the services it's running on. If no services appear, it means that the rule applies to all of the spans.


![Sampling rules overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/sampling-rules/sampling-rules.png)

## Create custom Sampling rules

:::tip
By creating a separate set of rules per each tracing account, you can control the span volume more accurately.
:::

To create Sampling rules, click on the **New rule** button at the top right corner.

Next, choose the services to which you'd like to apply this rule. To manually add your services, check the **These services** option and select the relevant services from the drop down menu.

Finally, choose the sampling action. Each rule can only have one of the following actions:

* Keep a certain percentage of the traces. You can choose any value between 1-100.
* Keep traces that are slower than a certain value. You can choose any value that's higher than 1.
* Keep all traces that contain span errors. This will allow you to focus on finding and identifying issues.

![Create a sampling rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/sampling-rules/create-a-rule.png)

While you can only choose one action per rule, you can create multiple rules on the same services.

For example, you can create the following rules:

* Sample ALL traces with spans that have errors
* Sample traces that are slower than 2000ms
* Sample 50% of the traces
* Sample all traces from a critical service

Once you create a set of rules, navigate to the **[OTEL configuration generator](https://app.logz.io/#/dashboard/settings/tracing-yaml-configuration/)** to activate them.



## Configure and apply your Sampling rules

Creating your Sampling rules is the first step. Once you've finished creating a set of rules for your chosen account, you need to configure them through the OTEL configuration generator. 

The OTEL configuration generator creates a YAML config file for your collector, which you’ll need to run for the rules to take effect.

You can access the generator by clicking on the button at the top right corner of the screen or navigating to the page by clicking **[Tracing > OTEL configuration](https://app.logz.io/#/dashboard/settings/tracing-yaml-configuration/)**.

Select the configuration method based on your OTEL deployment strategy. You can currently choose Localhost; Docker and Kubernetes support is coming soon.

Once you have selected the appropriate Tracing account, follow the instructions to apply your rules to your collector.

![Create a sampling rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/sampling-rules/otel-configuration-screen.png)