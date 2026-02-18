# 📖 Chapter 2: Two Pointers Patterns (Các Pattern Hai Con Trỏ)

## 🎯 Learning Objectives (Mục tiêu)

After this chapter (Sau chương này):
- Master 5 patterns that cover 95%+ of Two Pointer problems (Thành thạo 5 pattern bao phủ 95%+ bài)
- Know the signal/trigger for each pattern (Biết tín hiệu nhận biết từng pattern)
- Write code for each pattern confidently (Viết code tự tin cho từng pattern)

---

## Pattern 1: Pair Sum on Sorted Array (Tìm cặp trên mảng sorted) — O(n)

### What it does

Find two elements that satisfy a condition (usually sum) by narrowing from both ends (Tìm 2 phần tử thỏa điều kiện bằng thu hẹp từ 2 đầu).

### 🔍 Signal

- Array is **sorted** (Mảng **đã sắp xếp**)
- "Find pair with sum = target" (Tìm cặp có tổng = target)
- "Two Sum on sorted array"

### 💡 Why it works (Tại sao hoạt động)

```
Sorted: [1, 3, 5, 7, 9, 11]    target = 12

left=0, right=5: 1 + 11 = 12  ✅ Found!

If sum < target → left++ (tăng tổng bằng cách chọn số lớn hơn)
If sum > target → right-- (giảm tổng bằng cách chọn số nhỏ hơn)
If sum == target → Found! (Tìm thấy!)
```

### 💻 Code

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1      # Need bigger sum (Cần tổng lớn hơn)
        else:
            right -= 1     # Need smaller sum (Cần tổng nhỏ hơn)
    return []
```

### 📌 LeetCode: Two Sum II (LC 167), 3Sum (LC 15)

---

## Pattern 2: Palindrome Check (Kiểm tra đối xứng) — O(n)

### What it does

Check if a string reads the same forwards and backwards (Kiểm tra chuỗi đọc xuôi ngược giống nhau).

### 🔍 Signal

- "Palindrome" (Đối xứng)
- Compare from both ends (So sánh từ 2 đầu)

### 💻 Code

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        # Skip non-alphanumeric (Bỏ qua ký tự đặc biệt)
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

### 📌 LeetCode: Valid Palindrome (LC 125), Palindrome Linked List (LC 234)

---

## Pattern 3: Remove / Filter In-Place (Xóa / Lọc tại chỗ) — O(n)

### What it does

Use slow pointer as "write position", fast pointer as "read position". Only write elements that pass the filter (Slow = "vị trí ghi", fast = "vị trí đọc". Chỉ ghi phần tử qua bộ lọc).

### 🔍 Signal

- "Remove" + "in-place" (Xóa + tại chỗ)
- "Remove duplicates from sorted array" (Xóa trùng lặp từ mảng sorted)
- "Return new length" (Trả về độ dài mới)

### 💻 Code — Remove Duplicates

```python
def remove_duplicates(nums):
    """
    Trace example:
    [1, 1, 2, 2, 3]
     s  f            → 1 == 1? skip
     s     f         → 2 != 1? write! s=1, nums[1]=2
        s     f      → 2 == 2? skip
        s        f   → 3 != 2? write! s=2, nums[2]=3
    Result: [1, 2, 3, _, _], return 3
    """
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

### 💻 Code — Move Zeroes

```python
def move_zeroes(nums):
    """
    Move non-zero elements to front, fill rest with 0.
    (Di chuyển phần tử ≠ 0 ra trước, điền phần còn lại bằng 0.)
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

### 📌 LeetCode: Remove Duplicates (LC 26), Move Zeroes (LC 283), Remove Element (LC 27)

---

## Pattern 4: Container / Area Problems (Bài diện tích) — O(n)

### What it does

Find max area by starting from both ends and greedily moving the shorter side inward (Tìm diện tích max bằng cách bắt đầu từ 2 đầu, tham lam di chuyển cạnh ngắn vào).

### 🔍 Signal

- "Maximum area", "maximum water", "container" (Diện tích max, nước max)
- Two boundaries determining a region (2 biên xác định vùng)

### 💡 Why move the shorter side?

```
Height: [1, 8, 6, 2, 5, 4, 8, 3, 7]
         L                          R

Area = min(height[L], height[R]) × (R - L)
     = min(1, 7) × 8 = 8

If we move the TALLER side (R), area can only stay same or decrease.
(Nếu di chuyển cạnh CAO HƠN, diện tích chỉ giữ nguyên hoặc giảm.)

If we move the SHORTER side (L), area MIGHT increase.
(Nếu di chuyển cạnh THẤP HƠN, diện tích CÓ THỂ tăng.)

→ Always move the shorter pointer! (Luôn di chuyển con trỏ ngắn hơn!)
```

### 💻 Code

```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)
        
        if height[left] < height[right]:
            left += 1       # Move shorter side
        else:
            right -= 1
    
    return max_water
```

### 📌 LeetCode: Container With Most Water (LC 11), Trapping Rain Water (LC 42)

---

## Pattern 5: Subsequence Check (Kiểm tra chuỗi con) — O(n + m)

### What it does

Check if string `s` is a subsequence of string `t` by advancing two pointers (Kiểm tra chuỗi `s` có phải chuỗi con của `t`).

### 🔍 Signal

- "Is subsequence" (Là chuỗi con?)
- "Can we form string X from string Y by deleting characters?" (Có thể tạo X từ Y bằng cách xóa ký tự?)

### 💻 Code

```python
def is_subsequence(s, t):
    """
    s = "ace", t = "abcde"
    
    s_ptr:  a  →  c  →  e  → done!
    t_ptr:  a  b  c  d  e
            ↑     ↑     ↑
            match match match → True!
    """
    s_ptr, t_ptr = 0, 0
    while s_ptr < len(s) and t_ptr < len(t):
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1     # Match! advance both
        t_ptr += 1         # Always advance t
    return s_ptr == len(s)  # All of s matched?
```

### 📌 LeetCode: Is Subsequence (LC 392), Longest Word in Dictionary (LC 524)

---

## 📊 Quick Reference Table (Bảng tra cứu nhanh)

| Pattern | Direction | Signal Keywords | Time |
|---------|-----------|----------------|------|
| Pair Sum | ← → | "sorted", "sum", "pair" | O(n) |
| Palindrome | ← → | "palindrome", "same forwards/backwards" | O(n) |
| Remove/Filter | → → | "in-place", "remove", "duplicates" | O(n) |
| Container/Area | ← → | "max area", "container", "water" | O(n) |
| Subsequence | → → | "subsequence", "deletions" | O(n+m) |

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

1. **Why does the Pair Sum pattern only work on sorted arrays?** What breaks if the array is unsorted? (Tại sao chỉ hoạt động trên mảng sorted?)

2. **In Remove Duplicates, why does `slow` start at 0, not 1?** (Tại sao `slow` bắt đầu từ 0, không phải 1?)

3. **Draw the Container With Most Water process for `height = [3, 1, 4, 1, 5]`** — show each step (Vẽ quá trình cho mỗi bước).

4. **"Find three numbers that sum to zero"** — which pattern is the base? How do you extend it from 2Sum to 3Sum? (Pattern nào là cơ sở? Mở rộng từ 2Sum sang 3Sum thế nào?)

5. **Can you solve "Valid Palindrome" without Two Pointers?** What would the complexity be? (Giải mà không dùng Two Pointers thì Big-O ra sao?)

---

**← Previous:** [Chapter 1: Introduction](./01_introduction.md)
**Next →** [Chapter 3: Complexity](./03_complexity.md)
