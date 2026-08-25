"""
Data ingestion utilities for MLApp pipeline.
"""
from pyspark.sql import SparkSession
from spark_utils import get_spark_session


def load_csv(spark, file_path, header=True, infer_schema=True):
    """Load a CSV file into a Spark DataFrame.

    Args:
        spark: SparkSession instance.
        file_path: Path to the CSV file.
        header: Whether the CSV has a header row.
        infer_schema: Whether to infer column types.

    Returns:
        Spark DataFrame.
    """
    df = spark.read \
        .option("header", header) \
        .option("inferSchema", infer_schema) \
        .csv(file_path)
    return df


def load_parquet(spark, file_path):
    """Load a Parquet file into a Spark DataFrame."""
    return spark.read.parquet(file_path)


def load_transactions(spark, source_path):
    """Load transaction data from source.

    Args:
        spark: SparkSession instance.
        source_path: Path to transactions data.

    Returns:
        Spark DataFrame with transactions.
    """
    print(f"Loading transactions from: {source_path}")
    df = load_csv(spark, source_path)
    print(f"Loaded {df.count()} transaction records")
    return df


if __name__ == "__main__":
    spark = get_spark_session("MLApp-DataLoader")
    # Example usage
    # df = load_transactions(spark, "data/transactions.csv")
    # df.show(5)
    spark.stop()
