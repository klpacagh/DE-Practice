unload ('select * from venue')
to 's3://redshift-unload-bucket-paca' 
iam_role 'arn:aws:iam::440542114397:role/service-role/AmazonRedshift-CommandsAccessRole-20220803T095421'
ALLOWOVERWRITE
--parallel off
maxfilesize 5 mb;

-- select pg_last_query_id();

-- select query, substring(path,0,40) as path
-- from stl_unload_log
-- where query=272
-- order by path;