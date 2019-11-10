# Date printer - write a script that displays current date in human-readable format
from datetime import datetime
current_datetime = datetime.now()
print('{:%Y-%m-%d %H:%M}'.format(current_datetime))
