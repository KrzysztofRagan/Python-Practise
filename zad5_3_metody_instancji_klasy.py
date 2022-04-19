
class Cake:
  def __init__(self, name, kind, taste, additives, filling):
    self.name = name
    self.kind = kind
    self.taste = taste
    self.additives = additives
    self.filling = filling

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

cakes_offer = [cake1, cake2, cake3]


cake2.set_filling('cream')
cake3.add_additives(['cocoa powder', 'coconuts'])

print('Today in our offer:')
for cake in cakes_offer:
  cake.show_info()