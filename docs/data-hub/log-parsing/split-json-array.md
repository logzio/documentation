---
sidebar_position: 1
---

# Split an array




Logs that are received as a JSON array cannot be properly parsed or mapping into fields.
This will impede your ability to search your logs efficiently.

Log data sent in an array cannot be used for configuring alerts or creating visualizations. This is why it's important to parse arrays into multiple log documents.

Some shipping methods offer the option to parse an array of JSON objects into discrete events. That way, the logs can be fully parsed and mapped by Logz.io.


### Shipping methods that support arrays

* The [Logz.io Kinesis Lambda function - The parameter `MESSAGES_ARRAY` controls the option to parse an array of JSON objects into discrete events.

#### Parsed array: before & after

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
