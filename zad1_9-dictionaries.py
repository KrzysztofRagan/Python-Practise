from multiprocessing.sharedctypes import Value


banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
values = []

for i in range(len((banknotes_coins))):
  values.append(0)

dict_denominations = dict(zip(banknotes_coins,values))

print(dict_denominations)

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1
 
dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2
 
dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for key in dict_denominations:
  print('Denominate: {} - amount      {}'.format(key, dict_denominations[key]))