# Question: Subarray Sum Equals K
# Hint: Prefix sum + HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)

def subarray_sum(nums, k):
    res = 0
    cur_sum = 0
    prefix_sums = {0: 1}
    
    for n in nums:
        cur_sum += n
        diff = cur_sum - k
        res += prefix_sums.get(diff, 0)
        prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
        
    return res

if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(f"Count of subarrays: {subarray_sum(nums, k)}")
