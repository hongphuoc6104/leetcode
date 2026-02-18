# 📖 Chapter 2: Sliding Window Patterns (Các Pattern Cửa Sổ Trượt)

## 🎯 Learning Objectives (Mục tiêu)

After this chapter (Sau chương này):
- Master 5 patterns covering 95%+ of Sliding Window problems
- Know the signal/trigger for each pattern
- Write the expand/shrink logic confidently

---

## Pattern 1: Fixed Window Sum/Average — O(n)

### What it does

Compute sum/average/max/min for every window of size k (Tính tổng/trung bình/max/min cho mọi cửa sổ kích thước k).

### 🔍 Signal

- "Maximum/minimum sum of k consecutive elements"
- "Average of subarray of size k"
- Window size **k is given explicitly**

### 💻 Code

```python
def max_sum_fixed(arr, k):
    # Initialize first window (Khởi tạo cửa sổ đầu)
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Add right, remove left
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### 📌 LeetCode: Max Average Subarray (LC 643), Min Difference Scores (LC 1984)

---

## Pattern 2: Fixed Window Frequency Match — O(n)

### What it does

Check if any window of size k matches a frequency pattern (Kiểm tra cửa sổ kích thước k có khớp pattern tần suất).

### 🔍 Signal

- "Find anagram" (Tìm đảo chữ)
- "Permutation in string" (Hoán vị trong chuỗi)
- Compare character frequencies in windows

### 💻 Code

```python
from collections import Counter

def find_anagrams(s, p):
    """Find all start indices where anagram of p exists in s."""
    if len(p) > len(s):
        return []
    
    p_count = Counter(p)
    window = Counter(s[:len(p)])
    result = []
    
    if window == p_count:
        result.append(0)
    
    for i in range(len(p), len(s)):
        # Add right (Thêm phải)
        window[s[i]] += 1
        # Remove left (Bỏ trái)
        left_char = s[i - len(p)]
        window[left_char] -= 1
        if window[left_char] == 0:
            del window[left_char]
        
        if window == p_count:
            result.append(i - len(p) + 1)
    
    return result
```

### 📌 LeetCode: Find All Anagrams (LC 438), Permutation in String (LC 567)

---

## Pattern 3: Variable Window — Longest/Maximum — O(n)

### What it does

Find the **longest** subarray/substring satisfying a condition. Expand right freely, shrink left only when condition is violated (Tìm subarray/substring **dài nhất** thỏa điều kiện. Mở rộng phải tự do, thu hẹp trái khi vi phạm).

### 🔍 Signal

- "**Longest** substring with..." (Chuỗi con **dài nhất** với...)
- "At most k distinct characters" (Tối đa k ký tự khác nhau)
- "Maximum length" (Độ dài tối đa)

### 💻 Code

```python
def longest_with_condition(s, k):
    """Longest substring with at most k distinct chars."""
    left = 0
    freq = {}
    max_len = 0
    
    for right in range(len(s)):
        # Expand: add s[right] (Mở rộng)
        freq[s[right]] = freq.get(s[right], 0) + 1
        
        # Shrink: while condition violated (Thu hẹp khi vi phạm)
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        
        # Update answer (Cập nhật đáp án)
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

### 📌 LeetCode: Longest Substring No Repeat (LC 3), Fruit Into Baskets (LC 904)

---

## Pattern 4: Variable Window — Shortest/Minimum — O(n)

### What it does

Find the **shortest** subarray satisfying a condition. Expand right until valid, then shrink left to minimize (Tìm subarray **ngắn nhất**. Mở rộng phải đến khi hợp lệ, thu hẹp trái để tối thiểu hóa).

### 🔍 Signal

- "**Minimum** size subarray with sum ≥ target"
- "**Shortest** substring containing all characters"
- "Minimum length" (Độ dài tối thiểu)

### 💻 Code

```python
def min_subarray_sum(nums, target):
    """Shortest subarray with sum >= target."""
    left = 0
    current_sum = 0
    min_len = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]  # Expand (Mở rộng)
        
        # Shrink while VALID (Thu hẹp khi CÒN hợp lệ)
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0
```

### ⚠️ Key Difference from Pattern 3

| | Longest (Pattern 3) | Shortest (Pattern 4) |
|---|---------------------|---------------------|
| Shrink when | Condition **violated** | Condition **satisfied** |
| Update when | After shrinking (always valid) | Before/during shrinking |
| While loop | `while invalid: shrink` | `while valid: update + shrink` |

### 📌 LeetCode: Min Size Subarray Sum (LC 209), Min Window Substring (LC 76)

---

## Pattern 5: Sliding Window with Counting — O(n)

### What it does

Count the number of subarrays/substrings satisfying a condition, often using the "at most K" trick (Đếm số subarray thỏa điều kiện, dùng thủ thuật "tối đa K").

### 🔍 Signal

- "Count subarrays with exactly K distinct" (Đếm subarray có đúng K phần tử khác nhau)
- "Number of subarrays with product < K"

### 💡 The "At Most K" Trick

```
exactly(K) = atMost(K) - atMost(K - 1)
```

### 💻 Code

```python
def count_subarrays_at_most_k(nums, k):
    """Count subarrays with at most k distinct elements."""
    left = 0
    freq = {}
    count = 0
    
    for right in range(len(nums)):
        freq[nums[right]] = freq.get(nums[right], 0) + 1
        
        while len(freq) > k:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1
        
        # All subarrays ending at 'right' with start in [left, right]
        count += right - left + 1
    
    return count

def count_subarrays_exactly_k(nums, k):
    """Count subarrays with EXACTLY k distinct elements."""
    return (count_subarrays_at_most_k(nums, k) -
            count_subarrays_at_most_k(nums, k - 1))
```

### 📌 LeetCode: Subarrays K Different (LC 992), Subarray Product < K (LC 713)

---

## 📊 Quick Reference Table

| Pattern | Type | Signal | Shrink When |
|---------|------|--------|-------------|
| Fixed Sum | Fixed | "sum of k elements" | Never (slide) |
| Frequency Match | Fixed | "anagram", "permutation" | Never (slide) |
| Longest | Variable | "longest", "maximum" | Invalid |
| Shortest | Variable | "shortest", "minimum" | Valid |
| Counting | Variable | "count", "number of" | Invalid |

---

## ❓ Self-Check Questions

1. **"Find the maximum number of vowels in any substring of length k"** — which pattern? Fixed or Variable? (Pattern nào?)

2. **In Pattern 3 vs Pattern 4, explain WHY we shrink at different times** (Giải thích TẠI SAO thu hẹp ở thời điểm khác nhau).

3. **Draw the window movement for Pattern 4** with `nums=[2,3,1,2,4,3], target=7` — show each expand and shrink step.

4. **Why does `count += right - left + 1` work in Pattern 5?** How many new subarrays are added when right moves to a new position? (Tại sao `right - left + 1` đếm đúng?)

---

**← Previous:** [Chapter 1: Introduction](./01_introduction.md)
**Next →** [Chapter 3: Complexity](./03_complexity.md)
