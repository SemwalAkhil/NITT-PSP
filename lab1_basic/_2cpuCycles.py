# 2. Write a program to calculate CPU clock cycles for a given frequency and units.
# Input: (M 2.5), (G 1.2)
# Output: 2500000 cycles, 1200000000 cycles

"""
Read frequency, units
frequency <- frequency.first_char.lower_char
If frequency = "m" do
    Print(units * 1,000,000 cycles)
If frequency = "g" do
    Print(units * 1,000,000,000 cycles)
"""
frequency:str = input("Enter frequency unit (Mhz|Ghz): ")[:1].lower()
units:float = float(input("Enter number of units: "))
if frequency == "m":
    print(f"{int(units * 1_000_000)} cycles")
if frequency == "g":
    print(f"{int(units * 1_000_000_000)} cycles")