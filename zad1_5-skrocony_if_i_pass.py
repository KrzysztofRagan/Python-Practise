from datetime import date
import calendar

price = 123
bonus = 23
bonus_granted = True
 
# if bonus_granted:
#     price -= bonus
 
# print(price)

price = price - bonus_granted if bonus_granted else price

##################################

rating = 3
 
# if rating == 5:
#     print('very good')
# elif rating == 4:
#     print('good')
# else:
#     print('weak')

grade = 'very good' if rating == 5 else 'good' if rating == 4 else 'weak'
print(grade)


##################################

today_number = date.today().weekday()
today_weekday = calendar.day_name[today_number]
print(today_weekday)

what_to_do = 'helping mom' if today_weekday == 'Monday' else 'I have loundry to do' if today_weekday == 'Tuesday' or 'Wednesday' else 'I am on duty' if today_weekday == 'Thursday' else 'two meetings' if today_weekday == 'Friday' else 'you have lessons' if today_weekday == 'Saturday' else 'Sunday is for us'

print(what_to_do)






