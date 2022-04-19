def show_progress(how_much, character = '*'):
  line = character * how_much
  print(line)


show_progress(5)
show_progress(10)
show_progress(15)
show_progress(20)
show_progress(35)
show_progress(10, '+')