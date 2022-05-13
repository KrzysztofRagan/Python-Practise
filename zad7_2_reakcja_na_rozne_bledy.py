import requests
import os
import shutil
 
def save_url_to_file(url, file_path):
        
    r = requests.get(url, stream = True)     
    with open(file_path, "wb") as f: 
        f.write(r.content)
 
url = 'http://www.mobilo24.eu/spis/'
dir = '/Users/krzysztofragan/Desktop/vscode/demo1'
tmpfile = 'download.tmp'
file = 'spis.html'
file_path = os.path.join(dir, file)
tmpfile_path = os.path.join(dir, tmpfile)


#TRY IS USE TO CHECK SOMETHING
try:
  if os.path.exists(tmpfile_path):
    os.remove(tmpfile_path)

  save_url_to_file(url, tmpfile_path)
  shutil.copy(tmpfile_path, file_path)

#THERE ARE CONCRETE ERRORS FOR EACH SITUATION
except requests.exceptions.ConnectionError:
  print('Incorrect {} URL'.format(url))

except PermissionError:
  print('Only for reading file {}'.format(file_path))

except FileNotFoundError:
  print('File {} does not exist'.format(tmpfile_path))

# WHEN TRY DOEDNT WORK THEN EXCEPTION IS PRINTED
except Exception as e:  
  print('An error {} occured.'.format(e))

#YOU CAN USE ELSE WHEN PROGRAM WILL GO THROUGH TRY/EXCEPT
else:
  print('Operation went succesfully!')
  
# FINALLY CAN BE USED AFTER ALL PREVIOUS STATEMENTS
finally:
  print('-----Action finished--------')
  if os.path.exists(tmpfile):
    os.remove(tmpfile)





