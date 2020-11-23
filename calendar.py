import calendar 

date = input()
date = date.replace(" ", "")
month = int(date[:2])
day = int(date[2:4])
year = int(date[4:])

day_of_week = calendar.weekday(year,month,day)
if day_of_week == 0:
    print("MONDAY")
elif day_of_week == 1:
    print("TUESDAY")
elif day_of_week == 2:
    print("WEDNESDAY")
elif day_of_week == 3:
    print("THURSDAY")
elif day_of_week == 4:
    print("FRIDAY")
elif day_of_week == 5:
    print("SATURDAY")
elif day_of_week == 6:
    print("SUNDAY")