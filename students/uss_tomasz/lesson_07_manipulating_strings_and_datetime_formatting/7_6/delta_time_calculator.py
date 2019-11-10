# Delta time calculator - write a script that calculates time difference in days
# between current date and custom date in the future.
from datetime import datetime
from time import mktime


def calculate_delta_time(user_datetime):
    current_datetime = datetime.now()
    current_timestamp = mktime(current_datetime.timetuple())
    future_timestamp = mktime(user_datetime.timetuple())
    seconds_difference = future_timestamp - current_timestamp
    days_difference = int(seconds_difference / 24 / 3600)
    return days_difference


future_date = datetime(2019, 12, 6, 15, 00)
print(calculate_delta_time(future_date), "days until", future_date)
