# script used to provide number of lines in openaddress files

import glob, os, csv

def file_len(fname):
  with open(fname) as f:
    for i, l in enumerate(f):
        pass
  return i + 1

for file_csv in glob.glob("us/ca/*.csv"):
  filename = file_csv[6:]
  num_lines = file_len(file_csv) - 1
  print filename + ',' + str(num_lines)