# 📖 Chapter 1: Introduction to Sliding Window (Giới thiệu Cửa Sổ Trượt)

## 🎯 Learning Objectives (Mục tiêu)

After this chapter (Sau chương này):
- Understand the difference between Fixed and Variable windows (Hiểu sự khác biệt Fixed và Variable)
- Know when Sliding Window is applicable (Biết khi nào áp dụng được)
- See how it reduces O(n×k) to O(n) (Thấy cách giảm O(n×k) thành O(n))

---

## 1. What is Sliding Window? (Cửa Sổ Trượt là gì?)

Sliding Window maintains a **window** (a contiguous subarray/substring) that slides across the data. Instead of recomputing from scratch, you **add the new element** entering the window and **remove the old element** leaving it (Duy trì một **cửa sổ** trượt qua dữ liệu. Thay vì tính lại, bạn **thêm phần tử mới** vào và **bỏ phần tử cũ** ra).

### 🧠 The Core Insight

```
Brute Force: Recompute EVERYTHING for each position
  Window at pos 0: sum(arr[0:3]) = arr[0]+arr[1]+arr[2]
  Window at pos 1: sum(arr[1:4]) = arr[1]+arr[2]+arr[3]   ← Recalculates arr[1]+arr[2]!
  → O(n × k) for n positions, k window size

Sliding Window: Only update what CHANGED
  Window at pos 0: sum = arr[0]+arr[1]+arr[2]
  Window at pos 1: sum = sum - arr[0] + arr[3]            ← Remove left, add right!
  → O(n) — one addition and one subtraction per step
```

### Real-life Analogy (Ví dụ thực tế)

Imagine calculating a **7-day rolling average** of temperatures (Tưởng tượng tính **trung bình 7 ngày liên tiếp** nhiệt độ):
- **BF**: For each day, add up the last 7 days → 7 additions per day
- **Sliding Window**: Each new day, add today's temp, subtract the 8-day-ago temp → 2 operations per day!

---

## 2. Two Types of Windows (2 Loại cửa sổ)

### Type 1: Fixed Size Window (Cửa sổ kích thước cố định)

Window size **k** is given. Slide one position at a time (Kích thước cửa sổ **k** cho trước. Trượt 1 vị trí mỗi lần).

```
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2], k = 3

Step 0: [1, 3, 2] 6, -1, 4, 1, 8, 2    sum=6
Step 1:  1 [3, 2, 6] -1, 4, 1, 8, 2    sum=6-1+6=11
Step 2:  1, 3 [2, 6, -1] 4, 1, 8, 2    sum=11-3+(-1)=7
Step 3:  1, 3, 2 [6, -1, 4] 1, 8, 2    sum=7-2+4=9
...
```

**Signal** (Tín hiệu nhận biết):
- "Subarray of size k" (Subarray kích thước k)
- "Maximum/minimum sum of k consecutive elements" (Max/min tổng k phần tử liên tiếp)
- Window size is explicitly given (Kích thước cửa sổ được cho rõ ràng)

---

### Type 2: Variable Size Window (Cửa sổ kích thước biến đổi)

Window size **changes** based on a condition. Expand right, shrink left as needed (Kích thước **thay đổi** theo điều kiện. Mở rộng phải, thu hẹp trái khi cần).

```
s = "ADOBECODEBANC", need to contain "ABC"

Step: Expand right until window contains ALL of "ABC"
      Then shrink left to find MINIMUM window

  [A D O B E C] O D E B A N C    ← contains ABC! shrink left
   A [D O B E C] O D E B A N C   ← missing A! expand right
   ...
   A D O B E C O D E [B A N C]   ← contains ABC! length=4
```

**Signal** (Tín hiệu nhận biết):
- "Longest/shortest substring/subarray satisfying condition" (Dài/ngắn nhất thỏa điều kiện)
- "At most k distinct characters" (Tối đa k ký tự khác nhau)
- "Sum ≥ target" (Tổng ≥ target)
- Window size NOT given — you find the optimal size (Kích thước KHÔNG cho — bạn tìm kích thước tối ưu)

---

## 3. Sliding Window vs Two Pointers (So sánh)

| Aspect | Two Pointers | Sliding Window |
|--------|-------------|---------------|
| Focus | Finding pair/triple | Processing subarray/substring |
| Requirement | Usually sorted | Contiguous elements |
| Window concept | No explicit window | Explicit window with state |
| State tracking | Just indices | Sum, count, frequency map |
| Related | "Find pair with sum" | "Find subarray with property" |

> **Key insight**: Sliding Window is a specialized form of Two Pointers where you maintain additional **window state** (sum, frequency map, count) that gets updated incrementally (Sliding Window là dạng đặc biệt của Two Pointers, duy trì **trạng thái cửa sổ** được cập nhật tăng dần).

---

## 4. Decision Framework (Khung quyết định)

```
Does the problem involve CONTIGUOUS subarray/substring?
│
├── NO → Not Sliding Window
│
├── YES → Is the window size GIVEN (fixed)?
│   ├── YES → Fixed Size Window
│   │        Examples: max sum of k, average of k
│   │
│   └── NO → Variable Size Window
│       ├── "Longest/maximum" → Expand first, shrink when invalid
│       └── "Shortest/minimum" → Expand until valid, then shrink to minimize
```

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

1. **Why is Sliding Window O(n) instead of O(n×k)?** Explain using the "add right, remove left" concept (Giải thích bằng khái niệm "thêm phải, bỏ trái").

2. **"Find maximum sum of 5 consecutive elements"** — Fixed or Variable? Why? (Cố định hay Biến đổi? Tại sao?)

3. **"Find shortest subarray with sum ≥ 100"** — Fixed or Variable? Why?

4. **Can Sliding Window work on non-contiguous elements?** (e.g., subsequences?) Why or why not?

5. **How is Sliding Window different from Prefix Sum** for computing subarray sums?

---

**Next →** [Chapter 2: Patterns](./02_patterns.md)
