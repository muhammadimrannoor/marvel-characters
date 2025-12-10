import sys
print(sys.version)

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
print(spark.conf.get("spark.databricks.clusterUsageTags.sparkVersion"))