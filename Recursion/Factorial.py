# Question: Factorial
# Hint: Base case n==0
# Time Complexity: O(n)
# Space Complexity: O(n)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    n = 5
    print(f"Factorial of {n} is {factorial(n)}")
