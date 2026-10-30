# Retail Sales Big Data Pipeline

End-to-end big data pipeline built with PySpark.

## Pipeline
Ingest (CSV) -> Store (Parquet) -> Analyze (Spark SQL) -> Predict (Spark MLlib) -> Visualize (matplotlib)

## Files
- generate_data.py : creates 500k row synthetic sales dataset
- analysis.py : Spark aggregations by category, city, month
- charts.py : builds dashboard.png
- upgrade.py : Parquet + Spark SQL + Linear Regression + timing

## Run
python3 generate_data.py
python3 analysis.py
python3 charts.py
python3 upgrade.py

## Tech
PySpark 3.5.3, Spark SQL, MLlib, Parquet, Java 17, Git
