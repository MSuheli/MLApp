"""
PySpark transformation logic for MLApp pipeline.
"""
from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def clean_data(df):
    df = df.na.drop(how='any')
    df = df.filter(df['amount'].isNotNull())
    return df

def segment_customers(df):
    """RFM-based customer segmentation for MLAPP-1234."""
    from pyspark.sql import functions as F

    return df.withColumn(
        "segment",
        F.when(F.col("total_spend") > 10000, "Premium")
        .when(F.col("total_spend") > 5000, "Gold")
        .when(F.col("total_spend") > 1000, "Silver")
        .otherwise("Bronze")
    )

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
