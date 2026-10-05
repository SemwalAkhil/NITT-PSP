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