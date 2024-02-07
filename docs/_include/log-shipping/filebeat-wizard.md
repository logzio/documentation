###### Adding log sources to the configuration file

For each of the log types you plan to send to Logz.io, fill in the following:

* Select your operating system - **Linux** or **Windows**.
* Specify the full **Path** to the logs.
* Select a log **Type** from the list or select **Other** and give it a name of your choice to specify a custom log type. 
  * If you select a log type from the list, the logs will be automatically parsed and analyzed. [List of types available for parsing by default](https://docs.logz.io/docs/user-guide/data-hub/log-parsing/default-parsing/#built-in-log-types).
  * If you select **Other**, contact support to request custom parsing assistance. Don't be shy, it's included in your plan!
* Select the log format - **Plaintext** or **Json**.
* (_Optional_) Enable the **Multiline** option if your log messages span
multiple lines. You’ll need to give a regex that
identifies the beginning line of each log.
* (_Optional_) Add a custom field. Click **+ Add a field** to add additional fields.

If you're running Filebeat 8.1+, the `type` of the `filebeat.inputs` is `filestream` instead of `logs`:

```yaml
filebeat.inputs:
- type: filestream
  paths:
    - /var/log/*.log
```

###### Add additional sources (_Optional_)

The wizard makes it simple to add multiple log types to a single configuration file. Click **+ Add a log type** to fill in the details for another log type. Repeat as necessary.

