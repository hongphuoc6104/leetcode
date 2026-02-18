# 📖 Chapter 3: Complexity Analysis

## 1. Core Complexities

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| BFS / DFS | **O(V + E)** | O(V) | Visit each vertex and edge once |
| Topological Sort | **O(V + E)** | O(V + E) | Same as BFS + store graph |
| Union-Find (amortized) | **O(α(n)) ≈ O(1)** | O(V) | α = inverse Ackermann |
| Dijkstra (min-heap) | **O((V+E) log V)** | O(V) | Log V from heap operations |
| Bellman-Ford | **O(V × E)** | O(V) | Handles negative weights |
| Floyd-Warshall | **O(V³)** | O(V²) | All-pairs shortest path |
| Grid BFS/DFS | **O(R × C)** | O(R × C) | R rows, C columns |

---

## 2. Why O(V + E)?

BFS and DFS visit:
- Each **vertex** exactly once → O(V) from the vertex loop
- Each **edge** at most twice (once from each endpoint in undirected) → O(E)
- Total: O(V) + O(E) = **O(V + E)**

For grids: V = R × C, E ≤ 4 × R × C, so O(R × C).

---

## 3. Space Analysis

| Data Structure | Space | When |
|---------------|-------|------|
| Visited set | O(V) | Always needed |
| Queue (BFS) | O(V) | Worst: all nodes at same level |
| Stack (DFS) | O(V) | Worst: long chain |
| Adjacency list | O(V + E) | Storing the graph |
| Adjacency matrix | O(V²) | Dense graphs |
| Grid (in-place) | O(1) extra | Mark cells directly |

---

## 4. Common Mistakes (Lỗi thường gặp)

### Forgetting visited check → infinite loop! ⚠️
```python
# ❌ WRONG — infinite loop on cyclic graphs!
def bfs(graph, start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            queue.append(nei)  # May revisit endlessly!

# ✅ CORRECT
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
```

### BFS: mark visited when ENQUEUING, not DEQUEUING ⚠️
```python
# ❌ Slow — node may be enqueued multiple times!
while queue:
    node = queue.popleft()
    if node in visited: continue   # Waste!
    visited.add(node)              # Too late!
    for nei in graph[node]:
        queue.append(nei)

# ✅ Correct — mark immediately when adding to queue
while queue:
    node = queue.popleft()
    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)    # Mark NOW
            queue.append(nei)
```

> 🤔 **Why does this matter?** With the wrong approach, a node can be enqueued O(degree) times, leading to O(V × avg_degree) = O(V²) instead of O(V+E).

### Undirected edge: adding only one direction ⚠️
```python
# ❌ Missing reverse edge!
for u, v in edges:
    graph[u].append(v)

# ✅ Add both directions for undirected
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
```

### DFS on grid: not checking bounds ⚠️
```python
# ❌ IndexError!
def dfs(grid, r, c):
    grid[r][c] = '0'  # What if r, c out of range?

# ✅ Check bounds FIRST
def dfs(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return
    if grid[r][c] != '1':
        return
    grid[r][c] = '0'
    # ... recurse
```

---

## 5. Constraint Guide (Hướng dẫn từ constraints)

| Constraint | Approach | Expected Time |
|-----------|----------|--------------|
| V, E ≤ 100 | Any approach, even O(V³) | Floyd-Warshall OK |
| V ≤ 10⁴, E ≤ 10⁵ | BFS/DFS | O(V + E) |
| V ≤ 10⁵ | BFS/DFS, Union-Find | O(V + E) or O(V × α) |
| Grid 300×300 | DFS/BFS | O(R × C) = O(90K) |
| Need shortest + weights | Dijkstra | O((V+E) log V) |

---

## ❓ Self-Check Questions

1. **BFS uses O(max_level_width) space. What's the worst case?** (Trường hợp xấu nhất?)
2. **Union-Find is O(α(n)). What is α(n) for practical n?** (Giá trị thực tế?)
3. **Grid DFS may cause stack overflow for large grids. How to fix?** (Cách khắc phục?)
4. **Dijkstra with negative edges gives wrong answer. Why?** (Tại sao sai?)

---

**← Previous:** [Chapter 2: Patterns](./02_patterns.md)  
**Next →** [Chapter 4: Templates](./04_python_templates.md)
