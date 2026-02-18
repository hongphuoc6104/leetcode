# 📖 Chapter 3: Complexity Analysis

## 1. Operations Table

| Operation | Singly LL | Doubly LL | Array |
|-----------|-----------|-----------|-------|
| Access [i] | O(n) | O(n) | **O(1)** |
| Search | O(n) | O(n) | O(n) |
| Insert head | **O(1)** | **O(1)** | O(n) |
| Insert tail | O(n)* | **O(1)** | O(1)** |
| Insert mid (w/ ptr) | **O(1)** | **O(1)** | O(n) |
| Delete head | **O(1)** | **O(1)** | O(n) |
| Delete (w/ ptr) | O(n)*** | **O(1)** | O(n) |
| Reverse | O(n) | O(n) | O(n) |
| Find middle | O(n) | O(n) | O(1) |

\* O(1) with tail pointer
\** Amortized
\*** O(n) because need predecessor; O(1) in doubly

---

## 2. Space Overhead

| Structure | Storage per element |
|-----------|-------------------|
| Array (int) | 28 bytes (Python int) |
| Singly LL Node | 28 + 8 = 36 bytes (val + next ptr) |
| Doubly LL Node | 28 + 16 = 44 bytes (val + next + prev) |

> LL uses ~30-60% more memory than arrays due to pointer overhead.

---

## 3. When to Use LL vs Array

| Choose LL when | Choose Array when |
|---------------|-------------------|
| Frequent insert/delete at head | Need random access |
| Unknown size, dynamic growth | Known size, cache performance |
| Implementing Queue/Stack | Sorting, binary search |
| Need O(1) insert with pointer | Memory efficiency matters |

---

## 4. Common Mistakes

### Not handling empty list ⚠️
```python
# ❌ Crashes on empty list
def get_first(head):
    return head.val           # NoneType error!

# ✅ Check first
def get_first(head):
    return head.val if head else None
```

### Modifying while iterating ⚠️
```python
# ❌ WRONG — loses nodes
curr = head
while curr:
    if should_remove(curr):
        curr = curr.next.next  # Skips checking next node
    curr = curr.next

# ✅ Use Dummy Head + prev pointer
```

---

## ❓ Self-Check Questions

1. **Why is LL insert at head O(1) but Array insert at head O(n)?**
2. **"Sort a linked list" — which sort algorithm is best?** Why not QuickSort?
3. **Can you do Binary Search on a Linked List?** Why or why not?

---

**← Previous:** [Chapter 2: Patterns](./02_patterns.md)
**Next →** [Chapter 4: Templates](./04_python_templates.md)
