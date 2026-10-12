# 0 -> absent 1 -> present; Number of absent/present
abs_list = [0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0]
absent = len([i for i in abs_list if i == 0])
present = len([i for i in abs_list if i == 1])
print(f"Present: {present}")
print(f"Absent: {absent}")