


def is_sorted(arr):
        length = len(arr)
        for i in range(length - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 5]
    print("Array:", arr)
    if is_sorted(arr):
        print("The array is sorted.")
    else:
        print("The array is not sorted.")
