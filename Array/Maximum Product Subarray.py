# Question: Maximum Product Subarray
# Hint: Track max & min product
# Time Complexity: O(n)
# Space Complexity: O(1)

def max_product(nums):
    res = max(nums)
    cur_min, cur_max = 1, 1
    
    for n in nums:
        if n == 0:
            cur_min, cur_max = 1, 1
            continue
        tmp = cur_max * n
        cur_max = max(n * cur_max, n * cur_min, n)
        cur_min = min(tmp, n * cur_min, n)
        res = max(res, cur_max)
        
    return res

if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print(f"Max product: {max_product(nums)}")
