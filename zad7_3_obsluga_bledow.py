import datetime as dt
 
#You can work with the errors in classes from more specified to more general 

class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
 
    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")


    @classmethod
    def publish_offer(cls, trips):
      list_of_errors = []
      for trip in trips:
        try:
          cls.check_data(trip)
        except ValueError as e:
          list_of_errors.append('{} : {}'.format(trip.symbol, str(e)))
        except Exception as e:
          list_of_errors.append('{} : {}.'.format(trip.symbol, str(e)))

      if len(list_of_errors) > 0:
        print('The list of trips has errors: {}'.format(list_of_errors))
      else:
        print('The offer will be published')


 
trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]


try:
  print('Starting to check if trips are added correctly')
  Trip.publish_offer(trips)
  print('done')
except Exception as e:
  print('There was a mistake: {}'.format(str(e)))