# Question: Check if an Array is Sorted
# Hint: Compare arr[i] and arr[i+1]
# Time Complexity: O(n)
# Space Complexity: O(1)

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 3, 2, 4, 5]
    print(f"Is {arr1} sorted? {is_sorted(arr1)}")
    print(f"Is {arr2} sorted? {is_sorted(arr2)}")
