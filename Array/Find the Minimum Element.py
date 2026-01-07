# Question: Find the Minimum Element
# Hint: Compare each element
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_min(arr):
    if not arr:
        return None
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == "__main__":
    arr = [5, 3, 8, 1, 9]
    print(f"Min in {arr} is {find_min(arr)}")
