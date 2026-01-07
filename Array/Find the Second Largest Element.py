# Question: Find the Second Largest Element
# Hint: Track largest & second largest
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_second_largest(arr):
    if len(arr) < 2:
        return None
    
    largest = float('-inf')
    second = float('-inf')
    
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
            
    return second if second != float('-inf') else None

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(f"Second largest in {arr} is {find_second_largest(arr)}")
