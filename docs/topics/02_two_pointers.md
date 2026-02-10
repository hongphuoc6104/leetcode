# 📖 Chủ đề 2: Two Pointers

## Lý thuyết cơ bản

**Two Pointers** là kỹ thuật dùng 2 con trỏ di chuyển trên mảng/chuỗi để giảm complexity từ O(n²) xuống O(n).

### Các dạng Two Pointers
1. **Opposite direction**: 2 con trỏ đi từ 2 đầu vào giữa (ví dụ: palindrome, 2Sum sorted)
2. **Same direction**: 2 con trỏ đi cùng hướng, tốc độ khác nhau (ví dụ: remove duplicates, fast/slow)
3. **Fast & Slow**: 1 nhanh 1 chậm, thường dùng cho linked list cycle detection

### Template cơ bản
```python
# Dạng 1: Opposite direction
def two_pointer_opposite(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if condition:
            left += 1
        else:
            right -= 1

# Dạng 2: Same direction (remove duplicates)
def two_pointer_same(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1
```

---

## Complexity Analysis

| Dạng | Time | Space |
|------|------|-------|
| Opposite direction | O(n) | O(1) |
| Same direction | O(n) | O(1) |
| Fast & Slow | O(n) | O(1) |

---

## Danh sách 30 bài LeetCode

### 🟢 Easy (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Remove Duplicates | [LC 26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Same direction |
| 2 | Remove Element | [LC 27](https://leetcode.com/problems/remove-element/) | Same direction |
| 3 | Merge Sorted Array | [LC 88](https://leetcode.com/problems/merge-sorted-array/) | Merge từ cuối |
| 4 | Valid Palindrome | [LC 125](https://leetcode.com/problems/valid-palindrome/) | Opposite direction |
| 5 | Two Sum II | [LC 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Opposite, sorted array |
| 6 | Move Zeroes | [LC 283](https://leetcode.com/problems/move-zeroes/) | Same direction |
| 7 | Reverse String | [LC 344](https://leetcode.com/problems/reverse-string/) | Opposite direction, swap |
| 8 | Is Subsequence | [LC 392](https://leetcode.com/problems/is-subsequence/) | Same direction |
| 9 | Reverse Words III | [LC 557](https://leetcode.com/problems/reverse-words-in-a-string-iii/) | Reverse từng từ |
| 10 | Squares of Sorted Array | [LC 977](https://leetcode.com/problems/squares-of-a-sorted-array/) | Opposite, so sánh abs |

### 🟡 Medium (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Container With Most Water | [LC 11](https://leetcode.com/problems/container-with-most-water/) | Opposite, di chuyển bên nhỏ |
| 2 | 3Sum | [LC 15](https://leetcode.com/problems/3sum/) | Sort + 2 pointers |
| 3 | 3Sum Closest | [LC 16](https://leetcode.com/problems/3sum-closest/) | Tương tự 3Sum |
| 4 | 4Sum | [LC 18](https://leetcode.com/problems/4sum/) | Fix 2 + 2 pointers |
| 5 | Sort Colors | [LC 75](https://leetcode.com/problems/sort-colors/) | Dutch National Flag |
| 6 | Remove Duplicates II | [LC 80](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | Cho phép 2 lần |
| 7 | Linked List Cycle II | [LC 142](https://leetcode.com/problems/linked-list-cycle-ii/) | Fast & Slow |
| 8 | Reverse Words | [LC 151](https://leetcode.com/problems/reverse-words-in-a-string/) | Reverse all + reverse each |
| 9 | Longest Word in Dict | [LC 524](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/) | Subsequence check |
| 10 | Interval List Intersections | [LC 986](https://leetcode.com/problems/interval-list-intersections/) | 2 pointers trên 2 list |

### 🔴 Hard (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Substring with Concatenation | [LC 30](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | Sliding window biến thể |
| 2 | Trapping Rain Water | [LC 42](https://leetcode.com/problems/trapping-rain-water/) | Two pointers opposite |
| 3 | Minimum Window Substring | [LC 76](https://leetcode.com/problems/minimum-window-substring/) | Sliding window |
| 4 | Word Ladder II | [LC 126](https://leetcode.com/problems/word-ladder-ii/) | BFS + backtrack |
| 5 | Trapping Rain Water II | [LC 407](https://leetcode.com/problems/trapping-rain-water-ii/) | BFS + heap (3D) |
| 6 | Random Pick with Blacklist | [LC 710](https://leetcode.com/problems/random-pick-with-blacklist/) | Hash map remapping |
| 7 | Count Unique Characters | [LC 828](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/) | Contribution counting |
| 8 | Shortest Subarray Sum ≥ K | [LC 862](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | Deque + prefix sum |
| 9 | 3Sum With Multiplicity | [LC 923](https://leetcode.com/problems/3sum-with-multiplicity/) | Counting + 2 pointers |
| 10 | Subarrays K Different | [LC 992](https://leetcode.com/problems/subarrays-with-k-different-integers/) | atMost(K) - atMost(K-1) |

---

## Tips
- Luôn kiểm tra mảng đã **sorted** chưa trước khi dùng opposite direction
- **Same direction** thường dùng cho in-place modification
- Khi gặp bài "find pair", nghĩ đến Two Pointers trước hash map
