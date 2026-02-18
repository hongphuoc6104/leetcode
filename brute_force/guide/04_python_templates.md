# 📖 Chapter 4: Python Templates (Templates Python sẵn dùng)

## 🎯 How to Use This File (Cách sử dụng)

This file contains **ready-to-use templates** for each BF variant. When you encounter a new problem (Khi gặp bài mới):

1. **Identify the variant** using signals from Chapter 2 (Nhận diện biến thể bằng tín hiệu từ Chương 2)
2. **Copy the template** below (Copy template bên dưới)
3. **Fill in the blanks** — marked with `# TODO` comments (Điền vào chỗ trống)
4. **Test** with example inputs (Kiểm tra với input mẫu)

---

## ✅ Pre-Coding Checklist (Danh sách kiểm tra trước khi code)

Before writing ANY BF code, answer these 4 questions (Trước khi viết code BF, trả lời 4 câu hỏi):

```
□ 1. What is the SEARCH SPACE?
     (Không gian tìm kiếm là gì?)
     → All elements? All pairs? All subsets? All permutations?

□ 2. How do I ENUMERATE all candidates?
     (Liệt kê ứng viên bằng cách nào?)
     → Single loop? Nested loops? Recursion? Bitmask?

□ 3. What is the CHECK/VALIDATION step?
     (Bước kiểm tra/xác nhận là gì?)
     → Sum equals target? Condition is met? Is valid?

□ 4. What is n? Is BF feasible?
     (n bằng bao nhiêu? BF có khả thi không?)
     → Check with the table from Chapter 3
```

---

## Template 1: Linear Scan — O(n)

**When to use (Khi nào dùng)**: Find one element matching a condition in an unsorted collection (Tìm 1 phần tử thỏa điều kiện trong tập không sắp xếp).

```python
def linear_scan(collection):
    """
    Scan every element and check condition.
    (Duyệt mọi phần tử và kiểm tra điều kiện.)
    
    Time: O(n) | Space: O(1)
    """
    for item in collection:
        if condition(item):          # TODO: Define your condition
            return item              # Found! (Tìm thấy!)
    return None                      # Not found (Không tìm thấy)


# --- Variant: Find ALL matching elements --- #
def linear_scan_all(collection):
    """Find all elements matching condition. (Tìm mọi phần tử thỏa.)"""
    results = []
    for item in collection:
        if condition(item):          # TODO: Define your condition
            results.append(item)
    return results
```

---

## Template 2: Pair/Triple Check (Nested Loops) — O(n²) / O(n³)

**When to use**: Find pair(s) or triple(s) satisfying a condition (Tìm cặp/bộ ba thỏa điều kiện).

```python
def find_pair(nums, target):
    """
    Try every pair (i, j) where i < j.
    (Thử mọi cặp (i, j) với i < j.)
    
    Time: O(n²) | Space: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):            # j starts at i+1 to avoid duplicates
            if nums[i] + nums[j] == target:  # TODO: Your condition here
                return [i, j]
    return []


def find_triple(nums, target):
    """
    Try every triple (i, j, k) where i < j < k.
    (Thử mọi bộ ba (i, j, k) với i < j < k.)
    
    Time: O(n³) | Space: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:  # TODO
                    return [i, j, k]
    return []
```

---

## Template 3: Generate All Subsets (Bitmask) — O(2ⁿ)

**When to use**: Try every subset (include/exclude each element) (Thử mọi tập con — lấy/bỏ từng phần tử).

```python
def subset_search(nums):
    """
    Generate all 2ⁿ subsets using bitmask.
    (Sinh mọi 2ⁿ tập con bằng mặt nạ bit.)
    
    Time: O(2ⁿ × n) | Space: O(n)
    """
    n = len(nums)
    best = None                              # TODO: Track your answer
    
    for mask in range(1 << n):               # mask = 0 to 2ⁿ - 1
        # Build the current subset (Xây dựng tập con hiện tại)
        subset = []
        for i in range(n):
            if mask & (1 << i):              # Bit i is set → include nums[i]
                subset.append(nums[i])
        
        # Check / evaluate this subset (Kiểm tra tập con này)
        if is_valid(subset):                 # TODO: Your validation
            best = update_best(best, subset) # TODO: Your update logic
    
    return best


# --- Recursive variant --- #
def subset_search_recursive(nums):
    """Generate all subsets using backtracking. (Sinh tập con bằng quay lui.)"""
    result = []
    
    def backtrack(index, current):
        if index == len(nums):
            if is_valid(current):            # TODO: Your validation
                result.append(current[:])
            return
        
        # Choice 1: Exclude nums[index] (Không lấy)
        backtrack(index + 1, current)
        
        # Choice 2: Include nums[index] (Lấy)
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()                        # Backtrack (Quay lui)
    
    backtrack(0, [])
    return result
```

---

## Template 4: Generate All Permutations — O(n!)

**When to use**: Try every ordering/arrangement (Thử mọi thứ tự/sắp xếp).

```python
def permutation_search(nums):
    """
    Try every permutation of nums.
    (Thử mọi hoán vị của nums.)
    
    Time: O(n! × n) | Space: O(n)
    """
    best = None
    used = [False] * len(nums)
    
    def backtrack(path):
        nonlocal best
        
        if len(path) == len(nums):           # Complete permutation
            score = evaluate(path)           # TODO: Your evaluation
            best = max(best, score) if best else score
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue                     # Skip used (Bỏ qua đã dùng)
            
            used[i] = True
            path.append(nums[i])             # Choose (Chọn)
            backtrack(path)                  # Explore (Khám phá)
            path.pop()                       # Un-choose (Bỏ chọn)
            used[i] = False
    
    backtrack([])
    return best


# --- Quick version using itertools --- #
from itertools import permutations

def permutation_search_quick(nums):
    """Using itertools for convenience. (Dùng itertools cho tiện.)"""
    best = None
    for perm in permutations(nums):
        score = evaluate(perm)               # TODO: Your evaluation
        best = max(best, score) if best else score
    return best
```

---

## Template 5: Enumerate All Subarrays — O(n²) or O(n³)

**When to use**: Try every contiguous subarray/substring (Thử mọi subarray/substring liên tiếp).

```python
def subarray_search(nums):
    """
    Try every subarray [i..j] (inclusive).
    (Thử mọi subarray [i..j].)
    
    Time: O(n²) if check is O(1), O(n³) if check is O(n)
    Space: O(1)
    """
    n = len(nums)
    best = None
    
    for i in range(n):                       # Start index (Index bắt đầu)
        for j in range(i, n):                # End index (Index kết thúc)
            subarray = nums[i:j+1]           # Current subarray
            
            if is_valid(subarray):           # TODO: Your validation
                best = update(best, subarray)  # TODO: Your update
    
    return best


# --- Optimized: Maintain running sum --- #
def subarray_search_with_sum(nums, target):
    """
    Find subarray with sum equal to target.
    Maintains running sum to avoid recomputing.
    (Duy trì tổng chạy để tránh tính lại.)
    
    Time: O(n²) | Space: O(1)
    """
    n = len(nums)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]           # Add one element at a time
            if current_sum == target:        # (Cộng từng phần tử)
                return nums[i:j+1]
    return None
```

---

## 🔧 Utility: BF vs Optimized Comparison (So sánh BF và Tối ưu)

Use this pattern to verify your optimized solution against BF (Dùng mẫu này để xác minh lời giải tối ưu bằng BF):

```python
import random

def stress_test(brute_force_fn, optimized_fn, num_tests=10000):
    """
    Compare BF and optimized solutions on random inputs.
    (So sánh BF và tối ưu trên input ngẫu nhiên.)
    """
    for test_num in range(num_tests):
        # Generate random input (Tạo input ngẫu nhiên)
        n = random.randint(1, 20)            # Small n for BF
        nums = [random.randint(-100, 100) for _ in range(n)]
        
        # Run both (Chạy cả hai)
        bf_result = brute_force_fn(nums)
        opt_result = optimized_fn(nums)
        
        # Compare (So sánh)
        if bf_result != opt_result:
            print(f"❌ MISMATCH on test {test_num}!")
            print(f"   Input: {nums}")
            print(f"   BF result:  {bf_result}")
            print(f"   Opt result: {opt_result}")
            return False
    
    print(f"✅ All {num_tests} tests passed!")
    return True
```

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

1. **You see a problem: "Find the maximum product of any 3 numbers in the array."** Which template would you start with? (Bắt đầu với template nào?)

2. **What are the 4 questions you should answer before writing BF code?** (4 câu hỏi cần trả lời trước khi viết code BF?)

3. **When would you use the stress_test utility?** Give a specific scenario (Khi nào dùng stress_test? Cho tình huống cụ thể).

4. **In Template 3 (Subsets), why do we need `current[:]` instead of just `current`?** (Tại sao cần `current[:]` thay vì `current`?)

---

**← Previous:** [Chapter 3: Complexity Analysis](./03_complexity.md)
**Next →** [Run the Examples!](../examples/) 🚀
