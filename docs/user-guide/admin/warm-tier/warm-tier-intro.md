---
sidebar_position: 1
title: What is Warm Tier?
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Everything you need to know about Logz.io's Warm Tier solution
keywords: [manage, log redaction, admin controls, account administration, access control, warm, warm tier, warm logs, archive]
---

Logz.io offers a number of ways to store your data; Hot, Cold, and Warm tiers.

The Warm tier is designed for logs that don't require frequent acessability, but still need to be readily available for analysis and troubleshooting when needed.

It supports historical data and make it available when needed.

## When should you use Warm tier?

Warm tier is ideal for cases where data is needed periodically but doesn’t require the immediate speed of Hot tier. For example:

* Historical analysis - Access past logs for insights, trend analysis, or event data for weeks or months after the logs' initial ingestion. 

* Root cause analysis - When troubleshooting issues, you oftern need to look back at recent historical data. With Warm tier, you'll be able to access it directly from Explore and get additional and needed context for your investigation. 

* Compliance - Compliance regulations often require data to be available for a certain period. The warm tier enables compliance by keeping data available without real-time access costs.



## Why Use the Warm Tier?

* Cost Efficiency: The Warm Tier offers significant cost savings compared to the Hot Tier, making it ideal for storing data long-term without the high expenses associated with real-time access.
* Extended Retention: Logs automatically transition from the Hot Tier to the Warm Tier after a defined period, allowing for longer retention and access to historical data.
* Performance Balance: While slightly slower than the Hot Tier, the Warm Tier maintains search and query capabilities at a moderate performance level, suitable for semi-active data.




The Warm Tier provides a valuable balance of cost, retention, and performance for data storage needs. It is designed for long-term data storage, offering significant cost savings over the Hot Tier, making it ideal for data that doesn’t require real-time access. This approach allows businesses to reduce storage expenses without sacrificing accessibility. Logs automatically transition from the Hot Tier to the Warm Tier after a set period, enabling longer data retention and easier access to historical data for analysis, compliance, and reporting purposes. Though slightly slower than the Hot Tier, the Warm Tier maintains reliable search and query functionality at a moderate performance level, well-suited for semi-active data that benefits from accessible yet cost-effective storage.










## Key Features and Limitations

### Core Features
* Seamless UI Integration: Operates within the familiar Logz.io platform interface, allowing users to query and manage logs as usual.
* Flexible Retention: Data is retained longer than the Hot Tier, providing mid-term storage that’s cost-effective and accessible.
* Alerting and Exporting: While alerts cannot run directly on Warm Tier data, users can create alerts and export data as needed.

### Performance Considerations
* Query Speed: Searches may take longer, especially for free-text or complex queries. Applying filters can improve response time.
* Visualization: Graphs and dashboards may load slower; the Hot Tier is recommended for critical real-time visualization needs.

### Limitations
* Query Constraints: Certain limitations, like a maximum number of concurrent queries and daily scan quotas, ensure that the system isn’t overloaded. Complex queries might be restricted to maintain performance.
* Functionality Differences: Some features, such as real-time dashboards and alerting, are better suited for the Hot Tier due to performance and frequency requirements.


For more information, contact Logz.io support or visit the Warm Tier page on our website.