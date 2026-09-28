# anusenthil@gmail.com
import re
email = input("Email id: ")
match = re.search(r"(\w+)@(\w+\.\w+)", email)
print("Username: ", match.group(1))
print("Domain   : ", match.group(2))
