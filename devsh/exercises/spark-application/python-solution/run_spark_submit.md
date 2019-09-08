```bash
$ cd $DEVSH/exercises/spark-application/ 
$ spark-submit --master yarn-client --name 'Count JPGs' CountJPGs.py /loudacre/weblogs/*
# or
$ spark-submit --properties-file myspark.conf \ CountJPGs.py /loudacre/weblogs/*
```
