# this fold is for local delopy usage

## install Docker and docker compose on Linux [Ubuntu](https://docs.docker.com/desktop/install/ubuntu/)

### Install Docker Desktop on Ubuntu

'''sudo dpkg --configure -a'''
'''sudo apt install gnome-terminal'''

### Install Docker Desktop

sudo apt-get update

### all ready

(sudo systemctl start docker)

docker-compose up

## mysql database

docker exec -it backend-mysql bash
mysql -u root -p

mysql -u datasetdb -p

### [Got a packet bigger than 'max_allowed_packet' bytes](https://stackoverflow.com/questions/93128/mysql-error-1153-got-a-packet-bigger-than-max-allowed-packet-bytes)

TINYBLOB: maximum length of 255 bytes
BLOB: maximum length of 65,535 bytes
MEDIUMBLOB: maximum length of 16,777,215 bytes
LONGBLOB: maximum length of 4,294,967,295 bytes

mysql --max_allowed_packet=100M -u root -p

set global net_buffer_length=1000000; 
set global max_allowed_packet=1000000000;

### mysql queries

use backend_db;

CREATE TABLE examples_table (
    FileIndex int NOT NULL AUTO_INCREMENT,
    FileFullName varchar(120) NOT NULL,
    FileName varchar(100) NOT NULL,
    FileFormat varchar(20) NOT NULL,
    FileData LONGBLOB,
    FileExportData LONGBLOB,
    FileCategory varchar(50),
    CreatedTime DATE,
    Note varchar(255),
    UNIQUE (FileIndex),
    PRIMARY KEY (FileFullName)
);

mysql> describe examples_table;
+----------------+--------------+------+-----+---------+----------------+
| Field          | Type         | Null | Key | Default | Extra          |
+----------------+--------------+------+-----+---------+----------------+
| FileIndex      | int          | NO   | UNI | NULL    | auto_increment |
| FileFullName   | varchar(120) | NO   | PRI | NULL    |                |
| FileName       | varchar(100) | NO   |     | NULL    |                |
| FileFormat     | varchar(20)  | NO   |     | NULL    |                |
| FileData       | longblob     | YES  |     | NULL    |                |
| FileExportData | longblob     | YES  |     | NULL    |                |
| FileCategory   | varchar(50)  | YES  |     | NULL    |                |
| CreatedTime    | date         | YES  |     | NULL    |                |
| Note           | varchar(255) | YES  |     | NULL    |                |
+----------------+--------------+------+-----+---------+----------------+
9 rows in set (0.01 sec)

