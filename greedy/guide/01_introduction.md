# 📖 Chapter 1: Introduction to Greedy (Giới thiệu Tham lam)

## 🎯 Learning Objectives (Mục tiêu bài học)

After this chapter, you will be able to (Sau bài này, bạn sẽ có thể):
- Define what Greedy is (Định nghĩa tham lam là gì)
- Explain the **Greedy Choice Property** — WHEN it works (Giải thích TẠI SAO nó đúng)
- Decide WHEN to use Greedy — and when to use DP instead (Quyết định KHI NÀO dùng)

---

## 1. What is Greedy? (Tham lam là gì?)

A **Greedy algorithm** builds a solution **step by step**, always choosing the option that looks **best right now** (the "locally optimal" choice), without worrying about future consequences.

**Algorithms tham lam** xây dựng lời giải **từng bước**, luôn chọn lựa chọn **tốt nhất tại thời điểm hiện tại** (tối ưu cục bộ), không lo lắng về hậu quả tương lai.

### 🔑 The Key Idea (Ý tưởng chính)

```
Sort the input (usually)
For each element (in sorted order):
    IF this element improves the solution:
        → Take it (greedy choice)
    ELSE:
        → Skip it
```

### 🗝️ Real-life Analogy (Ví dụ đời thực)

Imagine you're at a **buffet** with limited stomach capacity (Tưởng tượng ở **buffet** với bụng có giới hạn):

| Approach | How it works | Result (Kết quả) |
|----------|-------------|----------|
| **Greedy** | Always grab the most expensive dish first (Luôn lấy món đắt nhất trước) | Fast decision, usually good (Nhanh, thường tốt) |
| **DP** | Calculate all possible combinations of dishes for max total value (Tính tất cả tổ hợp) | Optimal but slow (Tối ưu nhưng chậm) |
| **Backtracking** | Try every combination of dishes, put back ones that don't work (Thử mọi combo) | Correct but exhaustive (Đúng nhưng vét cạn) |

> **Key insight (Nhận xét quan trọng)**: Greedy is 🚀 FAST because it makes ONE decision at each step and NEVER backtracks. But it only works for problems where **local optimal = global optimal** (Tham lam NHANH vì chỉ chọn 1 lần, KHÔNG quay lui. Nhưng chỉ đúng khi tối ưu cục bộ = tối ưu toàn cục).

---

## 2. Why Learn Greedy? (Tại sao cần biết?)

### Reason 1: 🚀 Speed — O(n) or O(n log n)

Most Greedy algorithms are **much faster** than DP (O(n²)) or Backtracking (O(2ⁿ)):

```
Problem: Non-overlapping Intervals (LC 435)
  DP approach:    O(n²) — compare all pairs
  Greedy approach: O(n log n) — sort by end time, one pass
  → 100x speedup for n = 10⁵!
```

### Reason 2: 📊 ~15% of Interview Questions

Greedy appears frequently in FAANG interviews, especially combined with sorting:
- **Intervals:** Meeting rooms, non-overlapping (Lịch họp)
- **Arrays:** Jump game, gas station (Nhảy xa, trạm xăng)
- **Strings:** Partition labels, task scheduler (Phân tách chuỗi)

### Reason 3: ✅ Many Problems Have Greedy Solutions

If constraints are `n ≤ 10⁵` or `n ≤ 10⁶`, DP at O(n²) is too slow. You NEED Greedy's O(n log n).

---

## 3. When to USE Greedy (Khi nào NÊN dùng)

| Scenario (Tình huống) | Why Greedy works (Tại sao tham lam đúng) | Example (Ví dụ) |
|----------------------|-----------------------------------|--------------------|
| **Intervals / Scheduling** (Lịch trình) | Sort by end time → earliest finish = most room | LC 435, LC 452, LC 56 |
| **Greedy on sorted array** (Mảng đã sort) | After sorting, best local choice is clear | LC 455 (Assign Cookies), LC 881 (Boats) |
| **Reachability problems** (Bài "có đến được không?") | Track farthest reachable position | LC 55 (Jump Game), LC 45 |
| **String partitioning** (Phân tách chuỗi) | Extend partition to include last occurrence | LC 763 (Partition Labels) |
| **Coin change with canonical coins** (Đổi tiền US) | Largest coin first for standard denominations | US coins: 25, 10, 5, 1 |

### The Two Properties (Hai tính chất)

Greedy ONLY works if the problem has:
1. **Greedy Choice Property** (Tính chọn tham lam): Chọn tốt nhất AT THIS STEP luôn dẫn đến GLOBAL optimal
2. **Optimal Substructure** (Cấu trúc tối ưu): Sau khi chọn, bài toán con cũng giải được bằng Greedy

---

## 4. When NOT to Use Greedy (Khi nào KHÔNG nên dùng)

### ⚠️ Counter-example: Coin Change with arbitrary coins

```python
# Coins: [1, 3, 4], Target: 6
# Greedy: pick 4 → 1 → 1 = 3 coins (4+1+1)
# Optimal: pick 3 → 3     = 2 coins (3+3)  ← GREEDY WAS WRONG!
```

### When Greedy Fails (Khi tham lam SAI)

| Scenario | Why it fails | Use instead |
|----------|-------------|-------------|
| **0/1 Knapsack** | Can't split items — taking "best ratio" skips better combo | DP |
| **Coin Change (arbitrary)** | Larger coin doesn't always help | DP |
| **Longest Path in Graph** | Greedy picks heavy edges but may miss longer path | DP/DFS |
| **Edit Distance** | Local alignment ≠ global alignment | DP |

### How to Detect (Cách nhận biết)

| Signal → Greedy | Signal → DP |
|----------------|-------------|
| "Minimum/maximum with sorting" | "Count number of ways" |
| "Non-overlapping intervals" | "All subsets with constraint" |
| n ≤ 10⁶ (need O(n log n)) | n ≤ 10³ (O(n²) is OK) |
| No dependency between choices | Overlapping subproblems |

---

## 5. Greedy in the Algorithm Landscape (Tham lam trong bức tranh tổng thể)

```
                    Brute Force
                    /    |    \
                   /     |     \
            Backtracking |   Binary Search
                         |
                  Sliding Window
                  /           \
                DP          Greedy ← You are here!
            (memoize)    (one-pass)
```

- **Greedy** = BF where we **only try the best option** (chỉ thử lựa chọn tốt nhất)
- **DP** = BF where we **try all options but memoize** (thử tất cả nhưng ghi nhớ)
- **Backtracking** = BF where we **try all options and prune** (thử tất cả và cắt tỉa)

> If Greedy works → it's the fastest solution.
> If Greedy fails → fall back to DP.
> If DP is too complex → use Backtracking.

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

Answer these **on paper** before moving to Chapter 2 (Trả lời **trên giấy** trước khi sang Chương 2):

1. **Define Greedy in one sentence** (Định nghĩa Greedy trong 1 câu).

2. **Coins = [1, 5, 10, 25]. Target = 30. Does Greedy work?** Show your steps (Cho coins US, target = 30. Greedy đúng không? Trình bày từng bước).

3. **Coins = [1, 3, 4]. Target = 6. Does Greedy work?** Why or why not? (Greedy sai ở đâu?)

4. **Name 2 conditions for Greedy to work** (Kể 2 điều kiện để Greedy đúng).

5. **A problem asks "minimum intervals to remove". Should you try Greedy or DP first?** Why? (Bài hỏi "xóa ít interval nhất". Nên thử Greedy hay DP trước? Tại sao?)

---

**Next →** [Chapter 2: Patterns (Các dạng bài)](./02_patterns.md)
