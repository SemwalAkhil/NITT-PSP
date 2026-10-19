"""
3. Input is a list of dates. Using regex, print only valid dates

INPUT:  dates(D)  ["10-05-2026", "29-02-1909"]
OUTPUT: 10-05-2026
INPUT:  dates(D)  ["32-07-2006", "10-3-2000"]
OUTPUT: Not found
"""
import re
from datetime import datetime

dates = ["10-05-2026", "29-02-1909", "32-07-2006", "10-3-2000"]

for date in dates:
    if re.fullmatch(r"\d{2}-\d{2}-\d{4}", date):
        try:
            datetime.strptime(date, "%d-%m-%Y")
            print(date)
        except ValueError:
            pass