import functools as f
shares = [1000,1100,1040,1913,2000,1445]
print(f"Highest: {f.reduce(lambda x,y: x if x > y else y,shares)}")