---
sidebar_position: 2
---


# Integrate with Siemplify



Integrate your Logz.io Cloud SIEM with [Siemplify](https://www.siemplify.co/) to automatically remediate incidents identified by Logz.io Cloud SIEM and increase observability into incident details.

Siemplify is an industry-leading Security Orchestration, Automation & Response (SOAR) solution that gives SOC teams the ability to manage Security Operations from a single platform.

## Advantages of the Logz.io - Siemplify integration

* Siemplify can automatically fetch Logz.io security events as new cases.
  If you prefer to be selective about event fetching, filter Logz.io security events by rule severity and/or rule name. Retroactive fetching is fully supported.

* Siemplify playbooks can trigger automated responses to cases originating in security events identifed by Logz.io.

* Get event details for a specific case. Any Siemplify playbook can use Logz.io actions to increase observability by querying logs for additional details. Siemplify users will be able to run log queries on their Logz.io data within Siemplify playbook actions and investigate events directly from the Siemplify interface.

* Implement the out-of-the-box **Logz.io Indicator Hunting Playbook** for guidance and best practices for conducting an investigation.

## Setting up the integration in Siemplify


**Before you begin, you'll need**:

* An active account with Siemplify.
* An active account with Logz.io.
* A valid [Logz.io API](https://app.logz.io/#/dashboard/settings/manage-tokens/api) token. Contact support if your account doesn't have one.

### 1. Add a Logz.io instance to your Siemplify workspace

To set up an integration with Logz.io as a **Default Environment**, you can add Logz.io directly from the Siemplify Marketplace.

In Siemplify, open the **Marketplace** and search for Logz.io. Select the cogwheel to configure a new instance.

![Add Logz.io from the Siemplify Marketplace](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/siemplify-marketplace.png)


Alternatively, if you prefer to add Logz.io as a **Shared Instance**, select the **cogswheel <i class="fas fa-cog"></i> > Integrations** from the top right menu. Select **Shared Instance** from the left menu, then select the plus ➕ to add a new instance. Select the **Logz.io integration** and save.

![Add Logz.io as a Shared Instance to your Siemplify workspace](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/siemplify-shared-instance.png)



### 2. Configure a Custom Trigger for the Siemplify playbook

Each playbook starts with a custom trigger from an incoming alert. 

To associate your playbook with a specific Logz.io alert, you need to initialize this trigger with the relevant Logz.io alert parameters and conditions in the first action panel of the playbook. 
For incoming Logz.io alerts, the event trigger is **`[Event.event_name] Equals <title of a specific alert >`**


![Custom Trigger panel1](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/playbook_custom-trigger.png)


1. In the playbook, click **Custom Trigger**.
![Custom Trigger empty state](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/siemplify_custom-trigger-empty.png)

2. Set the first placeholder to `[Event.event_name]` and select the `=` operator
![Custom Trigger setting event](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/siemplify_custom-trigger-setplace1.png)


3. Enter the specific Logz.io alert title that will trigger the playbook, and **Save** the trigger. 
![Custom Trigger event name](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/custotrigger_eventname-equals.png)

4. Your configured Custom Trigger is ready to activate a playbook. 
![Configured Custom Trigger ](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/siemplify_custom-trigger-for-alert.png)


### 3. Fill in the Logz.io integration panel

Fill in the Logz.io integration panel:

1. **Logz.io Security Token** - Enter the API token for your selected Security account.
2. **Logz.io Region** - Enter the 2-letter region code for your Logz.io account. [Look up your Logz.io account region code](https://docs.logz.io/user-guide/accounts/account-region.html).
3. **Logz.io Operations Token** - Enter the token for your selected Log Management account.
4. **Logz.io Custom Endpoint** - (Optional) Only relevant if you use a custom URL with the Logz.io API.
    * Enter the base url, without the direct path to the method
    * Relevant if your Logz.io endpoint is _NOT_ in the standard format of `api(region_code).logz.io/`.
    * Overrides `logzio_region`
5. Test your connection and save it!

![Logz.io integration panel for Siemplify](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/siemplify-configure-instance.png)


### 4. Create the Logz.io connector


Configure the Logz.io connector `LOGZ.IO fetch-security-events` to create cases in your Siemplify workspace from Logz.io security events.

Logz.io writes a security event log whenever a security rule triggers in your Logz.io Cloud SIEM account. The event log contains details about the rule that was triggered and the conditions it met.


![Siemplify Logz.io connector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/siemplify-connector.png)


1. Configure the connector to open new Siemplify cases based on security events triggered in Logz.io Cloud SIEM. You can make use of the filtering options to be selective about the events.

:::note
Set the `Run Every` field to **at least** 30 seconds.
:::


2. Enable the connector.

3. Save the connector. Siemplify will now fetch security events from Logz.io and open new cases accordingly.

    If you have configured retroactive fetching, there may be many cases created all at once, when you first enable the connector.

![Configure a Siemplify Logz.io connector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/siemplify-integrations-panel.png)


### 5. Use Logz.io Actions and Playbooks

The Logz.io integration offers a sample indicator hunting playbook for Siemplify. The playbook can be used to investigate and hunt Indicators of Compromise (IOCs), such as file hashes, suspicious IP addresses, domains, and URLS.

The playbook makes use of Logz.io actions that investigate events and output related information concerning the events, including involved users, IP addresses, host names, etc. that can be used to further research the indicators. Learn more about [investigating security events in Logz.io and by [API.


![Sample playbook for threat hunting with Logz.io](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/siemplify-playbook.png)



## Logz.io Actions for Siemplify



### Logzio-search-logs

Searches the logs in your Logz.io Operations account using the [Logz.io log search API](https://api-docs.logz.io/docs/logz/search/). Upon success, returns the logs that match the query as a paginated list in JSON format.

```
{
  "results": [
    {
      #log
    },
    ....
    {
      #log
    }
  ]
}
```

* **Script timeout**: 30 seconds
* **Parameters extracted from the integration**:
    * `logzio_operations_token`
    * `logzio_region`
    * `logzio_custom_endopoint`

:::note
If the timeframe for your search exceeds 48 hours, the search is only applied to the first 48 hours of that timeframe.
:::



| Parameter | Type | Required/Default | Description |
|---|---|---|---|
| from_time | String | Required | Earliest time to search. Accepts any format supported by the [Date parser python library](https://dateparser.readthedocs.io/en/latest/). Examples include unix timestamps in milliseconds, relative time such as `yesterday` or `24 hours ago`, or the format  `%Y-%m-%dT%H:%M:%S.%f`. |
| to_time | String | -- | Latest time to search. (Leave blank if relative time was used for the parameter `from_time`.) | 
| query | String | `*` | A search query written in valid Lucene syntax. Cannot be null - send a wildcard (*) if not using a search query. [For more info and limitations](https://api-docs.logz.io/docs/logz/search/) |
| size |  String | -- | Number of log results per query. Limited to 1000 logs. |

### Logzio-get-logs-by-event-id

Fetches the logs that triggered a security event using the [Logz.io Cloud SIEM API](https://api-docs.logz.io/docs/logz/security-rules). Upon success, returns the logs that match the query as a paginated list in JSON format.

```
{
  "results": [
    {
      #log
    },
    ....
    {
      #log
    }
  ]
}
```

* **Script timeout**: 30 seconds
* **Parameters extracted from the integration**:
    * `logzio_operations_token`
    * `logzio_region`
    * `logzio_custom_endopoint`


| Parameter | Type | Required/Default | Description |
|---|---|---|---|
| alert_event_id | String | Required | Unique GUID of the security event in your Logz.io security account. This is the ID of the event you want to investigate.|
| page_size | String | 25 | Controls the number of results per page. Valid inputs are 1 to 1000. Defaults to 25. |


### Json-adapter

Converts logs from your Logz.io accounts into a constant JSON format that is compatible with Siemplify’s playbooks. Receives fields to search, and a json to search them in.


The json must be received in the following format: 

```
{
    "results": [
        { 
            #log
        },
        .....
    ]
}

```



If the fields exist in the json, it returns them in the following format:

```
{
    "results": [
        { 
            "entityType": "field_from_json",
            "entityIdentifier": "value_from_json"
        },
        .....
    ]
}

```


* **Script timeout**: 30 seconds



| Parameter | Type | Required/Default | Description |
|---|---|---|---|
| fields_to_search | String | Required | Comma separated list of fields to search within the JSON. |
| raw_json | String | Required | Raw data in JSON format that is to be searched. |


### Ping

Pings Logz.io to test and validate connectivity to both your Logz.io security and operations accounts using the [Logz.io API](https://api-docs.logz.io/docs/category/logz-api/).

* **Script timeout**: 20 seconds.
* **Parameters extracted from the integration**:
    * `logzio_security_token`
    * `logzio_operations_token`
    * `logzio_region`
    * `logzio_custom_endopoint`




## Initializing the Logz.io playbook in Siemplify



### 1. Add the Logz.io Playbook

In your Siemplify workspace, import the playbook **Logz.io Indicator Hunting**.

The playbook makes use of the following actions:

* logzio-search-logs
* logzio Json-adapter
* Trigger - custom value
* Blocks
* Previous action conditions
* Instruction
* Case tag
* Create entity relationship


### 2. Initialize the block parameters

The playbook offers 4 use-cases (aka _branches_), each specific to a single indicator type: hash, URL, IP, and domain.


![Logz.io Indicator Hunting playbook for Siemplify should be initialized for a single indicator type](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/siemplify-initialize-block.png)


Configure the input parameter that will initialize the playbook.

| Action | Field | Description |
|---|---|---|
| Hash_initialize_block| PB_Hash | Initializes hash input parameters |
| URL_initialize_block| PB_Url | Initializes URL input parameters |
| IP_initialize_block| PB_IP | Initializes IP input parameters |
| Domain_initialize_block| PB_Domain | Initializes domain input parameters |

![Initialize the input block for the Logz.io playbook for Siemplify](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/siemplify-initialize-block2.png)


### 3. Initialize the json-adapter parameters

Whenever the initializing block is triggered, the `Logzio-search-logs` action will automatically run a search query in your Logz.io account for logs that match the output of the initializing block.

The action returns an array of relevant logs that matched the query in JSON format. The results are designed to help SOC analysts investigate the context surrounding the indicator.

The `Logzio-json-adapter` action translates Logz.io output into entities that conform to the Siemplify schema and can be reused by any Siemplify playbook and action.

In the example below, the action searches for `sourceHostName` in all the logs and extracts the results to a Siemplify entity.

:::note
You can provide more than 1 field, regardless of the log type.
:::


![Initialize the Logz.io json adapter for Siemplify](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/hash-json-adapter.png)


### 4. Investigate the indicator

In our example, the playbook ran an action to extract the field `sourceHostName` from all logs. As a result, the playbook identified another `hostname` affected by the same hash indicator. The red color indicates that the new station is involved and was discovered by the playbook.


![Output example for the Logz.io incident hunting playbook for Siemplify](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siemplify-integration/playbook-output-example.png)


##### Repeat for other indicator types


The **Logz.io Indicator Hunting Playbook** can help you track several indicator types. You'll need to repeat the process to initialize the playbook for each indicator type, as relevant.

:::note
The set of actions for each branch are indicator-specific, yet equivalent.
:::
