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
