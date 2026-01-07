# Question: Rotate Array by 1
# Hint: Save last, shift rest
# Time Complexity: O(n)
# Space Complexity: O(1)

def rotate_by_one(arr):
    if not arr:
        return arr
    last = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(f"Rotated by 1: {rotate_by_one(arr)}")
