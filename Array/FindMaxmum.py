def find_minimum_value(arr):
    min_val = arr[0]
    length = len(arr)
    for val in range(1,length):
        if min_val > arr[val]:
            min_val = arr[val]
    if length>0:
        return min_val
    else:
        raise ValueError("Array is empty")

def find_maxmum_value(arr):
    max_val = arr[0]
    length = len(arr)
    for val in range(1,length):
        if max_val < arr[val]:
            max_val = arr[val]
    if length>0:
        return max_val
    else:
        raise ValueError("Array is empty")


    




def main():
    arr = list(map(int,input("Enter the number in order with space separating :").split(" ")))
    print(arr)
    print(find_maxmum_value(arr))
    print(find_minimum_value(arr))

    


















if __name__ == "__main__":
    main()



