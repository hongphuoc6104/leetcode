# 📦 Hash Map / Set (Bảng Băm)

> **"O(1) lookup is a superpower — use it to turn O(n²) into O(n)."**
> *— Tra cứu O(1) là siêu năng lực — biến O(n²) thành O(n).*

Hash Map (`dict`) and Hash Set (`set`) provide O(1) average-case lookup, insert, and delete. They are the most frequently used data structures in coding interviews.

---

## 📚 Learning Roadmap

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 20 min | dict, set, Counter, defaultdict |
| 2 | [Patterns](./guide/02_patterns.md) | 40 min | 5 patterns: Frequency, Two Sum, Grouping, Prefix+Hash, Set ops |
| 3 | [Complexity](./guide/03_complexity.md) | 15 min | Why O(1), hash collisions |
| 4 | [Python Templates](./guide/04_python_templates.md) | 20 min | Ready-to-use templates |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code |
| 6 | [30 LeetCode Problems](../docs/topics/07_hash_map.md) | Ongoing | Practice by difficulty |

---

## 📋 Prerequisites

- ✅ Array basics — see [`arrayString/`](../arrayString/)
- ✅ Understanding of key-value pairs

---

## 📂 Folder Structure

```
hashMap/
├── README.md                    ← You are here
├── guide/
│   ├── 01_introduction.md       ← dict, set, Counter
│   ├── 02_patterns.md           ← 5 core patterns
│   ├── 03_complexity.md         ← O(1) analysis, collisions
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/
│   ├── 01_two_sum_hash.py
│   ├── 02_frequency_counting.py
│   ├── 03_group_anagrams.py
│   ├── 04_prefix_sum_hash.py
│   └── 05_longest_consecutive.py
├── easy/
├── medium/
└── hard/
```

---

## 💡 How to Study

1. **"Find pair/complement"? → Hash Map** — O(n) instead of O(n²)
2. **"Count occurrences"? → Counter / dict** — frequency problems
3. **"Subarray sum = k"? → Prefix Sum + Hash Map** — the power combo
