# a = b = c = 10
# print("to a: ", a, id(a))
# print("to b: ", b, id(b))
# print("to c: ", c, id(c))

# a = 20
# print("PO ZMIANIE")
# print("to a: ", a, id(a))
# print("to b: ", b, id(b))
# print("to c: ", c, id(c))

###########################


# a = b = c = [1,2,3]
# print("to a: ", a, id(a))
# print("to b: ", b, id(b))
# print("to c: ", c, id(c))

# a.append(4)
# print("PO ZMIANIE")
# print("to a: ", a, id(a))
# print("to b: ", b, id(b))
# print("to c: ", c, id(c))

##########################

x =10 
y= 10

print ('x: ', id(x), 'y: ', id(y))

y = y + 1 - 1

print ('x: ', id(x), 'y: ', id(y))

y = y + 1234567890 - 1234567890

print ('x: ', id(x), 'y: ', id(y))
