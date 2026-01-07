# Question: Reverse a String
# Hint: Use slicing or loop
# Time Complexity: O(n)
# Space Complexity: O(n)

def reverse_string(s):
    # Pythonic slicing
    return s[::-1]

if __name__ == "__main__":
    s = "hello"
    print(f"Reversed '{s}': {reverse_string(s)}")
