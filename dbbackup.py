# Import required python libraries
import os
import time
import datetime
import glob
import shutil
# MySQL database details to which backup to be done. Make sure below user having enough privileges to take databases backup.
# To take multiple databases backup, create any file like /backup/dbnames.txt and put databses names one on each line and assignd to DB_NAME variable.
#Here is your public ip address
DB_HOST = '1.1.1.102'
#Here is the database user name
DB_USER = 'backup'
#Fill in the database password here
DB_USER_PASSWORD = '**********'
BACKUP_PATH = '/home/backup/'
#DB_PORT
DB_PORT = '6447'
#DB_COMMAND
#DB_COMMAND = 'SELECT 'schema_name' from INFORMATION_SCHEMA.SCHEMATA WHERE 'SCHEMA_NAME' NOT in ('sys','information_schema' ,'mysql', 'performance_schema' ,'mysql_innodb_cluster_metadata')'

# Getting current datetime to create seprate backup folder like "2022013-071334".
DATETIME = time.strftime('%Y%m%d%H%M')

TODAYBACKUPPATH = BACKUP_PATH + DATETIME

# Checking if backup folder already exists or not. If not exists will create it.

print ('del folder one month ago')
folders = glob.glob('Here is the path to be backed up/*')
#Delete the first three backup file directories
today = datetime.datetime.now()
for item in folders:
    try:
        foldername = os.path.split(item)[1]
        day = datetime.datetime.strptime(foldername, "%Y%m%d")
        diff = today - day
        if diff.days >= 30:
            shutil.rmtree(item)
    except:
        pass

print ("creating backup folder")
if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)

print ("checking for databases names file.")
with open('/home/backup/dbnames.txt') as DB_LIST:
    M=DB_LIST.readlines()
    DB_LIST=[]
    for i in M:
        DB_LIST.append(i.strip())

    for DB_NAME in DB_LIST:
        if os.path.exists(DB_NAME):
            file1 = open(DB_NAME)
            multi = 1
            print ("Databases file found...")
            print ("Starting backup of all dbs listed in file " + DB_NAME)
        else:
            print ("Databases file not found...")
            print ("Starting backup of database " + DB_NAME)
            multi = 0

# Starting actual database backup process.
with open('/home/backup/dbnames.txt') as DB_LIST:
    M=DB_LIST.readlines()
    DB_LIST=[]
    for i in M:
        DB_LIST.append(i.strip())

    for DB_NAME in DB_LIST:
        if multi:
            in_file = open(DB_NAME,"r")
            flength = len(in_file.readlines())
            in_file.close()
            p = 1
            dbfile = open(DB_NAME,"r")

            while p <= flength:
                db = dbfile.readline()   # reading database name from file
                db = db[:-1]         # deletes extra line
                dumpcmd = "/usr/bin/mysqldump  -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " -h" + DB_HOST + " -P"+ DB_PORT + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
                os.system(dumpcmd)
                p = p + 1
            dbfile.close()
        else:
            db = DB_NAME
            dumpcmd = "/usr/bin/mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " -h" + DB_HOST + " -P" + DB_PORT + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
            os.system(dumpcmd)

        print ("Backup script completed")
        print ("Your backups has been created in '" + TODAYBACKUPPATH + "' directory")                                                                      
