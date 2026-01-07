# Question: Remove Duplicates from Sorted Array
# Hint: Slow-fast pointer technique
# Time Complexity: O(n)
# Space Complexity: O(1)

def remove_duplicates(arr):
    if not arr:
        return 0
    
    j = 0 
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
            
    return j + 1

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 4, 4]
    new_len = remove_duplicates(arr)
    print(f"Array after removing duplicates: {arr[:new_len]}")
