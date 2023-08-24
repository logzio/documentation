This section contains some guidelines for handling errors that you may encounter when trying to collect Python logs.

#### Problem: No logs received

No logs are observed in your Logz.io account.

##### Possible cause - Incorrect token and/or listener URL


Your Logz.io token and/or listener URL may be incorrect.

###### Suggested remedy


1. Navigate to  **[Manage tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/shared) > [Data shipping tokens - Logs](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs)** and verify your account's log shipping token and listener URL.

2. Check in the integration code whether the token and listener URL are specified correctly.


#### Problem: Exception while sending logs to Logz.io

The following error message appears:

```shell
Got exception while sending logs to Logz.io, Try (1/4). Message: HTTPSConnectionPool(host='listener.logz.io', port=8071): Max retries exceeded with url: /?token=<<LOG-SHIPPING-TOKEN>> (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x0000017839B4FD30>: Failed to establish a new connection: [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions.
```

##### Possible cause - Shipper connectivity failure


Your host/server may not be connected to your Logz.io listener.


###### Suggested remedy


Verify connectivity of your host/server as follows.

* For Linux and Mac servers, use `telnet`:

  ```shell
  telnet listener.logz.io <<PORT>>
  ```


* For Windows servers running Windows 8/Server 2012 and later, use the following command in PowerShell:

  ```shell
  Test-NetConnection listener.logz.io -Port <<PORT>>
  ```

  Replace `<<PORT>>` with the appropriate port nummber. For HTTPS communication use port 8053. For HTTP communication use port 8052.


If you see `Connected to listener-group.logz-data.com` the shipper can connect to the Logz.io listener. Enter `ctrl`+`c` and type `quit` to exit Telnet.

If you see `Trying xxx.xxx.xxx.xxx...` for more than 10 seconds, your machine is having trouble connecting to the Logz.io listener.



##### Possible cause - Cannot connect to Logz.io listener


Your host/server cannot connect to Logz.io listener and you see `Trying xxx.xxx.xxx.xxx...` for more than 10 seconds, when testing the connection.

###### Suggested remedy


Confirm that your firewall and network settings allow communication with the correct outbound port and the Logz.io listener IP addresses for your region.



##### Possible cause - Timeout parameter is too short



You can connect to Logz.io listener, but still see no logs.

###### Suggested remedy


Make sure you have the timeout setting increased as follows:

```yaml
network-timeout:20
timeout:10
logs_drain_timeout:10
```
