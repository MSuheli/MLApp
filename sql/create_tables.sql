-- MLApp: Table creation scripts
-- Environment: Azure SQL / Databricks SQL

-- ============================================================
-- Table: customers
-- ============================================================
CREATE TABLE IF NOT EXISTS customers (
    customer_id     STRING NOT NULL,
    customer_name   STRING,
    email           STRING,
    city            STRING,
    signup_date     DATE,
    is_active       BOOLEAN DEFAULT TRUE
);

-- ============================================================
-- Table: transactions
-- ============================================================
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id      STRING NOT NULL,
    customer_id         STRING NOT NULL,
    product_id          STRING,
    amount              DECIMAL(10, 2),
    transaction_date    DATE,
    payment_method      STRING
);

-- ============================================================
-- Table: products
-- ============================================================
CREATE TABLE IF NOT EXISTS products (
    product_id      STRING NOT NULL,
    product_name    STRING,
    category        STRING,
    price           DECIMAL(10, 2)
);
