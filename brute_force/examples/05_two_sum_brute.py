"""
=============================================================
 Example 5: Two Sum — BF vs Optimized Comparison
=============================================================

Problem: Find two numbers that add up to a target.
         (Tìm 2 số cộng lại bằng target.)

This example demonstrates:
  1. Brute Force solution — O(n²) (Lời giải vét cạn)
  2. Optimized Hash Map solution — O(n) (Lời giải tối ưu)
  3. Performance comparison — measure actual time (So sánh hiệu năng thực tế)
  4. Stress test — verify both give same answer (Kiểm tra cả 2 cho cùng đáp án)

Key Lesson (Bài học chính):
  BF is the STARTING POINT. Once you understand it,
  you can see WHY the optimization works.
  (BF là ĐIỂM XUẤT PHÁT. Khi hiểu BF, bạn thấy TẠI SAO tối ưu hoạt động.)
"""

import time
import random


def two_sum_brute_force(nums, target):
    """
    Brute Force: Try every pair.
    (Vét cạn: Thử mọi cặp.)

    Time: O(n²) | Space: O(1)
    
    Logic:
      - Outer loop: pick first number (Vòng ngoài: chọn số thứ nhất)
      - Inner loop: pick second number (Vòng trong: chọn số thứ hai)
      - Check if they add up to target (Kiểm tra tổng = target?)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hash_map(nums, target):
    """
    Optimized: Use Hash Map for O(1) lookup.
    (Tối ưu: Dùng Hash Map cho tra cứu O(1).)

    Time: O(n) | Space: O(n)
    
    Logic:
      - For each number, calculate complement = target - number
        (Với mỗi số, tính bù = target - số)
      - Check if complement was seen before using hash map
        (Kiểm tra bù đã thấy trước đó chưa bằng hash map)
      - If yes → return both indices (Nếu có → trả về 2 index)
    """
    seen = {}  # value → index (giá trị → index)
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:  # O(1) lookup! (Tra cứu O(1)!)
            return [seen[complement], i]
        seen[num] = i
    return []


def measure_time(func, *args, runs=10):
    """Measure average execution time. (Đo thời gian chạy trung bình.)"""
    total = 0
    for _ in range(runs):
        start = time.perf_counter()
        func(*args)
        total += time.perf_counter() - start
    return total / runs


def stress_test(num_tests=5000):
    """
    Compare BF and optimized on random inputs.
    (So sánh BF và tối ưu trên input ngẫu nhiên.)
    
    If they ever disagree, we found a bug! (Nếu khác nhau → có bug!)
    """
    print(f"  Running {num_tests} random tests...")
    for test in range(num_tests):
        # Generate random test case (Tạo test case ngẫu nhiên)
        n = random.randint(2, 20)
        nums = [random.randint(-100, 100) for _ in range(n)]
        # Pick a valid target (ensure answer exists)
        i, j = random.sample(range(n), 2)
        target = nums[i] + nums[j]
        
        # Run both (Chạy cả hai)
        bf = two_sum_brute_force(nums, target)
        opt = two_sum_hash_map(nums, target)
        
        # Verify both find a valid pair (Xác minh cả 2 tìm cặp hợp lệ)
        if bf:
            bf_sum = nums[bf[0]] + nums[bf[1]]
        else:
            bf_sum = None
            
        if opt:
            opt_sum = nums[opt[0]] + nums[opt[1]]
        else:
            opt_sum = None
        
        # Both should find a valid pair (Cả 2 phải tìm được cặp hợp lệ)
        if bf_sum != target or opt_sum != target:
            print(f"  ❌ MISMATCH on test {test}!")
            print(f"     Input: nums={nums}, target={target}")
            print(f"     BF: {bf} → sum={bf_sum}")
            print(f"     Opt: {opt} → sum={opt_sum}")
            return False
    
    print(f"  ✅ All {num_tests} tests passed — both solutions agree!")
    return True


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    # Test 1: Correctness (Kiểm tra tính đúng)
    print("=" * 60)
    print("TEST 1: Correctness — nums=[2, 7, 11, 15], target=9")
    print("=" * 60)
    bf_result = two_sum_brute_force([2, 7, 11, 15], 9)
    opt_result = two_sum_hash_map([2, 7, 11, 15], 9)
    print(f"  Brute Force:  {bf_result}")
    print(f"  Hash Map:     {opt_result}")
    assert bf_result == [0, 1]
    assert opt_result == [0, 1]
    print("  ✅ Both correct!")
    print()

    # Test 2: Performance comparison (So sánh hiệu năng)
    print("=" * 60)
    print("TEST 2: Performance — BF O(n²) vs Hash Map O(n)")
    print("=" * 60)
    for n in [100, 1000, 5000, 10000]:
        nums = list(range(n))
        target = nums[-2] + nums[-1]  # Worst case: answer at the end
        
        bf_time = measure_time(two_sum_brute_force, nums, target)
        opt_time = measure_time(two_sum_hash_map, nums, target)
        
        speedup = bf_time / opt_time if opt_time > 0 else float('inf')
        print(f"  n = {n:>6}: BF = {bf_time*1000:>8.3f}ms | "
              f"Hash = {opt_time*1000:>8.3f}ms | "
              f"Speedup = {speedup:>6.1f}x")
    print()

    # Test 3: Stress test (Kiểm tra stress)
    print("=" * 60)
    print("TEST 3: Stress Test — 5000 random cases")
    print("=" * 60)
    stress_test(5000)
    print()

    print("=" * 60)
    print("✅ All tests passed!")
    print("=" * 60)
    print()
    print("🔑 Key Takeaways (Bài học chính):")
    print("   1. BF Two Sum is O(n²) — simple but slow for large n")
    print("      (BF là O(n²) — đơn giản nhưng chậm khi n lớn)")
    print("   2. Hash Map Two Sum is O(n) — uses extra space for speed")
    print("      (Hash Map là O(n) — dùng thêm bộ nhớ để tăng tốc)")
    print("   3. BF helps VERIFY the optimized solution is correct")
    print("      (BF giúp KIỂM CHỨNG lời giải tối ưu đúng)")
    print("   4. The optimization insight: 'Can we avoid the inner loop?'")
    print("      (Nhận xét tối ưu: 'Có thể bỏ vòng lặp trong không?')")
