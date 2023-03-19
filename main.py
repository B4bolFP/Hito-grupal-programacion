from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('myApp').getOrCreate()

df = spark.read.csv('Tomato.csv', header=True, inferSchema=True)