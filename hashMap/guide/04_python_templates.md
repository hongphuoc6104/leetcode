# 📖 Chapter 4: Python Templates

## ✅ Pre-Coding Checklist

```
□ 1. "Find pair/complement"? → Hash Map lookup
□ 2. "Count occurrences"? → Counter or dict
□ 3. "Group by property"? → defaultdict(list)
□ 4. "Subarray sum = k"? → Prefix Sum + Hash Map
□ 5. "Check existence/duplicate"? → Set
```

---

## Template 1: Two Sum (Complement Lookup)

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []
```

---

## Template 2: Frequency Count

```python
from collections import Counter

def top_k_frequent(nums, k):
    return [x for x, _ in Counter(nums).most_common(k)]
```

---

## Template 3: Group by Key

```python
from collections import defaultdict

def group_by(items, key_fn):
    groups = defaultdict(list)
    for item in items:
        groups[key_fn(item)].append(item)
    return dict(groups)
```

---

## Template 4: Subarray Sum = K

```python
def subarray_sum(nums, k):
    count = prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count
```

---

## Template 5: Longest Consecutive Sequence

```python
def longest_consecutive(nums):
    num_set = set(nums)
    best = 0
    for n in num_set:
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            best = max(best, length)
    return best
```

---

## Template 6: Bijection Check (Isomorphic)

```python
def is_isomorphic(s, t):
    s2t, t2s = {}, {}
    for a, b in zip(s, t):
        if a in s2t and s2t[a] != b:
            return False
        if b in t2s and t2s[b] != a:
            return False
        s2t[a] = b
        t2s[b] = a
    return True
```

---

**← Previous:** [Chapter 3: Complexity](./03_complexity.md)
**Next →** [Run the Examples!](../examples/) 🚀
