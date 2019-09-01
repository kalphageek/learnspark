## 시험 참고 URL
* https://www.cloudera.com/about/training/certification/cca-spark.html  : sqoop 1.4, spark 2.3 검색
* https://community.cloud.databricks.com/?o=5888369366172583
* https://hub.docker.com/u/jupyter
* http://generatedata.com/

## 기타정보
* ORC is avaliable to transact by 1 row unit

## VM -> PC 데이터 이동
* VM shutdown > VM 설정 > Option 탭 > PC 'CCA175' folder와 연결 > VM Start
* VM > /mnt/hgfs/CCA175 확인

## Databricks Community Edition
* Notebook 에서 사용가능
```
%fs
system command
%sql
hive sql
~~~l
```

## VM에서 Jupyter Notebook 활성화d
```bash
vi .bashrc
#export ... -> export ... 
#export ... -> export ... 
```

# Use Pair RDD
### reduceByKey
```
logsrdd = sc.textFile("/loudacre/weblogs/*2.log") \
.map(lambda l: l.split(' '))

usercountrdd = logsrdd.map(lambda r: (r[2],1)) \
.reduceByKey(lambda v1,v2: v1+v2) 

frequencyrdd = usercountrdd.map(lambda (k,v): (v,1)) \
.reduceByKey(lambda v1,v2: v1+v2)
```
### keyBy, groupByKey, join
```
useridipsrdd = logsrdd.map(lambda r:(r[2],r[0])) \
.groupByKey()

accountrdd = sc.textFile("/loudacre/accounts") \
.map(lambda l: l.split(','))

joinrdd = accountrdd.keyBy(lambda r: r[0]) \
.join(usercountrdd)

resultrdd = joinrdd.map(lambda(k,(p,c)): (k,c,p[3],p[4]))

for (a,b,c,d) in resultrdd.take(10):
   print a,b,c,d
```
### mapValues
```
postrdd = accountrdd.keyBy(lambda r: r[8]) \
.mapValues(lambda v: (v[4],v[3])) \
.groupByKey()

for (k,vs) in postrdd.take(10):
   print '---', k
   for (v1,v2) in vs:
      print v1+',',v2
```  
* Iterable -> Actual Value
```
postrdd.map(lambda (k,v): (k, list(v))).take(5)  
```

# Spark 2.3
```
data = spark.read.format("csv") \
.option("inferSchema", infer_schema) \
.option("header", "true") \
.option("sep", "\t") \
.load("/loudacre/accounts)
```
```
parquet-tools head datafile.parquet
parquet-tools schema datafile.parquet
```
### CSV Schema 설정
accounts_schema = StructType([
  StructField(,)
  StructField(,)
])

### sqoop -> hive table 
```
sqoop import \
--connect jdbc:mysql://gateway/loudacre \
--username training --password training \
--table accounts \
--columns "acct_num, first_name, last_name" \
--target-dir "/user/hive/warehouse/loudacre.db/acct/" --delete-target-dir \
--as-avrodatafile \
-m1

/user/hive/warehouse/loudacre.db/acct/

CREATE external TABLE loudacre.acct
  COMMENT "just drop the schema right into the HQL"
  ROW FORMAT SERDE
  'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
  STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
  OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
  TBLPROPERTIES (
    'avro.schema.literal'='{
      "namespace": "com.howdy",
      "name": "some_schema",
      "type": "record",
      "fields": [ { "name":"acct_num","type":"int"}, { "name":"first_name","type":"string"}, { "name":"last_name","type":"string"}]
    }');
```
## Hive function
```
select id, item, dt, domain1, domain2, cal, trans
from (
  select 1 as id, 
    substr('abc@naver.com', instr('abc@naver.com', '@')+1) as domain1, substr('abc@naver.com', locate('@', 'abc@naver.com', 2)+1) as domain2,
    split("cc kk.aa/bb", '[ |//.]') as items, 
    from_unixtime(unix_timestamp(current_timestamp),'MM/dd') as dt,
    cast('100' as int) + cast(100.1 as float) as cal,
    translate('Make sure u knew that code','e','o') as trans
)
lateral view explode(items) tbl as item
```
## Hive Timestamp / Date
```
hive> select current_timestamp();
OK
2017-10-01 00:54:14.736

hive> select current_date();
OK
2017-10-01

Add 1 day to current date using HiveQL
hive> select date_add(current_date(), 1);
OK
2017-10-02

Subtract 1 day from current date using HiveQL
hive> select date_sub(current_date(),1);
OK
2017-09-30

Get first day of the given timstamp using HiveQL
hive> select trunc(current_timestamp(), 'MONTH');
OK
2017-10-01

Convert timestamp to date format using HiveQL
hive> select to_date(current_timestamp());
OK
2017-10-01

Data type conversion using Cast function in HiveQL
hive> select cast(current_timestamp() as date);
OK
2017-10-01

Convert Timestamp to YYYYMMDD format using HiveQL
hive> select from_unixtime(unix_timestamp(current_date()), 'yyyyMMdd');
OK
20170001
```
