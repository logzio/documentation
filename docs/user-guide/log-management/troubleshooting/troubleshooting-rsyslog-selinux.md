---
sidebar_position: 5
title: Troubleshooting Rsyslog - SELinux
description: Learn about common errors when running Rsyslog - SELinux configuration
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, troubleshooting, Rsyslog, SELinux, log analysis, observability]
slug: /log-management/troubleshooting/troubleshooting-rsyslog-selinux/
---

This section contains some guidelines for handling errors that you may encounter when trying to collect logs for Rsyslog - SELinux configuration.

SELinux is a Linux feature that allows you to implement access control security policies in Linux systems. In distributions such as Fedora and RHEL, SELinux is in Enforcing mode by default.

Rsyslog is one of the system processes protected by SELinux. This means that rsyslog by default is not allowed to send to a port other than 514/udp (the standard syslog port) has limited access to other files and directories outside of their initial configurations.

To send information to Logz.io properly in a SELinux environment, it is necessary to add exceptions to allow:

* rsyslog to communicate with logz.io through the desired port
* rsyslog to access the files and directories needed for it to work properly



### Possible cause - Issue not related to SELinux

The issue may not be caused by SELinux.

<h3 id="related-remedy"> Suggested remedy</h3>


Disable SELinux temporarily and see if that solves the problem.

Run the following command to check the current status of SELinux:

```shell
$ getenforce
```

SElinux's status can be in any of the following states: 

* Enforcing: SELinux is active and blocking the actions that do not match the policy
* Permissive: SELinux is active but is not blocking the actions that do not match the policy -- it only leaves logs indicating which actions had been performed
* Disable: SELinux is disabled

If SELinux is not in Enforcing mode, no other action is needed because it is not blocking communication to Logz.io

If SELinux is Enforced, try to disable it temporally and then restart rsyslog:

```shell
$ sudo setenforce 0
$ sudo service rsyslog restart
```

Check if rsyslog is working and that you see the logs in you account.

To re-enable SELinux, run: 

```shell
$ sudo setenforce 1
$ sudo service rsyslog restart
```

The above command only disables SELinux temporarily. To disable it completely, you will have to edit its configuration file. Although from a security point of view it's not recommended, if you want the changes to be permanent, edit the /etc/selinux/config file and restart the machine:

```shell
SELINUX=disabled 
SELINUX=permissive 
```

### Possible cause - Need exceptions to SELinux for Logz.io

You may need to add exception to SELinux configuration to enable Logz.io.

<h3 id="exception-remedy"> Suggested remedy</h3>


<h3 id="exception-1"> 1. Install the policycoreutils and the setroubleshoot packages</h3>


```shell
# Installing policycoreutils & setroubleshoot packages
$ sudo yum install policycoreutils setroubleshoot
```

<h3 id="exception-2"> 2. Check which syslog ports are allowed by SELinux</h3>

Run the command as in the example below:

```shell
$ sudo semanage port -l| grep syslog

output:
syslogd_port_t udp 514
```

<h3 id="exception-3"> 3. Add a new port to policy for Logz.io</h3>


```shell
# Adding a port to SELinux policies
$ sudo semanage port -m -t syslogd_port_t -p tcp 5000
```

<h3 id="exception-4"> 4. Authorize Rsyslog directory</h3>


```shell
# instructing se to authorize the /var/spool/rsyslog directory
$ sudo semanage fcontext -a -t syslogd_var_lib_t "/var/spool/rsyslog/*"
$ sudo restorecon -R -v /var/spool/rsyslog
```

Depending on the distribution, run the following command:

```shell
# instructing se to authorize /etc/rsyslog.d/*
$ sudo semanage fcontext -a -t syslog_conf_t "/etc/rsyslog.d/"

$ sudo restorecon -R -v /etc/rsyslog.d/

$ sudo semanage fcontext -a -t etc_t "/etc/rsyslog.d"

$ sudo restorecon -v /etc/rsyslog.d
```

<h3 id="exception-5"> 5. Restart Rsyslog</h3>


```shell
$ sudo service rsyslog restart
```
