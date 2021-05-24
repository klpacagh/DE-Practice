from pyspark.sql.functions import col
from pyspark.sql.functions import col


def filter_spark_data_frame(dataframe,column_name='age',value=20):
    return dataframe.where(col(column_name) > value)

def get_sorted_data_frame(data_frame, columns_list):
    return data_frame.sort_values(columns_list).reset_index(drop=True)

#from .main import filter_spark_data_frame
#from pyspark import SparkContext
#from pyspark.sql import SQLContext
import pandas as pd
from pyspark.sql import SparkSession

'''
you would not want to initialize resource-intensive Spark Context over and over again. 
For that reason, with Pytest you can create conftest.py that launches a single Spark session for all 
of your tests and when all of them were run, the session is closed. In order to make the session visible 
for tests, you should decorate the functions with Pytest fixtures. Here is the content of conftest.py:
-- Uses the conftest.py file
'''


def test_filter_spark_data_frame_by_value(spark_context):
    # Spark Context initialisation
    #spark_context = SparkContext()
    #sql_context = SQLContext(spark_context)
    #sql_context = (SparkSession.builder.appName("Test").getOrCreate())

    # Input and output dataframes
    input = spark_context.createDataFrame(
        [('charly', 15),
         ('fabien', 18),
         ('sam', 21),
         ('sam', 25),
         ('nick', 19),
         ('nick', 40)],
        ['name', 'age'],
    )
    expected_output = spark_context.createDataFrame(
        [('sam', 25),
         ('sam', 21),
         ('nick', 40)],
        ['name', 'age'],
    )
    real_output = filter_spark_data_frame(input)
    real_output = get_sorted_data_frame(
        real_output.toPandas(),
        ['age', 'name'],
    )
    expected_output = get_sorted_data_frame(
        expected_output.toPandas(),
        ['age', 'name'],
    )

    # Equality assertion
    # check_like = True ignores the ordering of columns
    pd.testing.assert_frame_equal(
        expected_output,
        real_output,
        check_like=True,
    )

    # Close the Spark Context
    spark_context.stop()