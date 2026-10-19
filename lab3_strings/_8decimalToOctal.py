in_value = input("Enter a decimal number: ").split(".")
integer = in_value[0]
if len(in_value) == 2:
    fractional = in_value[1]
else:
    fractional = "0"
integer = int(integer)
fractional = float("." + fractional)
octa = ""

while (integer != 0):
    octa = str(integer % 8) + octa
    integer = integer // 8

limit = 0
octa += "."

while fractional != 0 and limit < 10:
    fractional = fractional * 8
    octa += str(int(fractional))
    fractional = fractional - int(fractional)
    limit += 1

print(f"Octal value is: {octa}")