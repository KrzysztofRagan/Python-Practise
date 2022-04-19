from datetime import date, datetime

def f_minutes(start, end):
  difference = end - start
  minutes_difference = difference.total_seconds() / 60
  return print(round(minutes_difference , 1))

def f_hours(start, end):
  difference = end - start
  hours_difference = difference.total_seconds() / 3600
  return print(round(hours_difference , 1))


def f_days(start, end):
  difference = end - start
  days_difference = difference.total_seconds() / 86400
  return print(round(days_difference , 1))


def create_function(span):
  if span == 'm':
    sec = 60
  elif span == 'h':
    sec = 3600
  elif span == 'd':
    sec = 86400

  source = '''
def f(start, end):
  difference = end - start
  minutes_difference = difference.total_seconds() / {}
  return print(round(minutes_difference , 1))
'''.format(sec)
  exec(source, globals())
  return f


start = datetime(2022,3,31,23,3)
end = datetime.now()
f_minutes(start , end)
f_hours(start, end)
f_days(start, end)

minutes = create_function('m')
minutes(start, end)


hours = create_function('h')
hours(start, end)

days = create_function('d')
days(start, end)