# import math

# argument_list = []

# i = 0
# element = 0

# while i != 100:
#   argument_list.append(round(element,1))
#   element += 0.1
#   i += 1



# formula = input("Please write pattern with using x as an argument")


# value = 0



# while argument_list[value]+1:
#   if value != 99:
#     x = argument_list[value]
#     equation = round(eval(formula),1)
#     print(equation, value)
#     value+=1
#   else:
#     break

  
import math
 
argument_list = []
 
for i in range (100):
    argument_list.append(i/10)
    
formula = input("Please enter a formula, use 'x' as the argument: ")
 
for x in argument_list:
    print("{0:3.1f} {1:6.2f}".format(x, eval(formula)))

    