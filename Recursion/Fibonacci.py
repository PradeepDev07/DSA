# Question: Fibonacci
# Hint: Return fib(n-1)+fib(n-2)
# Time Complexity: O(2^n)
# Space Complexity: O(n)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    n = 6
    print(f"Fibonacci at {n} is {fibonacci(n)}")
