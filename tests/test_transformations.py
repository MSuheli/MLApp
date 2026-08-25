"""
Unit tests for transformations module.
"""
import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="module")
def spark():
    """Create a Spark session for testing."""
    spark = SparkSession.builder \
        .appName("MLApp-Tests") \
        .master("local[2]") \
        .getOrCreate()
    yield spark
    spark.stop()


def test_clean_data_removes_negative_amounts(spark):
    """Test that clean_data removes rows with negative amounts."""
    from src.transformations import clean_data

    data = [
        ("T001", "C001", 100.0),
        ("T002", "C002", -50.0),
        ("T003", "C003", 200.0),
    ]
    df = spark.createDataFrame(data, ["transaction_id", "customer_id", "amount"])
    result = clean_data(df)

    assert result.count() == 2


def test_calculate_totals(spark):
    """Test that calculate_totals aggregates correctly."""
    from src.transformations import calculate_totals

    data = [
        ("C001", 100.0),
        ("C001", 200.0),
        ("C002", 150.0),
    ]
    df = spark.createDataFrame(data, ["customer_id", "amount"])
    result = calculate_totals(df)

    assert result.count() == 2
