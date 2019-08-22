ORC is avaliable to transact by 1 row unit

# VM에서 Jupyter Notebook 활성화d
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
