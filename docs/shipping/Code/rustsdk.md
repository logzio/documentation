---
id: Rust
title: Rust
overview: Deploy this integration to collect logs from your Rust application.
product: ['logs']
os: ['windows', 'linux']
filters: ['Code']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/rust-logo-blk.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

This guide explains how to configure your Rust application to send logs to Logz.io.

## Prerequisites

* A Rust application with logging capabilities.
* An active Logz.io account
* Your log shipping token
* Port `8071` available on your host system



## Add Dependencies

To send logs to Logz.io, add the required dependencies to your `Cargo.toml` file:

```yaml
[dependencies]
log = "0.4"
opentelemetry = "0.27"
opentelemetry-appender-log = "0.27"
opentelemetry_sdk = { version = "*", features = ["rt-tokio"] }
opentelemetry-otlp = { version = "*", features = ["http-proto", "reqwest-client", "reqwest-rustls"] }
rand = "0.8"
tokio = { version = "1", features = ["full"] }
```

## Configure Logging and Implement OTLP Communication

The following example demonstrates logging setup and sending logs to Logz.io:

```bash
use rand::Rng;
use opentelemetry_appender_log::OpenTelemetryLogBridge;
use opentelemetry_otlp::{WithExportConfig, WithHttpConfig};
use std::collections::HashMap;

fn roll_dice() -> i32 {
    let mut rng = rand::thread_rng();
    rng.gen_range(1..=6)
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync + 'static>> {

    let endpoint = "https://otlp-listener.logz.io/v1/logs";
    let api_token = "LOGZ_IO_TOKEN";

    let logger_provider = opentelemetry_sdk::logs::LoggerProvider::builder()
        .with_batch_exporter(
            opentelemetry_otlp::LogExporter::builder()
                .with_http()
                .with_endpoint(endpoint)
                .with_headers(HashMap::from([
                    ("Authorization".to_string(), format!("Bearer {}", api_token), ),
                ]))
                .build()?,
            opentelemetry_sdk::runtime::Tokio,
        )
        .build();
    
    let log_bridge = OpenTelemetryLogBridge::new(&logger_provider);

    log::set_boxed_logger(Box::new(log_bridge))?;
    log::set_max_level(log::LevelFilter::Info);

    let result = roll_dice();
    log::info!("Player is rolling the dice: {}", result);

    println!("Done");

    // Force flush any pending logs
    logger_provider.force_flush();

    Ok(())
}
```

Replace `LOGZ_IO_TOKEN` with the shipping token of the account.

If needed, update the `https://otlp-listener.logz.io/v1/logs` with the URL of [your hosting region](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region).


## Run the application and check Logz.io for logs

Run your application with `cargo run`. Give your logs some time to get from your system to ours.

Encounter an issue? See our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.
