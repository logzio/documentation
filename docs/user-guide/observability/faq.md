---
sidebar_position: 3
title: Observability IQ Assistant FAQ
description: Frequently asked questions about Observability IQ Assistant
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [AI, observability, Assistant, iq, logs, metrics, traces, siem, insights, analysis, services, logz.io]
---

## What is Observability IQ Assistant?

Observability IQ Assistant is Logz.io's chat-driven, AI-enhanced platform, enabling active dialogue with your data. You can access it from your Services dashboard, where you can transition from merely observing data to actively acquiring immediate insights on your metrics, identifying anomalies, discerning trends, and assessing the well-being of your ecosystem in real time.

## Is Observability IQ Assistant available to all users?

Observability IQ Assistant is currently available to all Logz.io users, whose data is hosted in the EU, Australia, and in the US regions.

## Is Observability IQ Assistant accessible via API?

No. To access Observability IQ Assistant, you must use Logz.io's app.

## How do I activate the Observability IQ Assistant?

Observability IQ Assistant is available in the **[Explore](https://app.logz.io/#/dashboard/explore)**, **[Kubernetes 360](https://app.logz.io/#/dashboard/observability/k8s360)**, and **[App 360](https://app.logz.io/#/dashboard/spm/services/table)** dashboards. Click the Observability IQ button at the top to open the interface.

Once you provide input to the assistant, the dashboard's data will be shared with Claude3.


## What data can Observability IQ Assistant access upon activation?


The Observability IQ Assistant activates when you input a prompt in its interface and operates within the same region in which your Logz.io data is hosted. It is designed to access only the data currently visible in your browser, including your current query, the graphs visible on the screen, and a limited number of logs due to size constraints. This setup ensures that the IQ Assistant interacts exclusively with the data you're actively analyzing.



Observability IQ Assistant activates when you input a prompt in its interface. It is designed to access only the data currently visible on the browser, your current query, and a limited number of logs due to size constrictions and limits. This setup ensures the IQ Assistant only interacts with the data you're currently analyzing.

## Can account admins see my queries and chat history?

No. Account admins or any other users within your organization cannot view or access any queries or chat history from the Observability IQ Assistant. Logz.io does not retain your query or chat history. 

## Will the input and the model output served through the Observability IQ Assistant be available to Claude3?

No, they are not shared with any model provider. The data is processed and stored in Logz.io's private instance within AWS, similar to the current setup of your Logz.io data.

## Will the input and the model output served through the Observability IQ Assistant be used to train the AI Model? ​

No, they will not be used by AWS or third-party model providers to train the AI models. You can read more about this [here](https://aws.amazon.com/bedrock/faqs/#product-faqs#bedrock-faqs#security-and-privacy).

## How does the Observability IQ Assistant comply with security and privacy standards?

Since the data is processed and stored in Logz.io's private instance within AWS, from a privacy and security perspective, there is no significant change compared to the current situation where your data is processed by AWS (being Logz.io’s sub-processor). You can read more about it [here](https://aws.amazon.com/bedrock/faqs/#product-faqs#bedrock-faqs#general:~:text=Why%20should%20I%20use%20Amazon%20Bedrock%3F).