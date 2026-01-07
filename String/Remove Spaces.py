# Question: Remove Spaces
# Hint: Replace or rebuild string
# Time Complexity: O(n)
# Space Complexity: O(n)

def remove_spaces(s):
    return s.replace(" ", "")

if __name__ == "__main__":
    s = "Hello World From Python"
    print(f"Removed spaces: {remove_spaces(s)}")
