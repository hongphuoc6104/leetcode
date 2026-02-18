# 📦 Linked List (Danh Sách Liên Kết)

> **"Pointers are the key — master node manipulation to master Linked Lists."**
> *— Con trỏ là chìa khóa — thành thạo thao tác node để thành thạo Linked List.*

Linked List is the first non-contiguous data structure you'll learn. Unlike arrays, elements are scattered in memory, connected by pointers. This gives O(1) insertion/deletion but sacrifices random access.

---

## 📚 Learning Roadmap

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 20 min | Node structure, types, Array vs LL trade-offs |
| 2 | [Patterns](./guide/02_patterns.md) | 40 min | 5 patterns: Dummy Head, Reverse, Fast/Slow, Merge, Two Lists |
| 3 | [Complexity](./guide/03_complexity.md) | 15 min | Operation costs, when to use LL vs Array |
| 4 | [Python Templates](./guide/04_python_templates.md) | 20 min | Ready-to-use templates |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code |
| 6 | [30 LeetCode Problems](../docs/topics/05_linked_list.md) | Ongoing | Practice by difficulty |

---

## 📋 Prerequisites

- ✅ Python classes (`class`, `self`, `__init__`)
- ✅ Pointer/reference concepts
- ✅ Two Pointers — see [`twoPointers/`](../twoPointers/) (Fast/Slow extends here)

---

## 📂 Folder Structure

```
linkedList/
├── README.md                    ← You are here
├── guide/
│   ├── 01_introduction.md       ← Node, types, Array vs LL
│   ├── 02_patterns.md           ← 5 core patterns
│   ├── 03_complexity.md         ← Operation costs
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/
│   ├── 01_basic_operations.py
│   ├── 02_reverse_list.py
│   ├── 03_merge_lists.py
│   ├── 04_cycle_detection.py
│   └── 05_remove_nth_end.py
├── easy/
├── medium/
└── hard/
```

---

## 💡 How to Study

1. **Always DRAW before coding** — sketch nodes and arrows on paper
2. **Master the Dummy Head** — it eliminates 90% of edge cases
3. **Key question**: "Which pointers need to change? In what order?"
