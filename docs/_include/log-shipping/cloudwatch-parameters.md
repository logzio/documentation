| Parameter | Description | Required/Default |
|---|---|---|
| LogzioToken | Your Logz.io account token. {@include: ./log-shipping-token.html}  | Required |
| LogGroup | CloudWatch Log Group name from where you want to send logs.  | Required |
| LogzioListenerUrl | Listener host, and port (for example, `https://<<LISTENER-HOST>>:8071`). | Required |
| LogzioType | The log type you'll use with this Lambda. This can be a [built-in log type](https://docs.logz.io/user-guide/log-shipping/built-in-log-types.html), or a custom log type. You should create a new Lambda for each log type you use. | `logzio_apprunner_logs` |
| LogzioFormat | `json` or `text`. If `json`, the Lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields. | `text` |
| LogzioSendAll | By default, we do not send logs of type `START`, `END`, `REPORT`. Change to `true` to send all log data. | `false` |
| LogzioCompress | Set to `true` to compress logs before sending them. Set to `false` to send uncompressed logs. | `false` |
| LogzioEnrich | Enrich AppRunner events with custom properties, formatted as `key1=value1;key2=value2`. | -- |