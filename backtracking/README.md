# 📦 Backtracking (Quay lui)

> **"Try all possibilities, backtrack when stuck — explore the decision tree."**
> *— Thử mọi khả năng, quay lui khi bế tắc — duyệt cây quyết định.*

Backtracking generates all valid combinations/permutations by building solutions incrementally and abandoning paths that can't lead to valid solutions (pruning). It's "Brute Force with early stopping."

---

## 📚 Learning Roadmap (Lộ trình học)

Follow these steps **in order** (Học theo thứ tự):

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 20 min | Choose-Explore-Unchoose pattern (Mô hình chọn-thử-bỏ) |
| 2 | [Patterns](./guide/02_patterns.md) | 40 min | 5 patterns: Subsets, Permutations, Combinations, Grid, Constraint (5 dạng bài) |
| 3 | [Complexity](./guide/03_complexity.md) | 15 min | O(2^n), O(n!), pruning analysis (Phân tích Big-O) |
| 4 | [Python Templates](./guide/04_python_templates.md) | 20 min | Ready-to-use templates (Templates sẵn dùng) |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code (Chạy & sửa code thực tế) |
| 6 | [30 LeetCode Problems](../docs/topics/12_backtracking.md) | Ongoing | Practice problems by difficulty (Bài tập theo độ khó) |

---

## 📋 Prerequisites (Yêu cầu trước)

- ✅ Recursion basics (Đệ quy cơ bản — backtracking = đệ quy + quay lui)
- ✅ Brute Force — see [`brute_force/`](../brute_force/) (Backtracking = BF + pruning)
- ✅ Array slicing, list.append/pop (Biết thao tác mảng)

---

## 📂 Folder Structure (Cấu trúc thư mục)

```
backtracking/
├── README.md                    ← You are here (Bạn đang ở đây)
├── guide/                       ← Theory & concepts (Lý thuyết)
│   ├── 01_introduction.md       ← Choose-Explore-Unchoose
│   ├── 02_patterns.md           ← 5 core patterns
│   ├── 03_complexity.md         ← O(2^n), O(n!) analysis
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/                    ← Runnable Python files (Code chạy được)
│   ├── 01_subsets.py
│   ├── 02_permutations.py
│   ├── 03_combinations.py
│   ├── 04_n_queens.py
│   └── 05_word_search.py
├── easy/                        ← Easy problems (Bài dễ)
├── medium/                      ← Medium problems (Bài trung bình)
└── hard/                        ← Hard problems (Bài khó)
```

---

## 💡 How to Study (Cách học)

1. **Read the guide** — don't skip sections (Đọc hướng dẫn — đừng bỏ qua phần nào)
2. **Answer Self-Check Questions** — write answers on paper before checking (Trả lời câu hỏi tự kiểm tra)
3. **Run the examples** — modify them, break them, fix them (Chạy code mẫu — sửa, phá, sửa lại)
4. **Solve LeetCode problems** — start with Easy, draw the decision tree first (Giải bài — vẽ cây quyết định trước)
