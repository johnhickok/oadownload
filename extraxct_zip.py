# script extracts all zipfiles in the folder into us/ca
import os, glob
from zipfile import ZipFile

# os.chdir("/mydir")
for file in glob.glob("*.zip"):
  file_csv = 'us/ca/' + file.split('.')[0] + '.csv'
  with ZipFile(file, 'r') as zip:
    zip.extract(file_csv)
    print(file, file_csv)
