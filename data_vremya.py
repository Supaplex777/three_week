from datetime import datetime,timedelta
import locale 
locale.setlocale(locale.LC_TIME,'ru_RU')
#Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
#Превратите строку "01/01/25 12:10:03.234567" в объект datetime
date_now = datetime.now() # cегодня 
delta = timedelta (days = 1 )
delta_2 = timedelta (days = 30)
date_yesterday = date_now - delta #вчера
date_30 = date_now - delta_2 # 30 дней назад 
date_string = "01/01/25 12:10:03.234567"
time_out_of_line = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f') #данные из строки 
print(time_out_of_line)
print(date_now)
print(date_yesterday)
print(date_30)