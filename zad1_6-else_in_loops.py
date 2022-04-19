import os
import urllib.request

data_dir = ('/Users/krzysztofragan/Desktop/vscode/python-kurs/katalog_na_pliki/')

pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'disney', 'url': 'http://go.com' },

    { 'name': 'tutorial',       'url': 'http://www.columbia.edu/~fdc/sample.html'} ]





for page in pages:
  try:
    files_name = '{}.html'.format(page['name'])
    path = os.path.join(data_dir,files_name)
    urllib.request.urlretrieve(page['url'],path)

  except Exception as exception:
    print("ERROR BLAAAAAD")
    assert type(exception).__name__ == 'NameError'
else:
  print("Congrats! You've just created html files.")
