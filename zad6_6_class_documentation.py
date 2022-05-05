#Here I practise how important is documentating classes made by myself. You have to remember to always document your class as it;s shown below

class Cake:
  """
  Class Cake is about cake and describes it's different properties
  """
  bakery_offer = []

  def __init__(self, name, kind, taste, additives, filling):
      """
      init - arguments accepted
      name - name of the cake
      kind - kind of the cake
      taste - taste, which the cake has
      additives - additives added to cake
      filling - filling of the cake
      bakery_offer - list of all cakes made from class Cake
      """      
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
    """full name shows you name of the cake connected with it's kind- most important atrubutes

    Returns:
        name,kind
    """
    return "--== {} - {} ==--".format(self.name.upper(), self.kind)

help(Cake)