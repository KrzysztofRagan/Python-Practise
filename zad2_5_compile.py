import math
import time


formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range (100000):
    argument_list.append(i/10)

for formula in formulas_list:
  results_list = []
  print("Current formula: {}".format(formula))
  start1 = time.time()
  for x in argument_list:
    results_list.append(eval(formula))
  stop1 = time.time()
  print('max is: {}'.format(max(results_list)))
  print('min is: {}'.format(min(results_list)))
  print('time for compiling in this formula: {}'.format(stop1-start1))



  for formula in formulas_list:
    results_list = []
    print("Current formula: {}".format(formula))
    start2 = time.time()
    compiled_code = compile(formula, 'internal variable source' ,'eval')
    for x in argument_list:
      results_list.append(eval(compiled_code))
    stop2 = time.time()
    print('max is: {}'.format(max(results_list)))
    print('min is: {}'.format(min(results_list)))
    print('time for compiling in this formula: {}'.format(stop2-start2))


    print('Compiled code is: {} faster than not compiled'.format(((stop1-start1)/(stop2-start2))))



