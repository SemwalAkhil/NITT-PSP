# 7. Write a program to search for a target value in a sorted list using recursive binary search.
# Input: ("10 20 30 40 50 60 70" 40), ("10 20 30" 99)
# Output: Found at index:  3, Not found

def binarySearch(arr: list, low: int, high: int, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, low, mid - 1, target)
    else:
        return binarySearch(arr, mid + 1, high, target)

if __name__ == "__main__":
    nums = [int(x) for x in input("Enter sorted elements: ").split()]
    target = int(input("Enter element to search: "))
    idx = binarySearch(nums, 0, len(nums) - 1, target)
    if idx != -1:
        print("Found at index: ", idx)
    else:
        print("Not found")
