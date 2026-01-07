# Question: Count Character Frequency
# Hint: Dictionary
# Time Complexity: O(n)
# Space Complexity: O(n)

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

if __name__ == "__main__":
    s = "hello"
    print(f"Frequency: {char_frequency(s)}")
