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
    exp_list[date_in]:exp_dict[exp_list[date_in]].append(exp_list[date_in+1]) if exp_dict.get(exp_list[date_in],False) else [exp_list[date_in+1]]
    for date_in in range(0,len(exp_list),2)
}
print(exp_dict)