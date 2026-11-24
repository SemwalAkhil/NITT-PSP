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


print(add("admin", "1234", 5, 10)) 
print(add("admin", "0000", 5, 10))  