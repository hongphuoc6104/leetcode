# 📖 Chapter 4: Python Templates (Templates Python sẵn dùng)

## ✅ Pre-Coding Checklist

```
□ 1. Is this about CONTIGUOUS subarray/substring?
     (Có phải subarray/substring LIÊN TIẾP?)

□ 2. Fixed or Variable window?
     (Cửa sổ Cố định hay Biến đổi?)

□ 3. What STATE do I maintain? (sum? freq map? count?)
     (Duy trì TRẠNG THÁI gì?)

□ 4. When do I SHRINK? (invalid? or valid?)
     (Khi nào THU HẸP?)
```

---

## Template 1: Fixed Window — Sum/Max/Min

```python
def fixed_window_sum(arr, k):
    """Fixed-size window, tracking sum."""
    window_sum = sum(arr[:k])
    result = window_sum               # Initialize with first window!
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Slide: +right -left
        result = max(result, window_sum)     # TODO: or min, or append
    
    return result
```

---

## Template 2: Fixed Window — Frequency Match

```python
from collections import Counter

def fixed_window_freq(s, p):
    """Fixed-size window matching character frequency."""
    k = len(p)
    target = Counter(p)
    window = Counter(s[:k])
    results = []
    
    if window == target:
        results.append(0)
    
    for i in range(k, len(s)):
        window[s[i]] += 1                     # Add right
        window[s[i - k]] -= 1                 # Remove left
        if window[s[i - k]] == 0:
            del window[s[i - k]]
        if window == target:
            results.append(i - k + 1)
    
    return results
```

---

## Template 3: Variable Window — Longest

```python
def variable_longest(arr):
    """Variable window, find LONGEST satisfying condition."""
    left = 0
    state = {}                                 # TODO: your state
    max_len = 0
    
    for right in range(len(arr)):
        update_state_add(state, arr[right])    # Expand
        
        while is_invalid(state):               # Shrink when INVALID
            update_state_remove(state, arr[left])
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

---

## Template 4: Variable Window — Shortest

```python
def variable_shortest(arr, target):
    """Variable window, find SHORTEST satisfying condition."""
    left = 0
    state = 0                                  # TODO: your state
    min_len = float('inf')
    
    for right in range(len(arr)):
        state += arr[right]                    # Expand
        
        while is_valid(state, target):         # Shrink while VALID
            min_len = min(min_len, right - left + 1)
            state -= arr[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0
```

---

## Template 5: Variable Window — Count (At-Most-K)

```python
def count_at_most_k(arr, k):
    """Count subarrays with at most k distinct."""
    left = 0
    freq = {}
    count = 0
    
    for right in range(len(arr)):
        freq[arr[right]] = freq.get(arr[right], 0) + 1
        
        while len(freq) > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]
            left += 1
        
        count += right - left + 1              # New subarrays ending at right
    
    return count

def count_exactly_k(arr, k):
    return count_at_most_k(arr, k) - count_at_most_k(arr, k - 1)
```

---

## Template 6: Min Window Substring (Classic Hard)

```python
from collections import Counter

def min_window(s, t):
    """Find minimum window in s containing all chars of t."""
    need = Counter(t)
    missing = len(t)
    left = 0
    best = (0, float('inf'))
    
    for right, char in enumerate(s):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        
        while missing == 0:                    # All chars found!
            if right - left < best[1] - best[0]:
                best = (left, right)
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    
    return s[best[0]:best[1]+1] if best[1] != float('inf') else ""
```

---

## ❓ Self-Check Questions

1. **"Maximum number of vowels in substring of length k"** — which template?
2. **What's the KEY difference between Template 3 and Template 4?** (Shrink timing)
3. **In Template 5, why does `count += right - left + 1` count correctly?**
4. **When should you use Template 6 vs Template 4?** (Khi nào dùng 6 thay vì 4?)

---

**← Previous:** [Chapter 3: Complexity](./03_complexity.md)
**Next →** [Run the Examples!](../examples/) 🚀
