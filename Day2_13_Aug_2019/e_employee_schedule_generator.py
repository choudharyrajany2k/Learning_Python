#!/usr/bin/python
"""
Purpose: Employee Schedule generator

MON-FRI :9:00 AM to 6:00 PM
SAT : 9:00 AM to 1:00 PM
SUN : HOLIDAY
"""
week_of_day = input("Please Enter Week of the day")

print("You Entered : ", week_of_day.tolower())

week_day_timing = "TIMING is 9:00 AM to 6:00 PM"
satur_day_timing = "TIMING is 9:00 AM to 1:00 PM"
sunday_timing = 'HOLIDAY'
if week_of_day == 'monday':
    print(Week_day_timing)
elif week_of_day == 'tuesday':
    print(Week_day_timing)
elif week_of_day == 'wednesday':
    print(Week_day_timing)
elif week_of_day == 'thursday':
    print(Week_day_timing)
elif week_of_day == 'friday':
    print(Week_day_timing)
elif week_of_day == 'saturday':
    print(satur_day_timing)
else:
    print(sunday_timing)
