import calendar

print(calendar.TextCalendar(firstweekday=6).formatyear(2015))
# calendar = calendar.setfirstweekday(calendar.SUNDAY)

print(calendar.isleap(2016))
print(calendar.weekday(2015, 8, 5))
print(list(calendar.day_name)[calendar.weekday(2015, 8, 5)])
print(int("08"))

