# 📦 Heap / Priority Queue (Đống / Hàng đợi ưu tiên)

> **"Always give me the min (or max) instantly? That's a Heap."**
> *— Luôn cho tôi min (hoặc max) ngay lập tức? Đó là Heap.*

Heaps give O(1) access to min/max and O(log n) insert/remove. Python's `heapq` is a min-heap. Used for "Top K", "Merge K Sorted", and scheduling problems.

---

## 📚 Learning Roadmap (Lộ trình học)

Follow these steps **in order** (Học theo thứ tự):

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 20 min | Heap property, heapq API (Thuộc tính heap, API heapq) |
| 2 | [Patterns](./guide/02_patterns.md) | 40 min | 5 patterns: Top K, Merge K, Two Heaps, Lazy Delete, Custom (5 dạng bài) |
| 3 | [Complexity](./guide/03_complexity.md) | 15 min | O(log n) push/pop, O(n) heapify (Phân tích Big-O) |
| 4 | [Python Templates](./guide/04_python_templates.md) | 20 min | Ready-to-use templates (Templates sẵn dùng) |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code (Chạy & sửa code thực tế) |
| 6 | [30 LeetCode Problems](../docs/topics/11_heap.md) | Ongoing | Practice problems by difficulty (Bài tập theo độ khó) |

---

## 📋 Prerequisites (Yêu cầu trước)

- ✅ Array basics (Mảng cơ bản — heap được lưu trong mảng)
- ✅ Binary Tree concept — see [`tree/`](../tree/) (Heap là binary tree đặc biệt)
- ✅ Python `heapq` module (Biết import heapq)

---

## 📂 Folder Structure (Cấu trúc thư mục)

```
heap/
├── README.md                    ← You are here (Bạn đang ở đây)
├── guide/                       ← Theory & concepts (Lý thuyết)
│   ├── 01_introduction.md       ← Heap property, heapq API
│   ├── 02_patterns.md           ← 5 core patterns
│   ├── 03_complexity.md         ← O(log n) push/pop analysis
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/                    ← Runnable Python files (Code chạy được)
│   ├── 01_heap_basics.py
│   ├── 02_top_k_elements.py
│   ├── 03_merge_k_sorted.py
│   ├── 04_median_stream.py
│   └── 05_task_scheduler.py
├── easy/                        ← Easy problems (Bài dễ)
├── medium/                      ← Medium problems (Bài trung bình)
└── hard/                        ← Hard problems (Bài khó)
```

---

## 💡 How to Study (Cách học)

1. **Read the guide** — don't skip sections (Đọc hướng dẫn — đừng bỏ qua phần nào)
2. **Answer Self-Check Questions** — write answers on paper before checking (Trả lời câu hỏi tự kiểm tra)
3. **Run the examples** — modify them, break them, fix them (Chạy code mẫu — sửa, phá, sửa lại)
4. **Solve LeetCode problems** — start with Easy, think "do I need min/max quickly?" (Giải bài — "tôi có cần min/max nhanh không?")
