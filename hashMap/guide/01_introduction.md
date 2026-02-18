# 📖 Chapter 1: Introduction to Hash Map / Set (Giới thiệu Hash Map / Set)

## 🎯 Learning Objectives (Mục tiêu bài học)

After this chapter, you will be able to (Sau bài này, bạn sẽ có thể):
- Use Python's `dict`, `set`, `Counter`, `defaultdict` fluently (Dùng thành thạo)
- Explain WHY hash lookup is O(1) (Giải thích TẠI SAO tra cứu hash O(1))
- Decide WHEN to use Hash Map vs Sort vs Array (Quyết định KHI NÀO dùng)

---

### 🗝️ Real-life Analogy (Ví dụ đời thực)

Imagine a **library card catalog** (Tưởng tượng **thẻ mục lục thư viện**):

| Approach | How to find a book | Speed |
|----------|-------------------|-------|
| **List (Array)** | Walk through every shelf until you find it | O(n) — slow! |
| **Sorted Array** | Binary search by title | O(log n) — moderate |
| **Hash Map** | Look up the catalog number → go directly to shelf | O(1) — instant! |

> **Key insight (Nhận xét)**: Hash Maps trade **space for speed** — use extra memory to get O(1) lookups. Whenever you need to check "have I seen this before?" — use a Hash Map/Set!

---

## 1. Hash Map (dict) — Key → Value mapping

A Hash Map stores **key-value pairs** with O(1) average lookup (Lưu **cặp khóa-giá trị** với tra cứu O(1) trung bình).

```python
# Create and use
d = {}
d["apple"] = 5         # Insert O(1)
d["banana"] = 3
print(d["apple"])       # Access O(1) → 5
d.get("cherry", 0)      # Safe access → 0 (default)
del d["banana"]         # Delete O(1)
"apple" in d            # Check O(1) → True
```

### Useful Methods
```python
d.keys()                # All keys
d.values()              # All values
d.items()               # All (key, value) pairs
d.get(key, default)     # Safe access with default
d.setdefault(key, [])   # Set if not exists
```

---

## 2. Hash Set (set) — Unique values

A Set stores **unique values** with O(1) membership test (Lưu **giá trị duy nhất** với kiểm tra O(1)).

```python
s = set()
s.add(1)                # Add O(1)
s.add(2)
s.add(1)                # Duplicate ignored!
1 in s                  # Check O(1) → True
s.remove(1)             # Remove O(1)
s.discard(99)           # Safe remove (no error)
```

### Set Operations
```python
a = {1, 2, 3}
b = {2, 3, 4}
a & b          # Intersection → {2, 3}
a | b          # Union → {1, 2, 3, 4}
a - b          # Difference → {1}
a ^ b          # Symmetric diff → {1, 4}
```

---

## 3. Counter — Frequency counting

```python
from collections import Counter

arr = [1, 2, 2, 3, 3, 3]
count = Counter(arr)       # {3: 3, 2: 2, 1: 1}
count.most_common(2)       # [(3, 3), (2, 2)]
count["new"] += 1          # Auto-creates with 0

# String frequency
Counter("hello")           # {'l': 2, 'h': 1, 'e': 1, 'o': 1}
```

---

## 4. defaultdict — Auto-initialize

```python
from collections import defaultdict

# Group items
groups = defaultdict(list)
groups["fruit"].append("apple")   # No KeyError!
groups["fruit"].append("banana")

# Count items
counts = defaultdict(int)
counts["a"] += 1                  # Auto-starts at 0
```

---

## 5. How Hash Tables Work (Simplified)

```
key "apple" → hash("apple") → 12345
12345 % table_size → index 5
Store at index 5

Lookup: same hash → same index → O(1)!
(Tra cứu: cùng hash → cùng index → O(1)!)
```

### Collision Handling
When two keys hash to the same index → **chaining** (linked list at that slot) or **open addressing** (probe next slot). Python uses open addressing.

---

## ❓ Self-Check Questions

1. **Why is dict lookup O(1) but list lookup O(n)?** (Tại sao dict O(1) nhưng list O(n)?)
2. **What's the difference between `d[key]` and `d.get(key)`?**
3. **When would you use set vs dict?** Give 2 examples.
4. **Can a list be a dict key? Why or why not?** (List có thể làm key không?)

---

**Next →** [Chapter 2: Patterns](./02_patterns.md)
