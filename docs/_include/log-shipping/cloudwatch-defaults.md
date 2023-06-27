###### Default settings

By default, we do not send logs of type START, END, REPORT.

If you prefer to send all log types, replace the method `_parse_cloudwatch_log` in the Lambda function with the following:

```py
def _parse_cloudwatch_log(log, additional_data):
    # type: (dict, dict) -> bool
    _add_timestamp(log)
    if LAMBDA_LOG_GROUP in additional_data['logGroup']:
        _extract_lambda_log_message(log)
    log.update(additional_data)
    _parse_to_json(log)
    return True
```
