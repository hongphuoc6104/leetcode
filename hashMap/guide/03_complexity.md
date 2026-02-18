# 📖 Chapter 3: Complexity Analysis

## 1. Operations Table

| Operation | dict (avg) | dict (worst) | set (avg) | list |
|-----------|-----------|-------------|-----------|------|
| Lookup | **O(1)** | O(n) | **O(1)** | O(n) |
| Insert | **O(1)** | O(n) | **O(1)** | O(1)* |
| Delete | **O(1)** | O(n) | **O(1)** | O(n) |
| Iteration | O(n) | O(n) | O(n) | O(n) |

\* Amortized for list.append()

### Why O(n) Worst Case?
Hash collision: all keys hash to same slot → degrades to linked list traversal. Extremely rare with Python's hash function (Cực hiếm với hàm hash của Python).

---

## 2. Space Complexity

| Structure | Space per element |
|-----------|-----------------|
| list | ~28 bytes (int) |
| set | ~50 bytes (hash + value) |
| dict | ~70 bytes (hash + key + value) |

> Hash tables use ~2-3x more memory than arrays due to hash overhead + load factor.

---

## 3. Algorithm Complexities

| Algorithm | Time | Space |
|-----------|------|-------|
| Two Sum (hash) | O(n) | O(n) |
| Two Sum (sort + 2ptr) | O(n log n) | O(1) |
| Group Anagrams | O(n × k log k) | O(n × k) |
| Subarray Sum = K | O(n) | O(n) |
| Longest Consecutive | O(n) | O(n) |
| Contains Duplicate | O(n) | O(n) |

---

## 4. Common Mistakes

### Modifying dict during iteration ⚠️
```python
# ❌ WRONG — RuntimeError!
for key in d:
    if should_remove(key):
        del d[key]

# ✅ CORRECT — iterate over copy
for key in list(d.keys()):
    if should_remove(key):
        del d[key]
```

### Using mutable key ⚠️
```python
# ❌ WRONG — lists are not hashable!
d = {[1, 2]: "value"}   # TypeError!

# ✅ CORRECT — use tuple
d = {(1, 2): "value"}
```

---

## 5. Constraint Guide (Hướng dẫn theo ràng buộc)

| Constraint (Ràng buộc) | Hash Map useful? | Approach |
|------------------------|-----------------|----------|
| n ≤ 10⁴ | ✅ | Hash Map or Sort both work |
| n ≤ 10⁵ | ✅ **Preferred** | Hash Map O(n) beats Sort O(n log n) |
| n ≤ 10⁶ | ✅ **Required** | Need O(n) — Hash Map or linear scan |
| Memory critical | ⚠️ | Consider sorting (O(1) space) over Hash Map |
| "Find duplicates" / "Count freq" | ✅ **Always** | Hash Set/Counter is ideal |
| "Two sum / pair matching" | ✅ **Classic** | Hash Map for complement lookup |

### Hash Map vs Alternatives

| Task | Hash Map | Sorted Array | Two Pointers |
|------|----------|-------------|-------------|
| Two Sum | O(n), O(n) space | O(n log n), O(1) space | After sort: O(n) |
| Contains Duplicate | O(n), O(n) space | O(n log n), O(1) space | N/A |
| Group Anagrams | O(n·k), O(n·k) space | O(n·k log k) | N/A |
| Intersection | O(n), O(n) space | O(n log n) | O(n) after sort |

> 🤔 **Think:** When would you choose Sort + Two Pointers over Hash Map? Answer: When memory is constrained or when the problem requires sorted output.

---

## ❓ Self-Check Questions

1. **Hash Map O(n) vs Sort O(n log n) for Two Sum?** When prefer sorting? (Khi nào ưu tiên sort hơn hash?)
2. **Why can't lists be dict keys?** What about tuples? (Tại sao list không thể làm key?)
3. **Memory: set of 1M ints vs list of 1M ints?** Estimate the difference (Ước lượng chênh lệch bộ nhớ).
4. **Name a problem where Hash Map is WORSE than sorting.** (Kể 1 bài Hash Map thua sorting)
5. **What happens when Python dict reaches ~67% load factor?** (Dict đầy 67% thì sao?)

---

**← Previous:** [Chapter 2: Patterns](./02_patterns.md)
**Next →** [Chapter 4: Templates](./04_python_templates.md)
