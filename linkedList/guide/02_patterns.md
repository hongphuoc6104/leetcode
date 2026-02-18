# 📖 Chapter 2: Linked List Patterns (Các Pattern Linked List)

---

## Pattern 1: Dummy Head (Nút giả) — Use for all modifications

### 🔍 Signal
- "Remove nodes" / "Merge lists" / "Head might change"

### 💻 Code — Remove Elements
```python
def remove_elements(head, val):
    dummy = ListNode(0, head)
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next
```

### 📌 LC 203, LC 83, LC 82

---

## Pattern 2: Reverse Linked List — O(n), O(1)

### 🔍 Signal
- "Reverse" / "Palindrome check" / "Reverse between positions"

### 💡 Key: 3 pointers — prev, curr, nxt

```
Before: None ← 1   2 → 3 → 4 → None
              prev curr

Step 1: save nxt = curr.next (2)
        curr.next = prev (None)
        prev = curr (1)
        curr = nxt (2)

After:  None ← 1   2 → 3 → 4 → None
              prev curr
```

### 💻 Code
```python
def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev  # New head!
```

### 📌 LC 206, LC 92, LC 234

---

## Pattern 3: Fast & Slow — O(n), O(1)

### 🔍 Signal
- "Find middle" / "Cycle detection" / "Nth from end"

### 💻 Code — Find Middle
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next       # 1 step
        fast = fast.next.next  # 2 steps
    return slow  # Middle!
```

### 💻 Code — Cycle Start (Floyd's Phase 2)
```python
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Phase 2: find start
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
```

### 📌 LC 141, LC 142, LC 876

---

## Pattern 4: Merge Two Lists — O(n + m)

### 🔍 Signal
- "Merge sorted lists" / "Combine two lists"

### 💻 Code
```python
def merge_two(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2  # Remaining
    return dummy.next
```

### 📌 LC 21, LC 23, LC 148

---

## Pattern 5: Two Pointers Gap — O(n)

### 🔍 Signal
- "Remove nth node from END" / "Kth from end"
- Need position from the END without knowing length

### 💡 Key: Advance first pointer by n, then move both

```
Gap = 2:  fast moves 2 ahead first
  dummy → 1 → 2 → 3 → 4 → 5 → None
  slow          fast
  
  Then move both until fast reaches end:
  dummy → 1 → 2 → 3 → 4 → 5 → None
               slow          fast
  
  slow.next is the node to remove!
```

### 💻 Code
```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):     # Gap of n+1
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next  # Skip target
    return dummy.next
```

### 📌 LC 19

---

## 📊 Quick Reference

| Pattern | When | Key technique |
|---------|------|---------------|
| Dummy Head | Head may change | `dummy = ListNode(0, head)` |
| Reverse | Reverse / palindrome | 3 pointers: prev, curr, nxt |
| Fast & Slow | Middle / cycle | slow×1, fast×2 |
| Merge | Combine sorted | Dummy + compare |
| Two Ptr Gap | Nth from end | Advance first by n |

---

## ❓ Self-Check Questions

1. **In Reverse, why must we save `nxt = curr.next` BEFORE changing `curr.next`?**

2. **Why does Fast & Slow find the middle?** When fast is at end, where is slow?

3. **"Check if linked list is palindrome"** — which patterns do you combine? (Kết hợp pattern nào?)

---

**← Previous:** [Chapter 1: Introduction](./01_introduction.md)
**Next →** [Chapter 3: Complexity](./03_complexity.md)
