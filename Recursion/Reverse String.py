# Question: Reverse String
# Hint: First char to end
# Time Complexity: O(n)
# Space Complexity: O(n)

def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    return reverse_string_recursive(s[1:]) + s[0]

if __name__ == "__main__":
    s = "recursion"
    print(f"Reversed: {reverse_string_recursive(s)}")
