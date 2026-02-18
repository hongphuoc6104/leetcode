# 📖 Chapter 2: Graph Patterns

Five core graph patterns that appear in 90%+ of interview graph problems.
(5 pattern đồ thị xuất hiện trong 90%+ bài phỏng vấn.)

---

## Pattern 1: BFS — Shortest Path (Unweighted)

### 🔍 Signal (Dấu hiệu)
- "Shortest path", "minimum steps", "nearest", "level-by-level"
- Unweighted or unit-weight edges

### 💡 Key Insight
BFS explores nodes **layer by layer** — the first time we reach a node is the shortest path. Mark visited when **ENQUEUING**, not when dequeuing!

### 💻 Code
```python
from collections import deque

def bfs_shortest_path(graph, start, end):
    visited = {start}
    queue = deque([(start, 0)])  # (node, distance)
    
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)       # Mark NOW, not later!
                queue.append((nei, dist + 1))
    
    return -1  # Unreachable
```

> ⚠️ **Common Bug:** If you mark visited when DEQUEUING instead of ENQUEUING, the same node might be added to the queue multiple times → TLE!

### 📌 LC 200 (Islands), LC 994 (Rotten Oranges), LC 542, LC 1091

---

## Pattern 2: DFS — Explore & Count Components

### 🔍 Signal
- "Number of islands", "connected components", "flood fill"
- "Can you reach from A to B?"

### 💡 Key Insight
Each DFS call from an unvisited node explores one connected component. Count starts = count components.

### 💻 Code — Adjacency List
```python
def count_components(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Undirected
    
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
```

### 💻 Code — Grid (Islands, LC 200)
```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or grid[r][c] != '1'):
            return
        grid[r][c] = '0'  # Mark visited in-place!
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            dfs(r + dr, c + dc)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count
```

> 💡 **Grid trick:** Mark visited by modifying the grid itself (`'1' → '0'`). No extra visited set needed!

### 📌 LC 200, LC 695, LC 547, LC 733, LC 130

---

## Pattern 3: Topological Sort — Order Dependencies

### 🔍 Signal
- "Course schedule", "build order", "prerequisites"
- "Is it possible to finish all tasks?"
- Any DAG ordering problem

### 💡 Key Insight
Process nodes with **0 in-degree** first (no prerequisites). When processed, decrement neighbors' in-degrees. If final order has all n nodes → valid. Less → cycle exists!

### 💻 Code — Kahn's Algorithm (BFS)
```python
from collections import deque, defaultdict

def topo_sort(n, edges):
    """edges = [(prerequisite, dependent), ...]"""
    graph = defaultdict(list)
    indegree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    
    # Start with nodes that have no prerequisites
    queue = deque(i for i in range(n) if indegree[i] == 0)
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    
    return order if len(order) == n else []  # Empty → cycle!
```

### How to detect cycles?
```
If len(order) < n → cycle exists → return False / []
Because nodes in a cycle never reach indegree 0
```

### 📌 LC 207, LC 210, LC 269 (Alien Dictionary)

---

## Pattern 4: Union-Find — Dynamic Connectivity

### 🔍 Signal
- "Are nodes connected?", "count components efficiently"
- "Redundant edge", "earliest time all connected"
- Processing edges one by one

### 💡 Key Insight
Union-Find tracks which nodes belong to the same group. Two optimizations make it nearly O(1):
1. **Path compression:** Point nodes directly to root
2. **Union by rank:** Attach smaller tree under larger

### 💻 Code
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression!
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already connected
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

### When Union-Find vs DFS/BFS?
```
Static graph (all edges known)   → DFS/BFS
Dynamic graph (edges added 1by1) → Union-Find
Need component count updates     → Union-Find
```

### 📌 LC 547, LC 684, LC 721, LC 1319

---

## Pattern 5: Weighted Shortest Path — Dijkstra

### 🔍 Signal
- "Shortest path" + **weighted** edges
- "Minimum cost to reach destination"

### 💡 Key Insight
Like BFS but with a **min-heap** instead of queue. Always process the node with smallest distance first.

### 💻 Code
```python
import heapq

def dijkstra(graph, start):
    """graph[u] = [(v, weight), ...]"""
    dist = {start: 0}
    heap = [(0, start)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float('inf')):
            continue  # Stale entry
        for v, w in graph[u]:
            new_dist = d + w
            if new_dist < dist.get(v, float('inf')):
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
    
    return dist
```

> ⚠️ **Dijkstra doesn't work with negative weights!** Use Bellman-Ford instead.

### 📌 LC 743, LC 787, LC 1514

---

## 📊 Pattern Decision Table

| Signal | Pattern | Time |
|--------|---------|------|
| Shortest path (unweighted) | BFS | O(V+E) |
| Connected components / islands | DFS | O(V+E) |
| Prerequisites / ordering | Topo Sort | O(V+E) |
| Dynamic connectivity | Union-Find | O(α(n)) |
| Shortest path (weighted) | Dijkstra | O((V+E)log V) |
| Detect cycle (directed) | DFS 3-color | O(V+E) |
| Detect cycle (undirected) | DFS + parent | O(V+E) |

---

## ❓ Self-Check Questions

1. **BFS guarantees shortest path. Why doesn't DFS?** (BFS cho đường ngắn nhất. Tại sao DFS không?)
2. **TopSort returns []. What does this mean?** (TopSort trả về mảng rỗng nghĩa là gì?)
3. **Union-Find is α(n) ≈ O(1). What is α?** (α là hàm gì?)
4. **Can you detect a cycle using topological sort?** How?

---

**← Previous:** [Chapter 1: Introduction](./01_introduction.md)  
**Next →** [Chapter 3: Complexity](./03_complexity.md)
