# 📦 Greedy Algorithms (Tham lam)

> **"Make the best local choice at each step, hoping for the global optimum."**
> *— Chọn tốt nhất ở hiện tại, hy vọng kết quả toàn cục cũng tốt nhất.*

Greedy algorithms are fast because they make decisions without backtracking. They work for specific problems like Interval Scheduling, Huffman Coding, and Dijkstra.

---

## 📚 Learning Roadmap (Lộ trình học)

Follow these steps **in order** (Học theo thứ tự):

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 15 min | When Greedy works vs fails (Khi nào tham lam đúng/sai) |
| 2 | [Patterns](./guide/02_patterns.md) | 30 min | 5 patterns: Intervals, Jump, Boats, Stock, Partition (5 dạng bài) |
| 3 | [Complexity](./guide/03_complexity.md) | 10 min | O(n log n) dominance (Phân tích Big-O) |
| 4 | [Python Templates](./guide/04_python_templates.md) | 15 min | Ready-to-use templates (Templates sẵn dùng) |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code (Chạy & sửa code thực tế) |
| 6 | [30 LeetCode Problems](../docs/topics/13_greedy.md) | Ongoing | Practice problems by difficulty (Bài tập theo độ khó) |

---

## 📋 Prerequisites (Yêu cầu trước)

- ✅ Sorting basics — see [`sorting/`](../sorting/) (Nhiều bài Greedy bắt đầu bằng sort)
- ✅ Heap basics — see [`heap/`](../heap/) (Heap hỗ trợ nhiều bài Greedy)
- ✅ Understanding time complexity (Hiểu Big-O để biết khi nào cần Greedy)

---

## 📂 Folder Structure (Cấu trúc thư mục)

```
greedy/
├── README.md                    ← You are here (Bạn đang ở đây)
├── guide/                       ← Theory & concepts (Lý thuyết)
│   ├── 01_introduction.md       ← When Greedy works
│   ├── 02_patterns.md           ← 5 core patterns
│   ├── 03_complexity.md         ← O(n log n) analysis
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/                    ← Runnable Python files (Code chạy được)
│   ├── 01_jump_game.py
│   ├── 02_interval_scheduling.py
│   ├── 03_gas_station.py
│   ├── 04_partition_labels.py
│   └── 05_huffman_coding.py
├── easy/                        ← Easy problems (Bài dễ)
├── medium/                      ← Medium problems (Bài trung bình)
└── hard/                        ← Hard problems (Bài khó)
```

---

## 💡 How to Study (Cách học)

1. **Read the guide** — don't skip sections (Đọc hướng dẫn — đừng bỏ qua phần nào)
2. **Answer Self-Check Questions** — write answers on paper before checking (Trả lời câu hỏi tự kiểm tra)
3. **Run the examples** — modify them, break them, fix them (Chạy code mẫu — sửa, phá, sửa lại)
4. **Solve LeetCode problems** — start with Easy, ask "does local optimal = global optimal?" (Giải bài — "chọn tốt nhất cục bộ có cho kết quả toàn cục tốt nhất?")
