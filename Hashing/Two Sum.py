# Question: Two Sum
# Hint: HashMap lookup
# Time Complexity: O(n)
# Space Complexity: O(n)

def two_sum_hash(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    t = 9
    print(f"Indices: {two_sum_hash(arr, t)}")
