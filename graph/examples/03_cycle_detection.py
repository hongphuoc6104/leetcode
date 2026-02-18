"""
=============================================================
 Example 3: Cycle Detection in Graphs
=============================================================

Directed graph: use DFS with 3 colors (white/gray/black)
Undirected graph: track parent

Time:  O(V + E)
Space: O(V)
"""
from collections import defaultdict


def has_cycle_directed(n, edges):
    """Detect cycle in directed graph using 3-color DFS."""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY
        for nei in graph[node]:
            if color[nei] == GRAY:
                return True  # Back edge → cycle!
            if color[nei] == WHITE and dfs(nei):
                return True
        color[node] = BLACK
        return False

    for i in range(n):
        if color[i] == WHITE:
            if dfs(i):
                return True
    return False


def has_cycle_undirected(n, edges):
    """Detect cycle in undirected graph tracking parent."""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei, node):
                    return True
            elif nei != parent:
                return True  # Visited and not parent → cycle!
        return False

    for i in range(n):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Directed Graph — Cycle Detection")
    print("=" * 60)
    # 0 → 1 → 2 → 0 (cycle)
    assert has_cycle_directed(3, [(0,1),(1,2),(2,0)]) is True
    print("  0→1→2→0 → cycle=True ✅")

    # 0 → 1 → 2 (no cycle)
    assert has_cycle_directed(3, [(0,1),(1,2)]) is False
    print("  0→1→2   → cycle=False ✅")

    # Self-loop
    assert has_cycle_directed(2, [(0,0)]) is True
    print("  0→0     → cycle=True ✅")
    print()

    print("=" * 60)
    print("TEST 2: Undirected Graph — Cycle Detection")
    print("=" * 60)
    # Triangle: 0-1-2-0
    assert has_cycle_undirected(3, [(0,1),(1,2),(2,0)]) is True
    print("  0-1-2-0 → cycle=True ✅")

    # Line: 0-1-2
    assert has_cycle_undirected(3, [(0,1),(1,2)]) is False
    print("  0-1-2   → cycle=False ✅")

    # 4 nodes, 1 cycle
    assert has_cycle_undirected(4, [(0,1),(1,2),(2,3),(3,1)]) is True
    print("  0-1-2-3-1 → cycle=True ✅")
    print()

    print("=" * 60)
    print("TEST 3: Course Schedule (LC 207)")
    print("=" * 60)
    def can_finish(n, prerequisites):
        return not has_cycle_directed(n, prerequisites)

    cases = [
        (2, [(1,0)], True),
        (2, [(1,0),(0,1)], False),
        (4, [(1,0),(2,1),(3,2)], True),
    ]
    for n, prereq, expected in cases:
        result = can_finish(n, prereq)
        status = "✅" if result == expected else "❌"
        print(f"  n={n}, prereqs={prereq} → {result} {status}")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Directed: 3 colors. GRAY→GRAY = cycle")
    print("   2. Undirected: track parent. visited ≠ parent = cycle")
    print("   3. Course Schedule = cycle detection in DAG!")
