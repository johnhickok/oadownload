# script imports csv files into geodatabase table
import arcpy
import glob, os

arcpy.env.workspace = os.getcwd()

arcpy.CreateFileGDB_management(os.getcwd(), 'load.gdb')

arcpy.CreateTable_management('load.gdb', 'table3')

in_table = 'load.gdb/table3'

arcpy.AddField_management(in_table, 'LON', 'DOUBLE')
arcpy.AddField_management(in_table, 'LAT', 'DOUBLE')
arcpy.AddField_management(in_table, 'NUMBER',   'TEXT', '', '', 30)
arcpy.AddField_management(in_table, 'STREET',   'TEXT', '', '', 200)
arcpy.AddField_management(in_table, 'UNIT',     'TEXT', '', '', 20)
arcpy.AddField_management(in_table, 'CITY',     'TEXT', '', '', 200)
arcpy.AddField_management(in_table, 'POSTCODE', 'TEXT', '', '', 20)

# field names used by search and insert cursors
field_names = ['LON','LAT','NUMBER','STREET','UNIT','CITY','POSTCODE']

# search and insert cursors
insert_cursor = arcpy.da.InsertCursor(in_table, field_names)

# a better structure will be to iterate files into a cleaned up csv
# then use pgsql to copy/append the clean file into postgres
# use postgres to convert to geospatial table
# convert coordinates to geometry, ref: https://postgis.net/docs/ST_MakePoint.html

# cleanup needed:
# convert lat, lon values to float as a test
# verify lat and lon values are reasonably within min/max for California
# verify street names and house numbers have values
# ogr2ogr -f "PostgreSQL" PG:"host=[your host] user=[your user name] dbname=[your database] password=[your password]" bigfile.csv

# Load data into file geodatabase
for file_csv in glob.glob("us/ca/*.csv"):
  print('Importing ' + file_csv + ' ...')
  try:
    search_cursor = arcpy.da.SearchCursor(file_csv, field_names)
    for row in search_cursor:
      insert_cursor.insertRow(row)
    del search_cursor
  except:
    print('bad data in ' + file_csv)
del insert_cursor
