# 📖 Chapter 1: Introduction to Dynamic Programming

## 1. What is DP? (Quy hoạch động là gì?)

Dynamic Programming optimizes problems with **overlapping subproblems** and **optimal substructure** by storing results to avoid recomputation (DP tối ưu bằng cách lưu kết quả để tránh tính lại).

**Analogy (Ví dụ):** Imagine calculating Fibonacci by hand. You'd write down f(3)=2, f(4)=3 etc. on paper so you don't recalculate. That's memoization!

> 🤔 **Socratic Question:** If a problem can be solved with brute force recursion, what TWO properties must it have for DP to help?

---

## 2. The Fibonacci Example — Why DP Matters

### Naive Recursion: O(2^n) — DON'T use this!
```python
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)  # Same subproblems solved repeatedly!
```

Call tree for fib(5) — notice the repeated work:
```
                fib(5)
              /        \
          fib(4)        fib(3)
         /     \       /     \
     fib(3)   fib(2) fib(2) fib(1)
     /   \
  fib(2) fib(1)
```
fib(3) calculated 2 times! fib(2) calculated 3 times!

### Top-Down (Memoization): O(n) ← Just add a cache!
```python
def fib_memo(n, memo={}):
    if n <= 1: return n
    if n not in memo:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

### Bottom-Up (Tabulation): O(n) ← Build from base cases
```python
def fib_tab(n):
    if n <= 1: return n
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]
```

### Space-Optimized: O(1) ← Only keep last 2 values
```python
def fib_opt(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
```

---

## 3. Top-Down vs Bottom-Up

| | Top-Down (Memo) | Bottom-Up (Table) |
|--|----------------|-------------------|
| **Approach** | Recursive + cache | Iterative + array |
| **Direction** | Big problem → smaller | Small → build up |
| **Base case** | In the recursion | dp[0], dp[1] |
| **Space** | O(n) + call stack | O(n) (can optimize to O(1)) |
| **Easier to** | Write (just add memo) | Optimize space |
| **Risk** | Stack overflow | None |

> 💡 **Tip (Mẹo):** Start with top-down (add memo to recursion). Convert to bottom-up for space optimization.

---

## 4. The DP Recipe — 5 Steps (Công thức DP — 5 bước)

```
1. Define STATE: dp[i] = what does it represent?
   (Xác định TRẠNG THÁI: dp[i] đại diện cho gì?)

2. Write TRANSITION: dp[i] = f(dp[i-1], dp[i-2], ...)
   (Viết CÔNG THỨC CHUYỂN: dp[i] phụ thuộc các trạng thái nào?)

3. Define BASE CASE: dp[0] = ?, dp[1] = ?
   (Xác định TRƯỜNG HỢP CƠ SỞ)

4. Determine ORDER: left→right? diagonal? reverse?
   (Xác định THỨ TỰ tính toán)

5. Find ANSWER: dp[n]? max(dp)? dp[m][n]?
   (Tìm KẾT QUẢ cuối cùng)
```

### Applying the recipe to Climbing Stairs (LC 70):
```
1. STATE: dp[i] = number of ways to reach step i
2. TRANSITION: dp[i] = dp[i-1] + dp[i-2]  (take 1 or 2 steps)
3. BASE: dp[1] = 1, dp[2] = 2
4. ORDER: left to right (i = 3, 4, ..., n)
5. ANSWER: dp[n]
```

---

## 5. When to Use DP? (Khi nào dùng DP?)

| Signal (Dấu hiệu) | Example |
|---------------------|---------|
| "Minimum/maximum" | Min cost climbing stairs |
| "Count the number of ways" | Number of paths in grid |
| "Can you achieve...?" | Can partition into equal subsets? |
| "Longest/shortest subsequence" | Longest Increasing Subsequence |
| Overlapping subproblems | Same subproblem solved many times |
| Optimal substructure | Optimal solution uses optimal sub-solutions |

### How to recognize overlapping subproblems?
If your recursive solution calls the **same function with same arguments** multiple times → DP can help! Draw the recursion tree to check.

---

## 6. DP vs Other Techniques

| Technique | When to Use |
|-----------|-------------|
| **Greedy** | Local optimal → global optimal (no backtracking) |
| **DP** | Need to explore multiple choices, has overlapping subproblems |
| **Backtracking** | Need ALL solutions, not just optimal |
| **Divide & Conquer** | Subproblems are independent (no overlap) |

> 🤔 Can you think of a problem that looks like DP but is actually Greedy? (Hint: Activity Selection)

---

## ❓ Self-Check Questions

1. **What are the two properties needed for DP?** (2 tính chất cần cho DP?)
2. **fib(50) takes how long with naive recursion?** Estimate. (Ước lượng thời gian?)
3. **When should you use top-down vs bottom-up?** (Khi nào dùng top-down vs bottom-up?)
4. **Write the DP recipe for "Min cost climbing stairs" (LC 746).**

---

**Next →** [Chapter 2: Patterns](./02_patterns.md)
