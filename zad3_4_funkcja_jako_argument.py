def double(x):
    return 2 *x
 
def square(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2


def generate_values(func,numbers):
  score = []
  for number in numbers:
    score.append(func(number))
  print(score)
  return score

xtable = list(range(11))

generate_values(double, xtable)
generate_values(square, xtable)
generate_values(negative, xtable)
generate_values(div2, xtable)

