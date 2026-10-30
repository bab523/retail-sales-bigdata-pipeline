from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, month, to_date

spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()
df = spark.read.csv("file:///root/sales.csv", header=True, inferSchema=True)

df = df.withColumn("revenue", col("quantity") * col("price"))
df = df.withColumn("month", month(to_date(col("date"))))

cat = df.groupBy("category").agg(_sum("revenue").alias("total")).orderBy("total", ascending=False)
cat.show()
city = df.groupBy("city").agg(_sum("revenue").alias("total")).orderBy("total", ascending=False)
city.show()
monthly = df.groupBy("month").agg(_sum("revenue").alias("total")).orderBy("month")
monthly.show()

cat.toPandas().to_csv("cat.csv", index=False)
city.toPandas().to_csv("city.csv", index=False)
monthly.toPandas().to_csv("monthly.csv", index=False)
