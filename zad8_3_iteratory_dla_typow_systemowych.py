import csv
 
# When you can go through all itarations in for loop that means, that variable is iterator. When you can go through next positions in that 
# variable thanks to next func, that means that the variable is iterable. 
# You can always try to make the variable iterable by func iter()
with open('/Users/krzysztofragan/Desktop/vscode/demo1/proba.csv', newline='') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))
    
  while True:
    try:    
      print(next(csvreader))
    except StopIteration:
      break
