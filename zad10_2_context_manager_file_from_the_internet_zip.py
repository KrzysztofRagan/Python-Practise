import os
import zipfile
import requests

# PROGRAM THAT DOWNLOADS FILES FROM THE INTERNET AND THEN SAVES THEM IN CONCRETE DIRECTORY. NOTICE USAGE OF CONTEXT MANAGER!
# __exit__ IS USED TO WORK WITH ERRORS IT RETURNS FALSE IF WE WANT TO SHOW THE ERROR OUTSIDE AND TRUE IF WE WANT TO HIDE ERROR
class FileFromWeb():
  def __init__(self, url, path):
    self.url = url
    self.path = path

  def __enter__(self):
    response = requests.get(self.url)
    with open(self.path, 'wb') as f:
      f.write(response.content)
    return self

  def __exit__(self, exc_type, exc_val, exc_traceback):
    print('>>>>>>>>>>> Error details',exc_type, exc_val, exc_traceback)
    if exc_type == KeyError:
        print('>>>>> There is no file in archive! {}'.format(exc_val))
        return True
    elif exc_type == FileNotFoundError:
        print('>>>>> Incorrect directory/file: {}'.format(exc_val))
        return  True
    else:
        return False



with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', '/Users/krzysztofragan/Desktop/vscode/demo1/eurofxref.zip') as f:
  with zipfile.ZipFile(f.path, 'r') as z:
    a_file = z.namelist()[0]
    print(a_file)
    os.chdir('/Users/krzysztofragan/Desktop/vscode/demo1/zipy')
    z.extract(a_file, '.', None)

  