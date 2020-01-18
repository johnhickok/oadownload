# creates a folder zip and moves your openaddress zip files into it

import glob, os, shutil

os.mkdir('zip')

zip_file_list = glob.glob('*.zip')

for f in zip_file_list:
  shutil.move(f, 'zip/' + f)
