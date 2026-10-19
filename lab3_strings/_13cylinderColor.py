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