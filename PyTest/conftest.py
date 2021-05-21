#from pyspark import SparkContext
#from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
import pytest


@pytest.fixture(scope='session')
def spark_context():
    #spark_context = SparkContext()
    #sql_context = SQLContext(spark_context)
    spark_context = (SparkSession.builder.appName("Test").getOrCreate())
    yield spark_context
    spark_context.stop()