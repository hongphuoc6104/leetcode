"""
=============================================================
 Example 1: BFS Shortest Path (Đường ngắn nhất BFS)
=============================================================

BFS guarantees shortest path in UNWEIGHTED graphs.
(BFS đảm bảo đường ngắn nhất trong đồ thị KHÔNG trọng số.)

Time:  O(V + E)
Space: O(V)
"""
from collections import defaultdict, deque


def bfs_shortest_path(graph, start, end):
    """Find shortest path using BFS."""
    if start == end:
        return [start]
    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        for nei in graph[node]:
            if nei == end:
                return path + [nei]
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, path + [nei]))

    return []  # No path


def bfs_all_distances(graph, start):
    """Find distance from start to all reachable nodes."""
    dist = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in dist:
                dist[nei] = dist[node] + 1
                queue.append(nei)

    return dist


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    # Build graph:
    #   0 -- 1 -- 3
    #   |    |
    #   2 -- 4 -- 5
    graph = defaultdict(list)
    edges = [(0,1), (0,2), (1,3), (1,4), (2,4), (4,5)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    print("=" * 60)
    print("TEST 1: BFS Shortest Path")
    print("=" * 60)
    path = bfs_shortest_path(graph, 0, 5)
    print(f"  0 → 5: {' → '.join(map(str, path))} "
          f"(length {len(path)-1})")
    assert len(path) - 1 == 3  # 0→1→4→5 or 0→2→4→5
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 2: All Distances from Source")
    print("=" * 60)
    dist = bfs_all_distances(graph, 0)
    for node in sorted(dist):
        print(f"  dist(0, {node}) = {dist[node]}")
    assert dist == {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3}
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 3: No Path")
    print("=" * 60)
    graph2 = defaultdict(list)
    graph2[0].append(1)
    graph2[1].append(0)
    # Node 2 is isolated
    path = bfs_shortest_path(graph2, 0, 2)
    assert path == []
    print("  0 → 2 (isolated): No path ✅")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. BFS guarantees shortest path (unweighted)")
    print("   2. Mark visited when ENQUEUING, not DEQUEUING")
    print("   3. Store path in queue tuple for reconstruction")
