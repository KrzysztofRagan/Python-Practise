import os
import zipfile
import requests
from contextlib import closing
from contextlib import suppress
# contextlib IS VERY USEFUL LIBRARY THAT CAN HELP YOU DO SOME STUFF IN MORE EFFECTIVE WAY
#METHODS LIKE: 
# closing- closes contextmanager automatically, 
# 
# suppress- you pass here exception that you want to be hidden ( So for example if you want to remvoe file, that doesn't exist you can use this not to stop the program), 
# 
# redirect_stdout- here you pass the file, in which things which are in context manager will be printed (useful, because you don;t have to print everything in the program)

class FileFromWeb:
 
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file
 
    def download_file(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self
 
    def close(self):
        #if os.path.isfile(self.tmp_file):
      os.remove(self.tmp_file)
 
with suppress(FileNotFoundError):
  with closing(FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', '/Users/krzysztofragan/Desktop/vscode/demo1/eurofxref.zip')) as f:  
    f.download_file()
  
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('/Users/krzysztofragan/Desktop/vscode/demo1/zipy')
        z.extract(a_file, '.', None)
    
    os.remove(f.tmp_file)