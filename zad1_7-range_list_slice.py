from itertools import chain, combinations

plot_colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def WhatColor(plot_colors, n):
  new_colors = plot_colors[:n]
  return new_colors

# DO GENEROWANIA WSYZSKTICH DOSTEPNYCH WARIANTOW Z LISTY
# def all_subsets(ss):
#     return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

# for subset in all_subsets(plot_colors):
#     print(subset)


for i in range(1, len(plot_colors)+1):
  print(WhatColor(plot_colors, i))

text = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.'

print(text[text.index('(')+1 : text.index(')')])