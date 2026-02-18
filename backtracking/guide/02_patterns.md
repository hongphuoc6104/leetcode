# 📖 Chapter 2: Backtracking Patterns

## Pattern 1: Subsets — Include or Exclude

### 🔍 Signal: "all subsets", "power set"

```python
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result
```

### With duplicates (LC 90):
```python
def subsets_with_dup(nums):
    nums.sort()
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]: continue  # Skip dups!
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result
```
📌 LC 78, LC 90

---

## Pattern 2: Permutations — All Orderings

### 🔍 Signal: "all permutations", "all arrangements"

```python
def permutations(nums):
    result = []
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    backtrack([], nums)
    return result
```
📌 LC 46, LC 47

---

## Pattern 3: Combinations — Choose K from N

### 🔍 Signal: "all combinations", "choose k", "combination sum"

```python
def combinations(n, k):
    result = []
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    backtrack(1, [])
    return result
```

### Combination Sum (LC 39) — numbers reusable:
```python
def combination_sum(candidates, target):
    result = []
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining: break  # Pruning!
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()
    candidates.sort()
    backtrack(0, [], target)
    return result
```
📌 LC 77, LC 39, LC 40, LC 216

---

## Pattern 4: Grid Search — Word Search, Islands

### 🔍 Signal: "word search", "path in grid"

```python
def word_search(board, word):
    rows, cols = len(board), len(board[0])
    def backtrack(r, c, idx):
        if idx == len(word): return True
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or board[r][c] != word[idx]):
            return False
        temp = board[r][c]
        board[r][c] = '#'  # Mark visited
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            if backtrack(r+dr, c+dc, idx+1): return True
        board[r][c] = temp  # Unmark (backtrack!)
        return False
    
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0): return True
    return False
```
📌 LC 79, LC 212

---

## Pattern 5: Constraint Satisfaction — N-Queens, Sudoku

### 🔍 Signal: "place N queens", "solve sudoku", "valid placement"

```python
def solve_n_queens(n):
    result = []
    cols = set()
    diag1 = set()  # r - c
    diag2 = set()  # r + c
    
    def backtrack(row, board):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row-col) in diag1 or (row+col) in diag2:
                continue
            cols.add(col); diag1.add(row-col); diag2.add(row+col)
            board[row][col] = 'Q'
            backtrack(row + 1, board)
            board[row][col] = '.'
            cols.remove(col); diag1.remove(row-col); diag2.remove(row+col)
    
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0, board)
    return result
```
📌 LC 51, LC 37

---

## 📊 Quick Reference

| Pattern | Output | Avoids duplicates by |
|---------|--------|---------------------|
| Subsets | 2^n subsets | `start` index |
| Permutations | n! orderings | `remaining` list |
| Combinations | C(n,k) | `start` index + stop at k |
| Grid search | True/False | Mark/unmark cells |
| Constraint | All valid placements | Sets for checking |

---

**← Previous:** [Chapter 1](./01_introduction.md) | **Next →** [Chapter 3](./03_complexity.md)
