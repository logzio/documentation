---
id: Auditbeat
title: Auditbeat
overview: As its name suggests, auditd is a service that audits activities in a Linux environment. It's available for most major Linux distributions.
product: ['logs','siem']
os: ['linux']
filters: ['audit','on premise']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/linux.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

As its name suggests, auditd is a service that audits activities in a Linux environment.
It's available for most major Linux distributions.

This page gives instructions for replacing auditd with Auditbeat
so you can easily ship your audit logs to Logz.io.

#### Configuration

**Before you begin, you'll need**:
auditd,
root access

 

{@include: ../_include/log-shipping/certificate.md}

##### Install Auditbeat

Download and install [Auditbeat 7.7](https://www.elastic.co/guide/en/beats/auditbeat/7.7/auditbeat-installation.html).

##### Copy auditd rules

Go to the audit rules location in you auditbeat directory. The default location:

```js
cd /etc/auditbeat/audit.rules.d/
```

Rename the file `sample-rules.conf.disabled` to `audit-rules.conf`. It will hold your audit rules for Auditbeat:

```shell
cp sample-rules.conf.disabled audit-rules.conf
```

:::note
You need root privileges to interact with the auditd rules file.
:::
 

##### Add auditd as a source input and Logz.io as an output

Open the Auditbeat configuration file (`/etc/auditbeat/auditbeat.yml`). Here's how to do it using CLI.

Go back to the Auditbeat directory:

  ```shell
  cd /etc/auditbeat
  ```

Wipe the file auditbeat.yml clean. In other words, delete its content.

  ```shell
  su
  echo "" > auditbeat.yml
  exit
  ```

Copy and paste the following yml configuration to the auditbeat.yml file:

```shell
# ...
fields:
  type: auditd
  logzio_codec: json
  token: <<LOG-SHIPPING-TOKEN>>
fields_under_root: true
processors:
- rename:
    fields:
    - from: "agent"
      to: "beat_agent"
    ignore_missing: true
- rename:
    fields:
    - from: "log.file.path"
      to: "source_auditd"
    ignore_missing: true
#==========================  Modules configuration =============================
auditbeat.modules:
- module: auditd
  # Load audit rules from separate files. Same format as audit.rules(7).
  audit_rule_files: [ '${path.config}/audit.rules.d/*.conf' ]
  audit_rules: |
    ## Define audit rules here.
    ## Create file watches (-w) or syscall audits (-a or -A). Uncomment these
    ## examples or add your own rules.
    ## If you are on a 64 bit platform, everything should be running
    ## in 64 bit mode. This rule will detect any use of the 32 bit syscalls
    ## because this might be a sign of someone exploiting a hole in the 32
    ## bit API.
    #-a always,exit -F arch=b32 -S all -F key=32bit-abi
    ## Executions.
    #-a always,exit -F arch=b64 -S execve,execveat -k exec
    ## External access (warning: these can be expensive to audit).
    #-a always,exit -F arch=b64 -S accept,bind,connect -F key=external-access
    ## Identity changes.
    #-w /etc/group -p wa -k identity
    #-w /etc/passwd -p wa -k identity
    #-w /etc/gshadow -p wa -k identity
    ## Unauthorized access attempts.
    #-a always,exit -F arch=b64 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EACCES -k access
    #-a always,exit -F arch=b64 -S open,creat,truncate,ftruncate,openat,open_by_handle_at -F exit=-EPERM -k access
- module: file_integrity
  paths:
  - /bin
  - /usr/bin
  - /sbin
  - /usr/sbin
  - /etc
- module: system
  datasets:
    - package # Installed, updated, and removed packages
  period: 2m # The frequency at which the datasets check for changes
- module: system
  datasets:
    - host    # General host information, e.g. uptime, IPs
    - login   # User logins, logouts, and system boots.
    - process # Started and stopped processes
    - socket  # Opened and closed sockets
    - user    # User information
  # How often datasets send state updates with the
  # current state of the system (e.g. all currently
  # running processes, all open sockets).
  state.period: 12h
  # Enabled by default. Auditbeat will read password fields in
  # /etc/passwd and /etc/shadow and store a hash locally to
  # detect any changes.
  user.detect_password_changes: true
  # File patterns of the login record files.
  login.wtmp_file_pattern: /var/log/wtmp*
  login.btmp_file_pattern: /var/log/btmp*
#================================ Outputs =====================================
# Configure what output to use when sending the data collected by the beat.
#-------------------------- Elasticsearch output ------------------------------
# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```


{@include: ../_include//general-shipping/replace-placeholders.html}



##### Start Auditbeat

Stop auditd, and then start Auditbeat.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).



 
