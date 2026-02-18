"""
=============================================================
 Example 2: DFS — Connected Components & Number of Islands
=============================================================

Time:  O(V + E) or O(R × C) for grid
Space: O(V) or O(R × C)
"""
from collections import defaultdict


def count_components(n, edges):
    """Count connected components using DFS."""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)

    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1

    return count


def num_islands(grid):
    """Number of Islands (LC 200) — Grid DFS."""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or grid[r][c] != '1'):
            return
        grid[r][c] = '0'  # Mark visited
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1

    return count


def max_island_area(grid):
    """Max Area of Island (LC 695)."""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    best = 0

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or grid[r][c] != 1):
            return 0
        grid[r][c] = 0
        area = 1
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            area += dfs(r + dr, c + dc)
        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                best = max(best, dfs(r, c))

    return best


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Connected Components")
    print("=" * 60)
    cases = [
        (5, [[0,1],[1,2],[3,4]], 2),
        (5, [[0,1],[1,2],[2,3],[3,4]], 1),
        (4, [], 4),
    ]
    for n, edges, expected in cases:
        result = count_components(n, edges)
        status = "✅" if result == expected else "❌"
        print(f"  n={n}, edges={edges} → {result} {status}")
    print()

    print("=" * 60)
    print("TEST 2: Number of Islands")
    print("=" * 60)
    grid1 = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    result = num_islands(grid1)
    assert result == 3
    print(f"  Grid 4×5 → {result} islands ✅")

    grid2 = [['1', '0'], ['0', '1']]
    result = num_islands(grid2)
    assert result == 2
    print(f"  Grid 2×2 → {result} islands ✅")
    print()

    print("=" * 60)
    print("TEST 3: Max Island Area")
    print("=" * 60)
    grid = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0],
    ]
    result = max_island_area(grid)
    assert result == 5
    print(f"  Max island area → {result} ✅")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Grid = implicit graph (4 neighbors)")
    print("   2. Mark visited IN-PLACE: grid[r][c] = '0'")
    print("   3. Components count = number of DFS calls")
