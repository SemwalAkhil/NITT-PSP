"""
12. Store logs of different types ( ex normal, critical etc) with time stamp. Show cateogyr wise logs and hour wise.

INPUT: logs(L) [("09:15","normal","Started")]
OUTPUT:
normal:
('09:15', 'normal', 'Started')
09:00
('09:15', 'normal', 'Started')

INPUT: logs(L) [("10:30","critical","Error")]
OUTPUT:
critical:
('10:30', 'critical', 'Error')
10:00
('10:30', 'critical', 'Error')
"""

logs = [
    ("09:15", "normal", "Started"),
    ("09:30", "critical", "Disk full"),
    ("10:10", "normal", "User login"),
    ("10:45", "critical", "System error"),
    ("09:50", "warning", "High memory")
]

categories = ("normal", "warning", "critical")

print("Category-wise logs:")
for category in categories:
    print(category + ":")
    for log in logs:
        if log[1] == category:
            print(log)

print("Hour-wise logs:")
hours = ()

for log in logs:
    hour = log[0][:2]
    if hour not in hours:
        hours += (hour,)
        print(hour + ":00")
        for item in logs:
            if item[0][:2] == hour:
                print(item)