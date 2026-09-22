from datetime import datetime, date, timedelta, time

d = date(2012,5,15)
print(d, type(d))

t = time(12,15,)
print(t, type(t))

dt = datetime. combine(d,t)
print(dt, type(dt))
print(datetime.now().replace(microsecond=0))
dtt = datetime.now()
dtt = dtt.replace(hour=0, minute=0, second=0, microsecond=0)
print(dtt)

# dat = input('Введите дату (формат: ДД.ММ.ГГГГ): ')
# date_ = datetime.strptime (dat, '%d.%m.%Y')
# print(date_)
# dt = datetime.now()
# d = dt.timetuple()
# for i in d:
#     print(i)

# print(dt.weekday())
# print(dt.isoweekday())
# cc = dt.isocalendar()
# print(cc)
#
# print(dt.strftime('%A %B'))
# print(dt.strftime('%X'))
# days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
# print(days[dt.weekday()])
#
# dat = input('Введите дату (формат: ДД.ММ.ГГГГ): ')
# date_ = datetime.strptime (dat, '%d.%m.%Y')
# td = date_ - dt
# print(td)


dt = datetime.now()
b_day = input('Введите дату (формат: ДД.ММ.ГГГГ): ')

try:
    date_ = datetime.strptime(b_day, '%d.%m.%Y')
except ValueError:
    print('Ошибка: некорректная дата')
    exit()

this_year_bday = date_.replace(year=dt.year)

if this_year_bday < dt:
    days = (dt - this_year_bday).days
    print(f'Прошло: {days} дней')
elif this_year_bday > dt:
    days = (this_year_bday - dt).days
    print(f'Осталось: {days} дней')
else:
    print('С днём рождения!')

