# This script iterates through the text file from openaddresses.io
# http://results.openaddresses.io/state.txt
# that is edited to include just California data sources, 
# excluding Los Angeles County

import csv, random, time, urllib.request

with open('state_cal.txt') as csvfile:
  reader = csv.DictReader(csvfile, delimiter='\t')
  for row in reader:
    country, state, json = row['source'].split('/')
    filename = json.split('.')[0] + '.zip'
    url = row['processed']
    wait = random.uniform(4.5, 9.0)
    time.sleep(wait)
	print('Waiting', wait, 'seconds...')
    print('Downloading ' + filename + ' ...')
    urllib.request.urlretrieve(url, filename)
