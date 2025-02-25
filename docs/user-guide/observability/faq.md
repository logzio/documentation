---
sidebar_position: 3
title: AI Agent FAQ
description: Frequently asked questions about AI Agent
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [AI, observability, Assistant, iq, logs, metrics, traces, siem, insights, analysis, services, logz.io]
---

## General

### What is AI Agent?


:::info note
The AI Agent is currently in beta and may not always be fully accurate. We recommend reviewing the information for confirmation.
:::

AI Agent is part of Logz.io's Observability IQ suite. It provides a chat-driven, AI-enhanced platform, that enables active dialogue with your data. You can access it from your **[Explore](https://app.logz.io/#/dashboard/explore)**, **[Kubernetes 360](https://app.logz.io/#/dashboard/observability/k8s360)**, and **[App 360](https://app.logz.io/#/dashboard/spm/services/table)** dashboards, where you can transition from merely observing data to actively acquiring immediate insights on your metrics, identifying anomalies, discerning trends, and assessing the well-being of your ecosystem in real time.


### What kind of information can I get from the AI Agent? 

The AI Agent can help you with queries related to log analysis, infrastructure monitoring, troubleshooting issues, and other aspects of using the Logz.io Platform.

### Is AI Agent available to all users?

AI Agent is currently available to all Logz.io users whose data is hosted in the EU and the US regions.

### Is AI Agent accessible via API?

No. To access AI Agent, you must use Logz.io's app.

### How do I activate the AI Agent?

AI Agent is available in the **[Explore](https://app.logz.io/#/dashboard/explore)**, **[Kubernetes 360](https://app.logz.io/#/dashboard/observability/k8s360)**, and **[App 360](https://app.logz.io/#/dashboard/spm/services/table)** dashboards. Click the AI Agent button at the top to open the interface.

Once you provide input to the agent, the **dashboard's data** will be shared with Claude3.

### What data can AI Agent access upon activation?

The AI Agent activates when you enter a prompt in its interface. It’s designed to access all your log data, current query, and visible graphs.

This setup allows the AI Agent to interact directly with the data you're analyzing, delivering tailored insights and suggestions.


### How do I provide feedback or report issues with the AI Agent? 

To provide feedback or report issues, click the **Share Your Feedback** button located to the top bar of the screen.



## Privacy and Security

### Where is the model hosted?

The model is hosted within the same region in which your Logz.io data is hosted. 

### Can account admins see my queries and chat history?

No. Account admins or any other users within your organization cannot view or access any queries or chat history from the AI Agent. 

### Do you use my data to train the AI model?

No, your data will not be used by AWS or third-party model providers to train the AI models. You can read more about this [here](https://aws.amazon.com/bedrock/faqs/#product-faqs#bedrock-faqs#security-and-privacy).


### Will the input and the model output served through the AI Agent be available to Claude3? Are you using a private or public instance?

The data is processed and stored in Logz.io's private instance within AWS, similar to the current setup of your Logz.io data. The model is stateless, and data will never be shared with third-party model providers.

### How does the AI Agent comply with security standards?

Your data is secured using industry-standard encryption both at rest and in transit. Since the data is processed and stored in Logz.io's private instance within AWS, there is no significant change compared to the current situation where AWS processes your data.

For more detailed information, please visit [Logz.io’s security and compliance page](https://logz.io/platform/features/soc-2-compliance/). You can read more about how AWS follows best practices for data security [here](https://aws.amazon.com/bedrock/faqs/#product-faqs#bedrock-faqs#general:~:text=Why%20should%20I%20use%20Amazon%20Bedrock%3F).

### How does the AI Agent comply with Privacy and GDPR standards?​

Your data is handled by Logz.io and AWS (being Logz.io’s sub-processor) in accordance with privacy and GDPR standards and requirements. For more detailed information, please visit Logz.io’s [privacy policy](https://logz.io/about-us/privacy-policy/). You can read more about how AWS handles data protection [here](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html).

