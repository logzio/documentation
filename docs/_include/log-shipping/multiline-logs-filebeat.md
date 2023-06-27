### Configuring Filebeat to concatenate multiline logs

Filebeat splits multiline logs by default. If your original logs span multiple lines, you may find that they arrive in your Logz.io account split into several partial logs.

Filebeat offers configuration options that can be used to concatenate multiline logs.
The configuration is managed differently, depending on your deployment method:

* **Standard configuration**: If you are using a standard configuration (but not autodiscover), use an explicit configuration. [Configuration options](https://www.elastic.co/guide/en/beats/filebeat/current/multiline-examples.html#multiline-examples) from Filebeat's official documentation.
  
  When using an explicit configuration, you will need to create a single regex expression that covers all of your pods. It also means that Filebeat will need to be reconfigured more often, with the introduction of every new use case.

* **Autodiscover configuration**: If you are using autodiscover hints & annotations, add an annotation to your deployment. [Configuration options](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-autodiscover-hints.html) from Filebeat's official documentation.

  Hints and annotations support the option to manage regex expressions separately for each component. This greatly simplifies the process, making it possible to add a dedicated regex expression to each pod, without needing to change anything on Filebeat itself.

###### Example

The following is an example of a multiline log sent from a deployment on a k8s cluster:

```shell
2021-02-08 09:37:51,031 - errorLogger - ERROR - Traceback (most recent call last):
File "./code.py", line 25, in my_func
1/0
ZeroDivisionError: division by zero
```

Filebeat's default configuration will split the above log into 4 logs, 1 for each line of the original log. In other words, each line break (`\n`) causes a split.

You can overcome this behavior by configuring Filebeat to meet your needs.

### Example of an explicit configuration for concatenating multiline logs

To add an explicit configuration to your Filebeat, edit your `filebeat.yml` file in a text editor and make the appropriate changes under the `filebeat.input` section.

For the above example, we could use the following regex expression to demarcate the start of our example log. This configuration example is set to identify the first log in a multiline log and concatenate the log lines that follow until it identifies the next log that matches the regex expression. In other words, there is no explicit regex expression to demarcate the _end_ of a multiline log.


```shell
filebeat.inputs:
- type: container
  paths:
    - /var/log/containers/*.log
  processors:
    - add_kubernetes_metadata:
        host: ${NODE_NAME}
        matchers:
        - logs_path:
            logs_path: "/var/log/containers/"
  multiline.type: pattern
  multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}'
  multiline.negate: true
  multiline.match: after
```

 See Filebeat's official documentation for additional [configuration options](https://www.elastic.co/guide/en/beats/filebeat/current/multiline-examples.html#multiline-examples).


### Example for using hints & annotations to concatenate multiline logs

If you're using Filebeat autodiscover hints, you can use annotations to identify multiline logs and concatenate them.

You will need to first configure Filebeat to enable the hints system, and add annotations to the relevant components when you deploy them to your cluster.


##### Enable Filebeat's hints system

First, enable Filebeat's hints system. In your `filebeat.yml` file, set `hints.enabled: true` under the `filebeat.autodiscover` section. For example:


```shell
filebeat.autodiscover:
	providers:
	  - type: kubernetes
	    node: ${NODE_NAME}
	    hints.enabled: true # This part enables the hints
	    hints.default_config:
	      type: container
	      paths:
	        - /var/log/containers/*-${data.kubernetes.container.id}.log
```

##### Add multiline annotations to your deployment

Whenever you plan to deploy a component to your cluster and want the hints system to detect the multiline logs, you'll need to add multiline annotations.


For the above log example, you can add the following annotations to your deployment:

```shell
annotations:
  co.elastic.logs/multiline.type: 'pattern'
  co.elastic.logs/multiline.pattern: '^[0-9]{4}-[0-9]{2}-[0-9]{2}'
  co.elastic.logs/multiline.negate: 'true'
  co.elastic.logs/multiline.match: 'after'
```

The above configuration ensures that Filebeat will look for log lines that match the regex under `multiline.pattern` and concatenate all subsequent lines, until it reaches the next regex match. 


See Filebeat's official documentation for additional [configuration options](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-autodiscover-hints.html).
