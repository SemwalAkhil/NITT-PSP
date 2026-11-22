# 6. Write a program to solve the Tower of Hanoi puzzle using recursion.
# Input: (2), (3)
# Output:
#   Move disk 1 from A to B
#   Move disk 2 from A to C
#   Move disk 1 from B to C

def toh(n: int, source: str, aux: str, dest: str):
    if n == 1:
        print(f"Move disk 1 from {source} to {dest}")
        return
    toh(n - 1, source, dest, aux)
    print(f"Move disk {n} from {source} to {dest}")
    toh(n - 1, aux, source, dest)

if __name__ == "__main__":
    disks = int(input("Enter number of disks: "))
    toh(disks, 'A', 'B', 'C')
