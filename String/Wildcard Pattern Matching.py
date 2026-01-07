# Question: Wildcard Pattern Matching
# Hint: DP with state transitions
# Time Complexity: O(n·m)
# Space Complexity: O(n·m)

def is_match_wildcard(s, p):
    import  fnmatch
    # Actually can use DP but fnmatch is built-in for wildcard
    # However, strict DP implementation:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    
    for j in range(1, len(p) + 1):
        if p[j-1] == '*':
            dp[0][j] = True
        else:
            break
            
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif p[j-1] == '?' or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
                
    return dp[len(s)][len(p)]

if __name__ == "__main__":
    s = "adceb"
    p = "*a*b"
    print(f"Match '{s}' with '{p}': {is_match_wildcard(s, p)}")
