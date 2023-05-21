---
sidebar_position: 2
---


# Understanding invalid log errors



The following guide will help you understand and troubleshoot some of the common log related issues you might encounter.

* toc list


### Field mapping types


### Mapping errors

Your logs are mapped daily, and each field is assigned a Dynamic or Explicit data type.

Dynamic mappings are automatically determined as logs are received, meaning the fields' data type is known. When a field is marked as Explicit, its data type is unclear.

Mapping errors occur when different data types are sent to the same field. For example, if field `weather` receives the numeric value `35`, then gets the value `hot`, it'll result in a mapping error since the same field can't contain two different types of inputs.

The **`type`** field is changed to **`logzio-index-failure`**,  and the **`tags`** field is added to the log to identify the issue.

![Fail log example](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/logzio-index-fail.png)

Here are some of the **common mapping errors** you might encounter and why they happen:

|**MPE**| **Description**|
|object mapping for [FIELD_NAME] tried to parse field [FIELD_NAME] as object, but found a concrete value|Field is mapped as a JSON object but is being sent as a string (or is being stringified by other means)|
|Can't get text on a START_OBJECT|Field is mapped as a string, but is sent as a JSON object|
|failed to parse field [FIELD_NAME] of type [DATA_TYPE]|Field is being mapped as one data type but being sent as another|
|Index -1 out of bounds for length 0|A field exists in the log with a dot "." in its name. For these cases, the system treats the field as an object when mapping it. For example: `log.level`, `app.kubernetes`, etc.|
|Numeric value (NUMBER) out of range of long (-9223372036854775808 - 9223372036854775807)|Field mapped as a number, but its value is outside the range of the "Long" data type|
|object field starting or ending with a [.] makes object resolution ambiguous|Some fields in the logs contain invalid characters in the name. For example: `.` , `,` , `_` , `#`|

##### Mapping errors through sub accounts



### Invalid logs

#### What causes an invalid log? 

When a log that includes specific issues is received, the log is flattened and ingested, the **`type`** field is changed to **`logzio-invalid-log`**,  and the **`tags`** field is added to the log to identify the issue.

![Invalid log example](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/invalid_log_eg-dec2021.png)

#### Invalid log tags

The tags in the table below explain the character or field issues that may cause a log to be labeled with the **`logzio-invalid-log`** field.

|Tag|Description|
|---|---|
| MAX_LOG_LINE_LENGTH | Exceeded the maximum of 500K characters per log|
| MAX_FIELD_KEY_SIZE *-or-*  INVALID_FIELD_VALUE_LENGTH | Exceeded the maximum of 32700 characters per field|
| MAX_JSON_DEPTH | Exceeded the maximum of 10 field nesting levels per log message |
| MAX_FIELDS_NUMBER *-or-*<  INVALID_FIELDS_NUMBER | Exceeded the maximum of 1000 fields per log message|
| FIELDS_MISSING | This error is related to required fields that are missing from your logs: For example, `@timestamp`.  Check if the parsing rules remove or rename the relevant fields. |
| ARRAY_INDEX_OUT_OF_BOUNDS_EXCEPTION | One of the field names in the log has a dot (**`.`**) as a name: To resolve the issue, flatten the field that the **`.`** is nested under.  If the field is inside an array, you'll need to flatten the array field.   For  example, you'd need to flatten the field `xxx.yyy` |







