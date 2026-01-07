# Question: Count Pairs with Given Sum
# Hint: HashMap for complements
# Time Complexity: O(n)
# Space Complexity: O(n)

def count_pairs_with_sum(arr, k):
    count = 0
    freq = {}
    for x in arr:
        target = k - x
        count += freq.get(target, 0)
        freq[x] = freq.get(x, 0) + 1
    return count

if __name__ == "__main__":
    arr = [1, 5, 7, 1]
    k = 6
    print(f"Pairs with sum {k}: {count_pairs_with_sum(arr, k)}")
