# 📦 Array & String (Mảng & Chuỗi)

> **"The most fundamental data structure — master it, and everything else builds on top."**
> *— Cấu trúc dữ liệu cơ bản nhất — nắm vững nó, mọi thứ khác xây dựng trên nền tảng này.*

Array and String are the building blocks of almost every algorithm problem. Over 60% of LeetCode problems involve arrays or strings in some form. Understanding their properties, common operations, and patterns is essential before moving to more advanced techniques.

---

## 📚 Learning Roadmap (Lộ trình học)

| Step | File | ⏱️ Time | 🎯 What you'll learn |
|------|------|---------|---------------------|
| 1 | [Introduction](./guide/01_introduction.md) | 20 min | What are Arrays & Strings? Memory layout, properties (Mảng & Chuỗi là gì? Bố cục bộ nhớ) |
| 2 | [Patterns](./guide/02_patterns.md) | 40 min | 6 core patterns with code (6 pattern cốt lõi + code) |
| 3 | [Complexity](./guide/03_complexity.md) | 15 min | Time/Space for every operation (Big-O cho mọi thao tác) |
| 4 | [Python Templates](./guide/04_python_templates.md) | 20 min | Ready-to-use templates (Templates sẵn dùng) |
| 5 | [Examples](./examples/) | 30 min | Run & modify real code (Chạy & sửa code thực tế) |
| 6 | [30 LeetCode Problems](../docs/topics/01_array_string.md) | Ongoing | Practice problems by difficulty (Bài tập theo độ khó) |

---

## 📋 Prerequisites (Yêu cầu trước)

- ✅ Basic Python: variables, loops, conditionals (Biến, vòng lặp, điều kiện)
- ✅ Understanding of indexing (arr[0], arr[-1]) (Hiểu cách truy cập bằng index)
- ✅ Brute Force basics — see [`brute_force/`](../brute_force/) first if needed

---

## 📂 Folder Structure (Cấu trúc thư mục)

```
arrayString/
├── README.md                    ← You are here (Bạn đang ở đây)
├── guide/
│   ├── 01_introduction.md       ← Memory, properties, Python basics
│   ├── 02_patterns.md           ← 6 core patterns
│   ├── 03_complexity.md         ← Big-O for every operation
│   └── 04_python_templates.md   ← Copy-paste templates
├── examples/
│   ├── 01_traversal_basics.py
│   ├── 02_prefix_sum.py
│   ├── 03_in_place_ops.py
│   ├── 04_string_manipulation.py
│   └── 05_kadane_algorithm.py
├── easy/
├── medium/
└── hard/
```

---

## 💡 How to Study (Cách học)

1. **Read guides in order** — each builds on the previous (Đọc theo thứ tự — mỗi bài xây trên bài trước)
2. **Answer Self-Check Questions** on paper before checking (Trả lời câu hỏi tự kiểm tra trên giấy)
3. **Run examples** — modify inputs, predict output, check (Chạy code — đổi input, dự đoán output, kiểm tra)
4. **Solve LeetCode problems** — Easy first, always analyze O(?) before coding (Easy trước, luôn phân tích Big-O trước khi code)
