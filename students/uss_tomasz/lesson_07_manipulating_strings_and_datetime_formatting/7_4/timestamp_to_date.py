# Timestamp to date - write a script that converts unix timestamp to human-readable date format
from datetime import datetime
from time import time
unix_timestamp = int(time())
converted_datetime = datetime.fromtimestamp(unix_timestamp)
print(converted_datetime)
