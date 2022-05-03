#YOU CAN USE CLASS OPERATORS TO ADD ETC. ELEMENTS TO CLASS. THERES NO NEED TO WRITE IT FROM THE BEGGINING


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

    def __str__(self):
      return "Kind: {}, Name: {}, Additives: {}".format(self.kind, self.name, self.additives)

    def __iadd__(self, other):
      if type(other) is str:
        self.additives.append(other)
        return self
      elif type(other) is list:
        self.additives.extend(other)
        return self
      else:
        print('Wrong format of text is given')
        
 
       
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
print(cake01)

cake01 += 'nice text'
print(cake01)

cake01 += ['hello', 'Kinga']
print(cake01)