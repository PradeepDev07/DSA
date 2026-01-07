# Question: Longest Substring Without Repeating Characters
# Hint: Sliding window + set
# Time Complexity: O(n)
# Space Complexity: O(n)

def length_of_longest_substring(s):
    char_set = set()
    l = 0
    res = 0
    
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        res = max(res, r - l + 1)
    return res

if __name__ == "__main__":
    s = "abcabcbb"
    print(f"Length: {length_of_longest_substring(s)}")
