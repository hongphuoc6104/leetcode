# 📖 Chapter 1: Introduction to Two Pointers (Giới thiệu Hai Con Trỏ)

## 🎯 Learning Objectives (Mục tiêu)

After this chapter (Sau chương này):
- Understand the 3 variants of Two Pointers (Hiểu 3 biến thể)
- Know when Two Pointers is applicable (Biết khi nào áp dụng được)
- See how it reduces O(n²) to O(n) (Thấy cách giảm O(n²) thành O(n))

---

## 1. What is Two Pointers? (Hai Con Trỏ là gì?)

Two Pointers is a technique that uses **two index variables** to scan through data, eliminating unnecessary comparisons (Hai Con Trỏ dùng **hai biến index** để quét qua dữ liệu, loại bỏ so sánh không cần thiết).

### 🧠 The Core Insight (Nhận xét cốt lõi)

**Brute Force** checks **all** pairs → O(n²) (Vét cạn kiểm tra **tất cả** cặp)
**Two Pointers** skips pairs intelligently → O(n) (Hai Con Trỏ bỏ qua cặp thông minh)

```
Brute Force: Check EVERY pair
  (i,j) = (0,1), (0,2), (0,3), ..., (1,2), (1,3), ...
  → n(n-1)/2 pairs = O(n²)

Two Pointers: Move INTELLIGENTLY
  left → ... ← right
  Each step eliminates many pairs at once
  → Each pointer moves at most n times = O(n)
```

### Real-life Analogy (Ví dụ thực tế)

Imagine searching for a page in a book (Tưởng tượng tìm trang trong sách):

- **Brute Force**: Flip from page 1 → page 2 → page 3... (Lật từ trang 1)
- **Two Pointers**: Open in the middle. Too far? Go left. Not enough? Go right. (Mở giữa. Quá xa? Đi trái. Chưa đủ? Đi phải.)

---

## 2. The 3 Variants (3 Biến thể)

### Variant 1: Opposite Direction (Đối hướng) — left ↔ right

Two pointers start from **opposite ends** and move toward each other (2 con trỏ bắt đầu từ **2 đầu đối diện**, di chuyển vào giữa).

```
     left →         ← right
  [  1,  3,  5,  7,  9,  11  ]
   ↑                        ↑
  left=0              right=5

  Step: Compare, move the pointer that helps.
  (So sánh, di chuyển con trỏ giúp ích.)
```

**When to use** (Khi nào dùng):
- Array is **sorted** (Mảng **đã sắp xếp**)
- Find pair with specific sum (Tìm cặp có tổng cụ thể)
- Palindrome check (Kiểm tra đối xứng)
- Container/area problems (Bài tính diện tích)

**Why it works on sorted arrays**: If `arr[left] + arr[right] < target`, increasing `left` increases the sum. If too big, decreasing `right` decreases it. Each step eliminates one possibility → O(n) total (Mỗi bước loại bỏ 1 khả năng → O(n)).

---

### Variant 2: Same Direction (Cùng hướng) — slow & fast

Two pointers move in the **same direction**, at **different speeds** (2 con trỏ di chuyển **cùng hướng**, **tốc độ khác nhau**).

```
  slow  fast →→→
   ↓     ↓
  [1, 1, 2, 2, 3, 3, 4]
   w     r

  slow = "write position" (vị trí ghi)
  fast = "read position" (vị trí đọc)
```

**When to use** (Khi nào dùng):
- **In-place modification** (Sửa tại chỗ)
- Remove duplicates (Xóa trùng lặp)
- Move/filter elements (Di chuyển/lọc phần tử)
- Subsequence check (Kiểm tra chuỗi con)

---

### Variant 3: Fast & Slow (Nhanh & Chậm) — Floyd's Cycle

One pointer moves **1 step**, the other moves **2 steps** (Một con trỏ đi **1 bước**, con trỏ kia đi **2 bước**).

```
  Step 0: slow=A, fast=A
          A → B → C → D → E → C (cycle!)
          s              f

  Step 1: slow=B, fast=C
  Step 2: slow=C, fast=E
  Step 3: slow=D, fast=D  ← MEET! Cycle detected!
```

**When to use** (Khi nào dùng):
- Linked List cycle detection (Phát hiện vòng lặp)
- Find middle of linked list (Tìm giữa linked list)
- Find duplicate number (Tìm số trùng lặp)

**Why it works**: If there's a cycle, fast will eventually "lap" slow (Nếu có vòng lặp, fast sẽ "vượt vòng" slow).

---

## 3. Decision Framework (Khung quyết định)

```
Is the array SORTED?
├── YES → Opposite Direction (most likely)
│   ├── "Find pair/triple with sum = target" → Opposite
│   ├── "Palindrome check" → Opposite
│   └── "Container/area maximization" → Opposite
│
├── NO, but can you SORT it?
│   ├── YES, and order doesn't matter → Sort first, then Opposite
│   └── NO, order matters → Same Direction or other technique
│
└── LINKED LIST problem?
    ├── "Cycle detection?" → Fast & Slow
    ├── "Find middle?" → Fast & Slow
    └── "In-place modification?" → Same Direction
```

---

## 4. Two Pointers vs Brute Force (So sánh)

| Aspect | Brute Force | Two Pointers |
|--------|------------|--------------|
| Approach | Try all pairs | Skip intelligently |
| Time | O(n²) | O(n) |
| Space | O(1) | O(1) |
| Requirement | None | Usually sorted or special structure |
| Code complexity | Simple nested loop | Slightly more logic |

> **Key insight (Nhận xét quan trọng)**: Two Pointers is NOT always applicable. It requires a **monotonic property** — moving one pointer must consistently help or hurt the objective (Hai Con Trỏ KHÔNG phải lúc nào cũng dùng được. Cần **tính đơn điệu** — di chuyển 1 con trỏ phải nhất quán giúp ích hoặc bất lợi cho mục tiêu).

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

1. **Why can Two Pointers reduce O(n²) to O(n)?** Explain using the "elimination" concept (Giải thích bằng khái niệm "loại bỏ").

2. **"Find two numbers in an UNSORTED array that sum to target"** — can you use Two Pointers directly? Why or why not? (Tìm 2 số trong mảng CHƯA SẮP XẾP có tổng bằng target — dùng Two Pointers trực tiếp được không? Sao?)

3. **Match each problem to a variant** (Ghép bài với biến thể):

   | Problem | Variant? |
   |---------|----------|
   | Check if string is palindrome | ? |
   | Remove duplicates from sorted array | ? |
   | Detect cycle in linked list | ? |
   | Find pair summing to target in sorted array | ? |

4. **Why does Fast & Slow work for cycle detection?** What would happen if both moved at the same speed? (Tại sao Nhanh & Chậm phát hiện được vòng lặp? Nếu cả 2 cùng tốc độ thì sao?)

---

**Next →** [Chapter 2: Patterns](./02_patterns.md)
