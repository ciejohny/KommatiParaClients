# utils.py
from pyspark.sql import SparkSession


def get_spark() -> SparkSession:
    """
    This function prepares Spark session
    """
    return SparkSession.builder.master("local[1]") \
        .appName("Client filter") \
        .getOrCreate()
