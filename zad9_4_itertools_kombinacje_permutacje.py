import itertools as it
import math

from sympy import factor

#ITERTOOLS IS MODULE, WHERE YOU CAN MAKE COMBINATIONS, AND PERMUTATIONS
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
n = len(notes)
k = 4

#HOW MANY POSIBLE VARIANTS WITHOUT REPETITION
possible_var = (math.factorial(n)/math.factorial((n-k)))
print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(possible_var))
# PERMUTATIONS RETURN VALUES WITHOUT REPETITION. SO HERE FROM LIST OF NOTES BELOW IS RETURNED
for i, variant in enumerate(it.permutations(notes, k), 1):
  print(i, variant)

#HOW MANY POSIBLE VARIANTS WITH REPEATING
possible_rep_var = math.pow(n,k)
print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(possible_rep_var))
#COMBINATIONS WITH REPEATING
for i, variant in enumerate(it.product(notes, repeat=k), 1):
  print(i, variant)
  