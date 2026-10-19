usage = float(input("Enter usage (KWh): "))
print('''Valid category's
Residential
Commercial
Industrial''')

user_type =  input("Enter usage category: ").lower()

if user_type == "residential":
    print("Amount to pay: Rs. ", usage * 6)
elif user_type == "commercial":
    print("Amount to pay: Rs. ", usage * 10)
elif user_type == "industrial":
    print("Amount to pay: Rs. ", usage * 8)
else:
    print("Invalid category")
