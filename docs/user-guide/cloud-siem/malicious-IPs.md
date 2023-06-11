---
sidebar_position: 6
---

# Investigate Malicious IPs


The **Threats Overview** dashboard aggregates all suspected IPs from all sources in a single dashboard.

You can filter the dashboard by feed name, feed confidence, or country of origin. You can also filter by log type to check for malicious IPs reported by a specific security product.

Once you are ready to investigate a particular IP, click the IP drilldown link. It will lead you to the **IP Investigation** dashboard for the selected IP. There you'll be able to see the details of its activity in your environments and investigate the original logs for further information.

<div>
    <video width="100%" height="auto" controls autoplay loop muted>
      <source src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/investigate-ip2_aug2021.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
</div>


### Log enrichment for IPs

Cloud SIEM scans logs for malicious IOCs sourced from threat intelligence feeds. The process involves enrichment of the original logs with additional fields.

Below is the list of enrichment fields for IPs.

![Attacker IP list](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/malicious-ip-logs.png)

|Field|Description|
|--|--|
| logzio_security.ioc.malicious_ip | The malicious or suspected IP. It is also a **drilldown link**. Click on it to open the **IP Investigation** dashboard and quickly pull up the relevant logs and a summary of the IP's activity. |
| logzio_security.origin_feeds | The name of the threat intelligence feed that defined the IP as malicious. To research the feed, the last time the feed was synced, and more, go to **Threats > Threat Intelligence Feeds** from the top menu and review the feed information. |
| logzio_security.severity | Threats are ranked by severity on a scale of 1-5, 5 being the highest, to help reduce false-positives and to promote response to higher-risk threats. Severity is extrapolated from the feed's confidence. Feed confidence is determined by Logz.io and is not configurable. |
| logzio_security.context | Additional context as provided by the threat intelligence feed. |

