import datetime
import calendar

current_date = datetime.datetime.now()
print ("Current date:", current_date)
print("Year:", current_date.year)
print("Month:", current_date.month)
print("Day:", current_date.day)

print(calendar.calendar(2025))
print(calendar.month(2025, 2))