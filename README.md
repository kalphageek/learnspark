# learnspark

## sqlContext를 이용해 HDFS --> DF생성 --> RDD생성 --> DF생성 (컬럼명 변경) --> HDFS에 저장
1. sqlContext를 이용해 DF생성
```python
webpageDF = sqlContext.read.load("/loudacre/webpage")
assocFilesDF = webpageDF.select(webpageDF.webpage_num, webpageDF.associated_files)
```
2. RDD생성
```python
aFilesRDD = assocFilesDF.map(lambda row: row.webpage_num, row.associated_files)
aFilesRDD2 = aFilesRDD.flatMapValues(lambda s: s.split(','))
```
3. DF생성
```python
aFilesDF = sqlContext.createDataFrame(aFilesRDD2, assocFilesDF.schema())
finalDF = aFilesDF.withColumnRenamed('associated_files', 'associated_file')
```
4. HDFS에 다시 save
```python
finalDF.write.mode('overwrite').save("/loudacre/webpage_files")
```