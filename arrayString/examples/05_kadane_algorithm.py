"""
=============================================================
 Example 5: Kadane's Algorithm (Thuật toán Kadane)
=============================================================

Problem: Find the maximum sum of any contiguous subarray.
         (Tìm tổng lớn nhất của subarray liên tiếp bất kỳ.)

This is a classic example of OPTIMIZING Brute Force:
  BF:     O(n²) — try every subarray (thử mọi subarray)
  Kadane: O(n)  — single pass with running max (1 lần duyệt)

The key insight: At each position, decide:
  "Is it better to EXTEND the current subarray, or START fresh?"
  (Ở mỗi vị trí, quyết định: "Nên MỞ RỘNG subarray hiện tại hay BẮT ĐẦU MỚI?")
"""


def max_subarray_brute(nums):
    """
    Brute Force: Try every possible subarray.
    (Vét cạn: Thử mọi subarray có thể.)

    Time: O(n²) | Space: O(1)
    """
    n = len(nums)
    max_sum = float('-inf')
    best_start = best_end = 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum
                best_start, best_end = i, j

    return max_sum, nums[best_start:best_end + 1]


def max_subarray_kadane(nums):
    """
    Kadane's Algorithm: Single-pass optimization.
    (Thuật toán Kadane: Tối ưu 1 lần duyệt.)

    Time: O(n) | Space: O(1)
    
    Logic at each step (Logic tại mỗi bước):
      current_sum = max(nums[i], current_sum + nums[i])
      → Either start a NEW subarray at i (Bắt đầu mới tại i)
      → Or EXTEND the existing subarray to include i (Mở rộng để bao gồm i)
    """
    max_sum = nums[0]
    current_sum = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        # Decision: extend or restart? (Quyết định: mở rộng hay bắt đầu lại?)
        if current_sum + nums[i] >= nums[i]:
            current_sum += nums[i]  # Extend (Mở rộng)
        else:
            current_sum = nums[i]   # Restart (Bắt đầu lại)
            temp_start = i

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, nums[start:end + 1]


def max_subarray_kadane_trace(nums):
    """
    Kadane's with step-by-step trace.
    (Kadane với theo dõi từng bước.)
    """
    max_sum = nums[0]
    current_sum = nums[0]

    print(f"  {'i':>3} | {'nums[i]':>7} | {'curr+nums[i]':>12} | {'Decision':>10} | {'current_sum':>11} | {'max_sum':>7}")
    print(f"  {'-'*3}-+-{'-'*7}-+-{'-'*12}-+-{'-'*10}-+-{'-'*11}-+-{'-'*7}")
    print(f"  {'0':>3} | {nums[0]:>7} | {'—':>12} | {'start':>10} | {current_sum:>11} | {max_sum:>7}")

    for i in range(1, len(nums)):
        extended = current_sum + nums[i]
        if extended >= nums[i]:
            decision = "extend"
            current_sum = extended
        else:
            decision = "restart"
            current_sum = nums[i]

        max_sum = max(max_sum, current_sum)
        print(f"  {i:>3} | {nums[i]:>7} | {extended:>12} | {decision:>10} | {current_sum:>11} | {max_sum:>7}")

    return max_sum


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 70)
    print("TEST 1: Step-by-step trace of Kadane's Algorithm")
    print("=" * 70)
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"  Input: {nums}")
    print()
    result = max_subarray_kadane_trace(nums)
    print(f"\n  Maximum subarray sum = {result}")
    assert result == 6
    print("  ✅ Correct! (subarray [4, -1, 2, 1] = 6)")
    print()

    # Compare BF vs Kadane
    print("=" * 70)
    print("TEST 2: BF vs Kadane — Both give same answer")
    print("=" * 70)
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [5, 4, -1, 7, 8],
        [-1, -2, -3, -4],
        [1, -1, 1, -1, 1],
    ]
    for nums in test_cases:
        bf_sum, bf_sub = max_subarray_brute(nums)
        kd_sum, kd_sub = max_subarray_kadane(nums)
        status = "✅" if bf_sum == kd_sum else "❌"
        print(f"  {str(nums):>35} → BF={bf_sum:>3} {bf_sub} | Kadane={kd_sum:>3} {kd_sub} {status}")
    print()

    # Performance comparison
    print("=" * 70)
    print("TEST 3: Performance — O(n²) vs O(n)")
    print("=" * 70)
    import time
    import random

    for n in [100, 1000, 5000, 10000]:
        nums = [random.randint(-100, 100) for _ in range(n)]

        start = time.perf_counter()
        bf_result = max_subarray_brute(nums)[0]
        bf_time = time.perf_counter() - start

        start = time.perf_counter()
        kd_result = max_subarray_kadane(nums)[0]
        kd_time = time.perf_counter() - start

        assert bf_result == kd_result
        speedup = bf_time / kd_time if kd_time > 0 else float('inf')
        print(f"  n={n:>6}: BF={bf_time*1000:>8.2f}ms | "
              f"Kadane={kd_time*1000:>8.3f}ms | "
              f"Speedup={speedup:>7.1f}x")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways (Bài học chính):")
    print("   1. Kadane = single-pass accumulation pattern")
    print("      (Kadane = pattern tích lũy 1 lần duyệt)")
    print("   2. The DECISION at each step: extend or restart?")
    print("      (QUYẾT ĐỊNH tại mỗi bước: mở rộng hay bắt đầu lại?)")
    print("   3. BF O(n²) → Kadane O(n) = massive speedup")
    print("      (BF O(n²) → Kadane O(n) = tăng tốc cực lớn)")
