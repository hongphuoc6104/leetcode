# 📦 Graph (Đồ thị)

> **"DFS explores deep, BFS explores wide — know when to use each."**
> *— DFS đi sâu, BFS đi rộng — biết khi nào dùng.*

Graphs model relationships between entities. BFS finds shortest paths in unweighted graphs, DFS detects cycles and explores components. Union-Find handles connectivity efficiently.

---

## 📚 Learning Roadmap (Lộ trình học)

Follow these steps **in order** (Học theo thứ tự):

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 20 min | Representations, directed vs undirected (Biểu diễn đồ thị) |
| 2 | [Patterns](./guide/02_patterns.md) | 40 min | 5 patterns: BFS, DFS, Topo Sort, Union-Find, Dijkstra (5 dạng bài) |
| 3 | [Complexity](./guide/03_complexity.md) | 15 min | O(V+E) analysis (Phân tích Big-O) |
| 4 | [Python Templates](./guide/04_python_templates.md) | 20 min | Ready-to-use templates (Templates sẵn dùng) |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code (Chạy & sửa code thực tế) |
| 6 | [30 LeetCode Problems](../docs/topics/09_graph.md) | Ongoing | Practice problems by difficulty (Bài tập theo độ khó) |

---

## 📋 Prerequisites (Yêu cầu trước)

- ✅ Tree basics — see [`tree/`](../tree/) (DFS/BFS trên cây — nền tảng cho đồ thị)
- ✅ Hash Map — see [`hashMap/`](../hashMap/) (Adjacency list dùng dict)
- ✅ Queue — see [`stackQueue/`](../stackQueue/) (BFS dùng deque)

---

## 📂 Folder Structure (Cấu trúc thư mục)

```
graph/
├── README.md                    ← You are here (Bạn đang ở đây)
├── guide/                       ← Theory & concepts (Lý thuyết)
│   ├── 01_introduction.md       ← Representations, types
│   ├── 02_patterns.md           ← 5 core patterns
│   ├── 03_complexity.md         ← O(V+E) analysis
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/                    ← Runnable Python files (Code chạy được)
│   ├── 01_bfs_shortest_path.py
│   ├── 02_dfs_components.py
│   ├── 03_cycle_detection.py
│   ├── 04_topological_sort.py
│   └── 05_union_find.py
├── easy/                        ← Easy problems (Bài dễ)
├── medium/                      ← Medium problems (Bài trung bình)
└── hard/                        ← Hard problems (Bài khó)
```

---

## 💡 How to Study (Cách học)

1. **Read the guide** — don't skip sections (Đọc hướng dẫn — đừng bỏ qua phần nào)
2. **Answer Self-Check Questions** — write answers on paper before checking (Trả lời câu hỏi tự kiểm tra)
3. **Run the examples** — modify them, break them, fix them (Chạy code mẫu — sửa, phá, sửa lại)
4. **Solve LeetCode problems** — start with Easy, draw the graph first (Giải bài — bắt đầu Easy, vẽ đồ thị trước)
