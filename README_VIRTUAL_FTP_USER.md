# User Management on BerkeleyDB for Virtual Vsftpd Users

You setup a vsftpd server with virtual users using Berkeley DB and PAM. Now, you are wondering how to add/remove users to the database. 

This simple python script manages that:

## Getting started

You already need to install bdb packages. For example, on RHEL:

```
yum install db4-utils db4
```

### Adding or updating a user:
```
./virtual_ftp_user.py -a <username> -p <password>
```

### Removing a user: 
if -r is provided, removes the home directory
```
./virtual_ftp_user.py -d <username> -r True
```

### Displaying all account information (usernames and their passwords):
```
./virtual_ftp_user.py -s
./virtual_ftp_user.py --showdb
```

### Which file?
You can specify the file name of the database in all of the above switches with -f:
```
./virtual_ftp_user.py -a <username> -p <password> -f /etc/vsftpd/virtual-virtual-user.db
```

You can also display help with -h or --help :
```
./virtual_ftp_user.py -h
Usage: virtual_ftp_user.py (-a <USERNAME> -p <PASSWORD> || -d <USERNAME> -r True || -s (True|False) ) -f <VIRTUALDB_FILE>

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -a USERNAME, --add=USERNAME
                        Username to add
  -d DEL_USER, --delete=DEL_USER
                        Username to delete
  -r REM_DIR, --remove_dir=REM_DIR
                        Should we remove the home directory of the deleted user?
  -p PASSWORD, --password=PASSWORD
                        User Password
  -s SHOWDB, --showdb=SHOWDB
                        Show Virtual User Database Content
  -f BSDDB_FILE, --file=BSDDB_FILE
                        Virtual User Database. Default is /etc/vsftpd/vsftpd-virtual-user.db
```
