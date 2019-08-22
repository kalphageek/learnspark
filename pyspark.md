## 시험 참고 URL
* https://www.cloudera.com/about/training/certification/cca-spark.html
* https://community.cloud.databricks.com/?o=5888369366172583
* https://hub.docker.com/u/jupyter

## 기타정보
* ORC is avaliable to transact by 1 row unit

## VM -> PC 데이터 이동
* VM shutdown > VM 설정 > Option 탭 > PC 'CCA175' folder와 연결 > VM Start
* VM > /mnt/hgfs/CCA175 확인

## Databricks Community Edition
* notbook에서 폴더아래 삭제
> dbutils.fs.rm("", True)

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
file_location = "/..."
file_type = "csv"

infer_schema = "true"
first_row_is_header = "true"
delimiter = ","

data = spark.read.format(file_type) \
.option("inferSchema", infer_schema) \
.option("firstRwIsHeader", first_row_is_header) \
.option("delim", delimiter) \
.load(file_type)
```

parquet-tools head datafile.parquet
parquet-tools schema datafile.parquet

### CSV Schema 설정
accounts_schema = StructType([
  StructField(,)
  StructField(,)
[)

### Hive -> hdfs 
ccountdf = sqlContext.read.table('accounts')
accountdf.printSchema()

accountrdd = accountdf.where("zipcode = 94913").rdd
accountrdd.saveAsTextFile("/loudacre/accounts_tsv94913")

spark.read.parquet('python/test_support/sql/parquet_partitioned')
spark.read.text('python/test_support/sql/text-test.txt')
spark.read.text('python/test_support/sql/text-test.txt', wholetext=True)
spark.read.orc('python/test_support/sql/orc_partitioned')
spark.read.csv('python/test_support/sql/ages.csv')
spark.read.json('python/test_support/sql/people.json')
spark.read.json(rdd)

s = spark.read.schema("col0 INT, col1 DOUBLE")

spark.read.schema("col0 INT, col1 DOUBLE")

df.createOrReplaceTempView('tmpTable')

df.write.format('parquet')  
...     .bucketBy(100, 'year', 'month')
...     .mode("overwrite")
...     .saveAsTable('bucketed_table')
df.write.format('parquet')  
...     .bucketBy(100, 'year', 'month')
...     .sortBy('day')
...     .mode("overwrite")
...     .saveAsTable('sorted_bucketed_table')
df.write.parquet(os.path.join(tempfile.mkdtemp(), 'data'))
df.write.mode('append').parquet(os.path.join(tempfile.mkdtemp(), 'data'))
