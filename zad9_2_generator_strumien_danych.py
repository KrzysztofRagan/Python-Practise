import random


#HERE GENERATOR IS USED TO CREATE A LIST OF SUM 100 OF 3 RANDOM NUMBERS. 
def random_with_sum(number_of_values, asserted_sum):
  trial = 0
  numbers = []
  while True:
    trial += 1
    for i in range(number_of_values):
      i = random.randint(1,101)
      numbers.append(i)
    if sum(numbers) == asserted_sum:
      yield ((trial, numbers))
      trial = 0
      break
    else:
      numbers.clear()


for i in range(10):
  (number_of_trials, numbers) = next(random_with_sum(3,100))
  print(number_of_trials, numbers)
