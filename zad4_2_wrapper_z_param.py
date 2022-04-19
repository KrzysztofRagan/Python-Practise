import functools
from datetime import datetime as dt
import os 



def wrapper_with_logged_file(logged_action, log_file_path):
  def wrapper_with_logged_to_known_file(func):
    def the_real_wrapper(path):
      file = open(log_file_path, 'a')
      file.write('action {} executed on {} on {} '.format(logged_action , path , dt.now().strftime("%Y-%m-%d %H:%M:%S")))
      file.close()
      return func(path)
    return the_real_wrapper
  return wrapper_with_logged_to_known_file
    




@wrapper_with_logged_file('FILE_CREATE',r'/Users/krzysztofragan/Desktop/vscode/python-kurs/katalog_na_pliki/file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path,"w+")
 

@wrapper_with_logged_file('FILE_CREATE', r'/Users/krzysztofragan/Desktop/vscode/python-kurs/katalog_na_pliki/file_delete.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'/Users/krzysztofragan/Desktop/vscode/python-kurs/katalog_na_pliki/dummyfile.txt')
delete_file(r'/Users/krzysztofragan/Desktop/vscode/python-kurs/katalog_na_pliki/dummyfile.txt')

