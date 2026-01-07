# Question: Convert to Uppercase Lowercase
# Hint: ASCII or built-in
# Time Complexity: O(n)
# Space Complexity: O(n)

def to_upper_lower(s):
    return s.upper(), s.lower()

if __name__ == "__main__":
    s = "Hello"
    upper, lower = to_upper_lower(s)
    print(f"Upper: {upper}, Lower: {lower}")
