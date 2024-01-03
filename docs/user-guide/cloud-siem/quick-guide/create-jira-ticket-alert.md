---
sidebar_position: 7
title: Create JIRA Tickets Through SIEM Alerts
description: Automatically create JIRA tickets through SIEM alerts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [SIEM, Security, Event Management, JIRA, Notifications, tickets, alerts, automatic]
---

You can configure your notification endpoints to automatically create JIRA tickets based on triggered alerts. 


## Pre-Requisites

* Make sure that you have the required permissions to create a task in the required JIRA board.

* Create an API token for your [Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

* Convert the API token using the following command:

  ```shell
  echo -n <YOUR-EMAIL>:<YOUR-ATLASSIAN-API-TOKEN> | base64
  ```
  Replace `<YOUR-EMAIL>` with the email for your Atlassian account and `<YOUR-ATLASSIAN-API-TOKEN>` with the API token for your Atlassian account.

## Add a JIRA notification endpoint

Navigate to your Logz.io [SIEM account > Settings > Notification endpoints](https://app.logz.io/#/dashboard/alerts/endpoints). 

Select **+ Add endpoint** to open the configuration wizard, and select **Custom**. 

![custom endpoint](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/custom-siem-endpoint.png)

Next:

* Name your endpoint
* Provide the URL to your JIRA board as follows: `https://<tenantname>.atlassian.net/rest/api/3/issue`. Replace `<tenantname>` with the name of your JIRA domain stated before `.atlassian`
* Select **POST** from the **method** menu
* Enter the following header into the **Headers** field: `authorization= Basic <API-TOKEN>`. Replace `<API-TOKEN>` with the API token to your Atlassian account
* Add the following code as the payload:

   ```json
   {
       "fields": {
           "project": {
               "key": <project board key>
           },
           "summary": "",
           "issuetype": {
               "name": <board specific issue type>
           },
           "description": {
               "type": "doc",
               "version": 1,
               "content": [
                   {
                       "type": "paragraph",
                       "content": [
                           {
                               "type": "text",
                               "text": ""
                           }
                       ]
                   }
               ]
           }
       }
   }
   ```
   
   Replace `<project board key>` with the key of your JIRA project board.
   Replace `<board specific issue type>` with the issue type specific to your project board.

Click **Add a new endpoint** to save it. 