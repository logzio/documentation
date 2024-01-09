---
sidebar_position: 2
title: Adding a Private Feed
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Add and manage private feeds in Logz.io SIEM
keywords: [SIEM, threat feeds, threats, feeds, managing threats, Security information]
---


You can enrich log threat detection by adding your own private feeds to those provided by Logz.io. To do so, you'll need to maintain files with lists of IOCs and host them online to make them accessible by HTTP/HTTPS to Logz.io. [Learn more](/docs/user-guide/admin/logzio-accounts/shared_repository/) about the SIEM Repository.

To share private feeds with your other SIEM accounts, include the feeds in a shared SIEM Repository account.

## Configure Logz.io to pull your private feed



### 1. Prepare a feed

Prepare a list of IOCs as described [here](/docs/user-guide/cloud-siem/threat-intelligence/ioc-types/) and host it where Logz.io can fetch it.

### 2. Add a new feed

Go to **[Threats > Threat Intelligence Feeds](https://app.logz.io/#/dashboard/security/threats/threat-intelligence-feeds)** from the top menu, and select the option **+ Add private feed**.

### 3. Configure the connection

Fill in the form to configure the connection. 

![Configure a private feed](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/feed-3.png)   

**About the feed**

* **IOC type** - Select one type. Supported types include IPs, DNSs (domain), URLs, md5/sha1/sha256 hash-based signatures, user-agent HTTP headers, and custom indicators of your choice.
* **Use STIX** - Toggle the option to use STIX format. _Structured Threat Information Expression_ (STIX™) is a language and serialization format that exchanges cyber threat intelligence (CTI). Logz.io currently supports a single IOC type per feed for this format. We recommend defining a separate private feed for each relevant IOC type in your STIX feed.
* **Confidence** - Select a reliability score for your feed.
* **Description** - Give some context for your feed. Adding contact info for the person who owns the feed is a good idea.

**Configure the feed connection**

* **URL** - Type in the URL where your feed is hosted. It provides the base URL for the HTTP/HTTPS request.
* **Method** - Select the request method for the HTTP/HTTPS request. Available methods: GET / POST / PUT.
* **Headers** - Add headers to the HTTP/HTTPS request if needed.

    Send 1 header per line. (In other words, separate headers with line breaks.)
  
    If your feed is password protected, you'll need to encode the credentials (username:password in base64) and pass them as an authorization header. See [this page for further instructions.

Click **Save** to generate the private feed. 

### 4. Give the sync some time

The first time Logz.io connects to your private feed, it will validate the connection and download the list within an hour.

After that, Logz.io will sync the feed once every 24 hours to look for updates.

If the connection fails at some point in the future, say if the feed is migrated to another hosting site or authorization headers are changed, you will be prompted to make the necessary changes.


### 5. Manage private feeds

To edit or delete a private feed, hover over the feed in the list,
  and click the pencil icon to edit, or the trash icon to delete.

If you delete a private feed, Logz.io will immediately stop using it to enrich logs.

![Configure a private feed](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/feed-info.png)