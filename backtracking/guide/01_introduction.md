# 📖 Chapter 1: Introduction to Backtracking (Giới thiệu Quay lui)

## 🎯 Learning Objectives (Mục tiêu bài học)

After this chapter, you will be able to (Sau bài này, bạn sẽ có thể):
- Define Backtracking and the Choose-Explore-Unchoose pattern (Định nghĩa quay lui)
- Explain the difference between Backtracking and Brute Force (Phân biệt quay lui và vét cạn)
- Decide WHEN to use Backtracking (Quyết định KHI NÀO dùng)

---

## 1. What is Backtracking? (Quay lui là gì?)

**Backtracking** is a systematic way to explore **all possible solutions** by building them incrementally, one step at a time. At each step:
1. **Choose** — pick an option (Chọn lựa chọn)
2. **Explore** — recurse to see if it leads to a valid solution (Duyệt đệ quy)
3. **Unchoose** — undo the choice and try the next option (Bỏ chọn, thử lựa chọn tiếp)

**Quay lui** là cách có hệ thống để duyệt **mọi lời giải có thể** bằng cách xây dựng từng bước. Mỗi bước: **Chọn → Thử → Bỏ (quay lui)**.

### 🔑 The Key Idea

```
def backtrack(path, choices):
    if is_solution(path):       # Base case: found a solution
        save(path)
        return
    
    for choice in choices:
        path.append(choice)      # 1. Choose
        backtrack(path, next_choices)  # 2. Explore
        path.pop()               # 3. Unchoose (BACKTRACK!)
```

### 🗝️ Real-life Analogy (Ví dụ đời thực)

Imagine you're in a **maze** (Tưởng tượng bạn ở trong **mê cung**):

| Approach | How it works | Speed |
|----------|-------------|-------|
| **Brute Force** | Try EVERY possible path (even obviously wrong ones) | Slowest |
| **Backtracking** | Walk forward. At dead end → go BACK to last fork, try another path | Faster (skips dead ends) |
| **BFS/DFS** | Explore systematically finding shortest path | Different goal |

> **Key insight (Nhận xét)**: Backtracking is **Brute Force + Pruning** (BF + cắt tỉa). We skip branches of the decision tree that can't possibly lead to a valid solution.

### Decision Tree (Cây quyết định)

For subsets of `[1, 2, 3]`:
```
                    []
                 /      \
              [1]        []
             /   \      /   \
          [1,2]  [1]  [2]    []
         /  \   / \   / \   / \
     [1,2,3][1,2][1,3][1][2,3][2][3][]
```

---

## 2. Backtracking vs BF vs DP (So sánh)

| | Brute Force | Backtracking | DP |
|--|-------------|-------------|-----|
| **Approach** | Try ALL | Try all, skip invalid early | Memorize + reuse |
| **Pruning** | ❌ No | ✅ Yes (đây là key!) | N/A |
| **Speed** | O(2ⁿ) or O(n!) | Better if good pruning | Often O(n²) or O(n·2ⁿ) |
| **When to use** | n ≤ 20 | n ≤ 15-20 | Overlapping subproblems |
| **Output** | One solution | ALL solutions | One optimal solution |

---

## 3. When to USE Backtracking (Khi nào NÊN dùng)

| Signal (Dấu hiệu) | Pattern | Example |
|---------------------|---------|---------|
| "Generate ALL subsets/combinations" | Subsets | LC 78, LC 90 |
| "Generate ALL permutations" | Permutations | LC 46, LC 47 |
| "Find ALL valid solutions" | Constraint satisfaction | LC 51 (N-Queens), LC 37 |
| "Search for a word in grid" | Grid DFS + backtrack | LC 79, LC 212 |
| "Generate all valid parentheses" | Pruned enumeration | LC 22 |
| n ≤ 15 with exponential search | Any pattern | n! or 2ⁿ feasible |

---

## 4. When NOT to Use Backtracking

| Scenario | Why | Use instead |
|----------|-----|-------------|
| n > 20 for subsets (2ⁿ > 10⁶) | Too many subsets | DP |
| n > 12 for permutations (12! = 479M) | Too many permutations | DP |
| "Count the NUMBER of" solutions | Don't need all solutions | DP |
| "Find the optimal/shortest" | Need one best, not all | DP/BFS |

### Constraint Quick Guide

| Constraint | Feasible | Algorithm |
|-----------|----------|-----------|
| n ≤ 10 | O(n!) ✅ | Backtracking (perms) |
| n ≤ 20 | O(2ⁿ) ✅ | Backtracking (subsets) |
| n ≤ 25 | O(2ⁿ/2 · n) ✅ | Meet in the middle |
| n ≤ 1000 | O(n²) | DP |

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

1. **What are the 3 steps of Backtracking?** (3 bước quay lui là gì?)
2. **How is Backtracking different from pure Brute Force?** (BT khác BF ở chỗ nào?)
3. **n = 25, need all subsets. Is backtracking feasible?** Calculate 2²⁵ (BT có khả thi không?)
4. **"Count the number of ways to make change" — Backtracking or DP?** Why? (Đếm số cách đổi tiền — BT hay DP?)
5. **Draw the decision tree for all subsets of [a, b]** (Vẽ cây quyết định cho tập con của [a, b])

---

**Next →** [Chapter 2: Patterns (Các dạng bài)](./02_patterns.md)
