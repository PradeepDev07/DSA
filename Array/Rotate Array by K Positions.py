# Question: Rotate Array by K Positions
# Hint: Reverse parts of array
# Time Complexity: O(n)
# Space Complexity: O(1)

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, k):
    n = len(arr)
    k %= n
    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"Rotated by {k}: {rotate_array(arr, k)}")
