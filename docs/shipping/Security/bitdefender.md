---
id: Bitdefender
title: Bitdefender
overview: Bitdefender is an antivirus software. This integration allows you to send Bitdefender logs to your Logz.io SIEM account.
product: ['logs', 'siem']
os: ['windows', 'linux']
filters: ['Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/bitdefender.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

Bitdefender is an antivirus software. This integration allows you to send Bitdefender logs to your Logz.io SIEM account.

**Before you begin, you'll need**:

* Access to the [Bitdefender GravityZone Control Center](https://gravityzone.bitdefender.com/)
* A MAC or Linux Terminal
* An API key for the Bitdefender cloud instance
* A Cloud Access URL for the Bitdefender cloud instance

 

### Generate Bitdefender GravityZone API key

* Log in to your Bitdefender GravityZone Control Center.
* Click the username in the upper-right corner and select **My Account**.
* Go to **API keys** and click **+ Add** (top left).
* Enable **Event Push Service API**.
* Click **Save**.

### Copy the Bitdefender GravityZone API Access URL

Open **Control Center API** and copy the **Access URL**. Keep it handy for the following steps.

It is needed to replace the placeholder `<<ACCESS_URL>>` below.

<!--![Copy Bitdefender API ACCESS URL](https://dytvr9ot2sszz.cloudfront.net/logz-docs/security-integrations/bitdefender.png)-->


### Encode the API Key in Base64

Open a MAC or linux terminal. Run the echo command with the new API Key created in the previous section.

```
echo -n "[<API_KEY]>": | base64
```
Sample response (shortened for simplicity): `AeFgjU5N0Eg4rRMwFGG=AeFgjU5N0Eg4rRMwFGG=`

Copy the encoded API Kay. Keep it handy for the next step. It is needed to replace the placeholder `<<ENCODED_API_KEY_BASE_64>>` below.

### Configure event push settings

Use a CURL command to configure Bitdefender event push settings.

Edit the placeholders before running the command:

```
curl -k -X POST
<<ACCESS_URL>>/v1.0/jsonrpc/push
-H 'authorization: Basic <<ENCODED_API_KEY_BASE_64>>'
-H 'cache-control: no-cache'
-H 'content-type: application/json'
-d '{"params": {"status": 1,"serviceType": "cef","serviceSettings": {"url": "https://<<LISTENER-HOST>>:8071?token=<<LOG-SHIPPING-TOKEN>>&type=bitdefender_grzone","requireValidSslCertificate": false,"authorization": "Basic <<ENCODED_API_KEY_BASE_64>>"},"subscribeToEventTypes": {"adcloud":true,"antiexploit":true,"aph":true,"av":true,"avc":true,"dp":true,"endpoint-moved-in":true,"endpoint-moved-out":true,"exchange-malware":true,"exchange-user-credentials":true,"fw":true,"hd":true,"hwid-change":true,"install":true,"modules":true,"network-monitor":true,"network-sandboxing":true,"new-incident":true,"registration":true,"supa-update-status":true,"sva":true,"sva-load":true,"task-status":true,"troubleshooting-activity":true,"uc":true,"uninstall":true}},"jsonrpc": "2.0","method": "setPushEventSettings","id": "1"}'
``` 


{@include: ../../_include/general-shipping/replace-placeholders.html}


* `<<ACCESS_URL>>`: Replace with the Access URL copied in a previous step.
* `<<ENCODED_API_KEY_BASE_64>>`: Replace with the encoded key returned in the previous step. (Do NOT delete the term `basic`. It belongs there.)


### Expected returned value

The returned value should look like this:

```
{"id":"1","jsonrpc":"2.0","result":true}
```

### Contact support to request custom parsing assistance

The logs will require customized parsing so they can be effectively mapped in Open Search Dashboards.

[Email our support](mailto:help@logz.io?subject=Requesting%20parsing%20assistance%20for%20Bitdefender%20security%20logs&body=Hi!%20Please%20be%20in%20touch%20with%20further%20instructions%20for%20parsing%20Bitdefender%20security%20logs.%20Thanks!) to request custom parsing assistance.


 