---
sidebar_position: 3
title: Observability Assistant FAQ
description: Frequently asked questions about Observability Assistant
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [AI, observability, Assistant, iq, logs, metrics, traces, siem, insights, analysis, services, logz.io]
---

## What is Observability Assistant?

Observability Assistant is Logz.io's chat-driven, AI-enhanced platform, enabling active dialogue with your data. You can access it from your Services dashboard, where you can transition from merely observing data to actively acquiring immediate insights on your metrics, identifying anomalies, discerning trends, and assessing the well-being of your ecosystem in real time.

## Is Observability Assistant available to all users?

Observability Assistant is available to Logz.io users whose data is hosted in the US East (N. Virginia) region.

## How do I activate the Observability Assistant?

Activate the Observability Assistant by navigating to your [Services](https://app.logz.io/#/dashboard/spm/services/table?start=now-1h&end=now) dashboard. Once you choose a service, click the **Observability IQ** button to open the assistant. Once you provide input to the assistant, the dashboard's data will be shared with Claude3.


## Is Observability Assistant accessible via API?

No. To access Observability Assistant, you must use Logz.io's app.

## Can account admins see my queries and chat history?

No. Account admins or any other users within your organization cannot view or access any queries or chat history from Observability Assistant. Logz.io does not retain your query or chat history. 

## Does Observability Assistant share information with Claude3?

No. The data is processed and contained within Logz.io's private instance within AWS, similar to the current setup of your Logz.io data. 


## How does Logz.io prevent sensitive internal content from being summarized using Observability Assistant?

Logz.io enforces Data Loss Prevention (DLP) policies for the Observability Assistant according to your organization's existing approach to preventing unauthorized data disclosure.