# Question: Find First Non-Repeating Character
# Hint: Frequency dictionary
# Time Complexity: O(n)
# Space Complexity: O(n)

def first_non_repeating(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        
    for char in s:
        if counts[char] == 1:
            return char
    return None

if __name__ == "__main__":
    s = "swiss"
    print(f"First non-repeating in '{s}' is {first_non_repeating(s)}")
