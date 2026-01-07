# Question: Check if Array is Palindrome
# Hint: Compare from both ends
# Time Complexity: O(n)
# Space Complexity: O(1)

def is_palindrome(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        if arr[start] != arr[end]:
            return False
        start += 1
        end -= 1
    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 2, 1]
    print(f"Is palindrome? {is_palindrome(arr)}")
