# 📖 Chủ đề 9: Graph (BFS, DFS)

## Lý thuyết cơ bản

**Graph** gồm đỉnh (vertex) và cạnh (edge). Biểu diễn bằng **adjacency list** hoặc **adjacency matrix**.

### Các thuật toán chính
```python
from collections import deque, defaultdict

# BFS - Tìm đường ngắn nhất (unweighted)
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# DFS - Duyệt sâu
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# BFS trên ma trận (grid)
def bfs_grid(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    queue = deque([(start_r, start_c)])
    visited = {(start_r, start_c)}
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))

# Topological Sort (Kahn's BFS)
def topo_sort(num_courses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * num_courses
    for u, v in prerequisites:
        graph[v].append(u)
        indegree[u] += 1
    queue = deque([i for i in range(num_courses) if indegree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    return order if len(order) == num_courses else []
```

---

## Danh sách 30 bài LeetCode

### 🟢 Easy (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Island Perimeter | [LC 463](https://leetcode.com/problems/island-perimeter/) | Count edges |
| 2 | Flood Fill | [LC 733](https://leetcode.com/problems/flood-fill/) | DFS/BFS grid |
| 3 | Find Town Judge | [LC 997](https://leetcode.com/problems/find-the-town-judge/) | Indegree/outdegree |
| 4 | Shortest Path Binary Matrix | [LC 1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | BFS |
| 5 | Jump Game IV | [LC 1345](https://leetcode.com/problems/jump-game-iv/) | BFS |
| 6 | Find if Path Exists | [LC 1971](https://leetcode.com/problems/find-if-path-exists-in-graph/) | DFS/BFS/Union-Find |
| 7 | Find Closest Node | [LC 2359](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/) | BFS from both |
| 8 | Center of Star | [LC 1791](https://leetcode.com/problems/find-center-of-star-graph/) | Check common node |
| 9 | Check Distances | [LC 2399](https://leetcode.com/problems/check-distances-between-same-letters/) | Hash map |
| 10 | Count Asterisks | [LC 2315](https://leetcode.com/problems/count-asterisks/) | Track inside/outside bars |

### 🟡 Medium (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Clone Graph | [LC 133](https://leetcode.com/problems/clone-graph/) | BFS/DFS + hash map |
| 2 | Number of Islands | [LC 200](https://leetcode.com/problems/number-of-islands/) | DFS/BFS, mark visited |
| 3 | Course Schedule | [LC 207](https://leetcode.com/problems/course-schedule/) | Topological sort |
| 4 | Course Schedule II | [LC 210](https://leetcode.com/problems/course-schedule-ii/) | Topological sort order |
| 5 | Walls and Gates | [LC 286](https://leetcode.com/problems/walls-and-gates/) | Multi-source BFS |
| 6 | Connected Components | [LC 323](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | DFS/Union-Find |
| 7 | Pacific Atlantic | [LC 417](https://leetcode.com/problems/pacific-atlantic-water-flow/) | BFS from borders |
| 8 | Number of Provinces | [LC 547](https://leetcode.com/problems/number-of-provinces/) | DFS/Union-Find |
| 9 | Redundant Connection | [LC 684](https://leetcode.com/problems/redundant-connection/) | Union-Find |
| 10 | Is Bipartite | [LC 785](https://leetcode.com/problems/is-graph-bipartite/) | BFS/DFS 2-coloring |

### 🔴 Hard (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Word Ladder | [LC 127](https://leetcode.com/problems/word-ladder/) | BFS word graph |
| 2 | Alien Dictionary | [LC 269](https://leetcode.com/problems/alien-dictionary/) | Topological sort |
| 3 | Longest Increasing Path | [LC 329](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | DFS + memo |
| 4 | Reconstruct Itinerary | [LC 332](https://leetcode.com/problems/reconstruct-itinerary/) | Hierholzer's (Euler path) |
| 5 | Redundant Connection II | [LC 685](https://leetcode.com/problems/redundant-connection-ii/) | Union-Find, directed |
| 6 | Network Delay Time | [LC 743](https://leetcode.com/problems/network-delay-time/) | Dijkstra |
| 7 | Swim in Rising Water | [LC 778](https://leetcode.com/problems/swim-in-rising-water/) | BS + BFS hoặc Dijkstra |
| 8 | Bus Routes | [LC 815](https://leetcode.com/problems/bus-routes/) | BFS on routes |
| 9 | Shortest All Nodes | [LC 847](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | BFS + bitmask |
| 10 | Critical Connections | [LC 1192](https://leetcode.com/problems/critical-connections-in-a-network/) | Tarjan's algorithm |

---

## Tips
- **Grid problems** (islands, paths) = BFS/DFS trên ma trận
- **Dependency/ordering** = Topological Sort
- **Shortest path** unweighted = BFS, weighted = Dijkstra
