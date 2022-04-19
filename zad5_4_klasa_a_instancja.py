
class Cake:
  known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
  bakery_offer = []


  def __init__(self, name, kind, taste, additives, filling):
    self.name = name
    if kind in Cake.known_types:
      self.kind = kind
    else:
      self.kind = 'other'
    self.taste = taste
    self.additives = additives
    self.filling = filling
    Cake.bakery_offer.append(self)

  def show_info(self):
    print(self.name.upper())
    print('Kind: {}'.format(self.kind))
    print('Taste: {}'.format(self.taste))
    if self.additives:
      print('Additives: ')
      for additive in self.additives:
        print(additive)
    if self.filling:
      print('Filling: ')
      print(self.filling)
    print(20*'-')


  def set_filling(self, filling):
    self.filling = filling

  def add_additives(self, additives):
    self.additives.extend(additives)

cake1_additives = ['chocolate', 'nuts']
cake1 = Cake('vanilla cake', 'cake', 'vanilla', cake1_additives, filling = None)
cake2 = Cake('chocolate muffin', 'muffin', 'chocolate', ['chocolate'],'')
cake3 = Cake('super sweet maringue', 'maringue', 'very sweet', [],'')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')
cake04.show_info()



cake2.set_filling('cream')
cake3.add_additives(['cocoa powder', 'coconuts'])

print('Today in our offer:')
for cake in Cake.bakery_offer:
  cake.show_info()

print(isinstance(cake1, Cake))
print('vars instance: {}'.format(vars(cake1)))
print('vars class: {}'.format(vars(Cake)))

print('dir instance: {}'.format(dir(cake1)))
print('dir class: {}'.format(dir(Cake)))
