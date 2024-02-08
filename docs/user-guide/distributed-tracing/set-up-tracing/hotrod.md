---
sidebar_position: 3
title: Sending Demo Traces With the HotROD Application
description: Send sample trace data with HotROD
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, traces, hotrod, sample data, tracing, observability, distributed tracing]
---

Not ready to instrument and deploy components? We've got you covered with an app that can send demo traces to your Distributed Tracing.

Using the **HotROD app** is so easy, and fast, that you'll be searching for traces in Logz.io within a few minutes of setting up the app! 



## What's HotROD demo application? ##

HotROD (Rides on Demand) is a demo application, created by Logz.io, that consists of several microservices that send requests to each other. The application illustrates the use of the OpenTracing API. It can be run standalone, but requires a Jaeger backend to view the traces. 

The _HotROD (Rides on Demand)_ application generates a web page with four customer buttons to order a car to the customer's business to pick up passengers or merchandise for delivery to a desired location. 

Clicking a button sends a request to the backend, which generates a trace. The app responds with the car license number and estimated time of arrival (ETA). 


![HotROD interface animation](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/tracing-hotrod-anim8.gif)

You have a web client ID in the upper left corner: A random session ID assigned by the Javascript UI. Each time you reload the page, it generates a new session ID.

In this example, the web client ID is 1465. All the ride requests generated in the session include this ID in a unique request ID. For each button click, you'll see the following information: 

+ Car license number
+ Driver ETA
+ Unique request ID, built from the session ID and a sequence number. 
+ Latency - how long the backend took to respond, as measured by the Javascript UI.


And once you open the Distributed Tracing tab, select a service, and **Find Traces**: ![HotROD traces in Logz.io](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/traces-hotrod-driver-results_oct21.png)

## Set up HotROD demo traces 

This topic explains how to set up the Logz.io HotROD sample application to send demo traces to your Distributed Tracing account. 

During this process, you'll use a simple yaml configuration file to deploy the following components in a Docker environment:

+ A modified HotROD sample application, based on the original project developed to demonstrate distributed tracing
+ The Jaeger agent
+ The Logz.io Jaeger collector

### Prerequisites

To run the demo configuration and deploy the components, you must have the following software installed: 

* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Docker](https://docs.docker.com/get-docker/)



### Update the **.env** file from the Logz.io tracing-demo repository

:::note
The **.env** file might be hidden.
:::


1. Use a **terminal** to grab the repo code using the git command:  `git clone https://github.com/logzio/tracing-demo.git` and change directories: `cd tracing-demo`.

2. Open the `.env` file and update the parameters with your preferred text editor.
3. Enter your Distributed Tracing account token in the first line: `ACCOUNT_TOKEN=Enter your account token here`. You must have admin permissions for the Logz.io account to view the **Manage tokens** page. If you’re not an admin user for the account, consult with an account admin to get the Distributed Tracing token information.
    
    1. From the **Tracing** or <i class="li li-gear"></i> (**Settings**) menu, go to **[Manage tokens > Data shipping tokens > Tracing](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=tracing)**
    ![Distributed Tracing tokens](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/tracing-token_sept2021.png)
    1. Find the Distributed Tracing account you want to ship to in the table, and copy the token.
4. Enter the correct 2-letter code for your region in the second line: `REGION_CODE=Enter your region code here`
    Look up the 2-letter code for your region in the Regions and Listener Hosts table.
   
   You can find the region code for your account in the General settings page, here >Settings > General**.

   ![Navigate to general settings](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/traces-general-settings_oct21.png	)


5. Save and close the updated **.env** file.

6. In the terminal, run `docker network create dockercompose_testcluster` to create a Docker network.

:::info
Updating the **.env** file in the Logz.io tracing demo repo with your tracing account token and region code 
adds your `jaeger-logzio-collector` definition parameters to the yaml file, in the `environment` section.
:::

### Deploy the demo app

_To run the demo:_

1. To start the HotROD demo app, in the terminal, run: `docker-compose up`.
2. To open the application, navigate to the main HotROD service at [127.0.0.1:18080](http://127.0.0.1:18080).
3. To send traces, click the buttons.
    You can view the logs in the foreground in the terminal. 
4. To stop the demo, run: `ctrl+c`.
5. To remove the docker container, run: `docker-compose down`.

### Command summary


|Command|Description|
|---------------|---------------|
|`docker-compose up`| Starts the demo app|
|`ctrl+c`|Interrupts the demo process |
|`docker-compose down`|Removes the demo container|


## Viewing demo traces

After sending traces with the tracing demo app, navigate to the [Distributed Tracing](https://app.logz.io/#/dashboard/jaeger/search?switchToAccountId=2977) tab in Logz.io, select a service and click **Find Traces** to view your generated trace data.    

## Additional resources

* [Learn more about Jaeger's HotROD project](https://github.com/jaegertracing/jaeger/tree/master/examples/hotrod).
* [See Read more about Logz.io's HotROD demo project](https://github.com/logzio/tracing-demo/blob/main/README.md).
* [Read about Logz.io Distributed Tracing platform](https://docs.logz.io/docs/user-guide/distributed-tracing/tracing-overview/why-tracing/).

