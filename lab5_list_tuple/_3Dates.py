import re
from datetime import datetime

dates = ["10-05-2026", "29-02-1909", "32-07-2006", "10-3-2003"]

for date in dates:
    if re.fullmatch(r"\d{2}-\d{2}-\d{4}", date):
        try:
            datetime.strptime(date, "%d-%m-%Y")
            print(date)
        except ValueError:
            pass