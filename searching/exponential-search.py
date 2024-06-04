def binary_search_in_range(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2
    return binary_search_in_range(arr, index // 2, min(index, len(arr) - 1), target)

# Example usage
arr = [1, 2, 4, 6, 9, 13, 18, 21, 25, 28, 33, 37, 41, 45, 50]
target = 25
result = exponential_search(arr, target)
print("Element found at index:", result)
