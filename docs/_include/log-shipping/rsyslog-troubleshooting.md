## Troubleshooting

This section provides guidelines for handling errors when collecting logs for Rsyslog with SELinux configuration.

SELinux is a Linux feature for implementing access control security policies. In distributions like Fedora and RHEL, SELinux is enabled in Enforcing mode by default.

Rsyslog, a system process protected by SELinux, is restricted by default to sending data only to port 514/udp (the standard syslog port) and has limited access to files and directories beyond its initial configuration.

To send data to Logz.io in a SELinux environment, you need to add exceptions to allow:

* rsyslog to communicate with logz.io through the desired port.
* rsyslog to access the necessary files and directories.


### Issue not related to SELinux

The issue may not be caused by SELinux.

**Suggested remedy**

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

### Need to add exceptions

You may need to add exception to SELinux configuration to enable Logz.io.

**Suggested remedy**

1. Install the policycoreutils and the setroubleshoot packages:

```shell
# Installing policycoreutils & setroubleshoot packages
$ sudo yum install policycoreutils setroubleshoot
```

2. Check which syslog ports are allowed by SELinux:

```shell
$ sudo semanage port -l| grep syslog

output:
syslogd_port_t udp 514
```

3. Add a new port to policy for Logz.io:

```shell
# Adding a port to SELinux policies
$ sudo semanage port -m -t syslogd_port_t -p tcp 5000
```

4. Authorize Rsyslog directory:


```shell
# instructing se to authorize the /var/spool/rsyslog directory
$ sudo semanage fcontext -a -t syslogd_var_lib_t "/var/spool/rsyslog/*"
$ sudo restorecon -R -v /var/spool/rsyslog
```

5. Depending on the distribution, run the following command:

```shell
# instructing se to authorize /etc/rsyslog.d/*
$ sudo semanage fcontext -a -t syslog_conf_t "/etc/rsyslog.d/"

$ sudo restorecon -R -v /etc/rsyslog.d/

$ sudo semanage fcontext -a -t etc_t "/etc/rsyslog.d"

$ sudo restorecon -v /etc/rsyslog.d
```

6. Restart Rsyslog:

```shell
$ sudo service rsyslog restart
```
