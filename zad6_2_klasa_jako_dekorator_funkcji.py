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
 
    def add_additives(self, additives):
        self.additives.extend(additives)
 
 

#TWORZYMY KLASE, KTORA SPRAWDZA, CZY NA NOWEJ LISCIE NIE POWTARZAJA SIE OBIEKTY ZE STAREJ.
class NoDuplicates:

  def __init__(self, funct):
    self.funct = funct


  def __call__(self, cake, new_additives):
    no_duplicate_list = []
    for add in cake.additives:
      no_duplicate_list.append(add)
    for new_add in new_additives:
      if new_add not in no_duplicate_list:
        cake.additives.append(new_add)
    return cake






#DEKORATOR FUNKCJI
@NoDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)





cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')






add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()
 
add_extra_additives(cake01, ['strawberries', 'sugar-flowers','chocolade', 'nuts'])
cake01.show_info()