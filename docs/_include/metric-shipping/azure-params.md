###### Parameters

| Parameter | Description |
|---|---|
| client_id | Azure client ID. Replace `<<CLIENT-ID>>` with the `appId` value from step 3. |
| client_secret | Azure client secret. Replace `<<CLIENT-SECRET>>` with the `password` value from step 3. |
| tenant_id | Azure tenant ID. Replace `<<TENANT-ID>>` with `tenantId` from step 2. |
| subscription_id | Azure subscription ID. Replace `<<SUBSCRIPTION-ID>>` with `id` from step 2. |
| resources _and_ namespace | Replace `<<RESOURCE-TYPE>>` with the Azure services you want to monitor. You can find these values in the _Resource type_ column in [_Metrics and Dimensions Supported_](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/alerts-metric-near-real-time#metrics-and-dimensions-supported) from Microsoft. |
| fields.token | Your Metrics account token. {% include metric-shipping/replace-metrics-token.html %} |
| output.logstash.hosts | Your Logz.io listener host. {% include log-shipping/listener-var.html %}  |
