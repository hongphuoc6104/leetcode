# 📖 Chapter 1: Introduction to Linked List (Giới thiệu Danh Sách Liên Kết)

## 1. What is a Linked List?

A Linked List is a sequence of **nodes**, where each node stores a **value** and a **pointer** to the next node (Chuỗi các **node**, mỗi node chứa **giá trị** và **con trỏ** đến node tiếp theo).

```
  Node 1        Node 2        Node 3
┌───┬───┐   ┌───┬───┐   ┌───┬──────┐
│ 1 │ ●─┼──▶│ 2 │ ●─┼──▶│ 3 │ None │
└───┴───┘   └───┴───┘   └───┴──────┘
  val next     val next     val  next
```

### Python Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## 2. Types (Các loại)

| Type | Description | Use case |
|------|-------------|----------|
| **Singly** | Each node → next | Most LeetCode problems |
| **Doubly** | Each node → next + prev | LRU Cache, Browser history |
| **Circular** | Last node → first node | Round-robin, Josephus |

---

## 3. Array vs Linked List (So sánh)

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Access by index | **O(1)** | O(n) |
| Search | O(n) | O(n) |
| Insert at head | O(n) | **O(1)** |
| Insert at tail | O(1)* | O(n) or O(1)** |
| Insert at middle | O(n) | **O(1)*** |
| Delete at head | O(n) | **O(1)** |
| Memory | Contiguous, compact | Scattered, +pointer overhead |

\* Amortized with dynamic array
\** O(1) if you maintain a tail pointer
\*** O(1) if you already have a pointer to the position

---

## 4. The Dummy Head Pattern (Pattern Dummy Head)

The **most important** pattern for Linked Lists! (Pattern **quan trọng nhất**!)

```python
# ❌ WITHOUT Dummy — messy edge cases
def remove_elements(head, val):
    while head and head.val == val:   # Handle head separately!
        head = head.next
    curr = head
    while curr and curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

# ✅ WITH Dummy — clean and uniform
def remove_elements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next
```

> **Rule**: Whenever the head might change, use a Dummy Head! (Bất cứ khi nào head có thể thay đổi, dùng Dummy Head!)

---

## 5. Common Pitfalls (Lỗi thường gặp)

### Lost reference ⚠️
```python
# ❌ WRONG — lost the rest of the list!
curr.next = new_node
new_node.next = curr.next  # curr.next is already new_node!

# ✅ CORRECT — save reference first
nxt = curr.next
curr.next = new_node
new_node.next = nxt
```

### NoneType error ⚠️
```python
# ❌ WRONG — crashes if curr is None!
if curr.next.val == target: ...

# ✅ CORRECT — check for None first
if curr.next and curr.next.val == target: ...
```

---

## ❓ Self-Check Questions

1. **Why is Array access O(1) but LL access O(n)?** (Tại sao Array O(1) nhưng LL O(n) khi truy cập?)

2. **When would you choose LL over Array?** Give 2 concrete scenarios (Cho 2 kịch bản cụ thể).

3. **Why does Dummy Head eliminate edge cases?** (Tại sao Dummy Head loại bỏ edge cases?)

4. **Draw what happens step by step when inserting a node after position 2** in: `1 → 3 → 5 → 7`

---

**Next →** [Chapter 2: Patterns](./02_patterns.md)
