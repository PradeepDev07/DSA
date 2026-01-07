def find_second_largest(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two distinct elements.")
    
    first = second = float('-inf')
    
    for number in arr:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    
    if second == float('-inf'):
        raise ValueError("Array must contain at least two distinct elements.")
    
    return second





if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    unique_arr = list(set(arr))


                 