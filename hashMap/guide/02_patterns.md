# 📖 Chapter 2: Hash Map Patterns

---

## Pattern 1: Complement / Two Sum — O(n)

### 🔍 Signal
- "Find pair that sums to target" / "Find complement"

### 💻 Code
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### 📌 LC 1, LC 167, LC 15

---

## Pattern 2: Frequency Counting — O(n)

### 🔍 Signal
- "Count occurrences" / "Most frequent" / "Duplicate check"

### 💻 Code
```python
from collections import Counter

def top_k_frequent(nums, k):
    return [x for x, _ in Counter(nums).most_common(k)]

def is_anagram(s, t):
    return Counter(s) == Counter(t)

def first_unique(s):
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1
```

### 📌 LC 242, LC 347, LC 387, LC 217

---

## Pattern 3: Grouping — O(n)

### 🔍 Signal
- "Group by property" / "Group anagrams" / "Categorize"

### 💻 Code
```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))  # Anagram key
        groups[key].append(s)
    return list(groups.values())
```

### 📌 LC 49, LC 290, LC 205

---

## Pattern 4: Prefix Sum + Hash Map — O(n)

### 🔍 Signal
- "Subarray sum equals k" / "Count subarrays with property"
- Converting subarray problem to prefix difference

### 💡 Key Insight
```
sum(nums[i..j]) = prefix[j] - prefix[i-1]
If prefix[j] - prefix[i-1] = k, then prefix[i-1] = prefix[j] - k
→ Look up (prefix[j] - k) in hash map!
```

### 💻 Code
```python
def subarray_sum(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count
```

### 📌 LC 560, LC 523, LC 930

---

## Pattern 5: Set Operations — O(n)

### 🔍 Signal
- "Intersection" / "Contains duplicate" / "Longest consecutive"

### 💻 Code — Longest Consecutive
```python
def longest_consecutive(nums):
    num_set = set(nums)
    best = 0
    for n in num_set:
        if n - 1 not in num_set:  # Start of sequence
            length = 1
            while n + length in num_set:
                length += 1
            best = max(best, length)
    return best
```

### 📌 LC 128, LC 349, LC 217

---

## 📊 Quick Reference

| Pattern | Signal | Key technique |
|---------|--------|--------------|
| Complement | "find pair" | `target - num` lookup |
| Frequency | "count/most frequent" | Counter |
| Grouping | "group by property" | defaultdict(list) |
| Prefix + Hash | "subarray sum = k" | prefix diff lookup |
| Set Ops | "unique/consecutive" | set membership O(1) |

---

## ❓ Self-Check Questions

1. **Why does Two Sum use hash map instead of sorting?** Trade-offs? (So sánh ưu nhược?)
2. **"Subarray sum = 0"** — how does Prefix + Hash solve it?
3. **In Longest Consecutive, why check `n-1 not in set`?** (Tại sao kiểm tra `n-1`?)

---

**← Previous:** [Chapter 1: Introduction](./01_introduction.md)
**Next →** [Chapter 3: Complexity](./03_complexity.md)
