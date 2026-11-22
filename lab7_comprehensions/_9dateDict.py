# 9. Write a program to group expenses datewise into a dictionary using list comprehension.
# Input: None (data defined in the script)
# Output: {'01-02-2026': [500, 100], '03-02-2026': [1500], '05-02-2026': [200], '06-02-2026': [350], '10-02-2026': [1200], '14-02-2026': [50, 450], '20-02-2026': [80], '25-02-2026': [2100]}

exp_list = [
    "01-02-2026", 500,
    "03-02-2026", 1500,
    "01-02-2026", 100,
    "05-02-2026", 200,
    "06-02-2026", 350,
    "10-02-2026", 1200,
    "14-02-2026", 50,
    "14-02-2026", 450,
    "20-02-2026", 80,
    "25-02-2026", 2100
]

exp_dict = {}
exp_dict = {
    date:[exp_list[date_in + 1] for date_in in range(len(exp_list)) if exp_list[date_in] == date]
    for date in exp_list[::2]
}

print(exp_dict)