# Question: Count Vowels and Consonants
# Hint: Check character sets
# Time Complexity: O(n)
# Space Complexity: O(1)

def count_vowels_consonants(s):
    vowels = set("aeiouAEIOU")
    v_count = 0
    c_count = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

if __name__ == "__main__":
    s = "Hello World"
    v, c = count_vowels_consonants(s)
    print(f"'{s}' has {v} vowels and {c} consonants")
