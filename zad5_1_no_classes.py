cake01 = {
'taste' : 'vanilia',
'glaze' : 'chocolate',
'text' : 'Happy Birthday',
'weight' : '0.7'
}

cake02 = {
'taste' : 'tee',
'glaze' : 'lemon',
'text' : 'Happy Python Coding',
'weight' : '1.3'
}

cakes = [cake01 , cake02]
 
 
def show_cake_info(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake['taste'], cake['glaze'], cake['text'], cake['weight']))
 

for cake in cakes:
  show_cake_info(cake)



