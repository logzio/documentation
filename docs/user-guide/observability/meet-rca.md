---
sidebar_position: 4
title: Observability IQ Root Cause Analysis FAQ
description: RCA FTW
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [AI, observability, Assistant, iq, logs, metrics, traces, rca, root cause analysis, root cause, analysis, services, logz.io]
---


<!--
Logz.io’s automated Root Cause Analysis (RCA) uses GenAI to transform the manner in which your team carry out investigation into any issues discovered in your cloud applications and infrastructure. Eliminating manual investigation steps, removing the need to pivot between multiple dashboards or run numerous queries to carry out in-depth troubleshooting.

With Logz.io's RCA you can quickly: 


* Move from issue detection directly into automated investigation, simplifying and reducing time from discovery to response.

* Execute broad, context-aware analysis that highlights the critical what, when, where, how and what was impacted, and what to do next.

* Pinpoint details about how an issue was introduced [ex. new deployment introduced latency] and identify related response steps.

* Generate detailed Conclusions, summarizing details for further analysis and communication.
-->


## General

### What is Observability IQ Root Cause Analysis?

Root Cause Analysis (RCA) is part of Logz.io's Observability IQ Assistant, offering an AI-enhanced platform that transforms how you can investigate any issues discovered in your cloud applications and infrastructure. You eliminate manual investigation steps, removing the need to pivot between multiple dashboards or run numerous queries for in-depth troubleshooting.

You can access it from **[Explore](https://app.logz.io/#/dashboard/explore)** > **Exceptions** to quickly execute a broad, context-aware analysis that highlights the critical what, when, where, how, and what was impacted and what to do next.



### What kind of information can I get from Observability IQ RCA? 

Observability IQ RCA can help you pinpoint how an issue was introduced [ex., new deployment introduced latency] and identify related response steps while generating detailed conclusions and summarizing details for further analysis and communication.


### Is Observability IQ RCA available to all users?

Observability IQ RCA is currently available to all Logz.io users whose data is hosted in the US regions.

### Is Observability IQ RCA accessible via API?

No. To access Observability IQ RCA, you must use Logz.io's app.

### How do I activate Observability IQ RCA?

Observability IQ RCA is available to all **[Explore](https://app.logz.io/#/dashboard/explore)** users. Open your Exceptions menu and click **Analyze** next to the issue you want to investigate.

Once you activate the RCA process, the following data will be shared with Claude3:

* Dashboard data
* Current logs
* Current exceptions
* Some visualizations
* Maybe traces
* Probably more

### What data can Observability IQ RCA access upon activation?

Observability IQ RCA activates when you click the **Analyze** button and start the process. It is designed to access the data ...., including your current query, the graphs visible on the screen, and a limited number of logs due to size constraints. 

This setup ensures that the IQ RCA simulated a real-time investigation to resolve the issue and find the root cause.


### How do I provide feedback or report issues with Observability IQ RCA? 

To provide feedback or report issues, click the **Share Your Feedback** button at the top of the Explore interface.



## Privacy and Security

### Where is the model hosted?

The model is hosted within the same region in which your Logz.io data is hosted. 

### Can account admins see RCA's previous steps and history?

No. Account admins or any other users within your organization cannot view or access any data from Observability IQ RCA. Logz.io does not retain your chat history, and it is deleted after the session ends.

### Do you use my data to train the AI model?

No, your data will not be used by AWS or third-party model providers to train the AI models. You can read more about this [here](https://aws.amazon.com/bedrock/faqs/#product-faqs#bedrock-faqs#security-and-privacy).


### Will the input and the model output served through Observability IQ RCA be available to Claude3? Are you using a private or public instance?

The data is processed and stored in Logz.io's private instance within AWS, similar to the current setup of your Logz.io data. The model is stateless, and data will never be shared with third-party model providers.

### How does Observability IQ RCA comply with security standards?

Your data is secured using industry-standard encryption both at rest and in transit. Since the data is processed and stored in Logz.io's private instance within AWS, there is no significant change compared to the current situation where AWS processes your data.

For more detailed information, please visit [Logz.io’s security and compliance page](https://logz.io/platform/features/soc-2-compliance/). You can read more about how AWS follows best practices for data security [here](https://aws.amazon.com/bedrock/faqs/#product-faqs#bedrock-faqs#general:~:text=Why%20should%20I%20use%20Amazon%20Bedrock%3F).

### How does Observability IQ RCA comply with Privacy and GDPR standards?​

Your data is handled by Logz.io and AWS (being Logz.io’s sub-processor) in accordance with privacy and GDPR standards and requirements. For more detailed information, please visit Logz.io’s [privacy policy](https://logz.io/about-us/privacy-policy/). You can read more about how AWS handles data protection [here](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html).


## Contact us

For further assistance with Observability IQ RCA, [contact Logz.io's Support Team](mailto:help@logz.io).