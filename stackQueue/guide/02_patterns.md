# 📖 Chapter 2: Stack & Queue Patterns

---

## Pattern 1: Bracket Matching — Stack

### 🔍 Signal
- "Valid parentheses" / "Matching brackets" / "Nested structure"

### 💻 Code
```python
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in pairs:
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
        else:
            stack.append(c)
    return len(stack) == 0
```

### 📌 LC 20, LC 32, LC 856

---

## Pattern 2: Monotonic Stack — Next Greater/Smaller

### 🔍 Signal
- "Next greater element" / "Next smaller" / "Daily temperatures"
- "Previous greater/smaller"

### 💡 Key Insight
Maintain a stack where elements are in monotonic (increasing or decreasing) order. When a new element violates the order, pop and process.

```
Array:  [2, 1, 4, 3]
Finding NEXT GREATER for each:

  i=0: push 2   stack=[2]
  i=1: 1 < 2    push 1   stack=[2, 1]
  i=2: 4 > 1    pop 1 → next_greater[1] = 4
       4 > 2    pop 2 → next_greater[0] = 4
       push 4   stack=[4]
  i=3: 3 < 4    push 3   stack=[4, 3]

  Remaining: next_greater = -1
  Result: [4, 4, -1, -1]
```

### 💻 Code
```python
def next_greater(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # indices
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
```

### 📌 LC 496, LC 503, LC 739, LC 84

---

## Pattern 3: Expression Evaluation — Stack

### 🔍 Signal
- "Evaluate expression" / "Calculator" / "Reverse Polish Notation"

### 💻 Code — RPN
```python
def eval_rpn(tokens):
    stack = []
    ops = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: int(a / b)}
    for t in tokens:
        if t in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[t](a, b))
        else:
            stack.append(int(t))
    return stack[0]
```

### 📌 LC 150, LC 224, LC 227

---

## Pattern 4: Decode / Nested Structure — Stack

### 🔍 Signal
- "Decode string" / "Nested brackets" / "Flatten nested"

### 💻 Code — Decode String
```python
def decode_string(s):
    stack = []
    curr_str = ""
    curr_num = 0
    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        elif c == '[':
            stack.append((curr_str, curr_num))
            curr_str, curr_num = "", 0
        elif c == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + curr_str * num
        else:
            curr_str += c
    return curr_str
```

### 📌 LC 394, LC 71

---

## Pattern 5: Monotonic Deque — Sliding Window Max/Min

### 🔍 Signal
- "Maximum in sliding window" / "Minimum in window"

### 💻 Code
```python
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()  # indices, decreasing values
    result = []
    for i in range(len(nums)):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove smaller values (they'll never be max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

### 📌 LC 239

---

## 📊 Quick Reference

| Pattern | DS | Signal | Time |
|---------|-----|--------|------|
| Bracket Matching | Stack | "valid parens" | O(n) |
| Monotonic Stack | Stack | "next greater" | O(n) |
| Expression Eval | Stack | "calculator/RPN" | O(n) |
| Decode/Nested | Stack | "decode/nested" | O(n) |
| Sliding Max/Min | Deque | "window max" | O(n) |

---

## ❓ Self-Check Questions

1. **Why does Monotonic Stack process each element at most twice?** (Push once, pop once = O(n))
2. **"Largest rectangle in histogram"** — why Monotonic Stack?
3. **How to find PREVIOUS smaller element?** (Traverse left-to-right or right-to-left?)

---

**← Previous:** [Chapter 1: Introduction](./01_introduction.md)  
**Next →** [Chapter 3: Complexity](./03_complexity.md)
