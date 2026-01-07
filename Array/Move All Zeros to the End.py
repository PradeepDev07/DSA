# Question: Move All Zeros to the End
# Hint: Two-pointer or overwrite non-zero
# Time Complexity: O(n)
# Space Complexity: O(1)

def move_zeros(arr):
    count = 0  # Count of non-zero elements
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
            
    while count < len(arr):
        arr[count] = 0
        count += 1
    
    return arr

if __name__ == "__main__":
    arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    print(f"Moved Zeros: {move_zeros(arr)}")
