# MySQL and replication

The configuration of replication server
Do not use Replication source. User master instead
THIS IS PROBABLY DUE TO USING OLD VERSION OF MYSQL
 ```sql
 CHANGE MASTER TO
  MASTER_HOST = '3.85.54.241',
  MASTER_USER = 'replica_user',
  MASTER_PASSWORD = 'replica',
  MASTER_LOG_FILE = 'mysql-bin.000001',
  MASTER_LOG_POS = 154;
 ```

 For restarting the replica
 ```sql
 START SLAVE;
 ```
