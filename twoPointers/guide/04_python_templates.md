# 📖 Chapter 4: Python Templates (Templates Python sẵn dùng)

## ✅ Pre-Coding Checklist (Kiểm tra trước khi code)

```
□ 1. Is the array SORTED? If not, do I need to sort it?
     (Mảng đã SORTED chưa? Nếu chưa, cần sort không?)

□ 2. Which variant? Opposite / Same Direction / Fast-Slow?
     (Biến thể nào?)

□ 3. What determines pointer movement?
     (Điều gì quyết định di chuyển con trỏ?)

□ 4. When do pointers stop? (left < right? or left == right?)
     (Khi nào dừng?)
```

---

## Template 1: Opposite Direction — Pair Finding

```python
def opposite_pair(arr, target):
    """Find pair satisfying condition from both ends."""
    left, right = 0, len(arr) - 1
    
    while left < right:
        current = evaluate(arr[left], arr[right])  # TODO
        
        if current == target:
            return [left, right]           # Found!
        elif current < target:
            left += 1                      # Need MORE
        else:
            right -= 1                     # Need LESS
    
    return []                              # Not found
```

---

## Template 2: Opposite Direction — Palindrome

```python
def palindrome_check(s):
    """Check palindrome with optional character filtering."""
    left, right = 0, len(s) - 1
    
    while left < right:
        # Optional: skip non-alphanumeric (Tùy chọn: bỏ qua ký tự đặc biệt)
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    
    return True
```

---

## Template 3: Same Direction — Remove / Filter

```python
def filter_in_place(arr):
    """Keep only elements passing a condition, in-place."""
    write = 0
    
    for read in range(len(arr)):
        if should_keep(arr[read]):         # TODO: Your condition
            arr[write] = arr[read]
            write += 1
    
    return write                           # New length
```

---

## Template 4: Same Direction — Remove Duplicates (Sorted)

```python
def remove_duplicates(nums):
    """Remove duplicates from sorted array in-place."""
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:      # New unique!
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

---

## Template 5: Same Direction — Subsequence

```python
def is_subsequence(s, t):
    """Check if s is a subsequence of t."""
    sp, tp = 0, 0
    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            sp += 1                        # Match! advance s
        tp += 1                            # Always advance t
    return sp == len(s)
```

---

## Template 6: Fast & Slow — Cycle Detection

```python
def has_cycle(head):
    """Detect cycle in linked list (Floyd's algorithm)."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next                   # 1 step
        fast = fast.next.next              # 2 steps
        if slow == fast:
            return True                    # Cycle!
    return False                           # No cycle
```

---

## Template 7: 3Sum — Fix One + Two Pointers

```python
def three_sum(nums, target=0):
    """Find all unique triplets summing to target."""
    nums.sort()                            # Must sort first!
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue                       # Skip duplicates
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1              # Skip dup
                while left < right and nums[right] == nums[right-1]:
                    right -= 1             # Skip dup
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    
    return result
```

---

## Template 8: Container With Most Water

```python
def max_area(height):
    """Find max water between two lines."""
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        w = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, w * h)
        
        if height[left] < height[right]:
            left += 1                      # Move shorter
        else:
            right -= 1
    
    return max_water
```

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

1. **"Remove all occurrences of value 3 from array"** — which template? (Template nào?)

2. **What is the key difference between Template 3 and Template 4?** (Khác biệt chính giữa Template 3 và 4 là gì?)

3. **In Template 7 (3Sum), why do we need to skip duplicates in TWO places?** (Tại sao cần bỏ qua trùng lặp ở HAI chỗ?)

4. **Can Template 6 (Fast/Slow) find WHERE the cycle starts?** How would you modify it? (Có thể tìm NƠI vòng lặp bắt đầu? Sửa thế nào?)

---

**← Previous:** [Chapter 3: Complexity](./03_complexity.md)
**Next →** [Run the Examples!](../examples/) 🚀
