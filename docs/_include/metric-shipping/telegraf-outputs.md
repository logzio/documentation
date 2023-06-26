After you create the configuration file, configure the output plug-in to enable Telegraf to send your data to Logz.io in Prometheus-format. To do this, add the following code to the configuration file:

``` ini
[[outputs.http]]
  url = "https://<<LISTENER-HOST>>:8053"
  data_format = "prometheusremotewrite"
  [outputs.http.headers]
     Content-Type = "application/x-protobuf"
     Content-Encoding = "snappy"
     X-Prometheus-Remote-Write-Version = "0.1.0"
     Authorization = "Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>"
```
