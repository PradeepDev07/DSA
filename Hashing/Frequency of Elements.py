# Question: Frequency of Elements
# Hint: Dictionary counter
# Time Complexity: O(n)
# Space Complexity: O(n)

def frequency_elements(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq

if __name__ == "__main__":
    arr = [1, 1, 2, 3, 3, 3]
    print(f"Frequency: {frequency_elements(arr)}")
