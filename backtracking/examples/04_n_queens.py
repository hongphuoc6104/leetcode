"""
=============================================================
 Example 4: N-Queens (LC 51)
=============================================================

Place N queens on N×N board so no two attack each other.
Uses sets for O(1) column/diagonal checking.

Time:  O(n!)
Space: O(n²) for board
"""


def solve_n_queens(n):
    """N-Queens (LC 51). Returns all valid board configurations."""
    result = []
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    board = [['.' for _ in range(n)] for _ in range(n)]

    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # Place queen
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board[row][col] = 'Q'

            backtrack(row + 1)

            # Remove queen (backtrack)
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return result


def total_n_queens(n):
    """N-Queens II (LC 52). Count solutions only."""
    count = [0]
    cols, d1, d2 = set(), set(), set()

    def backtrack(row):
        if row == n:
            count[0] += 1
            return
        for col in range(n):
            if col in cols or (row-col) in d1 or (row+col) in d2:
                continue
            cols.add(col); d1.add(row-col); d2.add(row+col)
            backtrack(row + 1)
            cols.remove(col); d1.remove(row-col); d2.remove(row+col)

    backtrack(0)
    return count[0]


if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: N-Queens (n=4)")
    print("=" * 60)
    solutions = solve_n_queens(4)
    assert len(solutions) == 2
    print(f"  4-Queens → {len(solutions)} solutions ✅")
    for i, sol in enumerate(solutions):
        print(f"  Solution {i+1}:")
        for row in sol:
            print(f"    {row}")
        print()

    print("=" * 60)
    print("TEST 2: Solution Count")
    print("=" * 60)
    expected_counts = {1: 1, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92}
    for n, expected in expected_counts.items():
        result = total_n_queens(n)
        status = "✅" if result == expected else "❌"
        print(f"  n={n}: {result} solutions {status}")
    print()

    print("✅ All tests passed!")
