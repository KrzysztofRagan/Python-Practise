projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

leaders_in_projects = zip(projects, leaders)

# for project,leader in leaders_in_projects:
#   print('The leader of {} is {}'.format(project,leader))

dates = ['2016-06-23', '2016-08-29', '1994-01-01']


for nummer, (project,date, leader) in enumerate(zip(projects, dates, leaders)):
  print('{} - The leader of {} started {} is {}'.format(nummer +1, project, date, leader))