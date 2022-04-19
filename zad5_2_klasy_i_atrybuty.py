
class Cake:
  def __init__(self, name, kind, taste, additives, filling):
    self.name = name
    self.kind = kind
    self.taste = taste
    self.additives = additives
    self.filling = filling



cake1 = Cake('big', 'brown', 'chocolate', 'sweets', 'good')
cake2 = Cake('small', 'fruity', 'strawberry', 'cookies', 'yummy')

bakery_offer = [cake1, cake2]

for cake in bakery_offer:
  print('Today in our offer is {} - {} main taste: {} with additives of {}, filled with {}'.format(cake.name, cake.kind, cake.taste, cake.additives, cake.filling))
  
