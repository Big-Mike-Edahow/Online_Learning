# current_date.py
# Get the current date and time; Add 1 month, 1 week, 1 hour.

from datetime import *
from dateutil.relativedelta import *

now = datetime.now()
print("\nCurrent Date and Time:")
print(now, "\n")

now += relativedelta(months=1, weeks=1, hour=10)
print("Date and Time 1 month, 1 week, 1 hour from now:")
print(now, "\n")

