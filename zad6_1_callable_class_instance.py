

class NoDuplicates:
  def __init__(self):
    self.list = []

  def __call__(self, new_items):
    for item in new_items:
      if item not in self.list:
        self.list.append(item)
      else:
        print('Item {} is already on the list'.format(item))
    





my_no_dup_list = NoDuplicates()
my_no_dup_list(['keyboard', 'mouse'])
my_no_dup_list(['keyboard', 'mouse', 'pendrive'])
my_no_dup_list(['charger', 'pendrive'])

print(my_no_dup_list.list)