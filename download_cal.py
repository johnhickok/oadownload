# This script downloads just California data sources from openaddresses.io
# excluding Los Angeles County

import csv, random, time, urllib.request

# download state.txt data.openaddresses.io
url_state_txt = 'http://results.openaddresses.io/state.txt'
urllib.request.urlretrieve(url_state_txt, 'state.txt')

# iterate through state.txt and download files in California
with open('state.txt', encoding = 'utf8') as csvfile:
  reader = csv.DictReader(csvfile, delimiter='\t')
  for row in reader:
      if (row['source'][0:5]) == 'us/ca' \
      and row['processed'] != '' \
      # remark out the line below if you want to include Los Angeles County
      and row['source'][0:17] != 'us/ca/los_angeles':
        country, state, json = row['source'].split('/')
        filename = json.split('.')[0] + '.zip'
        url = row['processed']
        wait = random.uniform(4.5, 9.0)
        time.sleep(wait)
        print('Waiting', wait, 'seconds...')
        print('Downloading ' + filename + ' ...')
        urllib.request.urlretrieve(url, filename)
