def calculate_paint(efficency_litr_per_m2=5, *how_many_m):
  total_area = sum(how_many_m)
  paint = efficency_litr_per_m2 * total_area

  return print(paint)


def log_it(*arguments_to_file):
  file = '/Users/krzysztofragan/Desktop/vscode/python-kurs/katalog_na_pliki/plik1'
  with open(file, 'a+') as f:
      for i in arguments_to_file:
        f.write(i + ' ')
      f.write('\n')


to_file = ['czesc', 'jak', 'sie', 'masz', 'jestem' , 'krzysiek', 'i' , 'jestem', 'fajny']



calculate_paint(5,10,15,20)

how_many_list = [10,15,20]

calculate_paint(5 , *how_many_list)

