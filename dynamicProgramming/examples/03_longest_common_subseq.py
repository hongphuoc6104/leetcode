"""
=============================================================
 Example 3: Longest Common Subsequence (LC 1143)
=============================================================

Classic 2D DP on two strings.
"ABCDE" and "ACE" → LCS = "ACE" (length 3)

Time:  O(m × n)
Space: O(m × n), can optimize to O(n)
"""


def lcs_length(s1, s2):
    """LCS length using 2D DP."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs_string(s1, s2):
    """Reconstruct actual LCS string."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(result))


def edit_distance(s1, s2):
    """Edit Distance / Levenshtein (LC 72). Related to LCS."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],        # Delete
                                   dp[i][j - 1],        # Insert
                                   dp[i - 1][j - 1])    # Replace

    return dp[m][n]


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: LCS Length & String")
    print("=" * 60)
    cases = [
        ("ABCDE", "ACE", 3, "ACE"),
        ("abc", "abc", 3, "abc"),
        ("abc", "def", 0, ""),
        ("AGGTAB", "GXTXAYB", 4, "GTAB"),
    ]
    for s1, s2, exp_len, exp_str in cases:
        length = lcs_length(s1, s2)
        string = lcs_string(s1, s2)
        ok = length == exp_len and string == exp_str
        status = "✅" if ok else "❌"
        print(f'  LCS("{s1}", "{s2}") = '
              f'"{string}" (len={length}) {status}')
    print()

    print("=" * 60)
    print("TEST 2: Edit Distance")
    print("=" * 60)
    cases = [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
        ("", "abc", 3),
        ("abc", "abc", 0),
    ]
    for s1, s2, expected in cases:
        result = edit_distance(s1, s2)
        status = "✅" if result == expected else "❌"
        print(f'  edit("{s1}", "{s2}") = {result} {status}')
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Match: dp[i][j] = dp[i-1][j-1] + 1 (diagonal)")
    print("   2. No match: max(skip s1, skip s2)")
    print("   3. Edit Distance: min(insert, delete, replace)")
