---
sidebar_position: 7
title: Cold Tier
description: Search your archived data before re-ingesting it with Cold Tier
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, cold tier, storage, archive, explore, log analysis, observability]
---

Archived data often contains a wealth of information, making it time-consuming and resource-intensive to sift through it. With Cold Tier, you can seamlessly search archived data in cold storage, view up to 1,000 raw logs matching your query, and gather the information you need. Additionally, you can re-ingest these logs to your Logz.io account for further analysis and investigation.



![cold Tier fetched logs](https://dytvr9ot2sszz.cloudfront.net/logz-docs/cold-search/cold-search-close-up.png)


:::info note 
Cold Tier is currently available for users with **Amazon S3 archives**. To get started, contact your account manager or [Logz.io's support team](mailto:help@logz.io).
:::

## Using Cold Tier


:::caution Important
All users can fetch raw logs from Cold Tier. However, only **account admins** can re-ingest logs into the account.
:::

To use Cold Tier, navigate to [Explore](https://app.logz.io/#/dashboard/explore), and click the **Cold Tier** button.


<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/cold-search/cold-tier-button.png" alt="cold-tier-button" width="700"/>

Enter your search term or query and select a time frame of up to 2 days. The search supports **case-sensitive** terms and operators like `"`, `AND`, `OR`, and `()` but does not allow nested brackets `(())`.

Your search result will only include data matching your exact search term.

For example, you can run any of the following searches:

* ("blue sky" OR clouds) AND rain OR "thunder storms"
* "ATLAS" AND "Error"
* "bucketName" AND ("Error" OR "Warning")


Next, choose the time frame for your search. You can select a time frame of up to 2 days. You can also choose the maximum number of results to display ranging from 50 to 1,000 lines.

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


**Note that the re-ingested data will count against your daily quota and may result in an additional charge if you exceed your account's limit.**

You can check your account usage and daily limit by navigating to [**Settings > Manage accounts**](https://app.logz.io/#/dashboard/settings/manage-accounts).

Once you click the **Re-ingest** button, you'll be asked to confirm your action. You can review the account name that will hold these re-ingested logs, the chosen time frame, your query, and the estimated size of re-ingested data. 

Click **Confirm** to approve and continue with the process. 

![cold Tier confirm](https://dytvr9ot2sszz.cloudfront.net/logz-docs/cold-search/confirmation-message.png)

This process might take a few minutes, during which you can continue using Logz.io. You'll get a notification via email once the process is complete, with a link to the relevant account in Explore.

:::note
Your re-ingested logs will be available to search and analyze from Explore for a period of **5 days**.
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
