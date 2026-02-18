# 📖 Chapter 3: Complexity Analysis (Phân tích Độ phức tạp)

## 1. Comparison Table (Bảng so sánh)

| Algorithm (Thuật toán) | Best | Average | Worst | Space | Stable? |
|-----------|------|---------|-------|-------|---------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | ❌ No |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ Yes |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ No |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ No |
| **Counting Sort** | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ Yes |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n+k) | ✅ Yes |
| **Timsort** (Python) | O(n) | O(n log n) | O(n log n) | O(n) | ✅ Yes |

### Key observations:
- **Insertion Sort** has O(n) best case — excellent for **nearly sorted** data!
- **Quick Sort** is O(n²) worst case but is **fastest in practice** due to cache locality
- **Timsort** is O(n) for already sorted data — Python's default!

---

## 2. The O(n log n) Lower Bound (Giới hạn dưới)

### Why can't comparison sorts be faster than O(n log n)?

Any comparison-based sort must distinguish between n! permutations. Each comparison gives 1 bit of info. So we need at least **log₂(n!)** comparisons.

```
log₂(n!) ≈ n log₂(n) (Stirling's approximation)
```

Therefore: **O(n log n) is optimal for comparison-based sorting.**

> 🤔 **Think:** Counting Sort is O(n). Does it violate this limit? (Counting Sort O(n) — có vi phạm giới hạn này không?) **No!** It's not comparison-based — it uses values as indices.

---

## 3. Space Complexity Details (Chi tiết không gian)

| Algorithm | Auxiliary space | Why |
|-----------|----------------|-----|
| **Merge Sort** | O(n) | Need temp array for merging |
| **Quick Sort** | O(log n) avg, O(n) worst | Recursion stack |
| **Heap Sort** | O(1) | In-place heap operations |
| **Timsort** | O(n) worst, O(1) best | Merge buffer for runs |
| **Counting Sort** | O(k) | Count array of size k |

---

## 4. Constraint Guide (Hướng dẫn theo ràng buộc)

| Constraint (Ràng buộc) | Max feasible | Recommended Sort |
|------------------------|-------------|-----------------|
| n ≤ 50 | O(n²) ✅ | Any sort works — even Bubble |
| n ≤ 10⁴ | O(n²) ✅ | Insertion Sort for nearly sorted |
| n ≤ 10⁵ | O(n log n) | `sort()`, Merge Sort, Quick Sort |
| n ≤ 10⁶ | O(n log n) | `sort()` — Timsort handles this |
| n ≤ 10⁷, values bounded | O(n) | **Counting Sort / Radix** |
| n ≤ 10⁸ | O(n) | Only linear-time algorithms |

---

## 5. Common Mistakes (Lỗi thường gặp)

### Mistake 1: QuickSort worst case
```python
# ❌ Always picking first/last element as pivot on sorted array
# → O(n²) because every partition has n-1 and 0 elements
# ✅ Fix: Use random pivot or median-of-three
import random
pivot_idx = random.randint(low, high)
arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
```

### Mistake 2: Not using Python's built-in sort
```python
# ❌ Writing your own sort for a normal sorting problem
# Timsort is highly optimized — faster than your QuickSort!
# ✅ Use sorted() or list.sort() unless the problem asks otherwise
```

### Mistake 3: Wrong stability assumption
```python
# ❌ Assuming QuickSort preserves order of equal elements
# Quick Sort is UNSTABLE — equal elements may swap
# ✅ Use Merge Sort or Timsort when stability matters
```

---

## ❓ Self-Check Questions

1. **Why is Insertion Sort O(n) on nearly sorted data?** (Tại sao Insertion Sort O(n) trên mảng gần sorted?)
2. **Quick Sort is O(n²) worst case but preferred over Merge Sort. Why?** (Quick Sort xấu nhất O(n²) nhưng thường dùng hơn Merge Sort. Tại sao?)
3. **How many comparisons does any comparison sort need at minimum for n=8 elements?** (Cần tối thiểu bao nhiêu phép so sánh cho 8 phần tử?)

---

**← Previous:** [Chapter 2](./02_patterns.md) | **Next →** [Chapter 4: Templates](./04_python_templates.md)
