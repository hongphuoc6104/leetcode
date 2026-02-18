# 📖 Chapter 1: Introduction to Heap (Giới thiệu Heap)

## 🎯 Learning Objectives (Mục tiêu bài học)

After this chapter, you will be able to (Sau bài này, bạn sẽ có thể):
- Define what a Heap/Priority Queue is (Định nghĩa Heap là gì)
- Explain WHY min/max access is O(1) (Giải thích TẠI SAO truy cập min/max O(1))
- Use Python's `heapq` module fluently (Dùng thành thạo heapq)

---

## 1. What is a Heap? (Heap là gì?)

A **Heap** is a **complete binary tree** stored as an array, where every parent satisfies the **heap property**:
- **Min-Heap**: Parent ≤ Children (Python's `heapq`)
- **Max-Heap**: Parent ≥ Children

**Heap** là **cây nhị phân đầy đủ** lưu trong mảng, mọi node cha thỏa mãn **tính chất heap**:
- **Min-Heap**: Cha ≤ Con
- **Max-Heap**: Cha ≥ Con

### 🗝️ Real-life Analogy (Ví dụ đời thực)

Imagine a **hospital ER waiting room** (Phòng cấp cứu):

| Approach | How it works | Speed |
|----------|-------------|-------|
| **Unsorted list** | Walk through everyone to find most urgent | O(n) to find min |
| **Sorted list** | Most urgent always at front, but inserting takes time | O(n) to insert |
| **Heap (Priority Queue)** | Most urgent always at top, fast insert | O(1) peek, O(log n) insert/remove |

> **Key insight**: Heap gives you the **best of both worlds** — fast access to min/max AND fast insertion.

### Array Representation (Biểu diễn mảng)

```
Index:    0    1    2    3    4    5
Value:   [1,   3,   2,   7,   6,   5]

Tree view:       1          ← root = min
                / \
               3   2
              / \ /
             7  6 5

Parent(i)    = (i-1) // 2
Left(i)      = 2*i + 1
Right(i)     = 2*i + 2
```

---

## 2. Python heapq — Key Operations (Các thao tác chính)

| Operation | Code | Time | Description (Mô tả) |
|-----------|------|------|---------------------|
| **Create heap** | `heapq.heapify(list)` | O(n) | Convert list to heap in-place |
| **Push** | `heapq.heappush(h, val)` | O(log n) | Add element (Thêm phần tử) |
| **Pop min** | `heapq.heappop(h)` | O(log n) | Remove & return min (Bỏ & trả min) |
| **Peek min** | `h[0]` | O(1) | View min without removing |
| **Push + Pop** | `heapq.heappushpop(h, val)` | O(log n) | More efficient than push then pop |
| **nsmallest** | `heapq.nsmallest(k, iterable)` | O(n + k log n) | k smallest elements |
| **nlargest** | `heapq.nlargest(k, iterable)` | O(n + k log n) | k largest elements |

### ⚠️ Python Gotcha: Min-Heap Only!

Python's `heapq` is a **min-heap**. For max-heap, negate the values:

```python
import heapq

# Max-heap trick: negate values (Trick max-heap: đảo dấu)
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)
max_val = -heapq.heappop(max_heap)  # Returns 8 ✅
```

### Custom Objects — Use Tuples

```python
# Sort by priority, then by name (Sort theo ưu tiên, rồi tên)
tasks = []
heapq.heappush(tasks, (1, 'urgent_task'))   # (priority, name)
heapq.heappush(tasks, (3, 'low_task'))
heapq.heappush(tasks, (2, 'medium_task'))

priority, name = heapq.heappop(tasks)  # (1, 'urgent_task')
```

> 🤔 **Think:** If two tuples have the same priority, Python compares the second element. What happens if the second element isn't comparable (e.g., a ListNode)? Answer: Use a counter as tiebreaker: `(priority, counter, object)`.

---

## 3. When to USE Heaps (Khi nào NÊN dùng)

| Scenario (Tình huống) | Why Heap (Tại sao Heap) | Example |
|----------------------|------------------------|---------|
| **"Kth largest/smallest"** | Maintain k elements in heap | LC 215, LC 703 |
| **"Merge K sorted lists"** | Pop min across K → always sorted | LC 23 |
| **"Find median in stream"** | Two heaps: max-heap ∣ min-heap | LC 295 |
| **"Top K frequent"** | Count + min-heap of size k | LC 347 |
| **"Schedule tasks"** | Priority queue of cooldowns | LC 621 |

---

## 4. When NOT to Use Heaps

| Scenario | Why | Use instead |
|----------|-----|-------------|
| Already sorted data | Just index directly | Array indexing O(1) |
| Need ALL elements sorted | Sort is O(n log n), heap sort too | `sorted()` |
| Need element at arbitrary position | Heap only gives min/max | Balanced BST |
| Static data, need kth element | QuickSelect is O(n) avg | QuickSelect |

---

## ❓ Self-Check Questions

1. **What is the time complexity of heapify?** Not O(n log n)! (Heapify mất bao lâu? Không phải O(n log n)!)
2. **How do you implement a max-heap with Python's heapq?** (Làm max-heap thế nào?)
3. **Why use `(priority, counter, object)` instead of `(priority, object)`?** (Tại sao cần counter?)
4. **Is a sorted array always a valid heap?** (Mảng đã sort có phải heap hợp lệ không?)

---

**Next →** [Chapter 2: Patterns (Các dạng bài)](./02_patterns.md)
