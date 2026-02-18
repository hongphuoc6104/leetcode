# 📦 Sorting Algorithms (Thuật toán Sắp xếp)

> **"Order out of chaos."**
> *— Trật tự từ hỗn loạn.*

Sorting is fundamental. While you usually use `sort()`, understanding QuickSort, MergeSort, and Bucket Sort helps you solve custom ordering problems and understand divide & conquer.

---

## 📚 Learning Roadmap (Lộ trình học)

Follow these steps **in order** (Học theo thứ tự):

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 20 min | Classification, stability (Phân loại, tính ổn định) |
| 2 | [Patterns](./guide/02_patterns.md) | 40 min | 5 patterns: Merge, Quick, Counting, Bucket, Custom (5 dạng sort) |
| 3 | [Complexity](./guide/03_complexity.md) | 15 min | O(n log n) limit, comparison vs non-comparison (Phân tích Big-O) |
| 4 | [Python Templates](./guide/04_python_templates.md) | 20 min | Ready-to-use templates (Templates sẵn dùng) |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code (Chạy & sửa code thực tế) |
| 6 | [30 LeetCode Problems](../docs/topics/14_sorting.md) | Ongoing | Practice problems by difficulty (Bài tập theo độ khó) |

---

## 📋 Prerequisites (Yêu cầu trước)

- ✅ Array basics (Mảng cơ bản)
- ✅ Recursion — see [`brute_force/`](../brute_force/) (cần cho Merge/Quick Sort)
- ✅ Python `list.sort()` and `sorted()` (Biết dùng sort tích hợp)

---

## 📂 Folder Structure (Cấu trúc thư mục)

```
sorting/
├── README.md                    ← You are here (Bạn đang ở đây)
├── guide/                       ← Theory & concepts (Lý thuyết)
│   ├── 01_introduction.md       ← Classification, stability
│   ├── 02_patterns.md           ← 5 sorting patterns
│   ├── 03_complexity.md         ← O(n log n) limit analysis
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/                    ← Runnable Python files (Code chạy được)
│   ├── 01_bubble_insertion.py
│   ├── 02_merge_sort.py
│   ├── 03_quick_sort.py
│   ├── 04_counting_sort.py
│   └── 05_custom_sort.py
├── easy/                        ← Easy problems (Bài dễ)
├── medium/                      ← Medium problems (Bài trung bình)
└── hard/                        ← Hard problems (Bài khó)
```

---

## 💡 How to Study (Cách học)

1. **Read the guide** — don't skip sections (Đọc hướng dẫn — đừng bỏ qua phần nào)
2. **Answer Self-Check Questions** — write answers on paper before checking (Trả lời câu hỏi tự kiểm tra)
3. **Run the examples** — modify them, break them, fix them (Chạy code mẫu — sửa, phá, sửa lại)
4. **Solve LeetCode problems** — start with Easy, ask "what sort property does this need?" (Giải bài — "bài này cần tính chất sort nào?")
