# 13. Write a program to identify the gas contained in a cylinder given its color code.
# Input: (red), (white)
# Output: Hydrogen, Oxygen

print("""Valid colors:
Red
Yellow
White
Black
Brown
Grey""")

cylinder_color = input("Enter cylinder color: ").lower()
if cylinder_color == "red":
    print("Hydrogen")
elif cylinder_color == "yellow":
    print("Chlorine")
elif cylinder_color == "white":
    print("Oxygen")
else:
    print("Invalid color")