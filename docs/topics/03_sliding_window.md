# 📖 Chủ đề 3: Sliding Window

## Lý thuyết cơ bản

**Sliding Window** là kỹ thuật duy trì một "cửa sổ" trượt trên mảng/chuỗi. Thay vì tính lại toàn bộ, ta chỉ cập nhật khi cửa sổ mở rộng hoặc thu hẹp.

### Hai dạng chính
1. **Fixed size window**: Cửa sổ có kích thước cố định k
2. **Variable size window**: Cửa sổ thay đổi kích thước theo điều kiện

### Template
```python
# Fixed size window
def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    result = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Thêm mới, bỏ cũ
        result = max(result, window_sum)
    return result

# Variable size window
def variable_window(s):
    left = 0
    window = {}  # hoặc set, counter
    result = 0
    for right in range(len(s)):
        # Mở rộng cửa sổ: thêm s[right]
        window[s[right]] = window.get(s[right], 0) + 1
        
        # Thu hẹp khi vi phạm điều kiện
        while invalid_condition(window):
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        
        result = max(result, right - left + 1)
    return result
```

---

## Complexity Analysis

| Dạng | Time | Space |
|------|------|-------|
| Fixed size | O(n) | O(1) hoặc O(k) |
| Variable size | O(n) | O(k) - k là kích thước alphabet/window |

---

## Danh sách 30 bài LeetCode

### 🟢 Easy (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Best Time to Buy/Sell Stock | [LC 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Track min, max profit |
| 2 | Contains Duplicate II | [LC 219](https://leetcode.com/problems/contains-duplicate-ii/) | Fixed window + set |
| 3 | Max Average Subarray I | [LC 643](https://leetcode.com/problems/maximum-average-subarray-i/) | Fixed window sum |
| 4 | Max Consecutive Ones III | [LC 1004](https://leetcode.com/problems/max-consecutive-ones-iii/) | Variable window, đếm zeros |
| 5 | Consecutive Characters | [LC 1446](https://leetcode.com/problems/consecutive-characters/) | Track current run |
| 6 | Min Difference | [LC 1984](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) | Sort + fixed window |
| 7 | K-Beauty | [LC 2269](https://leetcode.com/problems/find-the-k-beauty-of-a-number/) | Fixed window on digits |
| 8 | Substrings Size Three | [LC 1876](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/) | Fixed window k=3 |
| 9 | Longest Harmonious Subseq | [LC 594](https://leetcode.com/problems/longest-harmonious-subsequence/) | Hash map counting |
| 10 | Min Recolors | [LC 2379](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/) | Fixed window |

### 🟡 Medium (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Longest Substring No Repeat | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Variable window + set |
| 2 | Longest with 2 Distinct | [LC 159](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) | Variable + hash map |
| 3 | Min Size Subarray Sum | [LC 209](https://leetcode.com/problems/minimum-size-subarray-sum/) | Variable, tìm min length |
| 4 | Longest Repeating Replace | [LC 424](https://leetcode.com/problems/longest-repeating-character-replacement/) | Window - maxFreq ≤ k |
| 5 | Find All Anagrams | [LC 438](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Fixed window + freq count |
| 6 | Permutation in String | [LC 567](https://leetcode.com/problems/permutation-in-string/) | Tương tự 438 |
| 7 | Subarray Product < K | [LC 713](https://leetcode.com/problems/subarray-product-less-than-k/) | Variable window, product |
| 8 | Fruit Into Baskets | [LC 904](https://leetcode.com/problems/fruit-into-baskets/) | Variable, max 2 types |
| 9 | Get Equal Substrings | [LC 1208](https://leetcode.com/problems/get-equal-substrings-within-budget/) | Variable, cost ≤ budget |
| 10 | Max Vowels in Substring | [LC 1456](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Fixed window |

### 🔴 Hard (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Substring Concatenation | [LC 30](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | Fixed window, word-level |
| 2 | Min Window Substring | [LC 76](https://leetcode.com/problems/minimum-window-substring/) | Variable, tìm min contain |
| 3 | Sliding Window Maximum | [LC 239](https://leetcode.com/problems/sliding-window-maximum/) | Monotonic deque |
| 4 | Sliding Window Median | [LC 480](https://leetcode.com/problems/sliding-window-median/) | Two heaps |
| 5 | Smallest Range K Lists | [LC 632](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | Heap + sliding |
| 6 | Min Window Subsequence | [LC 727](https://leetcode.com/problems/minimum-window-subsequence/) | DP hoặc two pointers |
| 7 | Shortest Subarray Sum ≥ K | [LC 862](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | Deque + prefix sum |
| 8 | Subarrays K Different | [LC 992](https://leetcode.com/problems/subarrays-with-k-different-integers/) | exactly(K) = atMost(K) - atMost(K-1) |
| 9 | Min K Consecutive Flips | [LC 995](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/) | Greedy + queue |
| 10 | Submatrices Sum Target | [LC 1074](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/) | 2D prefix + hash |

---

## Tips
- Nếu bài yêu cầu **subarray/substring liên tục**, nghĩ đến Sliding Window
- **Fixed** khi biết kích thước cửa sổ, **Variable** khi tìm kích thước tối ưu
- Kết hợp với **hash map** để track tần suất ký tự/phần tử
