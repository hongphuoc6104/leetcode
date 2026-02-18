# 📦 Tree (Cây)

> **"Trees are recursive by nature — think recursively, code naturally."**
> *— Cây có bản chất đệ quy — suy nghĩ đệ quy, code tự nhiên.*

Trees are the most important non-linear data structure. Binary Trees and BSTs appear in ~25% of interview questions. Master DFS (preorder/inorder/postorder) and BFS (level-order).

---

## 📚 Learning Roadmap (Lộ trình học)

Follow these steps **in order** (Học theo thứ tự):

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 20 min | TreeNode, traversals, BST property (Cấu trúc cây, duyệt cây, tính chất BST) |
| 2 | [Patterns](./guide/02_patterns.md) | 40 min | 5 patterns: DFS, BFS, BST, Path, Construction (5 dạng bài) |
| 3 | [Complexity](./guide/03_complexity.md) | 15 min | O(n) traversal, O(h) BST, balanced vs skewed (Phân tích Big-O) |
| 4 | [Python Templates](./guide/04_python_templates.md) | 20 min | Ready-to-use templates (Templates sẵn dùng) |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code (Chạy & sửa code thực tế) |
| 6 | [30 LeetCode Problems](../docs/topics/08_tree.md) | Ongoing | Practice problems by difficulty (Bài tập theo độ khó) |

---

## 📋 Prerequisites (Yêu cầu trước)

- ✅ Recursion basics (Đệ quy cơ bản)
- ✅ Stack & Queue — see [`stackQueue/`](../stackQueue/) (Dùng cho iterative traversals)
- ✅ Understand linked nodes concept (Hiểu khái niệm node liên kết)

---

## 📂 Folder Structure (Cấu trúc thư mục)

```
tree/
├── README.md                    ← You are here (Bạn đang ở đây)
├── guide/                       ← Theory & concepts (Lý thuyết)
│   ├── 01_introduction.md       ← TreeNode, traversals, BST
│   ├── 02_patterns.md           ← 5 core patterns
│   ├── 03_complexity.md         ← O(n) vs O(h) analysis
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/                    ← Runnable Python files (Code chạy được)
│   ├── 01_traversals.py
│   ├── 02_max_depth.py
│   ├── 03_bst_operations.py
│   ├── 04_level_order.py
│   └── 05_path_sum.py
├── easy/                        ← Easy problems (Bài dễ)
├── medium/                      ← Medium problems (Bài trung bình)
└── hard/                        ← Hard problems (Bài khó)
```

---

## 💡 How to Study (Cách học)

1. **Read the guide** — don't skip sections (Đọc hướng dẫn — đừng bỏ qua phần nào)
2. **Answer Self-Check Questions** — write answers on paper before checking (Trả lời câu hỏi tự kiểm tra)
3. **Run the examples** — modify them, break them, fix them (Chạy code mẫu — sửa, phá, sửa lại)
4. **Solve LeetCode problems** — start with Easy, use DFS first (Giải bài — bắt đầu Easy, dùng DFS trước)
