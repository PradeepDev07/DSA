



def reverse_an_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    reversed_arr =  reverse_an_array(arr)
    print("Original array:", arr)
    print("Reversed array:", reversed_arr)



#buildin reversed function can also be used to reverse an array
#example: arr[::-1]
#time complexity: O(n)
#space complexity: O(n)


#operation: Reversing an array in place
#time complexity: O(n)
#space complexity: O(1)

