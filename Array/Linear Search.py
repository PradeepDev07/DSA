def search_element(arr, target):
    length = len(arr)
    for i in range(length):
        if arr[i] == target:
            return f"Element found at index {i}"
    return "Element not found in the array"



if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter the target number to search for: "))

    print ("searching for", target, "in", arr)
    print("result" , search_element(arr, target))
    