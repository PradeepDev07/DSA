# Question: Check Rotation of String
# Hint: s2 in (s1+s1)
# Time Complexity: O(n)
# Space Complexity: O(n)

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(f"Is rotation? {is_rotation(s1, s2)}")
