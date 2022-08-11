import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame


def directJDBCSource(
    glueContext,
    connectionName,
    connectionType,
    database,
    table,
    redshiftTmpDir,
    transformation_ctx,
) -> DynamicFrame:

    connection_options = {
        "useConnectionProperties": "true",
        "dbtable": database + "." + table,
        "connectionName": connectionName,
    }
    
    if redshiftTmpDir:
        connection_options["redshiftTmpDir"] = redshiftTmpDir

    return glueContext.create_dynamic_frame.from_options(
        connection_type=connectionType,
        connection_options=connection_options,
        transformation_ctx=transformation_ctx,
    )


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)


# Script generated for node MySQL table
MySQLtable_node1 = directJDBCSource(
    glueContext,
    connectionName="connect-to-mysql",
    connectionType="mysql",
    database="kev_db",
    table="employees",
    redshiftTmpDir="",
    transformation_ctx="MySQLtable_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=MySQLtable_node1,
    mappings=[
        ("date_of_birth", "date", "date_of_birth", "date"),
        ("employee_id", "decimal", "employee_id", "decimal"),
        ("last_name", "string", "last_name", "string"),
        ("junk", "string", "junk", "string"),
        ("phone_number", "string", "phone_number", "string"),
        ("first_name", "string", "first_name", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)


# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=ApplyMapping_node2,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://redshift-unload-bucket-paca/output_crawler/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="S3bucket_node3",
)

job.commit()
