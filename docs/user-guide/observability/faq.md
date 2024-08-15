---
sidebar_position: 3
title: Observability IQ Assistant FAQ
description: Frequently asked questions about Observability IQ Assistant
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [AI, observability, Assistant, iq, logs, metrics, traces, siem, insights, analysis, services, logz.io]
---

## General

### What is Observability IQ Assistant?

Observability IQ Assistant (IQ) is Logz.io's chat-driven, AI-enhanced platform, enabling active dialogue with your data. You can access it from your **[Explore](https://app.logz.io/#/dashboard/explore)**, **[Kubernetes 360](https://app.logz.io/#/dashboard/observability/k8s360)**, and **[App 360](https://app.logz.io/#/dashboard/spm/services/table)** dashboards, where you can transition from merely observing data to actively acquiring immediate insights on your metrics, identifying anomalies, discerning trends, and assessing the well-being of your ecosystem in real time.

### What kind of information can I get from the Observability IQ Assistant? 

The Observability IQ Assistant can help you with queries related to log analysis, infrastructure monitoring, troubleshooting issues, and other aspects of using the Logz.io Platform.

### Is Observability IQ Assistant available to all users?

Observability IQ Assistant is currently available to all Logz.io users whose data is hosted in the EU, UK, Canada, Australia, and the US.

### Is Observability IQ Assistant accessible via API?

No. To access Observability IQ Assistant, you must use Logz.io's app.

### How do I activate the Observability IQ Assistant?

Observability IQ Assistant is available in the **[Explore](https://app.logz.io/#/dashboard/explore)**, **[Kubernetes 360](https://app.logz.io/#/dashboard/observability/k8s360)**, and **[App 360](https://app.logz.io/#/dashboard/spm/services/table)** dashboards. Click the Observability IQ button at the top to open the interface.

Once you provide input to the assistant, the **dashboard's data** will be shared with Claude3.

### What data can Observability IQ Assistant access upon activation?

The Observability IQ Assistant activates when you input a prompt in its interface. It is designed to access only the data currently visible in your browser, including your current query, the graphs visible on the screen, and a limited number of logs due to size constraints. 

This setup ensures that the IQ Assistant interacts exclusively with the data you're actively analyzing.


### How do I provide feedback or report issues with the Observability IQ Assistant? 

To provide feedback or report issues, click the **Share Your Feedback** button at the top of the Observability IQ Assistant interface.



## Privacy and Security

### Where is the model hosted?

The model is hosted within the same region in which your Logz.io data is hosted. 

### Can account admins see my queries and chat history?

No. Account admins or any other users within your organization cannot view or access any queries or chat history from the Observability IQ Assistant. Logz.io does not retain your query or chat history and is deleted after the session ends.

### Do you use my data to train the AI model?

No, your data will not be used by AWS or third-party model providers to train the AI models. You can read more about this [here](https://aws.amazon.com/bedrock/faqs/#product-faqs#bedrock-faqs#security-and-privacy).


### Will the input and the model output served through the Observability IQ Assistant be available to Claude3? Are you using a private or public instance?

The data is processed and stored in Logz.io's private instance within AWS, similar to the current setup of your Logz.io data. The model is stateless, and data will never be shared with third-party model providers.

### How does the Observability IQ Assistant comply with security standards?

Your data is secured using industry-standard encryption both at rest and in transit. Since the data is processed and stored in Logz.io's private instance within AWS, there is no significant change compared to the current situation where AWS processes your data.

For more detailed information, please visit [Logz.io’s security and compliance page](https://logz.io/platform/features/soc-2-compliance/). You can read more about how AWS follows best practices for data security [here](https://aws.amazon.com/bedrock/faqs/#product-faqs#bedrock-faqs#general:~:text=Why%20should%20I%20use%20Amazon%20Bedrock%3F).

### How does the Observability IQ Assistant comply with Privacy and GDPR standards?​

Your data is handled by Logz.io and AWS (being Logz.io’s sub-processor) in accordance with privacy and GDPR standards and requirements. For more detailed information, please visit Logz.io’s [privacy policy](https://logz.io/about-us/privacy-policy/). You can read more about how AWS handles data protection [here](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html).

