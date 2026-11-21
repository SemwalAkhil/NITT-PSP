# AP/GP/HP
a = int(input("Enter first term: "))
d = int(input("Enter first common difference/ratio: "))
num = int(input("Enter number of terms: "))
print("AP: ",[a + (n-1)*d for n in range(1,num+1)])
print("GP: ",[a * d ** (n-1) for n in range(1,num+1)])
print("HP: ",[f"1/{a + (n-1)*d}" for n in range(1,num+1)])
