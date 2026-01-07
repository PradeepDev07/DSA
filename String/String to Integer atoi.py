# Question: String to Integer (atoi)
# Hint: Handle sign & overflow
# Time Complexity: O(n)
# Space Complexity: O(1)

def my_atoi(s):
    s = s.strip()
    if not s:
        return 0
        
    sign = 1
    i = 0
    if s[i] == '-':
        sign = -1
        i += 1
    elif s[i] == '+':
        i += 1
        
    res = 0
    while i < len(s) and s[i].isdigit():
        res = res * 10 + int(s[i])
        i += 1
        
    res *= sign
    # Clamp to 32-bit int
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    return max(min(res, INT_MAX), INT_MIN)

if __name__ == "__main__":
    s = "   -42 with words"
    print(f"Atoi: {my_atoi(s)}")
