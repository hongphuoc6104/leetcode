# 📖 Chapter 4: Python Templates (Templates Python)

## Template 1: Interval Scheduling (Max Non-overlapping)

```python
def erase_overlap_intervals(intervals):
    """Sort by END time. Keep earliest ending. (Sort theo end, giữ cái kết thúc sớm nhất)"""
    if not intervals: return 0
    intervals.sort(key=lambda x: x[1])  # ← KEY: sort by end!
    end = intervals[0][1]
    count = 0  # Number to remove (Số cần xóa)
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1        # Overlap → remove this one
        else:
            end = intervals[i][1]  # No overlap → update end
    return count
```

## Template 2: Jump Game (Greedy Reachability)

```python
def can_jump(nums):
    """Track max reach. O(n). (Theo dõi vị trí xa nhất)"""
    farthest = 0
    for i, n in enumerate(nums):
        if i > farthest:
            return False     # Can't reach position i
        farthest = max(farthest, i + n)
    return True  # Farthest >= last index
```

## Template 3: Jump Game II (Min Jumps)

```python
def jump_game_ii(nums):
    """Min jumps to reach end. O(n). (Số nhảy ít nhất)"""
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(len(nums) - 1):  # ← Don't process last index!
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= len(nums) - 1:
                break
    return jumps
```

## Template 4: Gas Station (Circular Tour)

```python
def can_complete_circuit(gas, cost):
    """If total_gas < total_cost → impossible.
    Else, start where tank doesn't dip below 0.
    (Nếu tổng gas < tổng cost → không thể. Bắt đầu ở nơi tank không âm.)"""
    if sum(gas) < sum(cost):
        return -1
    total, start = 0, 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            total = 0
            start = i + 1  # Reset start to next station
    return start
```

## Template 5: Two Pointers — Boats

```python
def num_rescue_boats(people, limit):
    """Sort + pair heaviest with lightest. (Sort + ghép nặng nhất với nhẹ nhất)"""
    people.sort()
    l, r = 0, len(people) - 1
    boats = 0
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1        # Light person fits on same boat
        r -= 1             # Heavy person always uses a boat
        boats += 1
    return boats
```

## Template 6: Partition Labels

```python
def partition_labels(s):
    """Two-pass: last occurrence map → extend partition.
    (2 bước: map xuất hiện cuối → mở rộng partition)"""
    last = {c: i for i, c in enumerate(s)}
    j = anchor = 0
    result = []
    for i, c in enumerate(s):
        j = max(j, last[c])
        if i == j:
            result.append(i - anchor + 1)
            anchor = i + 1
    return result
```

## Template 7: Stock Trading II (Unlimited Transactions)

```python
def max_profit(prices):
    """Accumulate all positive price differences (Cộng mọi chênh lệch dương)"""
    return sum(max(prices[i] - prices[i-1], 0)
               for i in range(1, len(prices)))
```

## Template 8: Merge Intervals

```python
def merge(intervals):
    """Sort by start. Merge overlapping. (Sort theo start. Gộp chồng lấn.)"""
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= result[-1][1]:
            result[-1][1] = max(result[-1][1], e)  # Extend
        else:
            result.append([s, e])
    return result
```

---

## 📋 Pre-Coding Checklist (Checklist trước khi code)

1. ✅ **Can Greedy work?** Does local optimal = global optimal? (Tham lam cục bộ = tối ưu toàn cục?)
2. ✅ **Need sorting?** Most Greedy problems start with `sort()` (Cần sort không?)
3. ✅ **Sort by what?** Start time? End time? Value? Weight? (Sort theo cái gì?)
4. ✅ **Counter-example?** Try small inputs to see if Greedy fails (Thử input nhỏ)
5. ✅ **Edge cases?** n=0, n=1, all same values, negative values (Trường hợp đặc biệt)
6. ✅ **Prove or trust?** In interviews, argue why Greedy works with the interviewer (Trong phỏng vấn, giải thích tại sao Greedy đúng)

---

## 🔄 Optimization Table (Bảng tối ưu)

| From BF | To Greedy | How |
|---------|-----------|-----|
| Try all pairs of intervals O(n²) | Sort by end + single pass O(n log n) | Sort key = end time |
| BFS/DFS all positions O(n²) | Track farthest O(n) | Single variable |
| Try all pairs of people O(n²) | Sort + two pointers O(n log n) | Match heavy + light |
| Check all transaction combos O(2ⁿ) | Sum positive diffs O(n) | Greedy observation |

---

**← Previous:** [Chapter 3](./03_complexity.md) | **Next →** [Examples](../examples/) 🚀
