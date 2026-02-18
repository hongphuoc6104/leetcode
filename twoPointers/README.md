# 📦 Two Pointers (Hai Con Trỏ)

> **"The art of reducing O(n²) to O(n) with just two variables."**
> *— Nghệ thuật giảm O(n²) xuống O(n) chỉ với 2 biến.*

Two Pointers is one of the most powerful optimization techniques. It transforms brute force nested loops into elegant single-pass solutions. If you see a sorted array or need to find pairs/triples, think Two Pointers first.

---

## 📚 Learning Roadmap (Lộ trình học)

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 20 min | What Two Pointers is, 3 variants, when to use (3 biến thể, khi nào dùng) |
| 2 | [Patterns](./guide/02_patterns.md) | 40 min | 5 core patterns with code (5 pattern cốt lõi + code) |
| 3 | [Complexity](./guide/03_complexity.md) | 15 min | Why it's O(n), proof & constraint guide |
| 4 | [Python Templates](./guide/04_python_templates.md) | 20 min | Ready-to-use templates (Templates sẵn dùng) |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code (Chạy & sửa code thực tế) |
| 6 | [30 LeetCode Problems](../docs/topics/02_two_pointers.md) | Ongoing | Practice problems by difficulty |

---

## 📋 Prerequisites (Yêu cầu trước)

- ✅ Array & String basics — see [`arrayString/`](../arrayString/) first
- ✅ Understanding of sorting: `arr.sort()` is O(n log n)
- ✅ Brute Force nested loops — how O(n²) works

---

## 📂 Folder Structure (Cấu trúc thư mục)

```
twoPointers/
├── README.md                    ← You are here
├── guide/
│   ├── 01_introduction.md       ← 3 variants, intuition, when to use
│   ├── 02_patterns.md           ← 5 patterns with code
│   ├── 03_complexity.md         ← Why O(n) works, proofs
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/
│   ├── 01_opposite_direction.py
│   ├── 02_same_direction.py
│   ├── 03_fast_slow.py
│   ├── 04_three_sum.py
│   └── 05_trapping_rain.py
├── easy/
├── medium/
└── hard/
```

---

## 💡 How to Study (Cách học)

1. **Read guides in order** — understand the 3 variants deeply
2. **Answer Self-Check Questions** on paper before proceeding
3. **Run examples** — predict output before running, compare
4. **Solve LeetCode** — always ask: "Is this Opposite, Same, or Fast/Slow?"
