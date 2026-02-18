# 📖 Chapter 2: Brute Force Variants (Các biến thể Vét Cạn)

## 🎯 Learning Objectives (Mục tiêu)

After this chapter (Sau chương này):
- Identify 5 BF variants by their patterns (Nhận diện 5 biến thể BF qua đặc điểm)
- Write code for each variant (Viết code cho từng biến thể)
- Know the "signal" — how to recognize which variant fits a problem (Biết "tín hiệu" nhận biết bài thuộc biến thể nào)

---

## Variant 1: Linear Search (Tìm kiếm tuyến tính) — O(n)

### What it does (Cách hoạt động)

Scan every element one by one, check if it satisfies the condition (Duyệt từng phần tử, kiểm tra điều kiện).

```
Input:  [3, 7, 2, 9, 5],  target = 9
         ↓
Step 1:  3 == 9? No  → move on (Tiếp)
Step 2:  7 == 9? No  → move on
Step 3:  2 == 9? No  → move on
Step 4:  9 == 9? YES → return index 3 ✅
```

### 🔍 Signal — When to use (Tín hiệu nhận biết)

- "Find an element that satisfies X in an **unsorted** collection"
  (Tìm phần tử thỏa X trong tập **không sắp xếp**)
- "Check if any element matches a condition"
  (Kiểm tra xem có phần tử nào khớp điều kiện không)

### 💻 Code

```python
def linear_search(arr, target):
    """
    Search for target in arr by checking every element.
    (Tìm target trong arr bằng cách kiểm tra từng phần tử.)
    
    Time: O(n) | Space: O(1)
    """
    for i in range(len(arr)):          # Try every index (Thử từng index)
        if arr[i] == target:           # Check condition (Kiểm tra điều kiện)
            return i                   # Found! Return index (Tìm thấy!)
    return -1                          # Not found (Không tìm thấy)
```

### ⚡ When does this become slow? (Khi nào chậm?)

Linear search is O(n) — it's only slow when:
- You call it **many times** on the same data (→ use a Hash Set instead)
- The data is **sorted** (→ use Binary Search for O(log n))

---

## Variant 2: Nested Loops (Vòng lặp lồng nhau) — O(n²), O(n³)

### What it does (Cách hoạt động)

Use 2 or 3 nested loops to try **every pair** or **every triple** of elements (Dùng 2-3 vòng lặp lồng nhau thử **mọi cặp** hoặc **mọi bộ ba**).

**Example: Two Sum — find 2 numbers that add up to target (Tìm 2 số cộng bằng target)**

```
Input:  [2, 7, 11, 15],  target = 9

Try ALL pairs (Thử mọi cặp):
  i=0, j=1:  2 + 7  = 9  ✅ Found!
  i=0, j=2:  2 + 11 = 13 ✗
  i=0, j=3:  2 + 15 = 17 ✗
  i=1, j=2:  7 + 11 = 18 ✗
  i=1, j=3:  7 + 15 = 22 ✗
  i=2, j=3:  11+ 15 = 26 ✗
```

Visualize as a **matrix** (Ma trận trực quan):

```
     j=0   j=1   j=2   j=3
i=0   —    ✅9    13    17
i=1   —     —    18    22
i=2   —     —     —    26
i=3   —     —     —     —
```

We only check the **upper triangle** because pair (i,j) = pair (j,i) (Chỉ kiểm tra **tam giác trên** vì cặp (i,j) = cặp (j,i)).

### 🔍 Signal — When to use (Tín hiệu nhận biết)

- "Find **two elements** that satisfy a condition" (Tìm **hai phần tử** thỏa điều kiện)
- "Compare **every pair**" (So sánh **mọi cặp**)
- "For each element, check against all others" (Với mỗi phần tử, so với tất cả phần tử khác)
- Three Sum → 3 nested loops (Bộ ba → 3 vòng lặp lồng nhau)

### 💻 Code — Two Sum BF

```python
def two_sum_brute(nums, target):
    """
    Find two indices whose values add up to target.
    (Tìm 2 index mà giá trị cộng lại bằng target.)
    
    Time: O(n²) | Space: O(1)
    """
    n = len(nums)
    for i in range(n):                     # First element (Phần tử thứ nhất)
        for j in range(i + 1, n):          # Second element (Phần tử thứ hai)
            if nums[i] + nums[j] == target:  # Check sum (Kiểm tra tổng)
                return [i, j]
    return []                              # No pair found (Không tìm thấy)
```

### 💻 Code — Three Sum BF

```python
def three_sum_brute(nums, target):
    """
    Find three indices whose values add up to target.
    (Tìm 3 index mà giá trị cộng lại bằng target.)
    
    Time: O(n³) | Space: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    return [i, j, k]
    return []
```

### ⚡ How to optimize? (Tối ưu bằng cách nào?)

- **Two Sum O(n²) → O(n)**: Use a **Hash Map** to look up the complement in O(1)
  (Dùng Hash Map tra complement trong O(1))
- **Three Sum O(n³) → O(n²)**: Sort first, then use **Two Pointers** for inner loop
  (Sắp xếp trước, dùng Two Pointers cho vòng trong)

---

## Variant 3: Permutation Search (Tìm kiếm hoán vị) — O(n!)

### What it does (Cách hoạt động)

Generate **every possible ordering** (permutation) and check each one (Sinh **mọi thứ tự** (hoán vị) và kiểm tra từng cái).

**Example: All permutations of [1, 2, 3]**

```
Decision Tree (Cây quyết định):

                    []
            /        |        \
         [1]        [2]       [3]
        /   \      /   \     /   \
     [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
       |     |     |     |     |     |
   [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]
   
   Total: 3! = 6 permutations (6 hoán vị)
```

### 🔍 Signal — When to use (Tín hiệu nhận biết)

- "Find the **best ordering/arrangement**" (Tìm **thứ tự/sắp xếp tốt nhất**)
- "Try **all possible orderings**" (Thử **mọi thứ tự có thể**)
- Constraint: **n ≤ 10-12** (Otherwise n! explodes)
- Keywords: "permutation", "arrangement", "ordering", "schedule"

### 💻 Code — Using itertools (Dùng thư viện)

```python
from itertools import permutations

def find_best_permutation(nums):
    """
    Try every permutation and find the one with maximum property.
    (Thử mọi hoán vị, tìm cái có thuộc tính lớn nhất.)
    
    Time: O(n! × n) | Space: O(n)
    """
    best = None
    for perm in permutations(nums):     # Generate all n! orderings
        score = evaluate(perm)           # Check this ordering
        if best is None or score > best:
            best = score
    return best
```

### 💻 Code — Manual recursion (Đệ quy thủ công)

```python
def generate_permutations(nums):
    """
    Generate all permutations using recursion + used array.
    (Sinh mọi hoán vị bằng đệ quy + mảng đã dùng.)
    
    Time: O(n!) | Space: O(n)
    """
    result = []
    used = [False] * len(nums)
    
    def backtrack(path):
        if len(path) == len(nums):       # Base case: full permutation
            result.append(path[:])       # Save a copy (Lưu bản sao)
            return
        
        for i in range(len(nums)):
            if used[i]:                  # Skip used elements (Bỏ qua đã dùng)
                continue
            used[i] = True               # Mark as used (Đánh dấu đã dùng)
            path.append(nums[i])         # Choose (Chọn)
            backtrack(path)              # Explore (Khám phá)
            path.pop()                   # Un-choose (Bỏ chọn)
            used[i] = False              # Unmark (Bỏ đánh dấu)
    
    backtrack([])
    return result
```

### ⚡ Growth rate of n! (Tốc độ tăng của n!)

| n | n! | Feasible? (Khả thi?) |
|---|-----|---------------------|
| 5 | 120 | ✅ Instant (Tức thì) |
| 8 | 40,320 | ✅ Fast (Nhanh) |
| 10 | 3,628,800 | ✅ OK (~0.04s) |
| 12 | 479,001,600 | ⚠️ ~5s — borderline (Sát giới hạn) |
| 15 | 1,307,674,368,000 | ❌ TLE — impossible |

### ⚡ How to optimize? (Tối ưu bằng cách nào?)

Use **Backtracking with pruning** — cut branches of the decision tree that can't lead to a valid solution (Dùng **quay lui với cắt tỉa** — cắt nhánh cây quyết định không thể dẫn tới lời giải hợp lệ).

---

## Variant 4: Subset / Combination Search (Tìm kiếm tập con) — O(2ⁿ)

### What it does (Cách hoạt động)

For each element, decide: **include it or exclude it** → generates all 2ⁿ subsets (Với mỗi phần tử, quyết định: **lấy hay không lấy** → sinh tất cả 2ⁿ tập con).

**Example: All subsets of [a, b, c]**

```
Bitmask Table (Bảng mặt nạ bit):

 Mask  |  c  b  a  |  Subset
-------|-----------|----------
  000  |  0  0  0  |  {}          (empty set - tập rỗng)
  001  |  0  0  1  |  {a}
  010  |  0  1  0  |  {b}
  011  |  0  1  1  |  {a, b}
  100  |  1  0  0  |  {c}
  101  |  1  0  1  |  {a, c}
  110  |  1  1  0  |  {b, c}
  111  |  1  1  1  |  {a, b, c}

Total: 2³ = 8 subsets (8 tập con)
```

For each bit position: `1` = include (lấy), `0` = exclude (bỏ).

### 🔍 Signal — When to use (Tín hiệu nhận biết)

- "Find a **subset** that satisfies X" (Tìm **tập con** thỏa X)
- "**Include or exclude** each element" (Mỗi phần tử **lấy hoặc không**)
- "Find all **combinations**" (Tìm mọi **tổ hợp**)
- Constraint: **n ≤ 20-25** (Otherwise 2ⁿ explodes)
- Keywords: "subset", "combination", "knapsack", "select"

### 💻 Code — Bitmask approach

```python
def generate_subsets_bitmask(nums):
    """
    Generate all subsets using bitmask enumeration.
    (Sinh mọi tập con bằng duyệt mặt nạ bit.)
    
    Time: O(2ⁿ × n) | Space: O(2ⁿ × n) for storing results
    """
    n = len(nums)
    result = []
    
    for mask in range(1 << n):           # mask from 0 to 2ⁿ-1
        subset = []
        for i in range(n):
            if mask & (1 << i):          # Bit i is set → include nums[i]
                subset.append(nums[i])   # (Bit i = 1 → lấy nums[i])
        result.append(subset)
    
    return result
```

### 💻 Code — Recursive approach

```python
def generate_subsets_recursive(nums):
    """
    Generate all subsets using recursion (include/exclude each element).
    (Sinh mọi tập con bằng đệ quy — lấy/bỏ từng phần tử.)
    
    Time: O(2ⁿ) | Space: O(n) stack depth
    """
    result = []
    
    def backtrack(index, current):
        if index == len(nums):           # Processed all elements (Đã xử lý hết)
            result.append(current[:])    # Save a copy (Lưu bản sao)
            return
        
        # Option 1: EXCLUDE nums[index] (Không lấy)
        backtrack(index + 1, current)
        
        # Option 2: INCLUDE nums[index] (Lấy)
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()                    # Backtrack (Quay lui)
    
    backtrack(0, [])
    return result
```

### ⚡ When does this become slow? (Khi nào chậm?)

| n | 2ⁿ | Feasible? |
|---|------|----------|
| 10 | 1,024 | ✅ Instant |
| 20 | 1,048,576 | ✅ ~0.01s |
| 25 | 33,554,432 | ⚠️ ~0.3s |
| 30 | 1,073,741,824 | ❌ TLE |

### ⚡ How to optimize?

- **Subset Sum** → use **Dynamic Programming** (DP) in O(n × target)
- **Knapsack** → DP O(n × W)
- **Combination with constraints** → **Backtracking** with pruning (prune when sum > target)

---

## Variant 5: Brute Force over Range / Subarray (Duyệt mọi khoảng/subarray) — O(n²) or O(n·k)

### What it does (Cách hoạt động)

Try every possible subarray (contiguous section), compute something for each (Thử mọi subarray (đoạn liên tiếp), tính toán cho từng cái).

**Example: Find max sum subarray of length k=3 in [1, 3, 2, 5, 4]**

```
All windows of size k=3 (Mọi cửa sổ kích thước k=3):

Window 1: [1, 3, 2]     → sum = 6
Window 2: [3, 2, 5]     → sum = 10
Window 3: [2, 5, 4]     → sum = 11  ← MAX ✅

Total windows checked: n - k + 1 = 3
Each window: sum k elements
→ Total: O(n × k)
```

### 🔍 Signal — When to use (Tín hiệu nhận biết)

- "Find a **subarray/substring** that satisfies X" (Tìm **subarray/substring** thỏa X)
- "Maximum/minimum of a **contiguous** section" (Max/min của **đoạn liên tiếp**)
- Keywords: "subarray", "substring", "contiguous", "window"

### 💻 Code

```python
def max_sum_subarray_brute(nums, k):
    """
    Find the maximum sum of any subarray of length k.
    (Tìm tổng lớn nhất của subarray length k.)
    
    Time: O(n × k) | Space: O(1)
    """
    n = len(nums)
    max_sum = float('-inf')
    
    for i in range(n - k + 1):          # Start of each window (Đầu mỗi cửa sổ)
        window_sum = 0
        for j in range(i, i + k):       # Sum k elements (Cộng k phần tử)
            window_sum += nums[j]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### 💻 Code — All subarrays (Mọi subarray với mọi kích thước)

```python
def all_subarrays(nums):
    """
    Generate all contiguous subarrays.
    (Sinh mọi subarray liên tiếp.)
    
    Time: O(n²) | Space: O(1) per subarray
    """
    n = len(nums)
    for i in range(n):                   # Start index (Index bắt đầu)
        for j in range(i + 1, n + 1):    # End index exclusive (Index kết thúc)
            print(nums[i:j])             # Subarray from i to j-1
```

### ⚡ How to optimize?

- **Fixed window size** → **Sliding Window**: subtract left, add right in O(1)
  (Cửa sổ cố định → Trượt: trừ trái, cộng phải trong O(1))
- **Variable window** → Sliding Window with expand/shrink
- **Subarray sum** → **Prefix Sum** in O(1) per query

---

## 📊 Quick Reference Table (Bảng tra cứu nhanh)

| Variant | Time | Signal Keywords | Max n | Optimize with |
|---------|------|----------------|-------|--------------|
| Linear Search | O(n) | "find", "any", "unsorted" | 10⁸ | Hash Set, Binary Search |
| Nested Loops | O(n²) | "pair", "two elements" | 10⁴ | Hash Map, Two Pointers |
| Permutations | O(n!) | "ordering", "arrangement" | 10-12 | Backtracking + pruning |
| Subsets | O(2ⁿ) | "subset", "include/exclude" | 20-25 | DP, Backtracking |
| Subarrays | O(n²) | "subarray", "contiguous" | 10⁴ | Sliding Window, Prefix Sum |

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

1. **"Find two numbers that add up to target"** — which variant? (Biến thể nào?)

2. **You have n = 8 items. How many subsets? How many permutations?** Calculate both (Tính cả hai: tập con? hoán vị?).

3. **Draw (on paper) the decision tree for permutations of [A, B]** (Vẽ cây quyết định cho hoán vị [A, B]).

4. **A problem says: "Find a contiguous subarray with maximum sum."** Which variant fits? What's the BF complexity? How would you optimize? (Biến thể nào? Độ phức tạp BF? Tối ưu bằng cách nào?)

5. **Match each problem to a variant** (Ghép bài với biến thể):

   | Problem | Variant? |
   |---------|----------|
   | Find if array contains target | ? |
   | Find 3 numbers summing to 0 | ? |
   | Find best route visiting all cities | ? |
   | Find subset summing to S | ? |

---

**← Previous:** [Chapter 1: Introduction](./01_introduction.md)
**Next →** [Chapter 3: Complexity Analysis](./03_complexity.md)
