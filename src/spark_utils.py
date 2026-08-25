"""
Spark session utilities for MLApp pipeline.
"""
from pyspark.sql import SparkSession


def get_spark_session(app_name="MLApp"):
    """Create and return a configured Spark session.

    Args:
        app_name: Name of the Spark application.

    Returns:
        Configured SparkSession instance.
    """
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.shuffle.partitions", "200") \
        .getOrCreate()
    return spark


def stop_spark_session(spark):
    """Cleanly stop the Spark session."""
    if spark is not None:
        spark.stop()
