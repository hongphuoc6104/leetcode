# 📖 Chapter 1: Introduction to Brute Force (Giới thiệu Vét Cạn)

## 🎯 Learning Objectives (Mục tiêu bài học)

After this chapter, you will be able to (Sau bài này, bạn sẽ có thể):
- Define what Brute Force is (Định nghĩa vét cạn là gì)
- Explain WHY it matters (Giải thích TẠI SAO nó quan trọng)
- Decide WHEN to use it — and when NOT to (Quyết định KHI NÀO dùng — và khi nào KHÔNG)

---

## 1. What is Brute Force? (Vét cạn là gì?)

**Brute Force** is an algorithmic strategy where you **try every possible solution** and check which one satisfies the problem's conditions (Vét cạn là chiến lược giải thuật mà bạn **thử mọi lời giải có thể** và kiểm tra cái nào thỏa mãn điều kiện).

### 🔑 The Key Idea (Ý tưởng chính)

```
For EVERY candidate solution:
    IF it satisfies the condition:
        → Return it (or save it)
```

That's it. No tricks, no clever optimizations. Just **exhaustive search** (Tìm kiếm toàn diện).

### 🗝️ Real-life Analogy (Ví dụ đời thực)

Imagine you have a **keychain with 100 keys** and a locked door (Tưởng tượng bạn có **100 chìa khóa** và một cánh cửa khóa):

| Approach | How it works | Speed |
|----------|-------------|-------|
| **Brute Force** | Try key #1 → doesn't work. Try #2 → doesn't work. ... Try #47 → ✅ works! | Slow but guaranteed (Chậm nhưng chắc chắn) |
| **Optimized** | Look at the key shape, match it to the lock type, try only matching keys | Fast but requires knowledge (Nhanh nhưng cần kiến thức) |

> **Key insight (Nhận xét quan trọng)**: Brute Force **always** finds the answer if one exists. It may be slow, but it's **never wrong** (BF **luôn** tìm được đáp án nếu có. Có thể chậm, nhưng **không bao giờ sai**).

---

## 2. Why Learn This? (Tại sao cần biết?)

You might think: *"If it's slow, why bother?"* (Bạn có thể nghĩ: *"Chậm thì học làm gì?"*). Here are 3 critical reasons (3 lý do quan trọng):

### Reason 1: 🏗️ Baseline — The Starting Point (Điểm xuất phát)

Every optimized algorithm starts from understanding the brute force version (Mọi thuật toán tối ưu đều bắt đầu từ việc hiểu phiên bản vét cạn). 

```
Understanding BF ──→ "This is O(n²)... can I do better?" ──→ Hash Map O(n) ✅
Not understanding BF ──→ "I don't even know where to start" ──→ 😰
```

When you learn **Sliding Window**, **Two Pointers**, **Binary Search** later, you'll see that they are all **optimizations of Brute Force** (Khi học các kỹ thuật sau, bạn sẽ thấy chúng đều là **tối ưu hóa của BF**).

### Reason 2: ✅ Correctness Check (Kiểm tra tính đúng)

In competitive programming and interviews, you can use BF to **verify** your optimized solution (Trong competitive programming và phỏng vấn, bạn dùng BF để **xác minh** lời giải tối ưu):

```python
# Run both solutions on random inputs (Chạy cả 2 trên input ngẫu nhiên)
for _ in range(10000):
    test_input = generate_random()
    bf_result = brute_force(test_input)   # Slow but correct (Chậm nhưng đúng)
    opt_result = optimized(test_input)     # Fast but maybe buggy (Nhanh nhưng có thể lỗi)
    assert bf_result == opt_result         # Must match! (Phải khớp!)
```

### Reason 3: 🎯 Sometimes BF IS the Answer (Đôi khi BF LÀ đáp án)

Many LeetCode problems have **small constraints** where Brute Force is the intended solution (Nhiều bài LeetCode có **ràng buộc nhỏ** mà BF là lời giải chính thức):

- `n ≤ 20` → Subsets: 2²⁰ = 1,048,576 operations → ✅ Fast enough (Đủ nhanh)
- `n ≤ 10` → Permutations: 10! = 3,628,800 operations → ✅ Fast enough
- `n ≤ 1000` → Nested loops: 10⁶ operations → ✅ Fast enough

---

## 3. When to USE Brute Force (Khi nào NÊN dùng)

| Scenario (Tình huống) | Why BF works (Tại sao BF phù hợp) | Example (Ví dụ) |
|----------------------|-----------------------------------|-----------------|
| **n is small** (n nhỏ, ≤ 10⁴ for O(n²), ≤ 20 for O(2ⁿ)) | Total operations fit within time limit (Tổng phép toán nằm trong giới hạn thời gian) | Subset Sum with n=15 |
| **Prototyping / Verifying** (Làm prototype / Xác minh) | Write a correct solution first, optimize later (Viết đúng trước, tối ưu sau) | Debug your DP by comparing with BF |
| **No better algorithm exists** (Không có thuật toán tốt hơn) | Some NP-hard problems have no polynomial solution (Một số bài NP-hard không có lời giải đa thức) | Traveling Salesman with n ≤ 12 |
| **First attempt at a new problem** (Lần đầu tiếp cận bài mới) | Helps you understand the problem before optimizing (Giúp hiểu bài trước khi tối ưu) | Any new LeetCode problem |

### The Golden Rule (Quy tắc vàng):

> **Always think Brute Force FIRST, then optimize.**
> (Luôn nghĩ BF TRƯỚC, rồi tối ưu sau.)
>
> *"Make it work, make it right, make it fast."* — Kent Beck

---

## 4. When NOT to Use Brute Force (Khi nào KHÔNG nên dùng)

| Scenario (Tình huống) | BF Complexity | n = 10⁵ → Operations | Result (Kết quả) |
|----------------------|---------------|----------------------|------------------|
| Nested loops on large n (Vòng lặp lồng trên n lớn) | O(n²) | 10¹⁰ | ❌ **TLE** (Time Limit Exceeded) |
| Triple nested loops | O(n³) | 10¹⁵ | ❌ **TLE** — way too slow |
| All permutations, n > 12 | O(n!) | astronomical | ❌ **TLE** — impossible |
| All subsets, n > 25 | O(2ⁿ) | 3.3 × 10⁷ | ⚠️ Borderline — may TLE |

### How to Read LeetCode Constraints (Cách đọc ràng buộc LeetCode)

When you see constraints like `1 ≤ n ≤ 10⁵`, this tells you the expected complexity (Khi thấy ràng buộc `1 ≤ n ≤ 10⁵`, bạn biết độ phức tạp mong đợi):

| Constraint (Ràng buộc) | Max feasible complexity (Độ phức tạp khả thi) | BF possible? |
|------------------------|----------------------------------------------|-------------|
| n ≤ 10 | O(n!) ✅ | Yes — even permutation BF works |
| n ≤ 20 | O(2ⁿ) ✅ | Yes — subset BF works |
| n ≤ 500 | O(n³) ✅ | Yes — triple loop works |
| n ≤ 10⁴ | O(n²) ✅ | Yes — double loop works |
| n ≤ 10⁵ | O(n log n) ⚠️ | **No** — need optimization |
| n ≤ 10⁶ | O(n) ⚠️ | **No** — need linear time |

---

## 5. BF in the Algorithm Landscape (BF trong bức tranh tổng thể)

Brute Force is the **root** of many optimization techniques (BF là **gốc** của nhiều kỹ thuật tối ưu):

```
                    Brute Force
                    /    |    \
                   /     |     \
            Two Pointers |   Binary Search
                         |
                  Sliding Window
                         |
                Dynamic Programming
                         |
                   Backtracking
                  (BF + Pruning)
```

- **Two Pointers** = BF pair search, but skip unnecessary pairs (BF tìm cặp, nhưng bỏ cặp không cần)
- **Sliding Window** = BF window search, but reuse previous computation (BF tìm window, nhưng tái sử dụng tính toán)
- **Binary Search** = BF linear search, but cut search space in half (BF tìm tuyến tính, nhưng chia đôi)
- **Backtracking** = BF + pruning — cut branches that can't lead to solution (BF + cắt tỉa nhánh)
- **DP** = BF + memoization — avoid recomputing same subproblems (BF + ghi nhớ)

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

Answer these **on paper** before moving to Chapter 2 (Trả lời **trên giấy** trước khi sang Chương 2):

1. **Define BF in one sentence** (Định nghĩa BF trong 1 câu).

2. **If `n = 15` and you need all subsets, is BF feasible?** Calculate the number of operations (Nếu `n = 15` và cần mọi tập con, BF có khả thi không? Tính số phép toán).

3. **Name 2 scenarios where BF is the BEST approach** (Kể 2 tình huống BF là cách tiếp cận TỐT NHẤT).

4. **A problem has constraint `n ≤ 10⁵`. Can you use O(n²)?** Why or why not? (Bài có ràng buộc `n ≤ 10⁵`. Dùng O(n²) được không? Tại sao?)

5. **What is the relationship between Brute Force and Backtracking?** (Mối quan hệ giữa BF và Backtracking là gì?)

---

**Next →** [Chapter 2: Variants (Các biến thể)](./02_variants.md)
