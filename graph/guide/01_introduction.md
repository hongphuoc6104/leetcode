# 📖 Chapter 1: Introduction to Graphs

## 1. What is a Graph? (Đồ thị là gì?)

A graph consists of **vertices (đỉnh)** and **edges (cạnh)** connecting them. Unlike trees, graphs can have **cycles**, **multiple paths**, and even **disconnected components**.

> 🤔 **Socratic Question:** A tree is actually a special type of graph. What constraints make a tree different from a general graph? (Cây là đồ thị đặc biệt. Điều gì phân biệt cây và đồ thị?)

```
Undirected Graph:        Directed Graph (DAG):     Weighted Graph:
 0 --- 1                  0 → 1                     0 --5-- 1
 |   / |                  ↓   ↓                     |       |
 |  /  |                  2 → 3                    3|      2|
 2 --- 3                                            2 --1-- 3
```

**Analogy (Ví dụ):** Think of a city's road map. Intersections = vertices, roads = edges. One-way roads = directed edges. Road distances = weights.

---

## 2. Graph Representations (Cách biểu diễn đồ thị)

### Adjacency List — Most Common in Interviews (Phổ biến nhất)
```python
from collections import defaultdict

# Build graph from edge list
graph = defaultdict(list)
edges = [(0, 1), (1, 2), (2, 3)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # Add for undirected only!

# Access neighbors
print(graph[0])  # [1]
print(graph[1])  # [0, 2]
```

### Edge List — Simple, used for Union-Find
```python
edges = [[0, 1], [1, 2], [2, 3]]  # Just a list of pairs
```

### Adjacency Matrix — Good for dense graphs
```python
# matrix[i][j] = 1 if edge i→j, else 0
n = 4
matrix = [[0] * n for _ in range(n)]
matrix[0][1] = matrix[1][0] = 1  # Edge 0-1
```

### Grid as Graph — 2D arrays in disguise!
```python
# grid[r][c] is a node, neighbors are 4 adjacent cells
grid = [
    ['1', '1', '0'],
    ['1', '0', '0'],
    ['0', '0', '1']
]
# Node (r,c) neighbors: (r±1, c), (r, c±1)
directions = [(0,1), (0,-1), (1,0), (-1,0)]
```

### When to Use Which?

| Representation | Space | Edge lookup | Best for |
|---------------|-------|-------------|---------|
| Adjacency List | O(V+E) | O(degree) | Sparse graphs, most problems |
| Adjacency Matrix | O(V²) | O(1) | Dense graphs, Floyd-Warshall |
| Edge List | O(E) | O(E) | Union-Find, Kruskal's |
| Grid | O(R×C) | O(1) | Islands, maze problems |

---

## 3. Key Terminology (Thuật ngữ quan trọng)

| Term | Vietnamese | Definition |
|------|-----------|-----------|
| **Directed** | Có hướng | Edges have direction (u → v) |
| **Undirected** | Vô hướng | Edges go both ways (u — v) |
| **Weighted** | Có trọng số | Edges have costs/distances |
| **Cycle** | Vòng lặp | Path that returns to start |
| **DAG** | Đồ thị không chu trình | Directed Acyclic Graph |
| **Connected** | Liên thông | Every node reachable from any node |
| **Component** | Thành phần liên thông | Maximal connected subgraph |
| **Degree** | Bậc | Number of edges to/from a node |
| **In-degree** | Bậc vào | Edges pointing TO this node (directed) |
| **Out-degree** | Bậc ra | Edges pointing FROM this node (directed) |
| **Adjacent** | Kề | Two nodes connected by an edge |
| **Path** | Đường đi | Sequence of vertices connected by edges |

---

## 4. BFS vs DFS — When to Use?

| Feature | BFS | DFS |
|---------|-----|-----|
| **Structure** | Queue (FIFO) | Stack/Recursion (LIFO) |
| **Explores** | Level by level (Theo tầng) | Deep first (Sâu trước) |
| **Shortest path?** | ✅ Yes (unweighted) | ❌ No |
| **Cycle detection?** | ✅ Yes | ✅ Yes |
| **Topological sort?** | ✅ Kahn's algorithm | ✅ DFS post-order |
| **Space** | O(max level width) | O(max depth) |
| **Connected components?** | ✅ | ✅ |

### Decision Guide
```
Need shortest path (unweighted)?  → BFS
Need to explore all possibilities? → DFS
Need topological order?           → Either (Kahn's BFS or DFS)
Grid/island problem?              → DFS (simpler code)
Shortest path (weighted)?         → Dijkstra (BFS with heap)
```

---

## 5. Graph vs Tree

| Property | Tree | Graph |
|----------|------|-------|
| Cycles? | ❌ No | ✅ Can have |
| Connected? | ✅ Always | Not necessarily |
| Root? | ✅ One root | ❌ No root |
| Edges | n - 1 | Any number |
| Path between two nodes | Exactly 1 | 0 or more |

---

## ❓ Self-Check Questions

1. **Given n=5 nodes and edges [(0,1),(1,2),(3,4)], how many components?** (Bao nhiêu thành phần liên thông?)
2. **Can BFS find shortest path in a weighted graph?** Why or why not?
3. **What's the max edges in an undirected graph with n nodes?** (Số cạnh tối đa?)
4. **A grid of size R×C has how many "vertices" and "edges"?** (Đỉnh và cạnh?)

---

**Next →** [Chapter 2: Patterns](./02_patterns.md)
