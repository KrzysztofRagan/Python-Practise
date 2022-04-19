import time
import functools

#lru_cache optymalizuje funkcje determistyczna poprzez zapisanie w pamieci wynikow juz obliczonych (nadaje sie tez np do silni)
@functools.lru_cache()
def fib(n):
  if n <= 2:
      result = n
  else:
      result = fib(n-1) + fib(n-2)    # dla 5   fib4  + fib3 = fib3+fib2 + fib2+fib1 = fib2+fib1 +2 + 2+1 = 2+1+2+1 = 8
      
  return result

                       



start = time.time()
for i in range(1, 10):
  print(fib(i))
stop = time.time()
print(stop - start)
print(fib.cache_info())

