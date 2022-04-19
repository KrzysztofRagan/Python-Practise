import os

def ReadingFile(path):
  file = open(path, 'r')
  words_in_file = file.read()
  words_counter = len(words_in_file.split())
  return words_counter


path = r'/Users/krzysztofragan/Desktop/vscode/python-kurs/okno.txt'
if os.path.isfile(path):
  print('There are {} words in file {}'.format(ReadingFile(path), path))
else:
  file = open(path, 'x').close()
