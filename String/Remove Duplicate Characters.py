# Question: Remove Duplicate Characters
# Hint: Set to track seen
# Time Complexity: O(n)
# Space Complexity: O(n)

def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)

if __name__ == "__main__":
    s = "banana"
    print(f"Unique chars: {remove_duplicates(s)}")
