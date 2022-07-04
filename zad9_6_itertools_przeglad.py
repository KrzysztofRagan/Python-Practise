#MODULE ITERTOOLS IS NICE TOOL TO WORK WITH DATA. REMEMBER ABOUT IT, BECAUSE IT HAS REALLY LOTS OF USEFUL TOOLS
import itertools as it

from sympy import is_perfect


def get_factors(x):
  factors = []
  for i in range(1, x):
    if x%i == 0:
      factors.append(i)
  return factors



candidate_list = []

for i in range(1, 101):
  candidate_list.append(i)

filtered_list = list(it.filterfalse(lambda x: x!= sum(get_factors(x)), candidate_list))

def is_perfect(_list):
  for i in _list:
    factors = get_factors(i)
    if sum(factors) == i:
      filtered_list.append(i)

# is_perfect(candidate_list)
print(filtered_list)