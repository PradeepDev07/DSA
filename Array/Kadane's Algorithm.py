# Question: Kadane's Algorithm (Max Subarray Sum)
# Hint: Dynamic running sum
# Time Complexity: O(n)
# Space Complexity: O(1)

def max_subarray_sum(arr):
    max_so_far = float('-inf')
    max_ending_here = 0
    
    for x in arr:
        max_ending_here += x
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Max subarray sum: {max_subarray_sum(arr)}")
