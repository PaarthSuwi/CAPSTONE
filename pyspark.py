from pyspark.sql import SparkSession
from pyspark import SparkContext

sc = SparkContext.getOrCreate()

data = range(10000)
distData=sc.parallelize(data)
distData.reduce(lambda x: not x&1).take(10)
