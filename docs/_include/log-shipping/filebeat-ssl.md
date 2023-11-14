###### Disabling SSL for Filebeat log shipping

By default, Filebeat uses SSL/TLS to secure the communication between Filebeat and Logz.io. However, if you want to disable SSL, you can modify the Filebeat configuration accordingly.

To ship logs without using SSL in Filebeat:

1. Open the Filebeat configuration file for editing. The configuration file's location may vary depending on your operating system, but it is commonly located at `/etc/filebeat/filebeat.yml` (Linux) or `C:\ProgramData\Filebeat\filebeat.yml` (Windows).

2. Look for the `output.logstash` section in the configuration file.

3. Uncomment the # character at the beginning of the #ssl.enabled line to disable SSL. The line should now look like this:
  `#ssl.enabled: false`

4. Save the changes to the configuration file and restart the Filebeat service to apply the changes.