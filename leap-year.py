import datetime
week = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
        5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

find = input('Please enter a date (yyyy/mm/dd): ')
year, month, day = map(int, find.split('/'))

day = datetime.date(year, month, day)
weekday = day.isoweekday()

if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    leap = 'is a leap year'
else:
    leap = 'is not a leap year'

print('%s, %s, %s.' %(find, week[weekday], leap))
