---
sidebar_position: 1
title: Data Storage Tiers Overview
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Everything you need to know about Logz.io's Warm Tier solution
keywords: [manage, log redaction, admin controls, account administration, access control, warm, warm tier, warm logs, archive]
---

Logz.io offers three distinct storage tiers: **Hot**, **Warm**, and **Cold**, designed to optimize data access, retention, and cost. Each tier suits different data usage patterns and needs, allowing you to tailor your storage to specific requirements.

:::info note
Warm and Cold tier configurations can be set up by contacting the [Sales team](mailto:sales@logz.io).
:::

## Hot Tier

The Hot tier is designed for data that requires immediate and frequent access. It's the logs that are ingested daily into your account, providing the fastest retrieval speeds, ideal for recent logs, metrics, or traces actively used in analysis, monitoring, and troubleshooting.

Hot tier data is available in real-time or near real-time, allowing you to identify, troubleshoot, and query ongoing active monitoring, alerts, and analytics, and is typically accessed within a shorter retention window.

## Warm Tier 

The Warm tier is designed to handle logs that don’t require frequent access but still need to be readily available for analysis and troubleshooting. By enabling Warm tier data, you can access historical data when necessary, making it a practical choice for mid-term storage.

Data in the Warm tier remains readily accessible, but with slightly slower retrieval times, making it ideal for historical analysis and trend monitoring. Use the Warm tier for data that:

* Is relevant for medium-term retention and analysis
* Supports periodic reporting or trend analysis
* Balances cost with retrieval speed, allowing less-frequent access at a lower cost than the Hot tier

## Cold Tier

The Cold tier is intended for long-term data storage, optimized for cost over speed. This tier is ideal for archived data that rarely needs access but must be retained for compliance, auditing, or historical records. Data retrieval from the Cold tier may take longer, making it suitable for data that:

* Requires long-term retention for regulatory compliance or record-keeping
* Is rarely accessed but must remain available if needed
* Offers the most cost-effective storage option for infrequently accessed data

## Archive & Restore

Archiving allows you to move rarely accessed data to a more cost-effective, long-term storage solution of logs that don't need to be instantly searchable. When you need to investigate old logs after they have expired from your account, you can restore them to a temporary account with no additional storage costs.


When to Use Archiving:

* When data is no longer actively used but must be retained for compliance, historical analysis, or regulatory requirements.
* To optimize storage costs without permanently deleting data.

By effectively managing your data lifecycle with archiving and restoring, you can maintain performance and cost-efficiency while ensuring long-term accessibility of critical information. 

[Read more about Logz.io's Archive & Restore options](https://docs.logz.io/docs/user-guide/data-hub/archive-restore/archive-and-restore/).



## Choosing the right tier for your data

When choosing which tier to store your data in, consider how often you need to access your data and the importance of immediate retrieval. 

The Hot tier is best for data that’s critical for immediate analysis and monitoring. The Warm tier is suitable for data that’s accessed occasionally but remains important for historical insights. The Cold tier is ideal for archived data that must be retained but is rarely accessed. 

By selecting the appropriate storage tier, you can effectively manage data access and costs based on your specific needs.