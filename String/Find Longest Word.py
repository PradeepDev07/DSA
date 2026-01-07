# Question: Find Longest Word
# Hint: Track max length
# Time Complexity: O(n)
# Space Complexity: O(1) (auxiliary)

def find_longest_word(s):
    words = s.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

if __name__ == "__main__":
    s = "I love programming in Python"
    print(f"Longest word: {find_longest_word(s)}")
