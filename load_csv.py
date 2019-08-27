# script imports csv files from openaddresses.io (oa) into an Esri file
# geodatabase. You will need ArcGIS Pro and the Python 3.x environment
import arcpy
import glob, os

arcpy.env.workspace = os.getcwd()

# Create a file geodatabase load.gdb in the current working directory.
arcpy.CreateFileGDB_management(os.getcwd(), 'load.gdb')

# Create a table and add fields to match oa 
arcpy.CreateTable_management('load.gdb', 'table1')

in_table = 'load.gdb/table1'
arcpy.AddField_management(in_table, 'LON', 'DOUBLE')
arcpy.AddField_management(in_table, 'LAT', 'DOUBLE')
arcpy.AddField_management(in_table, 'NUMBER',   'TEXT', '', '', 30)
arcpy.AddField_management(in_table, 'STREET',   'TEXT', '', '', 200)
arcpy.AddField_management(in_table, 'UNIT',     'TEXT', '', '', 20)
arcpy.AddField_management(in_table, 'CITY',     'TEXT', '', '', 200)
arcpy.AddField_management(in_table, 'DISTRICT', 'TEXT', '', '', 100)
arcpy.AddField_management(in_table, 'REGION',   'TEXT', '', '', 100)
arcpy.AddField_management(in_table, 'POSTCODE', 'TEXT', '', '', 20)

# field names used by search and insert cursors
field_names = ['LON','LAT','NUMBER','STREET','UNIT','CITY','DISTRICT','REGION','POSTCODE']

# set an insert cursor
insert_cursor = arcpy.da.InsertCursor(in_table, field_names)

# Desktop software is easy to use, but with over 13 million records, desktop
# software will take a while. Please consider using PostGIS.
# An improved script will iterate files into a cleaned up csv
# then use pgsql to copy/append the clean file into postgres

# cleanup needed:
# convert lat, lon values to float as a test
# verify lat and lon values are reasonably within min/max for California
# verify street names and house numbers have values

# iterate through csv's in the california (ca) folder. You will need to either copy
# the ca folder into the same folder this script runs in, or change the next line below.

for file_csv in glob.glob("ca/*.csv"):
  print('Importing ' + file_csv + ' ...')
  try:
    search_cursor = arcpy.da.SearchCursor(file_csv, field_names)
    for row in search_cursor:
      insert_cursor.insertRow(row)
    del search_cursor
  except:
    print('bad data in ' + file_csv)
del insert_cursor

# Postgres is great for finding and removing buggy records once your table is uploaded.

# To use postgres to convert to convert coordinates to geometry
# ref: https://postgis.net/docs/ST_MakePoint.html

# To convert from WGS84 (4326) to CCS State Plane Zone 5 (2229), 
# consider https://postgis.net/docs/ST_Transform.html

