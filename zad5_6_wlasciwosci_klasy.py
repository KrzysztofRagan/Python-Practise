
class Cake:
  known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
  bakery_offer = []

  # INICJOWANIE ATRYBUTÓW W KLASIE
  def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
    self.name = name
    if kind in Cake.known_types:
      self.kind = kind
    else:
      self.kind = 'other'
    self.taste = taste
    self.additives = additives
    self.filling = filling
    self.__gluten_free = gluten_free
    if kind == 'cake' or text == '':
      self.__text = text
    else:
      self.__text = ''
      print('Text can be only set for cake, not for {}'.format(self.kind))
    Cake.bakery_offer.append(self)

  def show_info(self):
    print(self.name.upper())
    print('Kind: {}'.format(self.kind))
    print('Taste: {}'.format(self.taste))
    print('Gluten free: {}'.format(self.__gluten_free))
    if self.additives:
      print('Additives: ')
      for additive in self.additives:
        print(additive)
    if self.filling:
      print('Filling: ')
      print(self.filling)
    if self.__text:
      print('Text: {}'.format(self.__text))
    print(20*'-')


  def set_filling(self, filling):
    self.filling = filling

  def add_additives(self, additives):
    self.additives.extend(additives)

  def __get_text(self):
    return self.__text

  def __set_text(self, new_text):
    if self.kind == 'cake':
      self.__text = new_text
    return self.__text

  Text = property(__get_text, __set_text, None, "if cake, then you can create a new text")

cake1_additives = ['chocolate', 'nuts']

# TWORZENIE NOWYCH INSTANCJI KLASY
cake1 = Cake('vanilla cake', 'cake', 'vanilla', cake1_additives, None, False, 'Happy birthday')
cake2 = Cake('chocolate muffin', 'muffin', 'chocolate', ['chocolate'],'', False, '')
cake3 = Cake('super sweet maringue', 'maringue', 'very sweet', [],'', True, '')
cake4 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, 'hello')




cake2.set_filling('cream')
cake3.add_additives(['cocoa powder', 'coconuts'])

print('Today in our offer:')

#SHOW_INFO POKAZUJE INFO O KLASIE

for cake in Cake.bakery_offer:
  cake.show_info()


# UKRYTE ATRYBUTY MOZNA ZMIENIAC, TYLKO TRZEBA PAMIETAC O BUDOWNIE- DODAC NAZWE KLASY I _ __
cake3._Cake__gluten_free = False

cake3.show_info()
print(dir(cake3))


#ZMIANA WLASCIWOSCI NA POPRAWNYM OBIEKCIE
cake1.Text = 'You are awesome'
cake1.show_info()

#ZMIANA WLASCIWOSCI NA NIEPOPRAWNYM
cake2.Text = 'Hello'
cake2.show_info()

#INFORMACJE O KLASACH

# print(isinstance(cake1, Cake))
# print('vars instance: {}'.format(vars(cake1)))
# print('vars class: {}'.format(vars(Cake)))

# print('dir instance: {}'.format(dir(cake1)))
# print('dir class: {}'.format(dir(Cake)))
