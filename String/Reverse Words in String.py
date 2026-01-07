# Question: Reverse Words in String
# Hint: Split → reverse → join
# Time Complexity: O(n)
# Space Complexity: O(n)

def reverse_words(s):
    words = s.split()
    return " ".join(words[::-1])

if __name__ == "__main__":
    s = "the sky is blue"
    print(f"Reversed words: {reverse_words(s)}")
