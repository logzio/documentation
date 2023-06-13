---
sidebar_position: 3
---


# Logz.io DIY Parsing



Parsing is the process of breaking down your log message into smaller chunks of data,
placing each chunk into its own specific named field,
and enriching data with additional information such as geolocation.
Parsed logs can be more easily analyzed than raw data,
allowing you to create rich visualizations and helpful alerts.

Parsing is not necessary for all types of logs,
but if you use a custom or uncommon log type,
parsing can be an invaluable tool.




### Customize your log parsing with Logz.io Data Parsing

Create your own parsing rule sets for logs that are being ingested to your Logz.io account. Once validated on your end and on ours, your rule sets will be applied to your Logz.io account to transform your logs. 

 
:::note
You must be an account admin to apply a parsing rule set to an account.
**Logz.io Data Parsing requires access to the Logz.io public API** If your API access is disabled, contact Support for help. 
Community (free) accounts do not have access to Logz.io Data Parsing because the Logz.io public API is not available for Community accounts.
:::

### What is Sawmill and what is the Logz.io Data Parsing Editor?

The [Sawmill open source library](https://github.com/logzio/sawmill) is used for text transformations. 

A Sawmill rule set is composed of a series of steps that are applied to a specific log type. Each step is a Sawmill processor that performs an action, a transformation, or includes some logic to enrich your logs. You set the processor step order according to the transformations and changes you need to apply to meet your parsing requirements.

The collection of Sawmill processors can be found in the [Github wiki for the project.](https://github.com/logzio/sawmill/wiki)  

:::note
The syntax requirements for the Logz.io Data Parsing Editor differ from the examples provided in the Sawmil wiki: The Data Parsing Editor requires that all attributes and values within the JSON be surrounded by double quotes.
:::


### The Logz.io Data Parsing Editor

The Logz.io Data Parsing Editor tool works with the Logz.io public API and lets you: 

1. Create, access, and edit custom parsing rules for a log type, using Sawmill processors.
2. Build a parsing rule set for your logs from the available Sawmill processor options.
2. Test and validate the rule set to examine how it impacts your logs.
3. Submit the rule set to Logz.io so that it can be reviewed, validated, and then applied to your ingested logs.

**Logz.io Data Parsing** is available [**here**](https://parsing.logz.io/).

:::caution Important
Logz.io's Data Parsing tool has strict guidelines and requires additional fields that are `optional` in GitHub. For example, when using the Date Processor, you must specify the timezone parameter with the relevant time zone; `"timeZone": "Europe/Paris"`.
:::


### Field mapping data types

Field data type determines how each field is indexed and shown in OpenSearch Dashboards. Account admins can change the data types according to a predefined set of options:

![Choose field data type](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-mapping/mapping-fields-main-.png)

Changing a field's data type may affect any dashboards, visualizations, searches, alerts, optimizers, and integrations using that field.

#### Date data fields

:::note
Before changing, editing, and sending date data fields, contact **[Logz.io Support team](mailto:help@logz.io)**.
:::

There are additional restrictions for **date data field** types:

* Automatic date detection is disabled by default in dynamic mapping, which detects values as `string` instead of `date`.
* To avoid conflict between the mapping of date fields, the data type **must** be identical across all indices.

Therefore, to change the mapping of any field to a date field, contact **[Logz.io Support team](mailto:help@logz.io)** before sending the fields.


### Create a parsing rule set with Sawmill

This process creates a parsing rule set for the specified log type. The log type is a field used to differentiate the source of each log. You need to select one of your existing log types (or create a new log type) for the parsing rules. When you submit a rule set to be applied on the backend, only the logs of the selected log type are processed.



#### 1. Prerequisites


To use the Data Parsing Editor you need a Logz.io API token. To get an API token, you must be an admin of a Logz.io account and follow the instructions below: 

1. To work with the Logz.io public API, obtain or create an API token in the [Manage tokens page](https://app.logz.io/#/dashboard/settings/manage-tokens/api). We recommend that you create a dedicated API token for parsing tasks. 
   
    ![Manage API Tokens](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-and-mapping/manage-api-tokens3.png)

2. Select your region. You can look up your Logz.io account region in [**Settings > General settings > Account settings > Region**](https://app.logz.io/#/dashboard/settings/general).  


#### 2. Set up the Data parsing editor

In the [Data parsing editor](https://parsing.logz.io), click **Editor setup**.  

![Sample log process](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-and-mapping/editor_setup-sept2021.png)
The **Editor setup** screen opens.

![credentials and log info](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-and-mapping/parsing_cred-sept2021.png)

#### 3. Set up your credentials and sample log information


In the **Editor setup** screen:

1. Enter your API token and region information. 
2. Choose a log type from the list of log types that have been ingested into your Logz.io account or create a new log type. 
   + New log type: This option lets you add a custom string for a log type and enables you to assign parsing rules for future logs that are associated with the log type you add.  
   + Pre-built parsing: These log types are documented in the [Default parsing](https://docs.logz.io/user-guide/log-shipping/built-in-log-types.html) topic. You can select a pre-built parsing type and create additional rules that run _after_ the default rules for these types are executed. 

:::note
When you select a pre-built parsing rule, the original rule configuration is not displayed in the **Parsing rules workspace**. The log types list displays log types ingested by Logz.io in the last 24 hours.
:::

   ![Custom log type](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-and-mapping/new_logtype2.gif)

3. Add a sample log to use to validate your parsing rules.  The sample log can be a text or JSON string. To test different log formats, you can change the sample at any time. The **Load latest sample** option lets you use the previous log sample you entered.
   ![Load latest sample](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-and-mapping/load_latest-sept2021.png)  
4. Click **Start parsing** to save your changes and start building your rule set.



#### 4. Write parsing rules


You create your Sawmill rule set in the left panel of the editor screen, either by writing a new rule set or by editing a predefined rule set loaded to the panel. The created rule set must be a valid JSON file.

The editor supports autocomplete for existing Sawmill processors: Enter the start of a processor name, scroll through the options, and select the relevant option to load the full processor template.  

![Processor autocomplete](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-and-mapping/parse_autocomplete-sept2021.png)

Use **Auto re-format** to clean up your indentations. 

![Processor autoreformat](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-and-mapping/reformat_parsing-sept2021.png) 


#### 5. Validate your rule set


Once you're satisfied with your draft rule set, click **Validate your rules** to execute your rule set against the log sample you provided. 

:::note
The Logz.io backend has a sequence of rule sets that run on your logs: Some of the rule sets are system wide and may affect the final result you see.   Once validation is complete, you'll  be able to see the results in the **PARSED LOG** tab of the right panel. Use the display in the right panel to verify that your results reflect the parsed logs you expect to see.
:::

#### 6. Test parsing rules


The right panel is where you view and modify your log sample, and test how your rules are applied. 
![Testing parsing rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-and-mapping/test_parsing-sept2021.gif)
   
#### 7. Submit your rule set for review


To ensure that your parsing works properly, our Support team reviews your rule set for consistency and then either applies the rule set or contacts you if there are issues that need to be addressed.

**To send your rule set to Logz.io:** When you're done editing the parsing rules, add the email for the admin user associated with your Logz.io account, along with information about the parsing mechanism you created, and click **Submit**.


:::note
The parsing rules you create can only be applied to the Logz.io account that matches your API token, and are only valid for the log type you chose. To apply the parsing rules you create, you must be an admin for the account. 
:::

### Parsing rule examples

The goal of log parsing is to transform your log text into useable data fields so you can then run queries and refine query performance, and to extend the text in your logs to create data visualizations and dashboards. 


#### Example 1: Grok transformation


Grok parsing leverages regular expressions to enable you to name existing patterns or combine them into more complex patterns, or both.

Use grok parsing to transform a *regex* (regular expression) into human-friendly patterns. 
In this example, for the log sample: `2021-06-21T20:19:40.45+01:00 DEBUG This should be a log sample`, the resulting transformation is:  ![Grok parsing example](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-and-mapping/grok-parse-example_sept2021.gif)


###### Log sample


```js
2021-06-21T20:19:40.45+01:00 DEBUG This should be a log sample

```

###### Applied parsing rules


```json
{
    "steps": [
        {
            "grok": {
                "config": {
                    "field": "message",
                    "patterns": [
                        "^%{TIMESTAMP_ISO8601:time} %{LOGLEVEL:logLevel} %{GREEDYDATA:logMessage}$"
                    ]
                }
            }
        }
    ]
}
```
 
###### Parsed sample


```json
{
        "@timestamp": "2021-06-30T08:40:57.684+0000",
        "logLevel": "DEBUG",
        "logMessage": "This should be a log sample\n\n",
        "time": "2021-06-21T20:19:40.45+01:00",
        "message": "2021-06-21T20:19:40.45+01:00 DEBUG This should be a log sample\n\n",
        "type": "All-Prod-Health"
}
```

###### **Click here for additional [Grok pattern examples for log parsing](https://logz.io/blog/grok-pattern-examples-for-log-parsing/).**


#### Example 2: Conditional parsing 


Logz.io parsing lets you apply conditional logic, based on your original logs. 

In this example, the field is renamed based on the result of the _IF_ statment used to check specific conditions.
The resulting transformation is:  ![Conditional parsing example](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-and-mapping/conditional-parse-example_sept2021.gif)

###### Log sample


``` java
{
    "date": "02/May/2021:15:27:05 +0000",
      "userAgent": "aws-sdk-java/1.9.35 Linux/3.13.0-36-generic Java_HotSpot(TM)_64-Bit_Server_VM/25.40-b25/1.8.0_40",
    "requestURI": "PUT /1019/150921/150921T152904.log.gz HTTP/1.1",
    "message": "7455bc43ad9c06bf1a5dcd3a1c7a30acfe2ff1bdc028bbfed6ccc8817927767b backups-logzio-prod [02/May/2021:15:27:05 +0000] 54.86.133.203 arn:aws:iam::406095609952:user/backups-logzio-prod-user 7E37FD23C998A4E6 REST.PUT.OBJECT 1019/150921/150921T152904.log.gz \"PUT /1019/150921/150921T152904.log.gz HTTP/1.1\" 200 - - 37325 39 22 \"-\" \"aws-sdk-java/1.9.35 Linux/3.13.0-36-generic Java_HotSpot(TM)_64-Bit_Server_VM/25.40-b25/1.8.0_40\" -",
    "UA-os_patch": "0",
       "@timestamp": "2021-05-02T15:27:05.000Z",
    "requestID": "7E37FD23C998A4E6",
    "http_status": 200,
  "fragment": "test",
    "UA-device": "Other"
}
```

###### Applied parsing rules


```json
{
  "steps": [
    {
      "if": {
        "condition": {
          "fieldType": {
            "path": "fragment",
            "type": "string"
          }
        },
        "then": [
          {
            "rename": {
              "config": {
                "from": "fragment",
                "to": "fragment_str"
              }
            }
          }
        ]
      }
    }
  ]
}
```

###### Parsed sample

```json
{
        "date": "02/May/2021:15:27:05 +0000",
        "userAgent": "aws-sdk-java/1.9.35 Linux/3.13.0-36-generic Java_HotSpot(TM)_64-Bit_Server_VM/25.40-b25/1.8.0_40",
        "requestURI": "PUT /1019/150921/150921T152904.log.gz HTTP/1.1",
        "message": "7455bc43ad9c06bf1a5dcd3a1c7a30acfe2ff1bdc028bbfed6ccc8817927767b backups-logzio-prod [02/May/2021:15:27:05 +0000] 54.86.133.203 arn:aws:iam::406095609952:user/backups-logzio-prod-user 7E37FD23C998A4E6 REST.PUT.OBJECT 1019/150921/150921T152904.log.gz \"PUT /1019/150921/150921T152904.log.gz HTTP/1.1\" 200 - - 37325 39 22 \"-\" \"aws-sdk-java/1.9.35 Linux/3.13.0-36-generic Java_HotSpot(TM)_64-Bit_Server_VM/25.40-b25/1.8.0_40\" -",
        "type": "All-Prod-Health",
        "UA-os_patch": "0",
        "@timestamp": "2021-05-02T15:27:05.000Z",
        "fragment_str": "test",
        "requestID": "7E37FD23C998A4E6",
        "http_status": 200,
        "UA-device": "Other"
}
```


#### Example 3: Template parsing


In Logz.io parsing, templating lets you include your original field values with various transformations, wherever you decide it's relevant. 

You can also use the templating option to consolidate or transform separate field strings into a single, aggregated field. 
In this example, the resulting transformation consolidates several fields and timestamps: ![Template parsing example](https://dytvr9ot2sszz.cloudfront.net/logz-docs/parsing-and-mapping/template-parse-example_oct2021.gif)

###### Log sample 


```java
{
"the_date": "20/6/2021",
"the_time": "17:34"
}
```

###### Applied parsing rule 

```json
{
    "steps": [
        {
            "addField": {
                "config": {
                    "path": "timestamp",
                    "value": "{% raw %}{{the_date}} {{the_time}}{% endraw %}"
                }
            }
        }
    ]
}
```


###### Parsed example 


```json
{
        "the_time": "17:34",
        "@timestamp": "2021-06-21T14:29:08.369+0000",
        "type": "All-Prod-Health",
        "the_date": "20/6/2021",
        "timestamp": "20/6/2021 17:34"
}
```
