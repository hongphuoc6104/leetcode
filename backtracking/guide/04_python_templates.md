# 📖 Chapter 4: Python Templates

## Template 1: Subsets
```python
def subsets(nums):
    result = []
    def bt(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            bt(i + 1, path)
            path.pop()
    bt(0, [])
    return result
```

## Template 2: Permutations
```python
def permutations(nums):
    result = []
    def bt(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            bt(path, remaining[:i] + remaining[i+1:])
            path.pop()
    bt([], nums)
    return result
```

## Template 3: Combinations
```python
def combine(n, k):
    result = []
    def bt(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            bt(i + 1, path)
            path.pop()
    bt(1, [])
    return result
```

## Template 4: Combination Sum (reusable)
```python
def combo_sum(candidates, target):
    candidates.sort()
    result = []
    def bt(start, path, remain):
        if remain == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain: break
            path.append(candidates[i])
            bt(i, path, remain - candidates[i])  # i, not i+1 (reuse!)
            path.pop()
    bt(0, [], target)
    return result
```

## Template 5: Grid Backtrack (Word Search)
```python
def search(board, word):
    R, C = len(board), len(board[0])
    def bt(r, c, idx):
        if idx == len(word): return True
        if r<0 or r>=R or c<0 or c>=C or board[r][c]!=word[idx]:
            return False
        tmp = board[r][c]
        board[r][c] = '#'
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            if bt(r+dr, c+dc, idx+1): return True
        board[r][c] = tmp
        return False
    return any(bt(r,c,0) for r in range(R) for c in range(C))
```

## 📋 Checklist
1. ✅ **Base case clear?** What makes a valid solution?
2. ✅ **path[:]?** Copy path before appending to result!
3. ✅ **Backtrack?** pop() after recursion!
4. ✅ **Skip duplicates?** Sort + check `nums[i] == nums[i-1]`
5. ✅ **Pruning?** Stop early if impossible

---

**← Previous:** [Chapter 3](./03_complexity.md) | **Next →** [Examples](../examples/) 🚀
