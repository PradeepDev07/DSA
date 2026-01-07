# Question: Find Missing Number
# Hint: Sum formula or XOR
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_missing_number(arr, n):
    # Sum of first n natural numbers
    total = n * (n + 1) // 2
    return total - sum(arr)

if __name__ == "__main__":
    arr = [1, 2, 4, 5, 6]
    n = 6
    print(f"Missing number: {find_missing_number(arr, n)}")
