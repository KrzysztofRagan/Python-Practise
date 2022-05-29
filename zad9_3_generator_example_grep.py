import os
from urllib import response
import requests

dir_list = os.listdir('/Users/krzysztofragan/Desktop/vscode/demo1/links_to_check')

# generator goes through all files in directory and returns them
def gen_get_files(dir_list):
  for dir in dir_list:
    file_path = os.path.join('/Users/krzysztofragan/Desktop/vscode/demo1/links_to_check', dir)
    yield file_path

#generator goes through all lines in file and return line without enter
def gen_get_file_lines(file_name):
  with open(file_name, 'r+') as f:
    for line in f.readlines():
      line.replace('\n', '')
      yield line

#func checks if this url exists
def check_webpage(url):
  try:
    response = requests.get(url)
    return response.status_code == 200
  except:
    return False




file_list = []
for c in gen_get_files(dir_list):
  file_list.append(c)

for file in file_list:
  for line in gen_get_file_lines(file):
    print('{} - {}'.format(line, check_webpage(line)))


