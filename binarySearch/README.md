# 📦 Binary Search (Tìm Kiếm Nhị Phân)

> **"Cut the search space in HALF every step — O(log n) power."**
> *— Cắt không gian tìm kiếm làm ĐÔI mỗi bước — sức mạnh O(log n).*

Binary Search is the ultimate "divide and conquer" technique for searching. It reduces O(n) linear search to O(log n) by eliminating half the possibilities each step. The key requirement: the data must have a **monotonic property**.

---

## 📚 Learning Roadmap (Lộ trình học)

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 20 min | 3 templates, boundary conditions (3 template, điều kiện biên) |
| 2 | [Patterns](./guide/02_patterns.md) | 40 min | 5 patterns: exact, lower/upper bound, rotated, answer |
| 3 | [Complexity](./guide/03_complexity.md) | 15 min | Why O(log n), search space analysis |
| 4 | [Python Templates](./guide/04_python_templates.md) | 20 min | Ready-to-use templates |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code |
| 6 | [30 LeetCode Problems](../docs/topics/04_binary_search.md) | Ongoing | Practice by difficulty |

---

## 📋 Prerequisites (Yêu cầu trước)

- ✅ Array basics — see [`arrayString/`](../arrayString/)
- ✅ Sorting concept: arrays must be sorted for classic BS
- ✅ Understanding of logarithms: log₂(n)

---

## 📂 Folder Structure

```
binarySearch/
├── README.md                    ← You are here
├── guide/
│   ├── 01_introduction.md       ← 3 templates, when to use
│   ├── 02_patterns.md           ← 5 core patterns
│   ├── 03_complexity.md         ← Why O(log n)
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/
│   ├── 01_basic_search.py
│   ├── 02_lower_upper_bound.py
│   ├── 03_rotated_array.py
│   ├── 04_search_on_answer.py
│   └── 05_peak_finding.py
├── easy/
├── medium/
└── hard/
```

---

## 💡 How to Study

1. **Master the 3 templates first** — `left <= right`, `left < right`, `left < right` with answer check
2. **Practice boundary conditions** — this is where 90% of bugs occur
3. **Key question**: "What is my search space? What am I binary searching ON?"
