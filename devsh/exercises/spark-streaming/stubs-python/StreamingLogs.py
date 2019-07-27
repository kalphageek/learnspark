import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Given an RDD of KB requests, print out the count of elements
def printRDDcount(t, rdd): print t, ":", "Number of KB requests: "+str(rdd.count())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: StreamingLogs.py <hostname> <port>"
        sys.exit(-1)
    
    # get hostname and port of data source from application arguments
    hostname = sys.argv[1]
    port = int(sys.argv[2])
     
    # Create a new SparkContext
    sc = SparkContext()

    # Set log level to ERROR to avoid distracting extra output
    sc.setLogLevel("ERROR")

    # TODO  
    ssc = StreamingContext(sc, 1)
    DStream = ssc.socketTextStream(hostname, port)\
        .filter(lambda line:"KBDOC" in line)

    DStream.pprint(5)
    DStream.foreachRDD(lambda t,r: printRDDcount(t, r))
    
    ssc.start()
    ssc.awaitTermination()
