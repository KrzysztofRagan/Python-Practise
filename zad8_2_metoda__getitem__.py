
class Combinations:
 
  def __init__(self, products, promotions, customers):
      self.products = products
      self.promotions = promotions
      self.customers = customers

#HOW TO BUILD AN OBJECT, THAT DOES NOT CONTAIN SELF ITERATOR BUT CONTAINS METHOD GETITEM
# THANKS TO GETITEM METHOD WE CAN GET TO EACH SINGLE ELEMENT OF SOME CLASS, BUT THIS CLASS DOESNT HAVE ITERATOR

  def __getitem__(self, item):
    if item < len(self.products) * len(self.promotions) * len(self.customers):
      pos_products = item // (len(self.promotions) * len(self.customers))
      item = item % (len(self.promotions)*len(self.customers))
     
     
      pos_promotions = item // len(self.customers)
      item = item // len(self.customers)
     
  
      pos_customers = item
      return '{} - {} - {}'.format(products[pos_products], promotions[pos_promotions], customers[pos_customers])
    else:
      raise StopIteration()
 
 
products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]
 

combinations = Combinations(products, promotions, customers)

combinations_iterator = iter(combinations)
print(next(combinations_iterator))


# --- GET EVERY SINGLE POSSIBLE COMBINATION (FOR FOR THERE IS NO PROBLEM IN ITERATE GETMETHOD)
# for i in range(30):
#   print(combinations.__getitem__(i))


# DOES THE SAME AS ABOVE BUT USES METHOD NEXT. BUT HERE IS PROBLEM WITH ITERATOR, SO YOU HAVE TO USE METHOD ITER (LINE 35)
for c in combinations_iterator:
  print(c)
