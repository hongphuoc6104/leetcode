# 📖 Chapter 4: Python Templates

## ✅ Pre-Coding Checklist

```
□ 1. Matching/nesting problem? → Stack
□ 2. "Next greater/smaller"? → Monotonic Stack
□ 3. Level-by-level processing? → Queue (BFS)
□ 4. Sliding window max/min? → Monotonic Deque
□ 5. Check: empty stack/queue before peek/pop?
```

---

## Template 1: Valid Parentheses

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
    return not stack
```

---

## Template 2: Monotonic Stack — Next Greater

```python
def next_greater(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
```

---

## Template 3: Monotonic Stack — Next Smaller

```python
def next_smaller(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
```

---

## Template 4: Evaluate RPN

```python
def eval_rpn(tokens):
    stack = []
    for t in tokens:
        if t in "+-*/":
            b, a = stack.pop(), stack.pop()
            if t == '+': stack.append(a + b)
            elif t == '-': stack.append(a - b)
            elif t == '*': stack.append(a * b)
            else: stack.append(int(a / b))
        else:
            stack.append(int(t))
    return stack[0]
```

---

## Template 5: Decode String

```python
def decode_string(s):
    stack = []
    curr_str, curr_num = "", 0
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

---

## Template 6: Sliding Window Max (Monotonic Deque)

```python
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    result = []
    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

---

## Template 7: Min Stack

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        m = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(m)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
```

---

**← Previous:** [Chapter 3: Complexity](./03_complexity.md)  
**Next →** [Run the Examples!](../examples/) 🚀
