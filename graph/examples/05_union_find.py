"""
=============================================================
 Example 5: Union-Find (Disjoint Set Union)
=============================================================

Efficiently tracks connected components.
Near O(1) per operation with path compression + union by rank.

Time:  O(α(n)) ≈ O(1) amortized per operation
Space: O(n)
"""


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        """Find root with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union by rank. Returns True if merged."""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)


def count_components_uf(n, edges):
    """Count connected components using Union-Find."""
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.components


def has_redundant_edge(edges):
    """Find redundant connection (LC 684)."""
    n = len(edges)
    uf = UnionFind(n + 1)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]  # Already connected → redundant!
    return []


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Union-Find Basics")
    print("=" * 60)
    uf = UnionFind(5)
    print(f"  Initial: {uf.components} components")

    uf.union(0, 1)
    print(f"  union(0,1): {uf.components} components")
    uf.union(2, 3)
    print(f"  union(2,3): {uf.components} components")
    uf.union(1, 3)
    print(f"  union(1,3): {uf.components} components")

    assert uf.connected(0, 3) is True
    assert uf.connected(0, 4) is False
    assert uf.components == 2
    print(f"  0↔3: True, 0↔4: False ✅")
    print()

    print("=" * 60)
    print("TEST 2: Count Components")
    print("=" * 60)
    cases = [
        (5, [(0,1),(1,2),(3,4)], 2),
        (5, [(0,1),(1,2),(2,3),(3,4)], 1),
        (4, [], 4),
    ]
    for n, edges, expected in cases:
        result = count_components_uf(n, edges)
        status = "✅" if result == expected else "❌"
        print(f"  n={n}, edges={edges} → {result} {status}")
    print()

    print("=" * 60)
    print("TEST 3: Redundant Connection (LC 684)")
    print("=" * 60)
    cases = [
        ([[1,2],[1,3],[2,3]], [2,3]),
        ([[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4]),
    ]
    for edges, expected in cases:
        result = has_redundant_edge(edges)
        status = "✅" if result == expected else "❌"
        print(f"  {edges} → redundant={result} {status}")
    print()

    print("=" * 60)
    print("TEST 4: Performance — 100K unions")
    print("=" * 60)
    import time
    n = 100000
    uf = UnionFind(n)
    start = time.perf_counter()
    for i in range(n - 1):
        uf.union(i, i + 1)
    t = time.perf_counter() - start
    assert uf.components == 1
    print(f"  {n} unions: {t*1000:.2f}ms ✅")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Path compression: parent → root directly")
    print("   2. Union by rank: keep tree balanced")
    print("   3. Redundant edge: union returns False → already connected")
