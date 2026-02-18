# 📖 Chapter 3: Complexity Analysis

## 1. Operations Table

| Operation | Stack (list) | Queue (deque) | Deque |
|-----------|-------------|--------------|-------|
| Push / Append | **O(1)**amz | **O(1)** | **O(1)** |
| Pop / Popleft | **O(1)** | **O(1)** | **O(1)** |
| Peek | **O(1)** | **O(1)** | **O(1)** |
| Search | O(n) | O(n) | O(n) |
| Size | **O(1)** | **O(1)** | **O(1)** |

### ⚠️ Python Trap: `list.pop(0)` is O(n)!

```python
# ❌ WRONG: O(n) per dequeue → O(n²) total
queue = [1, 2, 3, 4, 5]
queue.pop(0)   # Shifts ALL elements!

# ✅ CORRECT: O(1) per dequeue
from collections import deque
queue = deque([1, 2, 3, 4, 5])
queue.popleft()  # Doubly-linked list, O(1)
```

---

## 2. Algorithm Complexities

| Algorithm | Time | Space |
|-----------|------|-------|
| Valid Parentheses | O(n) | O(n) |
| Monotonic Stack (Next Greater) | O(n) | O(n) |
| Expression Evaluation | O(n) | O(n) |
| Decode String | O(output length) | O(depth) |
| Sliding Window Max (Deque) | O(n) | O(k) |

### Why Monotonic Stack is O(n)

Each element is pushed **once** and popped **at most once**. Total operations: at most 2n = O(n) (Mỗi phần tử push 1 lần, pop tối đa 1 lần → O(n)).

---

## 3. Common Mistakes

### Peek before checking empty ⚠️
```python
# ❌ WRONG
top = stack[-1]          # IndexError if empty!

# ✅ CORRECT
top = stack[-1] if stack else None
```

### Not popping all matching elements ⚠️
```python
# ❌ WRONG — only pops one
if stack and nums[stack[-1]] < nums[i]:
    result[stack.pop()] = nums[i]

# ✅ CORRECT — pop ALL smaller
while stack and nums[stack[-1]] < nums[i]:
    result[stack.pop()] = nums[i]
```

---

## ❓ Self-Check Questions

1. **What's the max stack size for Valid Parentheses with n chars?**
2. **Why does Monotonic Stack use O(n) space at most?**
3. **Sliding Window Max with k = n: what's the space?**

---

**← Previous:** [Chapter 2: Patterns](./02_patterns.md)  
**Next →** [Chapter 4: Templates](./04_python_templates.md)
