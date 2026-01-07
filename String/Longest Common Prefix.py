# Question: Longest Common Prefix
# Hint: Compare characters column-wise
# Time Complexity: O(n·m)
# Space Complexity: O(1)

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(f"Longest common prefix: {longest_common_prefix(strs)}")
