# 12. Write a program to group system log entries by category and by hour.
# Input: (5 09:15 normal Started 09:30 critical "Disk full" 10:10 normal "User login" 10:45 critical "System error" 09:50 warning "High memory"), (2 08:00 normal Login 09:00 warning High-RAM)
# Output:
#   Run 1:
#   Category-wise logs:
#   normal:
#   ('09:15', 'normal', 'Started')
#   ('10:10', 'normal', 'User login')
#   Hour-wise logs:
#   09:00
#   ('09:15', 'normal', 'Started')
#   Run 2:
#   Category-wise logs:
#   normal:
#   ('08:00', 'normal', 'Login')
#   warning:
#   ('09:00', 'warning', 'High-RAM')
#   critical:
#   Hour-wise logs:
#   08:00
#   ('08:00', 'normal', 'Login')
#   09:00
#   ('09:00', 'warning', 'High-RAM')

n = int(input("Enter number of logs: "))
logs = []
for i in range(n):
    t = input("Enter time (HH:MM): ")
    cat = input("Enter category: ")
    msg = input("Enter message: ")
    logs.append((t, cat, msg))

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
