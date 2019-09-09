```bash
$ sudo cp /usr/lib/spark/conf/log4j.properties.template /usr/lib/spark/conf/log4j.properties
$ sudo vi /usr/lib/spark/conf/log4j.properties 
"log4j.rootCategory=INFO, console" --> "log4j.rootCategory=DEBUG, console"

$ cd $DEVSH/exercises/spark-application/ 
$ spark-submit --master yarn-client --name 'Count JPGs' CountJPGs.py /loudacre/weblogs/*
# or
$ spark-submit --properties-file myspark.conf \ CountJPGs.py /loudacre/weblogs/*
```

