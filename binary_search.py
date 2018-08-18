from math import floor


def search(numbers, start, end, value):
    mid = floor((start + end) / 2)
    if len(numbers) > 0:
        if numbers[mid] == value:
            return mid
        elif numbers[mid] > value:
            return search(numbers, start, mid - 1, value)
        elif numbers[mid] < value:
            return search(numbers, mid + 1, end, value)
        else:
            return -1
    else:
        return "Array has length less than 1"


arr = [1, 5, 4, 3, 4, 5, 5, 6, 2, 4]
# arr1 = [1, 5, 4, 10, 39, 2, 6, 8, 3]
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = set(arr)

arr1.sort()
print(arr1)

arr = sorted(arr)
print(arr)

# num = input("Enter number to be searched: ")

index = search(arr1, 0, len(arr1) - 1, 3)
print("Index:", index if index != -1 else "Item not found")

index = search(arr, 0, len(arr) - 1, 3)
print("Index:", index if index != -1 else "Item not found")

index = search([], 0, len([]) - 1, 3)
print("Index:", index if index != -1 else "Item not found")
