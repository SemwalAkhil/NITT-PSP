# 6. Write a program to solve Tower of Hanoi for N disks using recursion.
# Input: (2), (3)
# Output:
#   Run 1:
#   Move disk 1 from A to B
#   Move disk 2 from A to C
#   Move disk 1 from B to C
#   Run 2:
#   Move disk 1 from A to C
#   Move disk 2 from A to B
#   Move disk 1 from C to B
#   Move disk 3 from A to C
#   Move disk 1 from B to A
#   Move disk 2 from B to C
#   Move disk 1 from A to C

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
