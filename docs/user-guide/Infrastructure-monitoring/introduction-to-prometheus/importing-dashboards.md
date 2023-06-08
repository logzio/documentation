---
sidebar_position: 2
---


You can import your existing dashboards to Logz.io via <!--a bulk process (using a Python script) or via --> a manual process.



  
### Importing multiple dashboards via script 
 
To enable easy migration, we created a Python [script](https://github.com/logzio/grafana-dashboard-migration-tool) to bulk upload your Grafana dashboards to our platform.


###### Notes
<!-- - Bulk import is supported for Grafana version 6 and above. -->
- Dashboards that include annotations, notification endpoints, and other  external resources imported without these resources during bulk  import. 
- Custom selection of dashboards is not possible with bulk import. All  your dashboard folders imported to a single folder within Logz.io.
<!-- - Grafana dashboards with schema version 14 or lower that include "row"  objects are not aded: You will receive a warning in the logs. We  recommend that you update your dashboard ma to the latest version. -->
- The`p8s_logzio_name` variable is not added to panel queries that don't  include filtering: will receive a warning in the logs.
- Some panel types are not supported by the Logz.io platform. If your  dashboard includes an pported panel type, you will receive a warning  in the logs. You may experience some issues le the panel renders in  Logz.io.   


<!-- ####  Bulk dashboard import procedure



From your Terminal, perform the following steps: 

##### Clone the repository.

Use the following command to clone the repo:

``` 
git clone https://github.com/logzio/grafana-dashboard-migration-tool.git
```

##### Switch directory.

Use the following command to switch to the repo directory:

```
cd grafana-dashboard-migration-tool
```

##### Run the script and configure environment variables.

Run the following script and configure your environment variables:

```
python main.py # If python 3 is your default version
```
```
python3 main.py # If python 2 is your default version
```

###### Bulk dashboard migration configuration parameters

| Environment variable | Description |
|---|---|
| GRAFANA_HOST | Your Grafana host without protocol specification (for example, localhost:3000) |
| GRAFANA_TOKEN | Your Grafana editor/admin API key: Find or create one under **Configuration > API keys** |
| LOGZIO_API_TOKEN | Your Logz.io account API token: You can find the API token under **Settings > Tools > Manage tokens > API tokens.** |
| REGION_CODE | Your Logz.io region code: You can look up your region code [here]( https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls) <br> For example, if your region is US, then your region code is `us`|


<!--tab end bulk -->


  
For the dashboard import to work smoothly, you'll need to change the name of the data source in your JSON file to the name of your Logz.io Metrics account. 
Your Metrics account information is located in the <a href ="https://app.logz.io/#/dashboard/settings/manage-accounts" target="_blank">Manage Accounts **(<i class="li li-gear"></i> > Settings > Manage accounts)**</a> page of your Operations workspace. ![Account settings navigation](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/p8s-account-token00.png)

For the record, notification endpoints and dashboard annotations are not imported: You'll need to recreate them in Logz.io.  See [Notification endpoints](/user-guide/integrations/endpoints.html) and [Annotations ](/user-guide/infrastructure-monitoring/annotations/)for more information. 

#### Importing individual dashboards



To import individual dashboards: 


##### Navigate to the Metrics tab.

Log into Logz.io and navigate to the **Metrics** tab.

##### Select the Import option.
In the left navigation pane, click <i class="fas fa-plus"></i> and select **Import**.
![Import dashboards to Logz.io](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/p8simport-dashboards.png)

  - To import your existing Prometheus dashboards, first export the relevant dashboards as JSON files, then click **Upload json file** and select the files to upload. 
    
    For related information see [Upload JSON logs]({{site.baseurl}}/shipping/log-sources/json-uploads). 
  - To import dashboards from Grafana.com, enter the relevant dashboard URL or ID in **Import via grafana.com** and **Load** them. 
