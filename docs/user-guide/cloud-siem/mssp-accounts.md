---
sidebar_position: 3
title: Create sub accounts as a Managed Security Service Provider (MSSP)
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Create and manage sub accounts as an MSSP
keywords: [mssp, siem, logz.io siem. security solution, Managed Security Service Provider, Security information and event management]
---


As a Managed Security Service Provider (MSSP) you can create a dedicated SIEM account for each logging account. This lets your customers access their data without the risk of accidentally seeing other customers’ data.

## Configure MSSP account


1. Sign in to Logz.io as an **administrator user**.

2. Go to **[Settings > Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts)**.

   <!-- ![Manage_accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/mssp-1.png) -->


3. In the **Plan Summary** section, select **Add sub account**.

   ![Manage_accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/mssp-3.png)

   * Give the new account a required name.

   * Select the required retention period for the account.

   * Select the required volume for the account. The default value is 1 GB.

   * Select the checkbox to enable the main account users to access this account.

   * Select the checkbox to make the account searchable from the main account.

   * If required, select the checkboxes to save the account utilization metrics and log size.

   * If required, add account names from which you want the new account to use dashboards, visualizations and saved searches.

4. Select **Create**.

   ![Manage_accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/mssp-4.png)

5. Scroll down the page to **Cloud SIEM plan** and select **Add security account**.

   <!-- >   ![Manage_accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/mssp-5.png)

   6. Select **Add security account**. -->

   ![Manage_accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/mssp-6.png)

   * Give the new account a required name

   * In the **Enable Cloud SIEM on these accounts** menu, select the account you created in the previous steps.

   * If required, add account names from which you want the new account to use dashboards, visualizations and saved searches.

7. Select **Create**.

   ![Manage_accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/mssp-7.png)

8. Go to your **Cloud SIEM** account in Logz.io. Click the account selection menu in the top right corner of the **Summary** screen.

   ![Manage_accounts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/mssp-8.png)

10. Select the new account. It takes a few minutes to get the account set up.
