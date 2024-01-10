---
sidebar_position: 2
title: Threats Overview Dashboard
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Investigate IOCs and malicious IPs with Logz.io Threats overview dashboard
keywords: [SIEM, threat feeds, threats, feeds, managing threats, Security information]
---
 


The **Threats Overview** dashboard aggregates all suspected IPs from all sources in a single dashboard.

You can filter the dashboard by feed name, feed confidence, or country of origin. You can also filter by log type to check for malicious IPs reported by a specific security product.

Once you are ready to investigate a particular IP, click the IP drilldown link. It will lead you to the **IP Investigation** dashboard for the selected IP. There, you'll be able to see the details of its activity in your environments and investigate the original logs for further information.

![Threats overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-threats-dashboard-jan.png)

<!-- 
<div>
    <video width="100%" height="auto" controls autoplay loop muted>
      <source src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/investigate-ip2_aug2021.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
</div>
-->

The dashboard includes the following elements:

### Threats by Feed Graph

Shows the number of threats detected over time, split into 30-minute intervals. The colors represent various threat intelligence feeds or sources, as seen on the legend on the right side of the table.

Hover over the different graphs to get additional information, such as the exact timestamp of the threat, the score, reputation, and the threat feed.

### Threats statistics

The number represents the number of unique malicious IP addresses in your environment.

### Threats by feed confidence

The bar chart represents the confidence level of the threat intelligence feeds. Hover over each graph to view the severity level and the number of threats.

### Top countries of origin

Geographic representation of where detected threats originate.

### Threats by attacker

The table lists attacker IP addresses, the count of threats associated with each IP, and timestamps for when the IP was first and last seen.

### Threats by log and attack type

The two tables show the types of log types and threats, along with the log lines count, and unique malicious IP addresses count for each type.

### Malicious IP logs

This table presents the logs in which malicious IPs were detected and their origin feed, type, and severity. Click on each line to expand your view and get additional information, including the environment, tags, ID, and more.



## Log enrichment for IPs

Logz.io scans logs for malicious IOCs sourced from threat intelligence feeds. The process involves enrichment of the original logs with additional fields.

Below is the list of enrichment fields for IPs.

![Attacker IP list](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/malicious-ip-logs.png)

|Field|Description|
|--|--|
| logzio_security.ioc.malicious_ip | The malicious or suspected IP. It is also a **drilldown link**. Click on it to open the **IP Investigation** dashboard and quickly pull up the relevant logs and a summary of the IP's activity. |
| logzio_security.origin_feeds | The name of the threat intelligence feed that defined the IP as malicious. To research the feed, the last time the feed was synced, and more, go to **Threats > Threat Intelligence Feeds** from the top menu and review the feed information. |
| logzio_security.severity | Threats are ranked by severity on a scale of 1-5, 5 being the highest, to help reduce false-positives and to promote response to higher-risk threats. Severity is extrapolated from the feed's confidence. Feed confidence is determined by Logz.io and is not configurable. |
| logzio_security.context | Additional context as provided by the threat intelligence feed. |

