# 📖 Chủ đề 13: Greedy

## Lý thuyết cơ bản

**Greedy** chọn phương án tối ưu **cục bộ** tại mỗi bước, hy vọng đạt tối ưu **toàn cục**. Không phải lúc nào cũng đúng — cần chứng minh tính đúng đắn.

### Khi nào dùng Greedy?
- Bài có **optimal substructure** và **greedy choice property**
- Thường liên quan: sắp xếp, intervals, scheduling

### Pattern phổ biến
```python
# Interval scheduling (chọn tối đa intervals không overlap)
def max_non_overlap(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count = 0
    end = float('-inf')
    for start, finish in intervals:
        if start >= end:
            count += 1
            end = finish
    return count

# Jump Game
def can_jump(nums):
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
    return True
```

---

## Danh sách 30 bài LeetCode

### 🟢 Easy (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Assign Cookies | [LC 455](https://leetcode.com/problems/assign-cookies/) | Sort cả 2, match nhỏ→lớn |
| 2 | Can Place Flowers | [LC 605](https://leetcode.com/problems/can-place-flowers/) | Check left/right empty |
| 3 | Valid Palindrome II | [LC 680](https://leetcode.com/problems/valid-palindrome-ii/) | Skip 1 char, check |
| 4 | Lemonade Change | [LC 860](https://leetcode.com/problems/lemonade-change/) | Track $5, $10 bills |
| 5 | DI String Match | [LC 942](https://leetcode.com/problems/di-string-match/) | D→max, I→min |
| 6 | Max Sum K Negations | [LC 1005](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/) | Sort, negate smallest |
| 7 | Max Units Truck | [LC 1710](https://leetcode.com/problems/maximum-units-on-a-truck/) | Sort by units desc |
| 8 | Min Moves Seat | [LC 2037](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/) | Sort both, pair up |
| 9 | Min Cost Candies | [LC 2144](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/) | Sort desc, free every 3rd |
| 10 | Distribute Money | [LC 2591](https://leetcode.com/problems/distribute-money-to-maximum-children/) | Greedy allocation |

### 🟡 Medium (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Jump Game II | [LC 45](https://leetcode.com/problems/jump-game-ii/) | BFS/greedy, max reach |
| 2 | Jump Game | [LC 55](https://leetcode.com/problems/jump-game/) | Track max reachable |
| 3 | Gas Station | [LC 134](https://leetcode.com/problems/gas-station/) | If total ≥ 0, find start |
| 4 | Wiggle Subsequence | [LC 376](https://leetcode.com/problems/wiggle-subsequence/) | Count direction changes |
| 5 | Non-overlapping Intervals | [LC 435](https://leetcode.com/problems/non-overlapping-intervals/) | Sort by end, count remove |
| 6 | Min Arrows Balloons | [LC 452](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Sort by end, merge |
| 7 | Task Scheduler | [LC 621](https://leetcode.com/problems/task-scheduler/) | Math: idle slots |
| 8 | Partition Labels | [LC 763](https://leetcode.com/problems/partition-labels/) | Track last occurrence |
| 9 | Hand of Straights | [LC 846](https://leetcode.com/problems/hand-of-straights/) | Counter + sort |
| 10 | Two City Scheduling | [LC 1029](https://leetcode.com/problems/two-city-scheduling/) | Sort by cost diff |

### 🔴 Hard (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Candy | [LC 135](https://leetcode.com/problems/candy/) | Two pass, left→right, right→left |
| 2 | Remove Dup Letters | [LC 316](https://leetcode.com/problems/remove-duplicate-letters/) | Stack + greedy |
| 3 | Patching Array | [LC 330](https://leetcode.com/problems/patching-array/) | Track reachable range |
| 4 | Remove K Digits | [LC 402](https://leetcode.com/problems/remove-k-digits/) | Monotonic stack |
| 5 | Course Schedule III | [LC 630](https://leetcode.com/problems/course-schedule-iii/) | Sort + max-heap |
| 6 | Set Intersection ≥ 2 | [LC 757](https://leetcode.com/problems/set-intersection-size-at-least-two/) | Sort by end |
| 7 | Min Refueling Stops | [LC 871](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | Max-heap greedy |
| 8 | Max Team Performance | [LC 1383](https://leetcode.com/problems/maximum-performance-of-a-team/) | Sort + min-heap |
| 9 | Max Non-overlap Substr | [LC 1520](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/) | Greedy substring |
| 10 | Max Binary String | [LC 1702](https://leetcode.com/problems/maximum-binary-string-after-change/) | Move zeros |

---

## Tips
- **Sort** thường là bước đầu tiên trong Greedy
- Nếu Greedy không đúng → thử **DP**
- Interval problems: sort by **end time** (scheduling) hoặc **start time** (merge)
