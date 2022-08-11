import json
import psycopg2
import os

def lambda_handler(event, context):
    print("event collected is {}".format(event))
    for record in event['Records'] :
        s3_bucket = record['s3']['bucket']['name']
        print("Bucket name is {}".format(s3_bucket))
        s3_key = record['s3']['object']['key']
        print("Bucket key name is {}".format(s3_key))
        from_path = "s3://{}/{}".format(s3_bucket, s3_key)
        print("from path {}".format(from_path))
        # Access_key = os.getenv('AWS_Access_key')
        # Access_Secret = os.getenv('AWS_Access_Secret')
        dbname = os.getenv('dbname')
        host = os.getenv('host')
        user = os.getenv('user')
        password = os.getenv('password')
        print("env variables: " + dbname + "," + host + "," + user + "," + password)
        # tablename = os.getenv('tablename')
        connection = psycopg2.connect(dbname = dbname,
                                       host = host,
                                       port = '5439',
                                       user = user,
                                       password = password)
                                    
        # print("CONNECTION: " + connection)
        print('after connection....')
        curs = connection.cursor()
        print('after cursor....')
        # query = "COPY {} FROM '{}' CREDENTIALS 'aws_access_key_id={};aws_secret_access_key={}' CSV;".format(tablename,from_path,Access_key,Access_Secret)
        query = "COPY employees_parquet_load FROM 's3://redshift-unload-bucket-paca/output_crawler/' IAM_ROLE 'arn:aws:iam::440542114397:role/service-role/AmazonRedshift-CommandsAccessRole-20220803T095421' FORMAT AS PARQUET;"
        print("query is {}".format(query))
        print('after query....')
        curs.execute(query)
        connection.commit()
        #print(curs.fetchmany(3))
        print('after execute....')
        curs.close()
        print('after curs close....')
        connection.close()
        print('after connection close....')
        print('wow..executed....')