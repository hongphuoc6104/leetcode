# 📖 Chapter 4: Python Templates

## ✅ Pre-Coding Checklist

```
□ 1. Does the HEAD potentially change? → Use Dummy Head
□ 2. Am I modifying pointers? → Save references BEFORE changing
□ 3. Can I draw the before/after state?
□ 4. Have I handled: empty list? single node? two nodes?
```

---

## Template 1: Dummy Head — Safe Modification

```python
def modify_list(head):
    dummy = ListNode(0, head)
    curr = dummy
    while curr.next:
        if should_remove(curr.next):
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next
```

---

## Template 2: Reverse Entire List

```python
def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

---

## Template 3: Reverse Between m and n

```python
def reverse_between(head, m, n):
    dummy = ListNode(0, head)
    prev = dummy
    for _ in range(m - 1):
        prev = prev.next
    curr = prev.next
    for _ in range(n - m):
        nxt = curr.next
        curr.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt
    return dummy.next
```

---

## Template 4: Fast & Slow — Middle

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

---

## Template 5: Merge Two Sorted

```python
def merge(l1, l2):
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next
```

---

## Template 6: Remove Nth from End

```python
def remove_nth(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
```

---

## Template 7: Check Palindrome

```python
def is_palindrome(head):
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Reverse second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    # Compare
    while prev:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next
    return True
```

---

## Utility: Build & Print List

```python
def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
```

---

**← Previous:** [Chapter 3: Complexity](./03_complexity.md)
**Next →** [Run the Examples!](../examples/) 🚀
