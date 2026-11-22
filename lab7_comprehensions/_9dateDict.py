# 9. Write a program to read expenses from the user and group them datewise into a dictionary using list comprehension.
# Input: (5 01-02-2026 500 03-02-2026 1500 01-02-2026 100 05-02-2026 200 06-02-2026 350), (2 01-01-2026 100 01-01-2026 200)
# Output: {'01-02-2026': [500, 100], '03-02-2026': [1500], '05-02-2026': [200], '06-02-2026': [350]}, {'01-01-2026': [100, 200]}

n = int(input("Enter number of expenses: "))
exp_list = []
for i in range(n):
    d = input("Enter date (DD-MM-YYYY): ")
    amt = int(input("Enter amount: "))
    exp_list.extend([d, amt])

exp_dict = {}
exp_dict = {
    date:[exp_list[date_in + 1] for date_in in range(len(exp_list)) if exp_list[date_in] == date]
    for date in exp_list[::2]
}

print(exp_dict)
