# 📖 Chapter 1: Introduction to Sorting (Giới thiệu Sắp xếp)

## 🎯 Learning Objectives (Mục tiêu bài học)

After this chapter, you will be able to (Sau bài này, bạn sẽ có thể):
- Classify sorting algorithms by approach (Phân loại thuật toán sắp xếp)
- Explain stability and why it matters (Giải thích tính ổn định)
- Choose the right sort for a given constraint (Chọn đúng sort theo ràng buộc)

---

## 1. Why Learn Sorting? (Tại sao cần học?)

Python has `list.sort()` (Timsort) which is O(n log n) and stable. So why learn sorting algorithms?

### Reason 1: 🏗️ Divide & Conquer Practice
Merge Sort and Quick Sort are the **best examples** of divide & conquer — a technique used everywhere in CS.

### Reason 2: 🎯 Interview Favorites
- **QuickSelect** (from QuickSort) finds kth element in O(n) average
- **Dutch National Flag** (3-way partition) solves LC 75 in one pass
- **Custom comparators** for LC 179 (Largest Number)

### Reason 3: ⚡ Linear-time Sorts
Counting Sort and Radix Sort run in O(n) — beating the O(n log n) comparison limit. Used when values are bounded.

---

## 2. Classification (Phân loại)

| Type (Loại) | Examples (Ví dụ) | Time | Space | Stable? (Ổn định?) |
|------|----------|------|-------|---------|
| **Simple** (Đơn giản) | Bubble, Insertion, Selection | O(n²) | O(1) | Yes (Bubble/Insert) |
| **Efficient** (Hiệu quả) | Merge Sort | O(n log n) | O(n) | ✅ Yes |
| **Efficient** | Quick Sort | O(n log n)* | O(log n) | ❌ No |
| **Efficient** | Heap Sort | O(n log n) | O(1) | ❌ No |
| **Linear** (Tuyến tính) | Counting, Bucket, Radix | O(n+k) | O(k) | ✅ Yes |

\* Quick Sort is O(n²) worst case, but O(n log n) average (trung bình).

---

## 3. Stability (Tính ổn định)

A sort is **stable** if it preserves the relative order of elements with equal keys.

**Sắp xếp ổn định** = các phần tử có key bằng nhau giữ nguyên thứ tự ban đầu.

```
Input:  [(5, 'apple'), (3, 'banana'), (5, 'cherry')]
Stable:  [(3, 'banana'), (5, 'apple'), (5, 'cherry')]   ← apple before cherry ✅
Unstable: [(3, 'banana'), (5, 'cherry'), (5, 'apple')]  ← order flipped ❌
```

> 💡 **Python's Timsort is STABLE!** This enables multi-key sorting:
> ```python
> # Sort by age, then by name (stable: name order preserved within same age)
> students.sort(key=lambda x: x.name)    # Secondary sort first
> students.sort(key=lambda x: x.age)     # Primary sort second
> ```

> 🤔 **Think:** Why must you sort by secondary key FIRST and primary key SECOND when using stable sort? (Tại sao phải sort secondary trước primary?)

---

## 4. When to Use Which? (Khi nào dùng cái nào?)

| Scenario (Tình huống) | Best Algorithm | Why (Tại sao) |
|----------------------|----------------|----------------|
| General purpose (Mục đích chung) | **Timsort** (Python default) | O(n log n), stable, optimized |
| Nearly sorted data (Gần đã sắp xếp) | **Insertion Sort** | O(n) for nearly sorted! |
| Memory-constrained (Giới hạn bộ nhớ) | **Heap Sort** | O(1) extra space |
| Linked list sorting | **Merge Sort** | No random access needed |
| Small integer range (Khoảng giá trị nhỏ) | **Counting Sort** | O(n+k), k = range |
| Find kth element only (Tìm phần tử thứ k) | **QuickSelect** | O(n) average |
| Custom ordering (Thứ tự tùy chỉnh) | **Python sort with key/cmp** | Use `key=lambda` |

---

## ❓ Self-Check Questions

1. **Is Quick Sort stable?** If not, give an example where order changes (Quick Sort có ổn định không? Cho ví dụ).
2. **Why can Counting Sort be O(n)?** What makes it different from comparison sorts? (Tại sao Counting Sort O(n)?)
3. **An array is "almost sorted" (2 elements swapped). Which algorithm is fastest?** (Mảng gần đã sắp xếp — thuật toán nào nhanh nhất?)

---

**Next →** [Chapter 2: Patterns (Các dạng)](./02_patterns.md)
