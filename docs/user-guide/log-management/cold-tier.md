---
sidebar_position: 11
title: Cold Tier
description: Search your archived data before re-ingesting it with Cold Tier
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, cold tier, storage, archive, opensearch dashboards, log analysis, observability]
---


Archived data usually contains a lot of information, and it can take time and resources to sift through it and find what you’re looking for.

With Cold Tier, you can seamlessly search cold storage data you've archived, view up to 1,000 raw logs that match your search query, and get the information you want. You can also re-ingest these logs to your Logz.io account to analyze and investigate them further.


![cold Tier fetched logs](https://dytvr9ot2sszz.cloudfront.net/logz-docs/cold-search/cold-search-close-up.png)

To start using Cold Tier, navigate to [Log analytics > Cold Tier](https://app.logz.io/#/dashboard/osd/discover/).


<!-- ### Cold search overview

Once you've [set up an AWS S3 archive](/user-guide/archive-and-restore/configure-archiving.html) and granted the relevant Cold search permissions, you can start using the feature from the main Log analytics dashboard.

Click on the Cold search button to open the relevant screen. 

-->

## Accessing Cold Tier

To get started with Cold Tier, contact your account manager or [Logz.io's support team](mailto:help@logz.io).

:::caution Important
All users can fetch raw logs from Cold Tier. However, only **account admins** and **Expert users** can re-ingest logs into the account.
:::

Once you activate Cold Tier, navigate to OpenSearch Dashboards and click on the **Cold Tier** button.

![cold Tier button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/cold-search/cold-tier-button-jul11.png)

Type the search term or query you'd like to use, and choose the relevant time frame. Your search result will only include data matching your exact search term.

The search is **case sensitive** and supports `“`, `AND`, `OR`, and `()` operators, but you can’t use nested brackets `(())`.

For example, you can run any of the following searches:

* ("blue sky" OR clouds) AND rain OR "thunder storms"
* "ATLAS" AND "Error"
* "bucketName" AND ("Error" OR "Warning")


Next, choose the time frame for your search. You can select a time frame of up to 7 days.

Click on **Fetch raw logs** to receive the logs that match your query criteria. You can click on each result to get more information about each log, including:

* Event ID
* AWS region
* Event version
* Source IP address
* Event source
* Error message
* Error code
* User agent 
* User identity
* Event type
* Type
* Tags
* Timestamp

And more.

![cold Tier log overviee](https://dytvr9ot2sszz.cloudfront.net/logz-docs/cold-search/cold-search-log-results.png)

To investigate the logs further, you can re-ingest them to your Logz.io account by clicking the **Re-ingest** button.

**Note that the re-ingested data will count against your daily quota and may result in an additional charge if you exceed your account's limit. Additionally, be aware that the maximum restore duration is limited to 24 hours.**

You can check your account usage and daily limit by navigating to [**Settings > Manage accounts**](https://app.logz.io/#/dashboard/settings/manage-accounts).

Once you click the **Re-ingest** button, you'll be asked to confirm your action. You can review the account name that will hold these re-ingested logs, the chosen time frame, your query, and the estimated size of re-ingested data. 

Click **Confirm** to approve and continue with the process. 

![cold Tier confirm](https://dytvr9ot2sszz.cloudfront.net/logz-docs/cold-search/confirmation-message.png)

This process might take a few minutes, during which you can continue using Logz.io. You'll get a notification via email once the process is complete, with a link to the relevant account in OpenSearch Dashboards.

:::note
Your re-ingested logs will be available to search and analyze from OpenSearch Dashboards for a period of **5 days**.
:::


## Troubleshooting Cold Tier

You might encounter an issue while fetching raw logs or re-ingesting them. Here are some common issues that can arise and how you can quickly resolve them:

<h3 id="max-limit"> Issue: Exceeded max limit of restored accounts</h3>

Cold Tier works with your cold storage archived accounts and has similar limitations. To re-ingest Cold Tier logs, you must have at least 1 available account in your restored accounts. Note that you can restore up to 5 accounts at a time.

<h3 id="max-remedy"> Suggested remedy</h3>

Ensure you have at least 1 available account to which you can restore the data. To check how many accounts you use, navigate to [Data Hub > Archive and restore > Restored account](https://app.logz.io/#/dashboard/tools/archive-and-restore) to review if you've exceeded your limit.

If you have exceeded your restored accounts limit, you can delete one or more accounts to use Cold Tier. 

If you wish to upgrade your existing quota, you can contact [Logz.io's support team](mailto:help@logz.io).


<h3 id="limit"> Issue: Limit exceeded</h3>

Re-ingesting logs process failed since you've exceeded your account's limit. This happens when you've reached your daily quota.

<h3 id="limit-remedy"> Suggested remedy</h3>


If your account has a [flexible volume](/docs/user-guide/admin/logzio-accounts/flexible-volume/), you can allocate available GB from one of the existing sub accounts.

Otherwise, you can update your plan and adjust your daily volume on the [Plan and usage](https://app.logz.io/#/dashboard/settings/plan-and-billing/plan) page.


<!-- ###### Additional resources


* [Read more](https://logz.io/blog/kibana-advanced/) about creating and running advanced searches in OpenSearch Dashboards.  -->