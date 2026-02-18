# 📖 Chapter 1: Introduction to Stack & Queue

## 1. Stack — LIFO (Last In, First Out)

Think of a stack of plates: you add to the TOP and take from the TOP (Chồng đĩa: thêm và lấy từ TRÊN CÙNG).

```
Push 1, Push 2, Push 3:     Pop:
    ┌───┐                    ┌───┐
    │ 3 │ ← top              │ 3 │ → removed!
    ├───┤                    └───┘
    │ 2 │                    ┌───┐
    ├───┤                    │ 2 │ ← new top
    │ 1 │                    ├───┤
    └───┘                    │ 1 │
                             └───┘
```

### Python: Use `list`

```python
stack = []
stack.append(1)     # Push → O(1)
stack.append(2)
stack.pop()         # Pop → O(1), returns 2
stack[-1]           # Peek → O(1), returns 1
len(stack)          # Size → O(1)
```

---

## 2. Queue — FIFO (First In, First Out)

Think of a line at a store: first person in line is served first (Hàng xếp: người đầu tiên được phục vụ trước).

```
Enqueue 1, 2, 3:             Dequeue:
    ┌───┬───┬───┐             ┌───┬───┐
    │ 1 │ 2 │ 3 │    →   1   │ 2 │ 3 │
    └───┴───┴───┘             └───┴───┘
    front    back             front back
```

### Python: Use `collections.deque`

```python
from collections import deque
queue = deque()
queue.append(1)       # Enqueue right → O(1)
queue.popleft()       # Dequeue left → O(1)
queue[0]              # Peek front → O(1)
```

> ⚠️ **Never use `list.pop(0)` for Queue!** It's O(n). Use `deque.popleft()` which is O(1).

---

## 3. Deque — Double-Ended Queue

Can add/remove from BOTH ends in O(1) (Thêm/xóa từ CẢ HAI đầu trong O(1)).

```python
from collections import deque
d = deque()
d.append(x)        # Add right  → O(1)
d.appendleft(x)    # Add left   → O(1)
d.pop()             # Remove right → O(1)
d.popleft()         # Remove left  → O(1)
```

---

## 4. When to Use What?

| Signal | Data Structure |
|--------|---------------|
| "Matching brackets/parens" | Stack |
| "Undo/redo" | Stack |
| "Next greater/smaller" | Monotonic Stack |
| "Process level by level" | Queue (BFS) |
| "Sliding window max/min" | Monotonic Deque |
| "Expression evaluation" | Stack |
| "DFS (iterative)" | Stack |

---

## ❓ Self-Check Questions

1. **Why is `list.pop(0)` O(n) but `deque.popleft()` O(1)?** (Tại sao khác chi phí?)
2. **How would you implement a Queue using two Stacks?**
3. **"Undo" feature in a text editor** — which DS? Why?

---

**Next →** [Chapter 2: Patterns](./02_patterns.md)
