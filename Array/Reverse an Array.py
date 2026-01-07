# Question: Reverse an Array
# Hint: Two pointers (start & end)
# Time Complexity: O(n)
# Space Complexity: O(1)

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(f"Reversed: {reverse_array(arr)}")
