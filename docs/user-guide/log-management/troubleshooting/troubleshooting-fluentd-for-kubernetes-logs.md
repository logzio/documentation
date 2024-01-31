---
sidebar_position: 3
title: Troubleshooting Fluentd for Kubernetes Logs
description: Learn about most common errors and remedies when running Fluentd for Kubernetes logs
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, troubleshooting, kubernetes, fluentd, invalid logs, log analysis, observability]
---

This section contains some guidelines for handling errors that you may encounter when trying to run Fluentd to collect Kubernetes logs.

### Problem: /file/path.log unreadable

The following error appears when running Fluentd:

```shell
/file/path.log unreadable. it is excluded and would be examined next time
```

<h3 id="#heading-id">Possible cause</h3>

You may need to add more volume and volume mount to your Daemonset.

<h3 id="#heading-id">Suggested remedy</h3>

<h4 id="check-node">Check on which node your pod is running</h4>

Find out on which node your Fluentd pod with the errors is running. To do so, use this command:

```shell
kubectl -n <<NAMESPACE>> get pod <<FLUENTD-POD-NAME>> -owide
```
  
<h4 id="connect-node"> Connect to the node</h4>

Connect to the node you found in the previous step (ssh, etc...).

<h4 id="log-path"> Find the log's path</h4>

1. Run the following command, to go to the logs directory:

```shell
cd /var/log/containers
```

2. Run the following command to display the log files symlinks:

```shell
ls -ltr
```

This command should present you a list of your log files and their symlinks, for example:

```shell
some-log-file.log -> /var/log/pods/file_name.log
```

3. Choose one of those logs, copy the symlink, and run the following command:

```shell
ls -ltr /var/log/pods/file_name.log
```

Again, this command will output the file and its symlink, or example:

```shell
/var/log/pods/file_name.log -> /some/other/path/file.log
```

This directory (`/some/other/path`) is the directory where your log files are mounted at the host. You'll need to add that path to your Daemonset.

<h4 id="mount-path"> Add the mount path to your Daemonset</h4>

1. Open your Daemonset in your preffered text editor.
2. In the `volumeMounts` section, add the following:

```yaml
- name: logextramount
  mountPath: <<MOUNT-PATH>>
  readOnly: true
```

Replace `<<MOUNT-PATH>>` with the directory path you found in step 3.

3. In the `volumes` section, add the following:

```yaml
- name: logextramount
  hostPath:
    path: <<MOUNT-PATH>>
```

Replace `<<MOUNT-PATH>>` with the directory path you found in step 3.

4. Save the changes.

<h4 id="deploy-new"> Deploy your new Daemonset</h4>

Remove your previous Daemonset from the cluster, and apply the new one.

:::info note
Applying the new Daemonset without removing the old one will **not** apply the changes.
:::



<h4 id="check-fluentd"> Check your Fluentd pods to ensure that the error is gone</h4>

```shell
kubectl -n <<NAMESPACE>> logs <<POD-NAME>>
```
  
###  Problem: You have reached your pull rate limit

vIn some cases (i.e. spot clusters) where the pods or nodes are replaced frequently, they might reach the pull rate limit for images pulled from dockerhub with the following error:

```yaml
You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: 
https://www.docker.com/increase-rate-limits
```

<h3 id="#heading-id">Suggested remedy</h3>


You can use the following `--set` commands to use an alternative image repository:

For the monitoring chart and the Telemetry Collector Kubernetes installation:

`--set logzio-fluentd.image=public.ecr.aws/logzio/logzio-fluentd`

For the fluentd chart:

`--set image=public.ecr.aws/logzio/logzio-fluentd`
