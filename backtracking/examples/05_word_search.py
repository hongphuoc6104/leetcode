"""
=============================================================
 Example 5: Word Search (LC 79)
=============================================================

Find if a word exists in grid by moving up/down/left/right.
Each cell used at most once per path.

Time:  O(m × n × 4^L) where L = word length
Space: O(L) recursion depth
"""


def word_search(board, word):
    """Word Search (LC 79)."""
    if not board:
        return False
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, idx):
        if idx == len(word):
            return True
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or board[r][c] != word[idx]):
            return False

        # Save and mark visited
        temp = board[r][c]
        board[r][c] = '#'

        # Explore 4 directions
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if backtrack(r + dr, c + dc, idx + 1):
                board[r][c] = temp  # Restore before returning!
                return True

        # Backtrack: unmark
        board[r][c] = temp
        return False

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False


if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Word Search — Found")
    print("=" * 60)
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    cases = [
        ("ABCCED", True),
        ("SEE", True),
        ("ABCB", False),
    ]
    for word, expected in cases:
        # Make a fresh copy for each test
        b = [row[:] for row in board]
        result = word_search(b, word)
        status = "✅" if result == expected else "❌"
        print(f'  "{word}" → {result} {status}')
    print()

    print("=" * 60)
    print("TEST 2: Edge Cases")
    print("=" * 60)
    assert word_search([['A']], 'A') == True
    print('  [["A"]] + "A" → True ✅')
    assert word_search([['A']], 'B') == False
    print('  [["A"]] + "B" → False ✅')
    assert word_search([['A', 'B'], ['C', 'D']], 'ABDC') == True
    print('  2x2 "ABDC" → True ✅')
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Mark cell '#', explore 4 dirs, restore cell")
    print("   2. No visited set needed — modify board in-place")
    print("   3. Pruning: check bounds + char match BEFORE recursing")
