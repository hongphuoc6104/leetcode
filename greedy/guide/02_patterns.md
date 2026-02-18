# 📖 Chapter 2: Greedy Patterns (Các dạng bài Greedy)

## Pattern 1: Intervals — Sort by End Time (Sắp xếp theo thời gian kết thúc)

### 🔍 Signal: "non-overlapping", "max meetings", "min arrows", "merge intervals"

### 💡 Key Insight (Ý tưởng chính)

Sort intervals by **end time**. Always pick the interval that **ends earliest** — this leaves the most room for future intervals.

**Tại sao sort theo end time?** Vì chọn interval kết thúc sớm nhất → còn nhiều chỗ nhất cho interval tiếp theo.

```python
def erase_overlap_intervals(intervals):
    """LC 435: Min removals to make non-overlapping."""
    intervals.sort(key=lambda x: x[1])  # Sort by end!
    end, count = float('-inf'), 0
    for s, e in intervals:
        if s >= end:
            end = e      # Non-overlapping → keep, update end
        else:
            count += 1   # Overlap → remove this one
    return count
```

### 🪲 Common Bug (Lỗi thường gặp)

```python
# ❌ WRONG: Sort by START time
intervals.sort(key=lambda x: x[0])
# With [[1,10], [2,3], [3,4]]:
#   Keeps [1,10], removes [2,3] and [3,4]  → removes 2
# ✅ RIGHT: Sort by END time
intervals.sort(key=lambda x: x[1])
# With [[2,3], [3,4], [1,10]]:
#   Keeps [2,3] and [3,4], removes [1,10] → removes 1 ← BETTER!
```

> 🤔 **Think:** Why does sorting by end time always give better results than sorting by start time? (Tại sao sort theo end time luôn tốt hơn?)

### Related Problems
📌 LC 435 (Non-overlapping), LC 452 (Burst Balloons), LC 56 (Merge Intervals), LC 253 (Meeting Rooms II)

---

## Pattern 2: Jump / Reachability — Track Max (Theo dõi farthest)

### 🔍 Signal: "can jump", "min jumps", "farthest reachable"

### 💡 Key Insight

Track `farthest` reachable index. If current position `i > farthest`, we're stuck — return False.

**Ý tưởng:** Theo dõi vị trí xa nhất có thể đến. Nếu `i > farthest`, bị kẹt → trả False.

```python
def can_jump(nums):
    """LC 55: Can we reach the last index? O(n)."""
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False   # Can't reach position i
        farthest = max(farthest, i + jump)
    return True

def jump_game_ii(nums):
    """LC 45: Minimum jumps to reach last index. O(n)."""
    jumps = 0
    current_end = 0   # Right boundary of current jump range
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= len(nums) - 1:
                break
    return jumps
```

### 🪲 Common Bug

```python
# ❌ WRONG: iterate to len(nums) (including last element)
for i in range(len(nums)):   # BUG: jumps from last index unnecessarily!

# ✅ RIGHT: iterate to len(nums) - 1
for i in range(len(nums) - 1):  # Don't need to jump FROM the last element
```

📌 LC 55, LC 45

---

## Pattern 3: Two Pointers + Sort — Pair Elements (Ghép cặp)

### 🔍 Signal: "pair elements", "minimize cost", "assign cookies", "boats"

### 💡 Key Insight

Sort the array. Then use two pointers: match **smallest with largest** (or check if they fit together).

**Ý tưởng:** Sort mảng. Dùng 2 con trỏ: ghép **nhỏ nhất với lớn nhất**.

```python
def num_rescue_boats(people, limit):
    """LC 881: Min boats. Each boat carries at most 2. O(n log n)."""
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1   # Carry the light person too!
        right -= 1       # Always carry the heavy person
        boats += 1
    return boats
```

### 🪲 Common Bug

```python
# ❌ WRONG: Always carry two people
while left < right:   # BUG: misses the case when left == right (1 person left)

# ✅ RIGHT: Use left <= right to handle the last single person
while left <= right:
```

📌 LC 881 (Boats), LC 455 (Assign Cookies), LC 870 (Advantage Shuffle)

---

## Pattern 4: Local Peak/Valley — Stock Trading (Đỉnh/Đáy cục bộ)

### 🔍 Signal: "buy and sell stock II (multiple transactions)", "max profit"

### 💡 Key Insight

If tomorrow's price > today's price, we "virtually" buy today and sell tomorrow. Accumulate ALL positive slopes.

**Ý tưởng:** Nếu giá mai > giá hôm nay, coi như mua hôm nay bán ngày mai. Cộng TẤT CẢ các đoạn tăng.

```python
def max_profit_ii(prices):
    """LC 122: Stock II — unlimited transactions. O(n)."""
    return sum(max(prices[i] - prices[i-1], 0) 
               for i in range(1, len(prices)))
```

This is equivalent to: buy at every valley, sell at every peak.

### Tracing Example (Ví dụ chi tiết)

```
Prices: [7, 1, 5, 3, 6, 4]
         ↓  ↑4  ↓  ↑3  ↓
Day 1→2: 1-7 = -6 → 0 (skip)
Day 2→3: 5-1 = +4 → +4 ✅
Day 3→4: 3-5 = -2 → 0 (skip)
Day 4→5: 6-3 = +3 → +3 ✅
Day 5→6: 4-6 = -2 → 0 (skip)
Total: 4 + 3 = 7 ✅
```

📌 LC 122

---

## Pattern 5: Partition Labels — Last Occurrence (Phân tách theo xuất hiện cuối)

### 🔍 Signal: "split string", "characters appear in one part only"

### 💡 Key Insight

Record `last_index` of every character. Iterate and extend current partition boundary to include all characters' last occurrences.

**Ý tưởng:** Ghi `last_index` mỗi ký tự. Duyệt và mở rộng biên partition để bao hết.

```python
def partition_labels(s):
    """LC 763: Partition so each char in at most one part. O(n)."""
    # Pass 1: find last index of each char
    last = {c: i for i, c in enumerate(s)}
    
    j = anchor = 0
    result = []
    
    # Pass 2: extend partition end greedily
    for i, c in enumerate(s):
        j = max(j, last[c])     # Must include last occurrence
        if i == j:               # Reached end of partition!
            result.append(i - anchor + 1)
            anchor = i + 1
    return result
```

### Tracing Example

```
s = "ababcbacadefegdehijhklij"
     ↑ a last=8, b last=5, c last=7 → partition end = 8
                  ↑ i=8, j=8 → partition [0:9] = "ababcbaca" (len 9)
                   ↑ d last=14, e last=15, f last=11 → partition end = 15
                                  ...
Result: [9, 7, 8]
```

📌 LC 763

---

## 📊 Decision Table: Which Pattern to Use? (Bảng quyết định)

| Signal (Dấu hiệu) | Pattern | Time |
|---------------------|---------|------|
| "Non-overlapping intervals" | Sort by end time | O(n log n) |
| "Can reach / min jumps" | Track farthest | O(n) |
| "Pair elements / boats" | Sort + two pointers | O(n log n) |
| "Buy/sell stock II" | Accumulate positive diffs | O(n) |
| "Split string / partition" | Last occurrence map | O(n) |
| "Gas station / circular" | Running sum, reset at negative | O(n) |

---

## ❓ Self-Check Questions

1. **LC 435: Why sort by END time, not START time?** Give a counter-example.
2. **LC 55: What would happen if you used BFS instead of Greedy?** What's the time?
3. **LC 122: The stock II solution seems too simple. Can you prove it's optimal?**
4. **Name a problem that LOOKS Greedy but isn't.** (Kể 1 bài trông Greedy nhưng cần DP)

---

**← Previous:** [Chapter 1](./01_introduction.md) | **Next →** [Chapter 3: Complexity](./03_complexity.md)
