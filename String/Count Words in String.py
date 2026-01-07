# Question: Count Words in String
# Hint: Split by space
# Time Complexity: O(n)
# Space Complexity: O(n)

def count_words(s):
    words = s.split()
    return len(words)

if __name__ == "__main__":
    s = "This is a sample string"
    print(f"Word count: {count_words(s)}")
