"""
=============================================================
 Example 4: Topological Sort (Sắp xếp topo)
=============================================================

Order tasks so prerequisites come first.
Only works on DAGs (Directed Acyclic Graphs).

Demonstrates Kahn's BFS algorithm (LC 207, LC 210).

Time:  O(V + E)
Space: O(V + E)
"""
from collections import defaultdict, deque


def topo_sort_bfs(n, edges):
    """Kahn's Algorithm — BFS-based topological sort."""
    graph = defaultdict(list)
    indegree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque(i for i in range(n) if indegree[i] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return order if len(order) == n else []  # Empty = cycle!


def topo_sort_trace(n, edges):
    """Kahn's with trace."""
    graph = defaultdict(list)
    indegree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    print(f"  Indegree: {indegree}")
    queue = deque(i for i in range(n) if indegree[i] == 0)
    print(f"  Start: {list(queue)} (indegree=0)")
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        freed = []
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
                freed.append(nei)
        info = f" freed: {freed}" if freed else ""
        print(f"    Process {node}{info} → order={order}")

    return order if len(order) == n else []


def course_order(n, prerequisites):
    """Course Schedule II (LC 210)."""
    # prerequisites[i] = [a, b] means b → a
    edges = [(b, a) for a, b in prerequisites]
    return topo_sort_bfs(n, edges)


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Topological Sort — Trace")
    print("=" * 60)
    # 0 → 1 → 3
    # 0 → 2 → 3
    order = topo_sort_trace(4, [(0,1),(0,2),(1,3),(2,3)])
    assert len(order) == 4
    assert order.index(0) < order.index(1)
    assert order.index(0) < order.index(2)
    assert order.index(1) < order.index(3)
    print(f"\n  Valid order: {order} ✅")
    print()

    print("=" * 60)
    print("TEST 2: Cycle Detection via TopSort")
    print("=" * 60)
    # Has cycle: 0 → 1 → 2 → 0
    order = topo_sort_bfs(3, [(0,1),(1,2),(2,0)])
    assert order == []
    print("  0→1→2→0 (cycle) → [] ✅")

    order = topo_sort_bfs(3, [(0,1),(1,2)])
    assert order == [0, 1, 2]
    print("  0→1→2   (no cycle) → [0,1,2] ✅")
    print()

    print("=" * 60)
    print("TEST 3: Course Schedule II")
    print("=" * 60)
    # 4 courses, prerequisites
    order = course_order(4, [[1,0],[2,0],[3,1],[3,2]])
    print(f"  Course order: {order}")
    assert len(order) == 4
    assert order.index(0) < order.index(1)
    assert order.index(0) < order.index(2)
    print("  ✅ Valid order!")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Indegree 0 → no prerequisites → process first")
    print("   2. If order length < n → cycle exists")
    print("   3. Course Schedule = topological sort!")
