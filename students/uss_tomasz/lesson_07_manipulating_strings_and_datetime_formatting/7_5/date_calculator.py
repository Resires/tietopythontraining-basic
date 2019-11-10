# Date calculator - write a script that adds custom number of years, days and hours and minutes to current
# date and displays the result in human readable format
from datetime import datetime
from time import mktime


def add_years_days_hours_minutes(user_datetime, **kwargs):
    timestamp = mktime(user_datetime.timetuple())
    for time_unit in kwargs:
        if time_unit == "year":
            timestamp += kwargs[time_unit] * 3600 * 24 * 365
        if time_unit == "day":
            timestamp += kwargs[time_unit] * 3600 * 24
        if time_unit == "hour":
            timestamp += kwargs[time_unit] * 3600
        if time_unit == "minute":
            timestamp += kwargs[time_unit] * 60
    return datetime.fromtimestamp(timestamp)


current_datetime = datetime.now()
print("Currently there is {:%Y-%m-%d %H:%M}".format(current_datetime))
print("One year from now will be", add_years_days_hours_minutes(current_datetime, year=1))
print("Two days from now will be", add_years_days_hours_minutes(current_datetime, day=2))
print("Three hours from now will be", add_years_days_hours_minutes(current_datetime, hour=3))
print("For minutes from now will be", add_years_days_hours_minutes(current_datetime, minute=3))
print("1 year, 1 day, 1 hour and 1 minute from now will be",
      add_years_days_hours_minutes(current_datetime, year=1, day=1, hour=1, minute=1))
