---
sidebar_position: 5
title: Observability IQ Root Cause Analyzer FAQ
description: Frequently asked questions about Root Cause Analyzer (RCA)
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [AI, observability, Assistant, iq, logs, metrics, traces, rca, root cause analysis, root cause, analysis, services, logz.io]
---


## General

### What kind of information can I get from Observability IQ RCA? 

Observability IQ RCA can help you pinpoint how an issue was introduced [ex., new deployment introduced latency] and identify related response steps while generating detailed conclusions and summarizing details for further analysis and communication.

### Is Observability IQ RCA available to all users?

Observability IQ RCA is currently available to all Logz.io users whose data is hosted in the US regions.

### Is Observability IQ RCA accessible via API?

No. To access Observability IQ RCA, you must use Logz.io's app.

### What data can Observability IQ RCA access upon activation?

Observability IQ RCA activates when you click the Analyze button. Once the process has started, RCA can query for more context and utilize log search to get relevant data needed to perform the analysis. The restrictions are the same as the ones that apply to your Logz.io account, and RCA can access any data as needed.

This setup ensures that the IQ RCA simulated a real-time investigation to resolve the issue and find the root cause.

### How do I provide feedback or report issues with Observability IQ RCA? 

Once the process is complete, you can provide feedback by clicking the Like or Dislike buttons. //Note that rating your answer shares it with us, helping us improve and enhance RCA and its results.

You can also provide feedback or report issues by clicking the **Share Your Feedback** button at the top of the Explore interface.

## Privacy and Security

### Where is the model hosted?

The model is hosted within the same region in which your Logz.io data is hosted. 

### Can account admins see RCA's previous steps and history?

No. Account admins or any other users within your organization cannot view or access any data from Observability IQ RCA. 

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