# Question: First Repeating Element
# Hint: Track seen elements
# Time Complexity: O(n)
# Space Complexity: O(n)

def first_repeating(arr):
    seen = {}
    # First pass to store frequency/first index
    for i, x in enumerate(arr):
        if x not in seen:
            seen[x] = 0
        seen[x] += 1
        
    for x in arr:
        if seen[x] > 1:
            return x
    return -1

if __name__ == "__main__":
    arr = [10, 5, 3, 4, 3, 5, 6]
    print(f"First repeating: {first_repeating(arr)}")
