# Question: Two Sum
# Hint: HashMap to store visited elements
# Time Complexity: O(n)
# Space Complexity: O(n)

def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Two sum indices: {two_sum(nums, target)}")
