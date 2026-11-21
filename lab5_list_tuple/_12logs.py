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