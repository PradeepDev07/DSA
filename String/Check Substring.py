# Question: Check Substring
# Hint: Sliding window or in-built
# Time Complexity: O(n)
# Space Complexity: O(1)

def is_substring(main, sub):
    return sub in main

if __name__ == "__main__":
    main = "Hello World"
    sub = "World"
    print(f"Is '{sub}' a substring of '{main}'? {is_substring(main, sub)}")
