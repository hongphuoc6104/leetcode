# 📖 Chủ đề 12: Backtracking

## Lý thuyết cơ bản

**Backtracking** là kỹ thuật thử tất cả khả năng, quay lui khi gặp ngõ cụt. Tạo cây quyết định và cắt tỉa (pruning).

### Template
```python
def backtrack(candidates, path, result, start):
    if is_valid(path):  # Base case
        result.append(path[:])
        return
    
    for i in range(start, len(candidates)):
        # Pruning (tùy bài)
        if not is_feasible(candidates[i]):
            continue
        
        path.append(candidates[i])       # Choose
        backtrack(candidates, path, result, i + 1)  # Explore
        path.pop()                        # Un-choose (backtrack)

# Permutation template
def permute(nums):
    result = []
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
    backtrack([], [False] * len(nums))
    return result
```

---

## Danh sách 30 bài LeetCode

### 🟢 Easy (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Binary Tree Paths | [LC 257](https://leetcode.com/problems/binary-tree-paths/) | DFS, track path |
| 2 | Binary Watch | [LC 401](https://leetcode.com/problems/binary-watch/) | Enumerate combinations |
| 3 | Letter Case Permutation | [LC 784](https://leetcode.com/problems/letter-case-permutation/) | Backtrack alpha chars |
| 4 | Sum All Subset XOR | [LC 1863](https://leetcode.com/problems/sum-of-all-subset-xor-totals/) | Generate subsets |
| 5 | Finding 3-Digit Even | [LC 2094](https://leetcode.com/problems/finding-3-digit-even-numbers/) | Permute digits |
| 6 | Count Ops to Zero | [LC 2169](https://leetcode.com/problems/count-operations-to-obtain-zero/) | Simulation |
| 7 | Shuffle String | [LC 1528](https://leetcode.com/problems/shuffle-string/) | Direct mapping |
| 8 | Decode XORed Array | [LC 1720](https://leetcode.com/problems/decode-xored-array/) | XOR property |
| 9 | Min Bit Flips | [LC 2220](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/) | XOR + count bits |
| 10 | Split Min Sum | [LC 2578](https://leetcode.com/problems/split-with-minimum-sum/) | Sort digits |

### 🟡 Medium (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Letter Combinations | [LC 17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Phone keypad backtrack |
| 2 | Generate Parentheses | [LC 22](https://leetcode.com/problems/generate-parentheses/) | open/close count |
| 3 | Combination Sum | [LC 39](https://leetcode.com/problems/combination-sum/) | Reuse allowed, start=i |
| 4 | Combination Sum II | [LC 40](https://leetcode.com/problems/combination-sum-ii/) | No reuse, skip dups |
| 5 | Permutations | [LC 46](https://leetcode.com/problems/permutations/) | Classic permutation |
| 6 | Permutations II | [LC 47](https://leetcode.com/problems/permutations-ii/) | Sort + skip dups |
| 7 | Combinations | [LC 77](https://leetcode.com/problems/combinations/) | n choose k |
| 8 | Subsets | [LC 78](https://leetcode.com/problems/subsets/) | Include/exclude each |
| 9 | Word Search | [LC 79](https://leetcode.com/problems/word-search/) | Grid backtrack |
| 10 | Subsets II | [LC 90](https://leetcode.com/problems/subsets-ii/) | Sort + skip dups |

### 🔴 Hard (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Sudoku Solver | [LC 37](https://leetcode.com/problems/sudoku-solver/) | Try 1-9, validate |
| 2 | N-Queens | [LC 51](https://leetcode.com/problems/n-queens/) | Column + diagonal check |
| 3 | N-Queens II | [LC 52](https://leetcode.com/problems/n-queens-ii/) | Count solutions |
| 4 | Word Ladder II | [LC 126](https://leetcode.com/problems/word-ladder-ii/) | BFS + backtrack |
| 5 | Word Search II | [LC 212](https://leetcode.com/problems/word-search-ii/) | Trie + grid backtrack |
| 6 | Remove Invalid Parens | [LC 301](https://leetcode.com/problems/remove-invalid-parentheses/) | BFS or backtrack |
| 7 | Zuma Game | [LC 488](https://leetcode.com/problems/zuma-game/) | DFS + pruning |
| 8 | Strange Printer | [LC 664](https://leetcode.com/problems/strange-printer/) | Interval DP |
| 9 | Unique Paths III | [LC 980](https://leetcode.com/problems/unique-paths-iii/) | Grid backtrack, visit all |
| 10 | Tiling Rectangle | [LC 1240](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/) | Backtrack + pruning |

---

## Tips
- **Subsets/Combinations**: dùng `start` index để tránh trùng
- **Permutations**: dùng `used[]` array
- **Skip duplicates**: sort trước, skip `if i > start and nums[i] == nums[i-1]`
- Luôn **backtrack** (undo choice) sau mỗi recursive call
