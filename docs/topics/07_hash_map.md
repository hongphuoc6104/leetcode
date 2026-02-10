# 📖 Chủ đề 7: Hash Map / Set

## Lý thuyết cơ bản

**Hash Map** (dict) và **Hash Set** (set) cho phép tra cứu, thêm, xóa trong **O(1)** trung bình.

### Python Implementation
```python
# Hash Map
d = {}
d[key] = value           # O(1)
val = d.get(key, default) # O(1)
del d[key]               # O(1)

# Hash Set
s = set()
s.add(x)                 # O(1)
s.remove(x)              # O(1)
x in s                   # O(1)

# Counter (đếm tần suất)
from collections import Counter
count = Counter(arr)     # O(n)
count.most_common(k)     # Top k phần tử

# defaultdict
from collections import defaultdict
graph = defaultdict(list)
```

### Pattern: Prefix Sum + Hash Map
```python
# Đếm subarray có tổng = k
def subarray_sum(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count
```

---

## Danh sách 30 bài LeetCode

### 🟢 Easy (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Two Sum | [LC 1](https://leetcode.com/problems/two-sum/) | Hash map complement |
| 2 | Single Number | [LC 136](https://leetcode.com/problems/single-number/) | XOR hoặc set |
| 3 | Happy Number | [LC 202](https://leetcode.com/problems/happy-number/) | Set detect cycle |
| 4 | Isomorphic Strings | [LC 205](https://leetcode.com/problems/isomorphic-strings/) | Two maps, bijection |
| 5 | Contains Duplicate | [LC 217](https://leetcode.com/problems/contains-duplicate/) | Set |
| 6 | Valid Anagram | [LC 242](https://leetcode.com/problems/valid-anagram/) | Counter hoặc sort |
| 7 | Word Pattern | [LC 290](https://leetcode.com/problems/word-pattern/) | Bijection mapping |
| 8 | Intersection of Arrays | [LC 349](https://leetcode.com/problems/intersection-of-two-arrays/) | Set intersection |
| 9 | Ransom Note | [LC 383](https://leetcode.com/problems/ransom-note/) | Counter |
| 10 | First Unique Char | [LC 387](https://leetcode.com/problems/first-unique-character-in-a-string/) | Counter, first freq=1 |

### 🟡 Medium (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Valid Sudoku | [LC 36](https://leetcode.com/problems/valid-sudoku/) | Sets cho row/col/box |
| 2 | Group Anagrams | [LC 49](https://leetcode.com/problems/group-anagrams/) | Sorted key → group |
| 3 | Longest Consecutive | [LC 128](https://leetcode.com/problems/longest-consecutive-sequence/) | Set, tìm start |
| 4 | LRU Cache | [LC 146](https://leetcode.com/problems/lru-cache/) | OrderedDict or DLL+hash |
| 5 | Fraction to Decimal | [LC 166](https://leetcode.com/problems/fraction-to-recurring-decimal/) | Hash track remainder |
| 6 | Top K Frequent | [LC 347](https://leetcode.com/problems/top-k-frequent-elements/) | Counter + heap |
| 7 | Insert Delete Random | [LC 380](https://leetcode.com/problems/insert-delete-getrandom-o1/) | List + hash map |
| 8 | Find All Anagrams | [LC 438](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Sliding window + counter |
| 9 | Continuous Subarray Sum | [LC 523](https://leetcode.com/problems/continuous-subarray-sum/) | Prefix sum mod k |
| 10 | Subarray Sum = K | [LC 560](https://leetcode.com/problems/subarray-sum-equals-k/) | Prefix sum + hash |

### 🔴 Hard (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Substring Concatenation | [LC 30](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | Hash + window |
| 2 | Min Window Substring | [LC 76](https://leetcode.com/problems/minimum-window-substring/) | Hash + sliding |
| 3 | Max Points on Line | [LC 149](https://leetcode.com/problems/max-points-on-a-line/) | Hash map slopes |
| 4 | LFU Cache | [LC 460](https://leetcode.com/problems/lfu-cache/) | Multi-hash + DLL |
| 5 | First Missing Positive | [LC 41](https://leetcode.com/problems/first-missing-positive/) | In-place hash |
| 6 | All O'one DS | [LC 432](https://leetcode.com/problems/all-oone-data-structure/) | DLL + hash |
| 7 | Random Pick Blacklist | [LC 710](https://leetcode.com/problems/random-pick-with-blacklist/) | Remap |
| 8 | Number of Atoms | [LC 726](https://leetcode.com/problems/number-of-atoms/) | Stack + hash |
| 9 | Max Freq Stack | [LC 895](https://leetcode.com/problems/maximum-frequency-stack/) | Freq → stack |
| 10 | K Different Integers | [LC 992](https://leetcode.com/problems/subarrays-with-k-different-integers/) | atMost sliding |

---

## Tips
- Hash map giải quyết hầu hết bài "find pair/duplicate" trong O(n)
- **Prefix Sum + Hash Map** = combo mạnh cho subarray problems
- Cẩn thận **collision** trong lý thuyết, nhưng Python dict xử lý tốt
