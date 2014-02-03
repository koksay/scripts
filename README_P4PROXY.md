# Perforce Proxy (p4p) init script

A simple init script that provide start, stop, restart and status commands for p4p.
Application can be downloaded from: http://www.perforce.com/product/components/perforce-proxy

## Getting started

Copy p4proxy file to /etc/init.d and edit the P4P_* parameters. Following variables must be set:

### P4P_PORT
Local proxy port number. Hostname/IP address would also be provided (e.g. host:port).

### P4P_REMOTE
Remote perforce server. Hostname or IP address with the port number should be provided.

### P4P_CACHEDIR
Local cache directory. Downloaded files will be written to that directory.

### P4P_BIN
Path of p4p binary.

### P4P_LOG
Path of the log file.

### P4P_USER
User name to run the script

### P4P_NAME
p4p binary name


## Script Usage

### Start
Starts the application:
````
/etc/init.d/p4proxy start
```

### Stop
Stops the application:
```
/etc/init.d/p4proxy stop
```

### Restart
Restarts the application:
```
/etc/init.d/p4proxy restart
```

### Status
Gets the status of the application (runnnig or stopped)
```
/etc/init.d/p4proxy status
```


## More information
More information about p4p usage can be gathered from:

http://www.perforce.com/perforce/r10.2/manuals/p4sag/09_p4p.html
