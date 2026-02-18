# 📦 Stack & Queue (Ngăn xếp & Hàng đợi)

> **"LIFO vs FIFO — two simple rules, infinite applications."**
> *— LIFO so với FIFO — hai quy tắc đơn giản, vô số ứng dụng.*

Stack (Last In, First Out) and Queue (First In, First Out) are the foundational data structures for managing order of processing. Mastering Monotonic Stack alone unlocks dozens of medium/hard problems.

---

## 📚 Learning Roadmap

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 20 min | Stack vs Queue, Python implementation, use cases |
| 2 | [Patterns](./guide/02_patterns.md) | 40 min | 5 patterns: Matching, Monotonic, Calculator, BFS Queue, Deque |
| 3 | [Complexity](./guide/03_complexity.md) | 15 min | All operations O(1), space trade-offs |
| 4 | [Python Templates](./guide/04_python_templates.md) | 20 min | Ready-to-use templates |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code |
| 6 | [30 LeetCode Problems](../docs/topics/06_stack_queue.md) | Ongoing | Practice by difficulty |

---

## 📋 Prerequisites

- ✅ Array basics — see [`arrayString/`](../arrayString/)
- ✅ Linked List (conceptual) — Queue can use LL internally

---

## 📂 Folder Structure

```
stackQueue/
├── README.md                    ← You are here
├── guide/
│   ├── 01_introduction.md       ← Stack vs Queue fundamentals
│   ├── 02_patterns.md           ← 5 core patterns
│   ├── 03_complexity.md         ← Operation costs
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/
│   ├── 01_valid_parentheses.py
│   ├── 02_monotonic_stack.py
│   ├── 03_calculator.py
│   ├── 04_decode_string.py
│   └── 05_sliding_window_max.py
├── easy/
├── medium/
└── hard/
```

---

## 💡 How to Study

1. **Parentheses/Brackets? → Stack** — almost guaranteed
2. **"Next greater/smaller element"? → Monotonic Stack**
3. **Level-by-level processing? → Queue (BFS)**
