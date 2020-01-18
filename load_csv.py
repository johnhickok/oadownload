import os, csv, psycopg2, glob, my_postgres_credentials

this_folder = os.getcwd()

# set up postgres connection string from values you updated in 
# my_postgres_credentials.py
connect_string = ''
connect_string += 'dbname=' + my_postgres_credentials.dbname + ' '
connect_string += 'user=' + my_postgres_credentials.user + ' '
connect_string += 'password=' + my_postgres_credentials.password

# Connect to PostGIS
connection = psycopg2.connect(connect_string)
cursor = connection.cursor()

# create table
psql_table_create = """
CREATE TABLE public.oa_california_text
(
    myid serial,
    lon character varying(100),
    lat character varying(100),
    number character varying(100),
    street character varying(200),
    unit character varying(100),
    city character varying(200),
    district character varying(100),
    region character varying(100),
    postcode character varying(100),
    id character varying(100),
	hash character varying(100),
    src character varying(150)
);
"""
cursor.execute(psql_table_create)
cursor.execute("commit")

# for each csv from openaddresses, copy values into the above table, then
# populate the field src with the source csv file
for file_csv in glob.glob("us/ca/*.csv"):
  file_name = file_csv[6:]
  copy_string = "copy oa_california_text (lon,lat,number,street,unit,city,"
  copy_string += "district,region,postcode,id,hash) FROM "
  copy_string += "'" + this_folder + "/us/ca/" + file_name + "' "
  copy_string += "DELIMITER ',' CSV HEADER ENCODING 'UTF8' QUOTE '\"' ESCAPE '''';"
  update_srs = "update oa_california_text set src = "
  update_srs += "'" + file_name + "' where src is null;"
  print("copying " + file_name + " ...")
  cursor.execute(copy_string)
  cursor.execute(update_srs)
  cursor.execute("commit")
