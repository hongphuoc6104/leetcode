# 📦 Dynamic Programming (Quy hoạch Động)

> **"DP = Recursion + Memoization. If you can write the recurrence, you can solve the problem."**
> *— DP = Đệ quy + Ghi nhớ. Viết được công thức truy hồi là giải được bài.*

DP is the most asked topic at FAANG interviews. It optimizes overlapping subproblems by storing results. Master the 5 classic patterns and you'll handle 80% of DP problems.

---

## 📚 Learning Roadmap (Lộ trình học)

Follow these steps **in order** (Học theo thứ tự):

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 25 min | Top-down vs Bottom-up, state definition (Công thức truy hồi, trạng thái) |
| 2 | [Patterns](./guide/02_patterns.md) | 45 min | 5 patterns: 1D, 2D, Knapsack, LIS, Interval (5 dạng DP) |
| 3 | [Complexity](./guide/03_complexity.md) | 15 min | State × transition analysis (Phân tích Big-O) |
| 4 | [Python Templates](./guide/04_python_templates.md) | 20 min | Ready-to-use templates (Templates sẵn dùng) |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code (Chạy & sửa code thực tế) |
| 6 | [30 LeetCode Problems](../docs/topics/10_dynamic_programming.md) | Ongoing | Practice problems by difficulty (Bài tập theo độ khó) |

---

## 📋 Prerequisites (Yêu cầu trước)

- ✅ Recursion basics (Đệ quy cơ bản — nền tảng của DP)
- ✅ Hash Map — see [`hashMap/`](../hashMap/) (Dùng cho memoization)
- ✅ Brute Force — see [`brute_force/`](../brute_force/) (DP tối ưu từ BF)

---

## 📂 Folder Structure (Cấu trúc thư mục)

```
dynamicProgramming/
├── README.md                    ← You are here (Bạn đang ở đây)
├── guide/                       ← Theory & concepts (Lý thuyết)
│   ├── 01_introduction.md       ← Top-down vs Bottom-up
│   ├── 02_patterns.md           ← 5 DP patterns
│   ├── 03_complexity.md         ← State × transition
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/                    ← Runnable Python files (Code chạy được)
│   ├── 01_fibonacci_stairs.py
│   ├── 02_knapsack.py
│   ├── 03_longest_common_subseq.py
│   ├── 04_coin_change.py
│   └── 05_house_robber.py
├── easy/                        ← Easy problems (Bài dễ)
├── medium/                      ← Medium problems (Bài trung bình)
└── hard/                        ← Hard problems (Bài khó)
```

---

## 💡 How to Study (Cách học)

1. **Read the guide** — don't skip sections (Đọc hướng dẫn — đừng bỏ qua phần nào)
2. **Answer Self-Check Questions** — write answers on paper before checking (Trả lời câu hỏi tự kiểm tra)
3. **Run the examples** — modify them, break them, fix them (Chạy code mẫu — sửa, phá, sửa lại)
4. **Solve LeetCode problems** — start with Easy, define dp[] state first (Giải bài — định nghĩa dp[] trước)
