
* Text File
```
sqoop import --connect jdbc:mysql://localhost/loudacre 
--username training --password training 
--table accounts 
--fields-terminated-by '\t' 
--target-dir /loudacre/accounts_tsv

sqoop export 
--connect jdbc:mysql://localhosts/loudacre 
--username training --password training 
--export-dir /loudacre/accounts_tab 
--fields-terminated-by '\t' 
--table accountscopy
```
* Binary File
```
sqoop import 
--connect jdbc:mysql://localhost/loudacre 
--username training --password training 
--table accounts 
--target-dir /loudacre/accounts_avro 
--delete-target-dir 
--compress --compression-codec org.apache.hadoop.io.compress.SnappyCodec 
--as-avrodatafile -m1

sqoop export 
--connect jdbc:mysql://localhost/loudacre 
--username training --password training 
--table accountscopy 
--export-dir /loudacre/accounts_avro
```
