# 10. Write a decorator to authenticate username and password before allowing function execution.
# Input: (admin 1234 5 10), (admin 0000 5 10)
# Output: 15, Access Denied

db = {"admin": "1234", "rahul": "pass"}

def auth(func):
    def wrapper(user, pwd, *args):
        if db.get(user) == pwd:
            return func(*args)
        return "Access Denied"
    return wrapper

@auth
def add(a, b):
    return a + b

user = input("Enter username: ")
pwd = input("Enter password: ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(add(user, pwd, a, b))
