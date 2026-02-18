# 📦 Sliding Window (Cửa Sổ Trượt)

> **"Don't recompute — slide, add right, remove left."**
> *— Đừng tính lại — trượt, thêm phải, bỏ trái.*

Sliding Window transforms O(n×k) brute force into O(n) by maintaining a running window that slides across the array. Instead of recomputing everything from scratch, you make incremental updates — add the new element, remove the old one.

---

## 📚 Learning Roadmap (Lộ trình học)

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 20 min | Fixed vs Variable window, intuition (Cửa sổ cố định vs biến đổi) |
| 2 | [Patterns](./guide/02_patterns.md) | 40 min | 5 patterns with code (5 pattern + code) |
| 3 | [Complexity](./guide/03_complexity.md) | 15 min | Why O(n) works, amortized analysis |
| 4 | [Python Templates](./guide/04_python_templates.md) | 20 min | Ready-to-use templates |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code |
| 6 | [30 LeetCode Problems](../docs/topics/03_sliding_window.md) | Ongoing | Practice by difficulty |

---

## 📋 Prerequisites (Yêu cầu trước)

- ✅ Array & String basics — see [`arrayString/`](../arrayString/)
- ✅ Two Pointers — see [`twoPointers/`](../twoPointers/) (Sliding Window extends Same Direction)
- ✅ Hash Map basics (for variable-size windows)

---

## 📂 Folder Structure

```
slidingWindow/
├── README.md                    ← You are here
├── guide/
│   ├── 01_introduction.md       ← Fixed vs Variable, when to use
│   ├── 02_patterns.md           ← 5 patterns
│   ├── 03_complexity.md         ← Why O(n), amortized
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/
│   ├── 01_fixed_window.py
│   ├── 02_variable_window.py
│   ├── 03_longest_substring.py
│   ├── 04_min_window_substring.py
│   └── 05_find_anagrams.py
├── easy/
├── medium/
└── hard/
```

---

## 💡 How to Study

1. **Read guides in order** — Fixed Window is simpler, start there
2. **Answer Self-Check Questions** on paper
3. **Run examples** — trace the window movement manually first
4. **Key question**: "Is this Fixed or Variable size?" (Cửa sổ Cố định hay Biến đổi?)
