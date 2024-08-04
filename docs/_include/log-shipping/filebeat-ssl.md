### Disabling SSL

Filebeat uses SSL/TLS to secure the communication between Filebeat and Logz.io. To disable SSL, modify the Filebeat configuration accordingly:

1. Open the Filebeat configuration file, typically located at `/etc/filebeat/filebeat.yml` (Linux) or `C:\ProgramData\Filebeat\filebeat.yml` (Windows).

2. Find the `output.logstash` section in the file.

3. Remove the # character at the beginning of the #ssl.enabled line to disable SSL. The line should now look like this: `#ssl.enabled: false`

4. Save the changes and restart the Filebeat service to apply the changes.