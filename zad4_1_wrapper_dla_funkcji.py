import functools
import datetime
from timeit import default_timer as timer


def wrapper(func):
  def func_wrapper(*args, **kwargs):
    starttime = timer()
    print('arguments given: {},{}'.format(args, kwargs))
    result = func(*args, **kwargs)
    finishtime= timer()
    print('Function "{}" has duration time: {}'.format(func.__name__ , (finishtime - starttime)))
    return result
  return func_wrapper

#@wrapper    TAK AUTOMATYCZNIE TWORZY SIE WRAPPER DO FUNKCJI, ALE W TYM PRZYPADKU ONA SIE ZAPETLA
def get_sequence(n):
    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v

wrapper_get_sequence = wrapper(get_sequence)
print(wrapper_get_sequence(18))


