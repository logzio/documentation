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

For Filebeat 8.1+, the `type` of the `filebeat.inputs` is `filestream` instead of `logs`:

```yaml
filebeat.inputs:
- type: filestream
  paths:
    - /var/log/*.log
```

### Add additional sources (_Optional_)

The wizard lets you add multiple log types to one configuration file. Click **+ Add a log type** and repeat as needed.











