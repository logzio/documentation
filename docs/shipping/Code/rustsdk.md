---
id: Rust
title: Rust
overview: Deploy this integration to collect logs from your Rust SDK application.
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
env_logger = "0.10"
reqwest = { version = "0.11", features = ["blocking", "json"] }
serde_json = "1.0"
chrono = "0.4"
```

## Configure Logging and Implement HTTP Communication

The following example demonstrates logging setup and sending logs to Logz.io:

```bash
use log::{info, warn, error};
use reqwest::blocking::Client;
use serde_json::json;
use std::env;

const LOGZ_IO_URL: &str = "https://listener.logz.io:8071/?token=";

fn main() {
    // Initialize logger
    env_logger::init();

    // Example usage
    info!("Application started");
    send_log_to_logzio("info", "Application started successfully.");
}

fn send_log_to_logzio(level: &str, message: &str) {
    let token = env::var("LOGZ_IO_TOKEN").expect("LOGZ_IO_TOKEN must be set");
    let client = Client::new();
    let payload = json!({
        "message": message,
        "level": level,
        "timestamp": chrono::Utc::now().to_rfc3339(),
    });

    let url = format!("{}{}", LOGZ_IO_URL, token);
    match client.post(&url).json(&payload).send() {
        Ok(response) if response.status().is_success() => {
            println!("Log sent successfully to Logz.io.");
        }
        Ok(response) => {
            eprintln!("Failed to send log: {}", response.status());
        }
        Err(e) => {
            eprintln!("Error occurred while sending log: {}", e);
        }
    }
}
```

Replace `LOGZ_IO_TOKEN` with the shipping token of the account. 

## Run the application and check Logz.io for logs

Run your application with `cargo run`. Give your logs some time to get from your system to ours.

## Troubleshooting

### Missing blocking Module:

Ensure you include the blocking feature in the reqwest dependency in Cargo.toml:

```bash
reqwest = { version = "0.11", features = ["blocking"] }
```

### `json` Method Not Found:

Enable the json feature in the reqwest dependency:

```bash
reqwest = { version = "0.11", features = ["blocking", "json"] }
```

### Missing `chrono` Crate:

Add the chrono crate to your Cargo.toml:

```yaml
chrono = "0.4"
```

### Environment Variable Not Set:

Make sure `LOGZ_IO_TOKEN` is exported in your environment:

```yaml
export LOGZ_IO_TOKEN="<Your_Logz.io_Token>"
```

### Network Issues:

Verify that your application can connect to `https://listener.logz.io:8071`.

Check firewall and network rules if needed.