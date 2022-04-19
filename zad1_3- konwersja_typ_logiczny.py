#MOJE :)
options = ['load data', 'export data', 'analyze & predict']
choice = 'x'

def DisplayOptions(options):
  print('1 - ', options[0])
  print('2 - ', options[1])
  print('3 - ', options[2])
  choice = input('Select option above or press enter to exit: ')
  return choice

while choice:
  choice = DisplayOptions(options)
  if choice == '':
    print("End of this programm")
    quit()
  else:
    try:
      choice_num = int(choice)
    except:
      print("Cannot convert choice to integer!")
  if choice_num >= 0 and choice_num <= 3:
    choice_num = choice_num - 1
    print("Choice is: ", options[choice_num])
  else:
    print("There was choosen wrong number!")




# GOTOWE ROZWIĄZANIE!!
# def DisplayOptions(options):
#     for i in range(len(options)):
#         print("{} - {}".format(i+1, options[i]))
 
#     choice = input('Select option above or press enter to exit: ')
#     return choice
    
 
# choice='x'
# options = ['load data', 'export data', 'analyze & predict']
 
# while choice:
 
#     choice = DisplayOptions(options)
 
#     #executed only if something was entered
#     if choice:
#         try:
#             choice_num = int(choice)-1
#             if choice_num >=0 and choice_num < len(options):
#                 print("you have selected {} - {}".format(choice_num+1, options[choice_num]))
#             else:
#                 print("choose a value from a list or press enter")
#         except:
#             print("You need to enter a number")
#     else:
#         print('----- END -----')
  