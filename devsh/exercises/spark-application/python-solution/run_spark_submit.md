```bash
$ sudo cp /usr/lib/spark/conf/log4j.properties.template /usr/lib/spark/conf/log4j.properties
$ sudo vi /usr/lib/spark/conf/log4j.properties 
"log4j.rootCategory=INFO, console" --> "log4j.rootCategory=DEBUG, console"

$ cd $DEVSH/exercises/spark-application/ 
$ spark-submit --master yarn-client --name 'Count JPGs' CountJPGs.py /loudacre/weblogs/*
# or
$ spark-submit --properties-file myspark.conf CountJPGs.py /loudacre/weblogs/*
```
```conf
$vi myspark.conf
spark.app.name  JJD App 2
spark.master    yarn-client
spark.executor.memory   400m
```

```py
# CountJPGs.py
import sys
from pyspark import SparkContext

def main(logfile):
    sc = SparkContext()
    sc.setLogLevel("WARN")
    cnt = sc.textFile(logfile).filter(lambda l: '.jpg' in l).count()
    print "The number of JPG requests :", cnt
    sc.stop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: CountJPGs.py <logfile>"
        exit(-1)
    logfile = sys.argv[1]
    main(logfile)
```

