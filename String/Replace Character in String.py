# Question: Replace Character in String
# Hint: Loop and rebuild
# Time Complexity: O(n)
# Space Complexity: O(n)

def replace_char(s, old, new):
    return s.replace(old, new)

if __name__ == "__main__":
    s = "apple"
    print(f"Replaced p with b: {replace_char(s, 'p', 'b')}")
