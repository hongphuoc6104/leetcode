# 📖 Chapter 3: Complexity Analysis (Phân tích Độ phức tạp)

## 1. Core Operation Complexities (Độ phức tạp thao tác)

| Operation (Thao tác) | Time | Why (Giải thích) |
|----------------------|------|-------------------|
| `heapify(list)` | **O(n)** | Bottom-up sifting (NOT n × O(log n)!) |
| `heappush(h, val)` | **O(log n)** | Sift up at most log n levels |
| `heappop(h)` | **O(log n)** | Sift down at most log n levels |
| `h[0]` (peek min) | **O(1)** | Min is always at root |
| `heappushpop(h, val)` | **O(log n)** | Optimized: avoids double sift |
| `nsmallest(k, list)` | **O(n + k log n)** | Heapify + k pops |
| `nlargest(k, list)` | **O(n + k log n)** | Same approach |

### ⚠️ Why is heapify O(n), not O(n log n)?

Common misconception (Hiểu lầm phổ biến): "heapify = n pushes × log n each = O(n log n)". WRONG!

Actually: heapify sifts DOWN from bottom. Most nodes are at the bottom (short sift). Only root needs full sift.

```
Level 0 (root):     1 node  × sift down log n levels
Level 1:            2 nodes × sift down log(n)-1 levels
Level 2:            4 nodes × sift down log(n)-2 levels
...
Last level:         n/2 nodes × sift down 0 levels
Total: O(n) (mathematical proof uses convergent geometric series)
```

---

## 2. Pattern Complexities (Độ phức tạp theo dạng)

| Pattern | Time | Space | Details |
|---------|------|-------|---------|
| Top K elements | O(n log k) | O(k) | Maintain heap of size k |
| Merge K sorted lists (total N) | O(N log K) | O(K) | K-way merge |
| Two Heaps (Median) | O(n log n) total | O(n) | log n per insert |
| Lazy deletion | O(n log n) | O(n) | Deleted items stay until popped |
| Heap Sort | O(n log n) | O(1) in-place | But not stable! |

### Top K: Heap of Size K vs Full Sort

```
N elements, want top K:
  Sort:       O(N log N)     ← sorts everything
  Heap size K: O(N log K)   ← only maintains K elements
  
  If K << N (e.g. K=10, N=10⁶):
    Sort:  10⁶ × 20 = 2×10⁷
    Heap:  10⁶ × 3.3 = 3.3×10⁶  ← 6x faster!
```

> 🤔 **Think:** When is `sorted(list)[:k]` faster than using a heap? Answer: When k ≈ n (e.g., k = n/2). At that point, sorting is simpler and has better constant factors.

---

## 3. Heap vs Alternatives (Heap vs Các lựa chọn khác)

| Task | Heap | Sorted Array | Hash Map | BST (SortedList) |
|------|------|-------------|----------|-------------------|
| Get min/max | **O(1)** ✅ | O(1) | O(n) | O(log n) |
| Insert | **O(log n)** ✅ | O(n) | O(1) | O(log n) |
| Delete min/max | **O(log n)** ✅ | O(1) amortized | O(n) | O(log n) |
| Delete arbitrary | O(n) | O(n) | O(1) | **O(log n)** ✅ |
| Find kth element | O(k log n) | **O(1)** ✅ | O(n) | O(log n) |

### When Heap WINS: Streaming data (need min/max with insertions)
### When Heap LOSES: Need arbitrary access or deletion

---

## 4. Constraint Guide (Hướng dẫn theo ràng buộc)

| Constraint (Ràng buộc) | Approach | Time |
|------------------------|----------|------|
| n ≤ 10⁴, k ≤ 100 | Heap size k OR sort | Both OK |
| n ≤ 10⁵, k ≤ 10 | **Heap size k** (optimal) | O(n log 10) ≈ O(n) |
| n ≤ 10⁶ | Heap or QuickSelect | O(n) avg |
| Streaming (n unknown) | **Heap** (only option!) | O(log n) per insert |

---

## 5. Common Mistakes (Lỗi thường gặp)

### Mistake 1: Using max-heap with wrong sign
```python
# ❌ Forgot to negate when popping
heapq.heappush(h, -val)
result = heapq.heappop(h)   # Gets -val, not val!

# ✅ Negate both push AND pop
heapq.heappush(h, -val)
result = -heapq.heappop(h)  # Gets val ✅
```

### Mistake 2: Comparing non-comparable elements
```python
# ❌ Tuples with same priority and non-comparable second element
heapq.heappush(h, (5, ListNode(1)))
heapq.heappush(h, (5, ListNode(2)))
# TypeError: '<' not supported between instances of 'ListNode'

# ✅ Use counter as tiebreaker
counter = 0
heapq.heappush(h, (5, counter, ListNode(1))); counter += 1
heapq.heappush(h, (5, counter, ListNode(2))); counter += 1
```

### Mistake 3: Thinking heapify is O(n log n)
```python
# It's O(n)! Don't avoid heapify in favor of n individual pushes.
# ✅ Use heapify when you have all elements upfront
nums = [5, 3, 8, 1, 9]
heapq.heapify(nums)  # O(n), NOT O(n log n)
```

---

## ❓ Self-Check Questions

1. **Prove that heapify is O(n)** by explaining the sift-down approach (Chứng minh heapify O(n))
2. **N = 10⁶, K = 5: Sort vs Heap?** Which is faster and by how much? (N = 10⁶, K = 5: Sort hay Heap nhanh hơn?)
3. **When would you use a BST (SortedList) instead of a Heap?** (Khi nào dùng BST thay Heap?)

---

**← Previous:** [Chapter 2](./02_patterns.md) | **Next →** [Chapter 4: Templates](./04_python_templates.md)
