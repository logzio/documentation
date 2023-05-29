---
sidebar_position: 5
---


# Threat Intelligence feeds


Cloud SIEM cross references incoming logs against lists of known Indicators of Compromise (IOCs) to automatically detect threats. Whenever an IOC is detected, the original log is [enriched with the relevant details](/user-guide/cloud-siem/malicious-IPs.html#log-enrichment).

## IOC types

Your Cloud SIEM pulls lists of IOCs, aka Threat Intelligence feeds, from industry recommended sources that crowdsource and scrape the internet for malicious and suspicious indicators, including:

* IPs
* md5/sha1/sha256 hash signatures
* Domains
* URLs
* User-Agent headers

There is also an option to add your own Private Feeds for any of the above IOC types or another, custom type of your choice. Generally, custom IOCs are used to create lists of usernames or email addresses.

### Review your Threat Intelligence feeds

To view the list of feeds in your Cloud SIEM, go to **SIEM > Threat Intelligence Feeds** from the navigation menu.

![TI feeds](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/add-private-feed-new-nav.png)

The list of feeds includes the feed name and description, IOC type, the calendar date when it was last synced, and a direct link to the source.

Logz.io syncs each feed once daily to look for updates. The last sync date is shown.

* To add your own private feed, see [Preparing your feed](/user-guide/siem/ioc-types/) for guidelines on compiling your lists of IOCs, and [Adding a private feed](/user-guide/cloud-siem/private-feeds.html) for instructions on setting up the sync.

#### Research sources for an IOC

You can look up specific IOCs to see in which feeds they appear. You can click the source links to look up additional details from each IOC reference.

![Look up an IOC](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/look-up-ioc-new-nav.png)
