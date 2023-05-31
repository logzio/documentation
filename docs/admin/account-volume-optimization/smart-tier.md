---
sidebar_position: 2
title: Smart tier - Data Management


---

Retention is a major factor that impacts the cost of your Log Management plan. If you are looking for ways to extend log retention and maximize cost savings, Logz.io Smart Tier may be a good solution for your needs.

Logz.io Smart Tier is a cost-effective data storage solution. Unlike Hot-Warm storage architectures, Smart Tier offers cost reduction _without_ increasing query latency or retrieval times. Instead, Smart Tier reduces costs by using cheaper storage solutions for data replication. [Learn more in our blog 🔗 ](https://logz.io/blog/smart-tiering/)



### Logz.io Data Tiering

To help optimize costs, you can choose where to store your logs:

* **Real-time tier** - Offers high performance and high availability to your log storage and critical data. Your most recent data is stored and replicated in Hot instances to guarantee top real-time performance. 
* **Smart tier** - Offers high-performance and cost-efficient log storage for aging logs. It offers the same real-time querying performance as the Real-time tier for less recent data. Data availability is guaranteed at a 97% SLA.
* **Historical tier** - Offers long-term storage for logs that age out of your plan’s retention policy by archiving them in S3/Azure Blob. You can restore the logs to Logz.io at any time. [Learn more

### 97% availability - guaranteed

As a user, most of the time, there is no difference between the experience of querying the Real-time tier and Smart tier data.

The only time the difference might become noticeable is on the rare occasion when you try to query a specific Smart tier data segment at the same time that it is being recovered from a replica. However, this coincidence is statistically rare enough for the trade-off between availability and cost to be competitive.

## Data integrity

Smart tier does not compromise data integrity.

Replicas ensure no data is lost to the same standard as the Real-time tier. The only consequence is that Smart tier _data replicas_ are not as highly available for immediate querying in OpenSearch Dashboards.

Since data replicas are only queried when a primary data center is temporarily down, the effects are likely to be minimal. Most of the time, replicas are a fail-safe precautionary measure that you as a user do not interact with.

## Smart tier does _not_ increase latency

Smart tier does not increase query latency and will not slow your workflow.
Unlike other hot-warm architectures, Logz.io Smart tier cuts costs by maintaining **replicas** on warm storage.

OpenSearch Dashboards search and query performance will be the same as you are used to from the top, Hot tier experience.
