

## Problem: No metrics received

No metrics are observed in your Logz.io account.

### Possible cause - Incorrect token and/or listener URL

Your Logz.io token and/or listener URL may be incorrect.

<h3 id="token-remedy"> Suggested remedy</h3>


1. Navigate to  **[Manage tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/shared) > [Data shipping tokens - Metrics](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=metrics)** and verify your account's metrics token and listener URL.

2. Check in the integration code whether the token and listener URL are specified correctly.

### Possible cause - Shipper connectivity failure

Your host/server may not be connected to your Logz.io listener.


<h3 id="connect-remedy"> Suggested remedy</h3>


Verify connectivity of your Logz.io listener as follows.

* For Linux and Mac servers, use `telnet`:

  ```shell
  telnet listener.logz.io <<PORT>>
  ```


* For Windows servers running Windows 8/Server 2012 and later, use the following command in PowerShell:

  ```shell
  Test-NetConnection listener.logz.io -Port <<PORT>>
  ```

  Replace `<<PORT>>` with the appropriate port nummber. For HTTPS communication use port 8053. For HTTP communication use port 8052.


### Possible cause - Incorrect listener endpoint

Your Logz.io listener may not be using the correct endpoint.

<h3 id="listener-remedy"> Suggested remedy</h3>


Change the endpoint of your listener from `https://<<LISTENER-HOST>>:<<PORT>>` to `http://<<LISTENER-HOST>>:<<PORT>>` or from `http://<<LISTENER-HOST>>:<<PORT>>` to `https://<<LISTENER-HOST>>:<<PORT>>`


{@include: ../log-shipping/listener-var.html}



### Possible cause - Pod is not running

One of your Kubernetes pods may not be running.

<h3 id="running-remedy"> Suggested remedy</h3>


Check if a required pod is runing by using the following command:

```shell
kubectl -n <<NAMESPACE>> get pods
```

Replace `<<NAMESPACE>>` with the name of the namespace for the required pod.

### Possible cause - Pod is not running

The `dotnet monitor`pod may not be running.

<h3 id="pod-remedy"> Suggested remedy</h3>


Check the logs of the pod that was created for dotnet monitor.

If the logs do not appear, check the pod's configuration by running:

```shell
dotnet monitor config show
```

If the configuration is correct, <a class="intercom-launch" href="mailto:help@logz.io">contact the Support team</a>.


