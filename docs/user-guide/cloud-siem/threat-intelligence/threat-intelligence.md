---
sidebar_position: 1
title: Threat Intelligence Feeds
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: View and manage threats and threat feeds in Logz.io
keywords: [SIEM, threat feeds, threats, feeds, managing threats, Security information]
---



Cloud SIEM cross references incoming logs against lists of known Indicators of Compromise (IOCs) to automatically detect threats. Whenever an IOC is detected, the original log is [enriched with the relevant details](/docs/user-guide/cloud-siem/malicious-ips/#log-enrichment-for-ips).

## IOC types

Your Cloud SIEM pulls lists of IOCs (Indicator of Compromise), aka Threat Intelligence feeds, from industry recommended sources that crowdsource and scrape the internet for malicious and suspicious indicators, including:

* IPs
* md5/sha1/sha256 hash signatures
* Domains
* URLs
* User-Agent headers

There is also an option to add your own **Private Feeds** for any of the above IOC types or another, custom type of your choice. Generally, custom IOCs are used to create lists of usernames or email addresses.

## Review your Threat Intelligence feeds

To view the list of feeds in your Cloud SIEM, go to **[SIEM > Threat Intelligence Feeds](https://app.logz.io/#/dashboard/security/threats/threat-intelligence-feeds)** from the navigation menu.

![TI feeds](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/feed-1.png)

You can search the table for IP addresses, domains, or URLs across the different feeds. The table includes the following information:

### Feed
This lists the names of different threat intelligence feeds.

### IOC type
IOCs, Indicator of Compromise, are identified by IP, hash, domain, URL, user-agent header, or other custom indicators.

### Confidence
Indicates the reliability score of the feed, assigned by Logz.io's team of security analysts.

### Investigation URL
URLs provided here are links to the sources of the feeds, where one can find more detailed information or investigate the threats further.

### Feed type
There are two different types of feeds:

* Logz.io threat feed is a predefined threat feed. It is included by default and cannot be edited. Logz.io threat feeds have a **Logz.io feed** tag.

* Private threat feed is a feed added by you or your team members. You can add, edit, or delete a private feed. Private feeds have a **Private feed** tag.

* Last sync

Logz.io syncs each feed once daily to look for updates. The table shows the date when the feed was last updated or synchronized.

## Private feeds

To add your own private feed, see [Preparing your feed](/docs/user-guide/cloud-siem/threat-intelligence/ioc-types/) for guidelines on compiling your lists of IOCs, and [Adding a private feed](/docs/user-guide/cloud-siem/threat-intelligence/private-feeds/) for instructions on setting up the sync.

<!-- <h2 tag="research"> Research sources for an IOC</h2>

You can look up specific IOCs to see in which feeds they appear. You can click the source links to look up additional details from each IOC reference.

![Look up an IOC](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/look-up-ioc-new-nav.png)
-->