# Question: Group Anagrams
# Hint: Sorted string as key
# Time Complexity: O(n·k log k)
# Space Complexity: O(n)

def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        key = tuple(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    return list(anagrams.values())

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(f"Grouped: {group_anagrams(strs)}")
