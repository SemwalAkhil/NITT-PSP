# 3. Write a program to filter and print valid calendar dates from a list of date strings.
# Input: None (data defined in the script)
# Output: 10-05-2026

import re

dates = ["10-05-2026", "29-02-1909", "32-07-2006", "10-3-2003"]

for date in dates:
    if re.fullmatch(r"\d{2}-\d{2}-\d{4}", date):
        d, m, y = [int(x) for x in date.split("-")]
        if 1 <= m <= 12:
            if m in (1, 3, 5, 7, 8, 10, 12):
                if 1 <= d <= 31:
                    print(date)
            elif m in (4, 6, 9, 11):
                if 1 <= d <= 30:
                    print(date)
            elif m == 2:
                is_leap = (y % 400 == 0) or (y % 100 != 0 and y % 4 == 0)
                if is_leap and 1 <= d <= 29:
                    print(date)
                elif not is_leap and 1 <= d <= 28:
                    print(date)
