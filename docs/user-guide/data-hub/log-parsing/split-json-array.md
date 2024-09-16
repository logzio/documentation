---
sidebar_position: 2
title: Split an Array
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn how to split JSON arrays in Logz.io
keywords: [log, monitoring, parsing, arrays, json, default parsing, built in log types, log types, observability]
---

Logs received as a JSON array cannot be effectively parsed or mapped into fields, making it difficult to search logs efficiently.

When log data is sent with **nested objects** in an array, it **cannot** be used for configuring alerts or creating visualizations. Therefore, it's crucial to parse arrays into separate log documents.



Example of log data that **can** be used for alerts and visualizations:

```json
{
  "nested_arr": [
    {
      "field": "test"
    },
    {
      "field": "test2"
    }
  ]
}
```

Example of log data that **cannot** be used for alerts or visualizations:

```json
"array_field": [
    {
      "field": "test"
    },
    {
      "field": "test2"
    }
  ]
```


Some log shipping methods allow you to parse a JSON array into individual events, ensuring that logs are fully parsed and mapped by Logz.io for better use in alerts and visualizations.

### Shipping methods that support arrays

* The [Logz.io Kinesis Lambda function](https://docs.logz.io/shipping/log-sources/kinesis.html) - The parameter `MESSAGES_ARRAY` controls the option to parse an array of JSON objects into discrete events.

### Parsed array: before & after

Here's an example of a log document that contains an array in the `messages` field:

```yml
{
   "eventID": "shardId-000000000000:495451152434977345683475644582180062593244200961",
   "level": "warning",
   "eventVersion": "1.0",
   "eventSource": "aws:kinesis",
   "type": "kinesis_lambda",
   "timestamp":"time",
   "messages":[
      {
         "message":"something went wrong in service A",
         "level":"error"
      },
      {
         "message":"something went wrong also in service B",
         "level":"error"
      },
      {
         "message":"something totally normal happened in service C",
         "level":"info"
      }
   ]
}
```

If the shipper has the option to split the array enabled, the array will be split into separate logs with identical metadata. Note that as a result, the field `level` which would have been duplicated in the process, is merged and as a result the field from the array overrides the metadata field.

In this example, the original log will be split into the following 3 logs. These are the logs that will be mapped in Logz.io:

```
{
   "eventID": "shardId-000000000000:495451152434977345683475644582180062593244200961",
   "level": "error",
   "eventVersion": "1.0",
   "eventSource": "aws:kinesis",
   "type": "kinesis_lambda",
   "timestamp":"time",
   "message":"something went wrong in service A"
}
{
   "eventID": "shardId-000000000000:495451152434977345683475644582180062593244200961",
   "level": "error",
   "eventVersion": "1.0",
   "eventSource": "aws:kinesis",
   "type": "kinesis_lambda",
   "timestamp":"time",
   "message":"something went wrong also in service B"
}
{
   "eventID": "shardId-000000000000:495451152434977345683475644582180062593244200961",
   "level": "info",
   "eventVersion": "1.0",
   "eventSource": "aws:kinesis",
   "type": "kinesis_lambda",
   "timestamp":"time",
   "message":"something totally normal happened in service C"
}
```
