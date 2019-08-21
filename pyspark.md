# Use Pair RDD
### reduceByKey
logsrdd = sc.textFile("/loudacre/weblogs/*2.log") \
.map(lambda l: l.split(' '))

usercountrdd = logsrdd.map(lambda r: (r[2],1)) \
.reduceByKey(lambda v1,v2: v1+v2) 

frequencyrdd = usercountrdd.map(lambda (k,v): (v,1)) \
.reduceByKey(lambda v1,v2: v1+v2)

### keyBy, groupByKey, join
useridipsrdd = logsrdd.map(lambda r:(r[2],r[0])) \
.groupByKey()

accountrdd = sc.textFile("/loudacre/accounts") \
.map(lambda l: l.split(',')) \
.keyBy(lambda r: r[0])

joinrdd = accountrdd.join(usercountrdd)

resultrdd = joinrdd.map(lambda(k,(p,c)): (k,c,p[3],p[4]))

for (a,b,c,d) in resultrdd.take(10):
   print a,b,c,d
