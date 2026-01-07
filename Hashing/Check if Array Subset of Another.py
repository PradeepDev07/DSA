# Question: Check if Array Subset of Another
# Hint: Convert one array to set
# Time Complexity: O(n+m)
# Space Complexity: O(n)

def is_subset(arr1, arr2):
    # Check if arr2 is subset of arr1
    set1 = set(arr1)
    for x in arr2:
        if x not in set1:
            return False
    return True

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 4]
    print(f"Is {arr2} subset of {arr1}? {is_subset(arr1, arr2)}")
