create table if not exists employees_parquet_load(
date_of_birth date not null,
employee_id  decimal(10,2)not null,
last_name varchar(100) not null,
junk varchar(100) not null,
phone_number varchar(100),
first_name varchar(100) not null
);  