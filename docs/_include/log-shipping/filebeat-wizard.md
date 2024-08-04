### Adding log sources to the configuration file

* Select your operating system - **Linux** or **Windows**.
* Specify the full log **Path**.
* Select a log **Type** from the list or select **Other** to create and specify a custom log type. 
  * If you select a log type from the list, the logs will be automatically parsed and analyzed. [List of types available for parsing by default](https://docs.logz.io/docs/user-guide/data-hub/log-parsing/default-parsing/#built-in-log-types).
  * If you select **Other**, contact support for custom parsing assistance.
* Select the log format - **Plaintext** or **Json**.
* (Optional) Enable the **Multiline** option if your log messages span
multiple lines. You’ll need to give a regex that
identifies the beginning line of each log.
* (Optional) Add a custom field. Click **+ Add a field** to add additional fields.

:::note
The wizard makes it simple to add multiple log types to a single configuration file. So to add additional sources, click **+ Add a log type** to fill in the details for another log type. Repeat as necessary.
:::

#### Filebeat 8.1+
If you're running Filebeat 8.1+, there are some adjustment you need to make in the config file:

1. Change `type` of the `filebeat.inputs` to `filestream` instead of `logs`:

```yaml
filebeat.inputs:
- type: filestream
  paths:
    - /var/log/*.log
```

2. **To configure multiline** nest the multiline settings under `parsers`:

```yaml
- type: filestream
  paths:
    - /var/log/*.log
  parsers:
  - multiline:
      type: pattern
      pattern: '^\d{4}-'
      negate: true
      match: after
```
