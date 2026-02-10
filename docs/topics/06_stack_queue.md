# 📖 Chủ đề 6: Stack & Queue

## Lý thuyết cơ bản

**Stack (LIFO)**: Phần tử vào sau ra trước. **Queue (FIFO)**: Phần tử vào trước ra trước.

### Python Implementation
```python
# Stack - dùng list
stack = []
stack.append(x)   # push O(1)
stack.pop()        # pop O(1)
stack[-1]          # peek O(1)

# Queue - dùng deque
from collections import deque
queue = deque()
queue.append(x)    # enqueue O(1)
queue.popleft()    # dequeue O(1)

# Monotonic Stack (giảm dần)
def mono_stack(arr):
    stack = []
    result = [-1] * len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]  # next greater element
        stack.append(i)
```

---

## Danh sách 30 bài LeetCode

### 🟢 Easy (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Valid Parentheses | [LC 20](https://leetcode.com/problems/valid-parentheses/) | Stack matching |
| 2 | Min Stack | [LC 155](https://leetcode.com/problems/min-stack/) | Stack phụ track min |
| 3 | Stack using Queues | [LC 225](https://leetcode.com/problems/implement-stack-using-queues/) | 1 hoặc 2 queues |
| 4 | Queue using Stacks | [LC 232](https://leetcode.com/problems/implement-queue-using-stacks/) | 2 stacks |
| 5 | Next Greater Element I | [LC 496](https://leetcode.com/problems/next-greater-element-i/) | Monotonic stack + hash |
| 6 | Baseball Game | [LC 682](https://leetcode.com/problems/baseball-game/) | Stack simulation |
| 7 | Backspace Compare | [LC 844](https://leetcode.com/problems/backspace-string-compare/) | Stack hoặc two pointers |
| 8 | Recent Calls | [LC 933](https://leetcode.com/problems/number-of-recent-calls/) | Queue, remove old |
| 9 | Remove Adjacent Dups | [LC 1047](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) | Stack |
| 10 | Make String Great | [LC 1544](https://leetcode.com/problems/make-the-string-great/) | Stack, check upper/lower |

### 🟡 Medium (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Simplify Path | [LC 71](https://leetcode.com/problems/simplify-path/) | Stack, split("/") |
| 2 | Eval Reverse Polish | [LC 150](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Stack, operators |
| 3 | Basic Calculator II | [LC 227](https://leetcode.com/problems/basic-calculator-ii/) | Stack, ưu tiên */  |
| 4 | Decode String | [LC 394](https://leetcode.com/problems/decode-string/) | Stack hoặc recursion |
| 5 | Next Greater II | [LC 503](https://leetcode.com/problems/next-greater-element-ii/) | Circular, duyệt 2 lần |
| 6 | Design Circular Queue | [LC 622](https://leetcode.com/problems/design-circular-queue/) | Array + modulo |
| 7 | Asteroid Collision | [LC 735](https://leetcode.com/problems/asteroid-collision/) | Stack simulation |
| 8 | Daily Temperatures | [LC 739](https://leetcode.com/problems/daily-temperatures/) | Monotonic stack |
| 9 | Score of Parentheses | [LC 856](https://leetcode.com/problems/score-of-parentheses/) | Stack, track depth |
| 10 | Online Stock Span | [LC 901](https://leetcode.com/problems/online-stock-span/) | Monotonic stack |

### 🔴 Hard (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Longest Valid Parens | [LC 32](https://leetcode.com/problems/longest-valid-parentheses/) | Stack track index |
| 2 | Trapping Rain Water | [LC 42](https://leetcode.com/problems/trapping-rain-water/) | Monotonic stack |
| 3 | Largest Rect Histogram | [LC 84](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Monotonic stack |
| 4 | Basic Calculator | [LC 224](https://leetcode.com/problems/basic-calculator/) | Stack, handle signs |
| 5 | Sliding Window Max | [LC 239](https://leetcode.com/problems/sliding-window-maximum/) | Monotonic deque |
| 6 | Remove Dup Letters | [LC 316](https://leetcode.com/problems/remove-duplicate-letters/) | Monotonic stack + greedy |
| 7 | Number of Atoms | [LC 726](https://leetcode.com/problems/number-of-atoms/) | Stack + parsing |
| 8 | Basic Calculator IV | [LC 770](https://leetcode.com/problems/basic-calculator-iv/) | Polynomial stack |
| 9 | Max Freq Stack | [LC 895](https://leetcode.com/problems/maximum-frequency-stack/) | Hash + stack per freq |
| 10 | Car Fleet II | [LC 1776](https://leetcode.com/problems/car-fleet-ii/) | Monotonic stack |

---

## Tips
- **Monotonic Stack** là pattern quan trọng nhất: tìm next/previous greater/smaller element
- Bài có **parentheses/brackets** → gần như chắc chắn dùng Stack
- **Queue** thường xuất hiện trong BFS
