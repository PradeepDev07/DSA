

def check_even_odd(arr):
    even_count = 0
    odd_count = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count



if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    even_count, odd_count = check_even_odd(arr)
    print("Count of even numbers:", even_count)
    print("Count of odd numbers:", odd_count)