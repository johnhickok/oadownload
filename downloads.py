# this script is superceded and does not work - for reference only

import csv, urllib.request

with open('state.txt') as csvfile:
  reader = csv.DictReader(csvfile, delimiter='\t')
  for row in reader:
    country, state, json = row['source'].split('/')
    filename = json.split('.')[0] + '.zip'
    url = row['processed']
    print('Downloading ' + filename + ' ...')
    urllib.request.urlretrieve(url, filename)
