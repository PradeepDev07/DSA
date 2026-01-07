# Question: Check Anagram
# Hint: Sort or frequency count
# Time Complexity: O(n)
# Space Complexity: O(1)

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    s1 = "listen"
    s2 = "silent"
    print(f"Are '{s1}' and '{s2}' anagrams? {is_anagram(s1, s2)}")
