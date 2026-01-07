# Question: Count Occurrences of an Element
# Hint: Counter variable
# Time Complexity: O(n)
# Space Complexity: O(1)

def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4]
    target = 2
    print(f"Occurrences of {target}: {count_occurrences(arr, target)}")
