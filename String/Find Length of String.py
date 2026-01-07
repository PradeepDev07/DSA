# Question: Find Length of String
# Hint: Counter variable
# Time Complexity: O(n)
# Space Complexity: O(1)

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

if __name__ == "__main__":
    s = "hello"
    print(f"Length of '{s}' is {string_length(s)}")
