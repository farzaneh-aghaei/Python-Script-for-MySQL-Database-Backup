# Python Script for MySQL all Databases Backup

This is a simple python script to backup MySQL all databases using the mysqldump utility. This script has been tested with the Python 3.5 and 2.7.17.

How to Use Script
This script is very easy to use, Download or copy this script on your local system and execute it with python. This script is capable to take multiple databases backup.

Multiple Databases Backup: To take multiple databases backup.

1- create an text file like /backup/dbnames.txt with bash script:


```
#!/bin/bash

echo "starting db dbnames"
db_dbnames="dbnames.txt"

mysql -ubackup -p'**********' -e 'SELECT 'schema_name' from INFORMATION_SCHEMA.SCHEMATA WHERE 'SCHEMA_NAME' NOT in ("sys","information_schema" ,"mysql", "performance_schema" ,"SCHEMA_NAME" ,"mysql_innodb_cluster_metadata")' -h 1.1.1.102 -P6446 | awk '{ print $1 }'  >  /home/backup/${dbnames}
```
```
# chmod +x dbnames.sh
# ./dbnames.sh
```

2- create an text file like /backup/dbnames.txt and add databases names one per line like below

## Python MySQL Backup Scriptls

Click here or use below command to download script from Github or you can simply copy below script.

## Execute Python Script
After downloading script make the script executable using following command

```
# chmod +x dbbackup.py
```
and execute this script like below
```
# python dbbackup.py
```
You can also schedule this script to run daily on regular interval using crontab. Add below command in crontab.


```Console
# crontab -e
```
```
0 */2 * * * /root/dbnames.sh
0 */2 * * * /usr/bin/python /root/dbbackup.py
```
