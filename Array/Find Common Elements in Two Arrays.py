# Question: Find Common Elements in Two Arrays
# Hint: Nested loop or set
# Time Complexity: O(n+m)
# Space Complexity: O(n)

def find_common(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1.intersection(set2))

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]
    print(f"Common elements: {find_common(arr1, arr2)}")
