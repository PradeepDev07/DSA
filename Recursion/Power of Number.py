# Question: Power of Number
# Hint: n * power(n-1)
# Time Complexity: O(n)
# Space Complexity: O(n)

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

if __name__ == "__main__":
    b, e = 2, 3
    print(f"{b}^{e} is {power(b, e)}")
