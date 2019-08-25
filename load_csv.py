# script imports csv files into geodatabase table
import arcpy
import glob, os

arcpy.env.workspace = os.getcwd()

arcpy.CreateTable_management('gc1.gdb', 'table3')

in_table = 'gc1.gdb/table3'

arcpy.AddField_management(in_table, 'LON', 'DOUBLE')
arcpy.AddField_management(in_table, 'LAT', 'DOUBLE')
arcpy.AddField_management(in_table, 'NUMBER',   'TEXT', '', '', 30)
arcpy.AddField_management(in_table, 'STREET',   'TEXT', '', '', 200)
arcpy.AddField_management(in_table, 'UNIT',     'TEXT', '', '', 20)
arcpy.AddField_management(in_table, 'CITY',     'TEXT', '', '', 200)
arcpy.AddField_management(in_table, 'DISTRICT', 'TEXT', '', '', 100)
arcpy.AddField_management(in_table, 'REGION',   'TEXT', '', '', 100)
arcpy.AddField_management(in_table, 'POSTCODE', 'TEXT', '', '', 20)
arcpy.AddField_management(in_table, 'ID',       'TEXT', '', '', 30)
arcpy.AddField_management(in_table, 'HASH',     'TEXT', '', '', 30)

# field names used by search and insert cursors
field_names = ['LON','LAT','NUMBER','STREET','UNIT','CITY','DISTRICT','REGION','POSTCODE','ID','HASH']

# search and insert cursors
insert_cursor = arcpy.da.InsertCursor(in_table, field_names)

for file_csv in glob.glob("ca/*.csv"):
  print('Importing ' + file_csv + ' ...')
  search_cursor = arcpy.da.SearchCursor(file_csv, field_names)
  for row in search_cursor:
    insert_cursor.insertRow(row)
  del search_cursor
del insert_cursor
