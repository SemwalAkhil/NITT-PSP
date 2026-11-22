# 14. Write a program to calculate the electricity bill based on usage and consumer category.
# Input: (100 residential), (200 commercial)
# Output: Amount to pay: Rs.  600.0, Amount to pay: Rs.  2000.0

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
