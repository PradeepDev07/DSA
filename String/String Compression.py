# Question: String Compression
# Hint: Two pointers
# Time Complexity: O(n)
# Space Complexity: O(n)

def compress(chars):
    anchor = 0
    write = 0
    for read, c in enumerate(chars):
        if read + 1 == len(chars) or chars[read + 1] != c:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
            anchor = read + 1
    return write

if __name__ == "__main__":
    chars = ["a","a","b","b","c","c","c"]
    new_len = compress(chars)
    print(f"Compressed: {chars[:new_len]}")
