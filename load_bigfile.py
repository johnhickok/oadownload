# -*- coding: utf-8 -*-

import glob, os, csv
from unidecode import unidecode

main_file = open('bigfile.csv', 'w')

main_file.write('LON,LAT,NUMBER,STREET,UNIT,CITY,ST,POSTCODE,FILENAME\n')

for file_csv in glob.glob("us/ca/*.csv"):
  filename = file_csv[6:]
  #p3 print('importing', filename)
  print 'importing', filename
  with open(file_csv) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
      try:
        test_lat = row['LAT'].split('.')[0]
        test_lon = row['LON'].split('.')[0].replace('-','')
        if test_lat.isdigit() and test_lon.isdigit():
          mylat = float(row['LAT'])
          mylon = float(row['LON'])
          if 32 < mylat < 42 and -125 < mylon < -113:
            writeline = ''
            writeline += unidecode(row['LON']) + ','
            writeline += unidecode(row['LAT']) + ','
            writeline += unidecode(row['NUMBER']) + ','
            writeline += unidecode(row['STREET']) + ','
            writeline += unidecode(row['UNIT']) + ','
            writeline += unidecode(row['CITY']) + ','
            writeline += 'CA,'
            writeline += unidecode(row['POSTCODE']) + ','
            writeline += filename + '\n'
            zmain_file.write(writeline)
      except:
        # p3 print('error in', file_csv)
        print 'error in', file_csv

main_file.close()

# after creating a big csv file, load into postgres for cleaning your data
# ogr2ogr -f "PostgreSQL" PG:"host=[your host] user=[your user name] dbname=[your database] password=[your password]" bigfile.csv