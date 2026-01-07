# Question: Sum of Digits
# Hint: Last digit + recursive call
# Time Complexity: O(n)
# Space Complexity: O(n)

def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

if __name__ == "__main__":
    n = 1234
    print(f"Sum of digits of {n} is {sum_of_digits(n)}")
