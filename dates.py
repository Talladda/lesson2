from datetime import datetime
from datetime import date, timedelta
print(datetime.now().strftime('%d.%m.%Y %H:%M'))
day_ago = datetime.now() - timedelta(days=1)
print(day_ago.strftime('%d.%m.%Y %H:%M'))
month_ago = datetime.now() - timedelta(days=30)
print(month_ago.strftime('%d.%m.%Y %H:%M'))

date_string = "01/01/17 12:10:03.234567"
#date_time = date_string.split(' ') #Решила не делить по пробелам

#print(date_time[0])
#print(date_time[1])
print(datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f'))