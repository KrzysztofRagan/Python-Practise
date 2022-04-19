from csv import excel
import os

files_to_process = [ r"/Users/krzysztofragan/Desktop/vscode/python-kurs/katalog_na_pliki/math_sin_square.py" , r"/Users/krzysztofragan/Desktop/vscode/python-kurs/katalog_na_pliki/math_square_root.py"]
z = int(0)
source = ''

# for file in files_to_process:
#   files_name = os.path.basename(str(files_to_process[z]))
#   print(files_name)
#   f = open(files_to_process[z], 'r')
#   for line in f:
#     source += line
#   make = exec(source)
#   z +=1

# LEPSZE :(

for file in files_to_process:
  print('Files name is: {}'.format(os.path.basename(file)))
  with open(file, 'r') as f:
    source = f.read()
    exec(source)





  