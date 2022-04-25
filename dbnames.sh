#!/bin/bash

echo "starting db show"
db_dbnames="dbnames.txt"

mysql -ubackup -p'**********' -e 'SELECT 'schema_name' from INFORMATION_SCHEMA.SCHEMATA WHERE 'SCHEMA_NAME' NOT in ("sys","information_schema" ,"mysql", "performance_schema" ,"SCHEMA_NAME" ,"mysql_innodb_cluster_metadata")' -h 1.1.1.102 -P6446 | awk '{ print $1 }'  >  /home/backup/${dbnames}
