# Question: Find the Sum of Array Elements
# Hint: Accumulate using loop
# Time Complexity: O(n)
# Space Complexity: O(1)

def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(f"Sum of {arr} is {array_sum(arr)}")
