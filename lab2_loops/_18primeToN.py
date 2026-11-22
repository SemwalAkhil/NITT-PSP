# 18. Write a program to find the Nth prime number using loops.
# Input: (5), (1)
# Output: 5 prime is : 11, 1 prime is : 2

primes = [2]
num: int = int(input("Enter N: "))
i = 3
while len(primes) != num:
    for j in primes:
        # print(f"Check {i} % {j}")
        if (i % j) == 0:
            break
    else:
        primes.append(i)
        # print(primes)
    i += 1
print(f"{num} prime is : {primes[-1]}")
