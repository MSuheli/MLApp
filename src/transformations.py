"""
PySpark transformation logic for MLApp pipeline.
"""
from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def clean_data(df: DataFrame) -> DataFrame:
    """Clean transaction data by filtering invalid records.

    Args:
        df: Raw transactions DataFrame.

    Returns:
        Cleaned DataFrame.
    """
    df = df.filter(df['amount'] > 0)
    return df


def add_transaction_date(df: DataFrame) -> DataFrame:
    """Ensure transaction_date is properly typed."""
    return df.withColumn(
        "transaction_date",
        F.to_date(F.col("transaction_date"), "yyyy-MM-dd")
    )


def calculate_totals(df: DataFrame) -> DataFrame:
    """Calculate total spend per customer.

    Args:
        df: Transactions DataFrame with customer_id and amount.

    Returns:
        DataFrame with customer_id and total_spend.
    """
    return df.groupBy("customer_id").agg(
        F.sum("amount").alias("total_spend"),
        F.count("*").alias("transaction_count")
    )


def enrich_with_categories(df: DataFrame, categories_df: DataFrame) -> DataFrame:
    """Join transactions with product categories."""
    return df.join(categories_df, on="product_id", how="left")
