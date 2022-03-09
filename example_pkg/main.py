from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import datetime
from somedir.util import *

def main():
    printToday()
    spark = SparkSession.builder.getOrCreate()

    df = spark.range(1,5)
    df.withColumn('x2', F.col('id') * 2).show()

if __name__ == '__main__':
    main()
