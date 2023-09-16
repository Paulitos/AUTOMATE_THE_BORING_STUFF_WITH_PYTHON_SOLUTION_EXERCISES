# Date Detection Page 186 Chapter 7
import re

# Define the regular expression pattern for DD/MM/YYYY dates
date_pattern = re.compile(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(1000|1[0-9]{3}|2000|20[0-9]{2}|2999)$')

# Example dates
example_dates = [
    "31/02/2020",
    "15/06/2022",
    "05-12-1990",
    "29/02/2020",
    "01/01/1001",
    "32/04/2021",
    "31/12/2999"
]

# Function to validate day and month
def is_valid_date(day, month):
    if (month in [4, 6, 9, 11] and day > 30) or (month == 2 and (day > 29 or (day > 28 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))))):
        return False
    return True

# Loop through the example dates
for date in example_dates:
    match = date_pattern.match(date)
    if match:
        day, month, year = map(int, match.groups())
        if is_valid_date(day, month):
            print(f"Valid date: {day}/{month}/{year}")
        else:
            print(f"Invalid date: Day is out of range for the given month. ({date})")
    else:
        print(f"Invalid date: Invalid date format. ({date})")

