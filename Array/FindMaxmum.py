# Question: Find the Maximum Element
# Hint: Traverse once, keep max
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == "__main__":
    arr = [1, 42, 3, 10, 5]
    print(f"Max in {arr} is {find_max(arr)}")
