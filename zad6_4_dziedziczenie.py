# YOU CAN SEE THAT THANKS TO INHERITANCE YOU CAN HAVE ALL ATRIBUTES FROM MOTHER CLASS, BUT IT DEPENDS TO YOU IF YOU WANT TO HAVE THEM, OR NOT

class Cake:
 
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
 
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
 
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)
 
    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


class SpecialCake(Cake):
  def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text):
    super().__init__(name, kind, taste, additives, filling)
    self.occasion = occasion
    self.shape = shape
    self.ornaments = ornaments
    self.text = text

#WHILE CREATING METHOD IN CHILD CLASS REMEMBER, THAT NOW THAT METHOD IS IMPORTANT. THANKS TO FUNCT SUPER() YOU CAN EASLY HAVE EVERYTHING FROM MOTHER CLASS
  def show_info(self):
    super().show_info()
    print("occasion:    {}".format(self.occasion))
    print("shape:    {}".format(self.shape))
    print("ornaments:    {}".format(self.ornaments))
    print("text:    {}".format(self.text))


birthday = SpecialCake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream',
                       'birthday', 'standard', 'hearts', '15')
wedding  = SpecialCake('Vanilla Cake','cake', 'vanilla', ['whipped cream', 'coconut shirms'], 'strawberries cream',
                       'wedding', 'pyramid', 'pigeons', 'Patricia & Tom')

for special in SpecialCake.bakery_offer:
  print(special.full_name)
  special.show_info()

