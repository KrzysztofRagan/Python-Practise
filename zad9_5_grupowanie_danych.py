import os
import itertools

#generator that checks if in concrete path are files or directories. If directories it goes recurently through next directory
def scantree(path):
    for entry in os.scandir(path):
      if entry.is_dir() == True:
        yield entry
        yield from scantree(entry.path)
      else:
        yield entry


path ='/Users/krzysztofragan/Desktop/vscode/demo1'

listing = scantree(path)

listing = sorted(listing, key = lambda e: e.is_dir())


#groupby can group elements of lists/dictionaries 
#here key is value returned from func is_dir() which returns True if path is directory and False if it's file
for is_dir, elements in itertools.groupby(listing, key = lambda e: e.is_dir()):
  print('DIRECTORY' if is_dir else 'FILE', len(list(elements)))

