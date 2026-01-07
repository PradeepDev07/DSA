# Question: Linear Search
# Hint: Traverse and compare
# Time Complexity: O(n)
# Space Complexity: O(1)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    target = 30
    print(f"Element {target} found at index {linear_search(arr, target)}")
