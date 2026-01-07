
def sum_of_array_values(arr):
    total = 0
    for val in arr:
        total += val
    return total



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    total = sum_of_array_values(arr)
    print("The sum of the array elements is:", total)