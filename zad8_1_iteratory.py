import time

#IN CLASSES THERE IS OPTION OF USING __next__ which makes obcject from class iterator. When you use __iter__ it means, that object is iterable. These build in methods make that in easy way there is option of iterate object. It s much faster and takes less memory than standard way of doing it in for

class Combinations():
  def __init__(self, products, promotions, customers):
    self.products = products
    self.promotions = promotions
    self.customers = customers
    self.current_product = 0
    self.current_promotion = 0
    self.current_customer = 0

  def __next__(self):
    item_to_return = 0
    if self.current_customer >= len(self.customers):
      self.current_customer = 0 
      self.current_promotion += 1

    if self.current_promotion >= len(self.promotions):
      self.current_promotion = 0
      self.current_product += 1

    if self.current_product >= len(self.products):
      self.current_product = 0
      raise StopIteration()

    item_to_return = "{} - {} - {}".format(self.products[self.current_product], 
    self.promotions[self.current_promotion],
     self.customers[self.current_customer],)
    self.current_customer += 1
    return item_to_return

  def __iter__(self):
    return self


products = ["Product {}".format(i) for i in range(1, 500)]


promotions = ["Promotion {}".format(i) for i in range(1, 50)]


customers = ['Customer {}'.format(i) for i in range(1, 500)]



# STANDARD WAY OF GOING THROUGH LISTS. IT TAKES A LOT OF MEMORY AND TIME
# for i in products:
#     for j in promotions:
#         for k in customers:
#             combinations.append("{} - {} - {}".format(i, j, k))


combinations = Combinations(products, promotions, customers)

for c in combinations:
    # here an analysis will be done - currently, just nothing happens :)
    pass

time.sleep(10)

