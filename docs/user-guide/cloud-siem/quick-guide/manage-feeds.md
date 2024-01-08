---
sidebar_position: 10
title: Managing Threat Feeds
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: View and manage threats and threat feeds in Logz.io
keywords: [SIEM, threat feeds, threats, feeds, managing threats, Security information]
---

Logz.io offers a Threat overview dashboard where you can quickly assess your environment's security and a threat intelligence feeds dashboard where you can search, add, and manage your feeds.

## Threat overview dashboard

The [threat overview dashboard](https://app.logz.io/#/dashboard/security/threats/overview) provides an eagle's view of your environment. You can filter your view according to a desired time frame or run a Lucene query to specify which threats you want to view.

![Threats dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-threats-dashboard-jan.png)

The dashboard includes the following elements:

#### Threats by Feed Graph

Shows the number of threats detected over time, split into 30-minute intervals. The colors represent various threat intelligence feeds or sources, as seen on the legend on the right side of the table.

Hover over the different graphs to get additional information, such as the exact timestamp of the threat, the score, reputation, and the threat feed.

#### Threats statistics 

The number represents the number of unique malicious IP addresses in your environment.


#### Threats by feed confidence 

The bar chart represents the confidence level of the threat intelligence feeds. Hover over each graph to view the severity level and the number of threats. 

#### Top countries of origin 

Geographic representation of where detected threats originate.

#### Threats by attacker 

The table lists attacker IP addresses, the count of threats associated with each IP, and timestamps for when the IP was first and last seen.

#### Threats by log and attack type

The two tables show the types of log types and threats, along with the log lines count, and unique malicious IP addresses count for each type.

#### Malicious IP logs

This table presents the logs in which malicious IPs were detected and their origin feed, type, and severity. Click on each line to expand your view and get additional information, including the environment, tags, ID, and more.

## Threat intelligence feeds

Logz.io automatically cross-references your incoming logs with public threat feeds to identify malicious IPs, DNSs, and URLs. The [Threat intelligence feed](https://app.logz.io/#/dashboard/security/threats/threat-intelligence-feeds) provides a complete list of public feeds, which you can cross-reference with private threat intelligence feeds to identify malicious activity.

![threats feed](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/feed-1.png)

You can search the table for IP addresses, domains, or URLs across the different feeds. The table includes the following information:

#### Feed

This lists the names of different threat intelligence feeds.

#### IOC type

IOCs, Indicator of Compromise, are identified by IP, hash, domain, URL, user-agent header, or other custom indicators.

#### Confidence 

Indicates the reliability score of the feed, assigned by Logz.io's team of security analysts. 

#### Investigation URL 

URLs provided here are links to the sources of the feeds, where one can find more detailed information or investigate the threats further.

#### Feed type

There are two different types of feeds:

* Logz.io threat feed is a predefined threat feed. It is included by default and cannot be edited. Logz.io threat feeds have a **Logz.io feed** tag.

* Private threat feed is a feed added by you or your team members. You can add, edit, or delete a private feed. Private feeds have a **Private feed** tag.


#### Last sync

The date when the feed was last updated or synchronized.

### Create a private feed

Account admins can create private feeds. Click on **+ Add private feed** to open the configuration wizard.

Name the feed, and select the type from the **IOC type** menu. This is the data that the feed will contain.

You can enable the use of STIX, Structured Threat Information Expression, a language and serialization format used to exchange cyber threat intelligence, if needed. 

![Feed](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/feed-3.png)

Next, select the confidence level for the feed, add the connection URL, method, and, if needed, connection header. 

Click **Save** to generate the private feed. 

<!-- ![Feed](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/feed-2.png)-->