# 📖 Chapter 4: Python Templates

Copy-paste these templates as starting points.
(Copy-paste template này để bắt đầu.)

---

## Template 1: BFS Shortest Path (Unweighted)

```python
from collections import deque

def bfs_shortest(graph, start, end):
    """Find shortest path in unweighted graph."""
    visited = {start}
    queue = deque([(start, 0)])         # (node, distance)
    
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)        # Mark when ENQUEUING!
                queue.append((nei, dist + 1))
    
    return -1  # Unreachable
```

---

## Template 2: BFS with Path Reconstruction

```python
def bfs_path(graph, start, end):
    """Find shortest path AND return the actual path."""
    visited = {start}
    queue = deque([(start, [start])])   # (node, path_so_far)
    
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, path + [nei]))
    
    return []  # No path
```

---

## Template 3: DFS Recursive

```python
def dfs(graph, node, visited):
    """Basic DFS — explore all reachable nodes."""
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(graph, nei, visited)
```

---

## Template 4: DFS on Grid (Islands)

```python
def dfs_grid(grid, r, c):
    """DFS on 2D grid — mark visited in-place."""
    rows, cols = len(grid), len(grid[0])
    if (r < 0 or r >= rows or c < 0 or c >= cols
            or grid[r][c] != '1'):
        return
    grid[r][c] = '0'  # Mark visited
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dfs_grid(grid, r + dr, c + dc)
```

---

## Template 5: Topological Sort (Kahn's BFS)

```python
from collections import deque, defaultdict

def topo_sort(n, edges):
    """Kahn's algorithm — BFS-based topological sort.
    edges: list of (prerequisite, dependent)."""
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
```

---

## Template 6: Union-Find (Disjoint Set Union)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
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
```

---

## Template 7: Dijkstra — Weighted Shortest Path

```python
import heapq

def dijkstra(graph, start):
    """graph[u] = [(v, weight), ...]
    Returns dict of shortest distances from start."""
    dist = {start: 0}
    heap = [(0, start)]  # (distance, node)
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float('inf')):
            continue  # Skip stale entries
        for v, w in graph[u]:
            new_dist = d + w
            if new_dist < dist.get(v, float('inf')):
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
    
    return dist
```

---

## Template 8: Cycle Detection — Directed (3-Color)

```python
def has_cycle_directed(n, edges):
    """3-color DFS: WHITE=unvisited, GRAY=in-progress, BLACK=done."""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    
    def dfs(node):
        color[node] = GRAY
        for nei in graph[node]:
            if color[nei] == GRAY:   # Back edge → cycle!
                return True
            if color[nei] == WHITE and dfs(nei):
                return True
        color[node] = BLACK
        return False
    
    return any(color[i] == WHITE and dfs(i) for i in range(n))
```

---

## 📋 Pre-Coding Checklist (Kiểm tra trước khi code)

1. ✅ **Directed or undirected?** Add both edges if undirected
2. ✅ **Weighted?** Use Dijkstra for weighted, BFS for unweighted
3. ✅ **Need shortest path?** BFS (unweighted) or Dijkstra (weighted)
4. ✅ **Visited check?** Use set, not re-visiting
5. ✅ **Grid problem?** Bounds check! Reuse grid for visited
6. ✅ **Cycle possible?** 3-color for directed, parent-track for undirected
7. ✅ **Dynamic edges?** Union-Find > DFS/BFS

---

**← Previous:** [Chapter 3: Complexity](./03_complexity.md)  
**Next →** [Examples](../examples/) 🚀
