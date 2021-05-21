import sys
from awsglue.transforms import *
from awsglue.utils import *
from pyspark.context import *
from awsglue.context import *
from awsglue.job import *

glueContext = GlueContext(SparkContext.getOrCreate())

salesDF_csv = glueContext.create_dynamic_frame.from_catalog(
    database = "gluespark-db",
    table_name = "sales_csv_csv"
)