# 📖 Chapter 3: Complexity Analysis (Phân tích độ phức tạp)

## 🎯 Learning Objectives (Mục tiêu)

After this chapter (Sau chương này):
- Calculate Big-O for any BF variant (Tính Big-O cho bất kỳ biến thể BF nào)
- Know exact limits: what n is feasible for each variant (Biết chính xác n tối đa cho từng biến thể)
- Read LeetCode constraints and decide if BF is possible (Đọc ràng buộc và quyết định BF có khả thi không)

---

## 1. The Master Table (Bảng tổng hợp)

| Variant (Biến thể) | Time Complexity | Space Complexity | Max n for ≤ 1s | Example Use Case |
|-------------------|-----------------|-----------------|-----------------|-----------------|
| Linear Search | O(n) | O(1) | ~10⁸ | Find element in array |
| Nested 2 Loops | O(n²) | O(1) | ~10⁴ | Two Sum BF |
| Nested 3 Loops | O(n³) | O(1) | ~500 | Three Sum BF |
| Subsets (2ⁿ) | O(2ⁿ × n) | O(n) | n ≤ 20-25 | Subset Sum |
| Permutations (n!) | O(n! × n) | O(n) | n ≤ 10-12 | TSP, scheduling |
| Subarrays | O(n² × k) | O(1) | ~10⁴ | Max sum subarray |

> **Why × n?** Because for each subset/permutation, we often need O(n) to process it — e.g., summing elements, checking validity.
> (Tại sao × n? Vì với mỗi tập con/hoán vị, ta thường cần O(n) để xử lý — ví dụ: tính tổng, kiểm tra.)

---

## 2. The Rule of Thumb: 10⁸ Operations per Second (Quy tắc ngón tay cái)

### The Core Idea (Ý tưởng chính)

Modern computers can perform approximately **10⁸ simple operations per second** (Máy tính hiện đại thực hiện ~10⁸ phép toán đơn giản mỗi giây).

LeetCode time limit is usually **1-2 seconds** (Giới hạn thời gian LeetCode thường là 1-2 giây).

So, your algorithm must use **≤ 10⁸ operations** to pass (Giải thuật phải dùng **≤ 10⁸ phép toán** để pass).

### How to Apply (Cách áp dụng)

```
Step 1: Read n from problem constraints
        (Đọc n từ ràng buộc bài toán)
        
Step 2: Calculate total operations = f(n) based on your approach
        (Tính tổng phép toán = f(n) theo cách tiếp cận)
        
Step 3: If f(n) ≤ 10⁸ → OK ✅
        If f(n) > 10⁸  → TLE ❌, need optimization
```

### Worked Examples (Ví dụ tính toán)

**Example 1: Two Sum, n = 10⁴**
```
Approach: Two nested loops → O(n²)
Operations: (10⁴)² = 10⁸  → ⚠️ Borderline, might pass
Verdict: Try it, but have O(n) Hash Map ready
```

**Example 2: Subset Sum, n = 20**
```
Approach: Try all subsets → O(2ⁿ × n)
Operations: 2²⁰ × 20 = 1,048,576 × 20 ≈ 2 × 10⁷  → ✅ Fast!
Verdict: BF works perfectly
```

**Example 3: Permutation, n = 15**
```
Approach: Try all permutations → O(n! × n)
Operations: 15! × 15 ≈ 1.3 × 10¹² × 15 ≈ 2 × 10¹³  → ❌ Way too slow!
Verdict: Need backtracking + pruning or DP
```

**Example 4: Three Sum, n = 3000**
```
Approach: Three nested loops → O(n³)
Operations: 3000³ = 2.7 × 10¹⁰  → ❌ TLE
Better: Sort + Two Pointers → O(n²) = 9 × 10⁶ → ✅
```

---

## 3. How to Calculate Big-O Step-by-Step (Cách tính Big-O từng bước)

### Method 1: Count Nested Loops (Đếm vòng lặp lồng nhau)

```python
# Each loop multiplies by n (Mỗi vòng lặp nhân thêm n)

for i in range(n):           # ← 1 loop = O(n)
    ...

for i in range(n):
    for j in range(n):       # ← 2 loops = O(n²)
        ...

for i in range(n):
    for j in range(n):
        for k in range(n):   # ← 3 loops = O(n³)
            ...
```

> **Important (Quan trọng)**: If inner loop depends on i, it's still O(n²) on average:
> ```python
> for i in range(n):
>     for j in range(i+1, n):   # j runs n-i-1 times
>         ...
> # Total: n(n-1)/2 = O(n²)
> ```

### Method 2: Count Recursive Calls (Đếm lệnh gọi đệ quy)

Draw the **recursion tree** and count total nodes (Vẽ **cây đệ quy** và đếm tổng node):

```
Subsets: 2 branches per node, depth n
         → Total nodes = 2ⁿ → O(2ⁿ)

                    root
                   /    \
              include   exclude     ← 2 choices per element
              /    \    /    \
            ...   ...  ...   ...
            
Permutations: n branches at level 0, n-1 at level 1, ...
              → Total leaves = n! → O(n!)
              
                      root
                   /   |   \
                  a    b    c         ← n choices
                / \   / \   / \
               b   c a   c a   b     ← n-1 choices
               |   | |   | |   |
               c   b c   a b   a     ← n-2 choices
```

### Method 3: Check Inner Work (Kiểm tra công việc bên trong)

Don't forget work **inside** loops (Đừng quên công việc **bên trong** vòng lặp):

```python
for i in range(n):              # O(n)
    for j in range(i+1, n):     # O(n)
        if sum(nums[i:j]) > k:  # sum() is O(n) here! ← Easy to miss!
            ...
# Total: O(n²) × O(n) = O(n³), NOT O(n²)!
```

---

## 4. Growth Rate Comparison (So sánh tốc độ tăng)

### The Numbers (Các con số)

| n | O(n) | O(n²) | O(n³) | O(2ⁿ) | O(n!) |
|---|------|-------|-------|--------|-------|
| 5 | 5 | 25 | 125 | 32 | 120 |
| 10 | 10 | 100 | 1,000 | 1,024 | 3,628,800 |
| 15 | 15 | 225 | 3,375 | 32,768 | **1.3 × 10¹²** |
| 20 | 20 | 400 | 8,000 | **1,048,576** | **2.4 × 10¹⁸** |
| 100 | 100 | 10,000 | **10⁶** | **1.3 × 10³⁰** | — |
| 10⁴ | 10⁴ | **10⁸** | **10¹²** | — | — |
| 10⁵ | 10⁵ | **10¹⁰** | — | — | — |

**Bold** = exceeds 10⁸ limit (Vượt giới hạn 10⁸)

### Key Takeaways (Điểm chính)

```
O(n)    → n can be up to 10⁸    (huge — rất lớn)
O(n²)   → n can be up to 10⁴    (medium — trung bình)
O(n³)   → n can be up to ~500   (small — nhỏ)
O(2ⁿ)   → n can be up to ~25    (tiny — rất nhỏ)
O(n!)   → n can be up to ~12    (minimal — tối thiểu)
```

---

## 5. BF vs Optimized — Real Comparisons (So sánh BF và Tối ưu)

| Problem (Bài toán) | BF Approach | BF Time | Optimized Approach | Opt Time | Technique (Kỹ thuật) |
|--------------------|-------------|---------|-------------------|----------|---------------------|
| Two Sum | 2 nested loops | O(n²) | Hash Map lookup | **O(n)** | Hash Map |
| Max Subarray Sum (k) | Recompute each window | O(n·k) | Add right, subtract left | **O(n)** | Sliding Window |
| Search in Sorted Array | Scan every element | O(n) | Divide in half | **O(log n)** | Binary Search |
| Subset Sum | Try all 2ⁿ subsets | O(2ⁿ) | DP table | **O(n·S)** | Dynamic Programming |
| Best Ordering | Try all n! permutations | O(n!) | Prune impossible branches | **O(varies)** | Backtracking |
| Longest Substring No Repeat | Check each substring | O(n³) | Expand/shrink window | **O(n)** | Sliding Window |

### The Pattern (Quy luật)

```
BF: Try ALL possibilities      → Correct but slow
                                   (Đúng nhưng chậm)

Optimized: Skip UNNECESSARY     → Correct AND fast
possibilities using insight        (Đúng VÀ nhanh)
```

Every optimization technique is about **recognizing what you DON'T need to check** (Mọi kỹ thuật tối ưu đều là về **nhận ra cái bạn KHÔNG CẦN kiểm tra**).

---

## 6. Decision Framework: Should I Use BF? (Khung quyết định: Có nên dùng BF?)

```
Read constraints → What is n?
         │
         ├── n ≤ 12        → O(n!) is feasible ✅ → Permutation BF
         │
         ├── n ≤ 20-25     → O(2ⁿ) is feasible ✅ → Subset BF
         │
         ├── n ≤ 500       → O(n³) is feasible ✅ → Triple loop BF
         │
         ├── n ≤ 10⁴       → O(n²) is feasible ✅ → Double loop BF
         │
         ├── n ≤ 10⁵       → Need O(n log n) ⚠️  → Optimize!
         │
         └── n ≤ 10⁶+      → Need O(n) or O(log n) → Definitely optimize!
```

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

1. **A problem says `n ≤ 10⁵`. Can you use O(n²)?** Calculate the operations and explain why or why not (Tính số phép toán và giải thích).

2. **What is the Big-O of this code?** (Big-O của code này là gì?)
   ```python
   for i in range(n):
       for j in range(i, n):
           total = sum(nums[i:j+1])
   ```
   *Hint: Don't forget the `sum()` call inside!*

3. **If n = 20, which is faster: O(2ⁿ) or O(n³)?** Calculate both (Tính cả hai).
   - 2²⁰ = ?
   - 20³ = ?

4. **A problem has n ≤ 8. What's the maximum complexity you can afford?** (n ≤ 8, độ phức tạp tối đa chấp nhận được?)

5. **Fill in the table** (Điền bảng):
   
   | n | Your BF approach | Operations | Pass? |
   |---|-----------------|------------|-------|
   | 100 | O(n²) | ? | ? |
   | 1000 | O(n³) | ? | ? |
   | 15 | O(2ⁿ) | ? | ? |
   | 12 | O(n!) | ? | ? |

---

**← Previous:** [Chapter 2: Variants](./02_variants.md)
**Next →** [Chapter 4: Python Templates](./04_python_templates.md)
