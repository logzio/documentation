---
sidebar_position: 4
---


# Troubleshooting Filebeat


This section contains some guidelines for handling errors you may encounter when running Filebeat (version 7 or older).



### Problem: Path is locked

You have an error saying another beat locks the data path:

```shell
2022-01-01T10:10:10.711Z ERROR instance/beat.go:956 Exiting: data path already locked by another beat. Please make sure that multiple beats are not sharing the same data path (path.data).
```

###### Possible cause


This error means that your data path (`/var/lib/filebeats`) is locked by a different Filebeat instance. 

###### Suggested remedy

You need to kill the process. To do so, run:

``` shell
ps aux | grep filebeat
kill -9 <pid>
```


### Problem: Old logs are not visible

You can view logs that are 3 hours old (or older).

###### Possible cause

Your `ignore_older` setting is enabled, and set to 3 hours. When enabled, this option ignores any file that has not been updated since the selected time.


###### Suggested remedy

Disable or clean the `ignore_older` setting.

To disable it, set the ignore_older to 0:

`ignore_older: 0`

For existing logs, you can run `clean_*` to clean up state entries in the registry file, or `clean_inactive` to remove the state of previously harvested files from the registry file.

Note that running one of the clean commands might result in data loss. 


### Problem: Invalid yaml

There's an invalid config in your yaml file. For example:

``` yaml
ERROR instance/beat.go:802 Exiting: 1 error: error loading config file: invalid config: yaml: line 9: could not find expected ':'
```

###### Possible cause

Filebeat configuration yaml files require a particular syntax to run, and your file doesn't match the requirements. 

###### Suggested remedy

Test your configuration file and verify its structure. You can use a yaml validator, such as [YAML Lint](http://www.yamllint.com/). 


### Problem: Elasticsearch.output issue

You're encountering an issue when configuring the Elasticsearch output.

``` shell
output.elasticsearch:
  hosts: ["https://myEShost:9200"] 
```

###### Possible cause

You have `elasticsearch.output` configured in addition to the Logz.io output.

###### Suggested remedy

Filebeat doesn't know how to send data to 2 different outputs. To solve this, you'll have to re-configure your settings to have Logz.io as your default output.


### Problem: Not outputs defined

You see a `no outputs are defined` error:

```shell
2022/01/01 11:11:00.404226 publish.go:269: INFO No outputs are defined. Please define one under the output section.
```

###### Possible cause

Your output is not configured correctly.

###### Suggested remedy

You need to ensure that you're using `output.logstash`, and that it's appropriately configured. In some cases, you'll need to indent your code.

Instead of this:

```shell
output.logstash:
  hosts: ["listenerlogz.io:5015"]
  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

The code should look like this:

```shell
output:
  logstash:
    hosts: ["listener.logz.io:5015"]  
    ssl:
      certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

### Problem: Connection error

When you're trying to connect to Filebeat, you get the following error:

```shell
Permanent error: Post \"https://<<LISTENER-HOST>>:8053\": context deadline exceeded
meaning that the post request timeout.
```

###### Possible cause - Connectivity issue

This error can occur due to a connectivity issue, an issue with your TLS, or the server's inability to access Logz.io's listener. 

###### Suggested remedy


###### Check connection and ports 

First, check your shipper's connectivity as follows:

For macOS and Linux, use telnet to ensure your log shipper can connect to Logz.io listeners.


:::note
As of macOS High Sierra (10.13),
telnet is not installed by default.
You can install telnet with Homebrew
by running `brew install telnet`.
:::


Run this command from the environment you're shipping from, **after adding the appropriate port number**:

```shell
telnet listener.logz.io 5015
```
For Windows servers running Windows 8/Server 2012 and later, run the following command in PowerShell:


```shell
Test-NetConnection listener.logz.io -Port 5015
```

**The port number is 5015.**

###### Verify TLS encryption

Confirm that you have downloaded and placed the correct certificate in the correct location.

* To find the location of the certificate, open the filebeat.yml file and search for the field `certificate_authorities`. In our example configuration, we recommend the following location:
certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']

###### Check if your server has access to the Logz.io listener

From the actual server on which you are running Filebeat, run the following command to verify that you have proper connectivity:

```
telnet listener.logz.io 5015
```

For Windows servers running Windows 8/Server 2012 and later, run the following command in PowerShell:

```shell
Test-NetConnection listener.logz.io -Port 5015
```

| Good response | Bad response |
|---|---|
| Connected to listener-group.logz.io Escape character is '^]' | trying xxx.xxx.xxx.xxx.... |

To exit the screen, type `Ctrl+:` and type in `quit`.

If you cannot telnet to listener.logz.io on port 5015, please adjust your network settings to allow this communication. For a complete list of IPs used by the Logz.io listener, click here.

###### Example for validating connection established

```
$ sudo netstat -taupn | grep filebeat
tcp        0      0  172.17.0.2:44912            52.21.71.179:5015            ESTABLISHED 39/filebeat
```

If no output has been sent, something is wrong. Check your network connectivity again.

Manually put something in the shipped log file to see if it is sent:

```
echo hello >> /var/log/my_log_file.log
```



### Problem: Operation not permitted

You get the following error message when trying to access or change your yml file:

``` yaml
filebeat.yml: Operation not permitted
```


###### Possible cause - insufficient permissions

This error occurs when the user doesn't have the proper permission to access or edit the file.


###### Suggested remedy

You need to update the write permissions to the file. To do so, run the following command:

``` yaml
chmod go-w /etc/filebeat/filebeat.yml
```


### Zero metrics in the last 30 seconds

Your logs show a `Non-zero metrics in the last 30s` INFO message:

```shell
2022-05-13T07:16:27.805Z    INFO    [monitoring]    log/log.go:184    Non-zero metrics in the last 30s    
{"monitoring": {"metrics": {"beat":{"cpu":{"system":{"ticks":300,"time":{"ms":304}},"total":{"ticks":480,"time":{"ms":489},"value":0},"user":{"ticks":180,"time":{"ms":185}}},"handles":{"limit":{"hard":1048576,"soft":1024},"open":11},"info":{"ephemeral_id":"e778ccbc-94e5-467e-8e34-b1443402c50e","uptime":{"ms":30085},"version":"7.17.3"},"memstats":{"gc_next":19787632,"memory_alloc":11823552,"memory_sys":37831688,"memory_total":58462392,"rss":125288448},"runtime":{"goroutines":38}},"filebeat":{"events":{"added":105,"done":105},"harvester":{"open_files":1,"running":1,"started":1}},"libbeat":{"config":{"module":{"running":0}},"output":{"events":{"acked":103,"active":0,"batches":1,"total":103},"read":{"bytes":6268},"type":"logstash","write":{"bytes":8781}},"pipeline":{"clients":1,"events":{"active":0,"filtered":2,"published":103,"retry":103,"total":105},"queue":{"acked":103,"max_events":4096}}},"registrar":{"states":{"current":1,"update":105},"writes":{"success":2,"total":2}},"system":{"cpu":{"cores":6},"load":{"1":0.01,"15":0,"5":0,"norm":{"1":0.0017,"15":0,"5":0}}}}}}
```

###### Possible cause

Filebeat couldn't find any files or events.

You can view and manage your logging output by opening the `filebeat.yml` config file and navigating to the logging section inside it:

```yaml
logging.level: debug
logging.to_files: true
logging.files:
  path: /var/log/filebeat
```

For example, you can use the -e command line flag to redirect the output to standard error instead:

```yaml
filebeat -e
```

Change the default configuration file from filebeat.yml to a custom file of your choice. To use a different configuration file, use the -c flag:

```yaml
filebeat -e -c customfilebeatconfig.yml
```

Filebeat's default log level is INFO. To get all debugging output you can use *:

```yaml
filebeat -e -d "*"
```


To verify that Filebeat was unable to find any files or events:


###### Check if any files are monitored

For each log that Filebeat locates, it starts a harvester. A harvester is a key inside the JSON.

Locate the relevant `harvester.open_files` key. Inside it you should be able to see how many files are being monitored in the chosen path.

If the result is 0, Filebeat was unable to find the specific file or failed to find any files in the specific folder.

###### Check how many files are being monitored

Locate the `output.events` key, also located inside the JSON. If it shows 0, the output didn't recognize any new data.

If it contains any objects, you'll be able to see `write > success` and the total number of files sent. However, if the `success` total number is 0, Filebeat could not send any data.


###### Suggested remedy

Re-configure your Filebeat to make sure files are sent properly.