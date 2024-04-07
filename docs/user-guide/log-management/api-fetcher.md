---
sidebar_position: 11
title: Logz.io API Fetcher Configuration Guide
description: This guide outlines the steps for configuring the Logz.io API Fetcher to fetch and send data to Logz.io. 
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, opensearch dashboards, log analysis, observability]
---

The Logz.io API Fetcher supports both auth and OAuth APIs and includes specific implementations for Azure Graph, Cisco Secure X, and Office365 Message Trace reports.

This guide outlines the steps for configuring the Logz.io API Fetcher to fetch and send data to Logz.io. Our aim is to develop the API Fetcher as a generic tool capable of fetching data from any API endpoint. However, this presents significant challenges. If you encounter difficulties configuring the API Fetcher with a particular API endpoint, please reach out to our support team for assistance.

The configuration example provided focuses on Azure Graph Security Center alerts. However, the same methodology can be applied to other API types.

Below is a sample configuration template for Azure Graph, as found in our documentation and on GitHub:

```yaml
logzio:
  url: https://<<LISTENER-HOST>>:8071
  token: <<LOG-SHIPPING-TOKEN>>

oauth_apis:
  - type: azure_graph
    name: azure_test
    credentials:
      id: <<AZURE_AD_SECRET_ID>>
      key: <<AZURE_AD_SECRET_VALUE>>
    token_http_request:
      url: https://login.microsoftonline.com/<<AZURE_AD_TENANT_ID>>/oauth2/v2.0/token
      body: client_id=<<AZURE_AD_CLIENT_ID>>&scope=https://graph.microsoft.com/.default
            &client_secret=<<AZURE_AD_SECRET_VALUE>>&grant_type=client_credentials
      method: POST
    data_http_request:
      url: https://graph.microsoft.com/v1.0/auditLogs/signIns
      method: GET
    json_paths:
      data_date: createdDateTime
      settings:
        time_interval: 1
        days_back_fetch: 30
  - type: general
    name: general_test
    credentials:
      id: aaaa-bbbb-cccc
      key: abcabcabc
    token_http_request:
      url: https://login.microsoftonline.com/abcd-efgh-abcd-efgh/oauth2/v2.0/token
      body: client_id=aaaa-bbbb-cccc&scope=https://graph.microsoft.com/.default
            &client_secret=abcabcabc&grant_type=client_credentials
      method: POST
    data_http_request:
      url: https://graph.microsoft.com/v1.0/auditLogs/directoryAudits
    json_paths:
      data_date: activityDateTime
      data: value
      next_url: '@odata.nextLink'
    settings:
      time_interval: 1
    start_date_name: activityDateTime
```

## Configuration

### Add Your Logz.io Listener and Token

Insert your Logz.io listener URL and token into the config to begin the setup process.

```yaml
logzio:
  url: https://<<LISTENER-HOST>>:8071
  token: <<LOG-SHIPPING-TOKEN>>
```

{@include: ../../_include/log-shipping/log-shipping-token.md}
{@include: ../../_include/log-shipping/listener-var.html}

### Identify the Required API Endpoint

Use the official documentation to find the necessary API endpoint. For Azure Graph alerts, relevant documentation can be found at [Microsoft's official site](https://learn.microsoft.com/en-us/graph/api/resources/alert?view=graph-rest-1.0).

:::note
The following step is specifically for using Azure-based APIs. If you are utilizing a different provider, please refer to the respective provider's documentation.
:::

#### Search for the necessary permissions for the API

In this instance: https://learn.microsoft.com/en-us/graph/api/alert-list?view=graph-rest-1.0&tabs=http#permissions

The type of permissions required is `Application permissions`. For security purposes, it's advisable to select the least privileged permissions available. In this case, that would be `SecurityEvents.Read.All`.


#### Register a new application in Azure Active Directory

API communication in Azure is facilitated through Applications. To fetch data from the API, it's necessary to create and configure an Azure Application. To do this:

1. Navigate to **App registration** in the Azure portal.
2. Select **New registration** at the top of the page.
3. Enter a name for your app.
4. Click **Register**.

#### Create a client secret

1. Go to **Certificates & secrets** in the side menu.
2. Select **New client secret**.
3. Provide a description. A specific identifier, such as "secret for Logzio-Api-fetcher," is recommended.
4. Choose **Never** for the **Expires** option.
5. Click **Add**.

Note the value of the generated secret for later use.

:::note
The secret's value cannot be retrieved once you navigate away from this page.
:::

#### Configure the App's Permissions

1. Select **API permissions** from the side menu and click **Add a permission**.
2. Choose **Microsoft Graph > Application permissions**.
3. Utilize the application permissions identified in step 1: `SecurityEvents.Read.All`.
4. Proceed to **Add permissions**.
5. Select **Grant admin consent for Default Directory** and confirm with **Yes**.

:::note
Granting admin consent for Default Directory is an action limited to Azure administrators. If the Grant admin consent option is not available, consult your Azure administrator to make the necessary adjustments.
:::


### Set Up Authentication

Determine the necessary authentication method and details for the API. Azure Graph requires [OAuth for authentication](https://learn.microsoft.com/en-us/entra/identity-platform/scenario-daemon-acquire-token?tabs=java#protocol).

### Configure OAuth and API Requests

Following the information gathered, configure the OAuth and API request details in your configuration file.

```yaml
logzio:
  url: https://<<LISTENER-HOST>>:8071
  token: <<LOG-SHIPPING-TOKEN>>

oauth_apis:
  - type: azure_graph
    name: azure_test
    credentials:
      id: <<YOUR-ID>>
      key: <<YOUR-KEY>>
    token_http_request:
      url: https://login.microsoftonline.com/aassddeeedff/oauth2/v2.0/token
      body: client_id=<<YOUR-CLIENT-ID>>
        &scope=https://graph.microsoft.com/.default
        &client_secret=aassddeee
        &grant_type=client_credentials
      headers:
      method: POST
    data_http_request:
      url: https://graph.microsoft.com/v1.0/security/alerts
      method: GET
      headers:
```

:::note
If you are trying to configure an unimplemented API type, please use `general` as the API type.
:::

Replace `<<YOUR-ID>>`, `<<YOUR-KEY>>` and `<<YOUR-CLIENT-ID>>` with your specifics.

### Define JSON Paths

Specify the JSON paths for data extraction. These fields usually use the same value, which is the field name that holds the value for the log creation/generation date. For Azure Graph, please refer to the [Azure documentation](https://learn.microsoft.com/en-us/graph/api/resources/alert?view=graph-rest-1.0#properties). Following this documentation, the `CreatedDateTime` field is the relevant field name for our requirements:

```yaml
   json_paths:
      data_date: CreatedDateTime
   start_date_name: CreatedDateTime
```

:::note
When using `general` API type, additional fields are required for the json paths.
:::


### Adjust General Settings

Set the interval between fetch cycles (in minutes) and configure how many days back to fetch logs on the first run.

```yaml
    settings:
      time_interval: 1
      days_back_fetch: 30
```

### Create a Last Start Dates Text File

Prepare a text file named `last_start_dates.txt` to track the last start date for each API and save it in the same directory as the configuration file.

### Launch the Docker Container

Use Docker to run the Logz.io API Fetcher with the provided command.

```shell
docker run --name logzio-api-fetcher \
-v "$(pwd)":/app/src/shared \
logzio/logzio-api-fetcher
```


### Manage the Last Start Dates File

After each successful API fetch cycle, the `last_start_dates.txt` file will be updated with the last start date for the next iteration. This allows for a seamless continuation of data fetching, even after the container is stopped.

