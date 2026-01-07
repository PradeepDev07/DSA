# Question: Find Duplicate Number
# Hint: Use set or Floyd’s cycle detection
# Time Complexity: O(n)
# Space Complexity: O(1) if Floyd's, O(n) if Set

def find_duplicate(nums):
    # Using Floyd's Tortoise and Hare
    if not nums:
        return -1
    tortoise = nums[0]
    hare = nums[0]
    
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
            
    ptr1 = nums[0]
    ptr2 = tortoise
    
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
        
    return ptr1

if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    print(f"Duplicate number: {find_duplicate(nums)}")
