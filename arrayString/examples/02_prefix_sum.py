"""
=============================================================
 Example 2: Prefix Sum (Tổng tiền tố)
=============================================================

Problem: Answer multiple "sum from index i to j" queries efficiently.
         (Trả lời nhiều truy vấn "tổng từ index i đến j" hiệu quả.)

Without prefix sum: Each query costs O(n) → Q queries = O(Q × n)
With prefix sum:    Build O(n) once → each query O(1) → total O(n + Q)

Time:  O(n) to build, O(1) per query
Space: O(n) for prefix array
"""


def build_prefix_sum(arr):
    """
    Build prefix sum array.
    (Xây mảng tổng tiền tố.)

    prefix[i] = sum of arr[0..i-1]
    prefix[0] = 0 (empty sum — tổng rỗng)
    """
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix


def range_sum(prefix, i, j):
    """
    Sum of arr[i..j] (inclusive) in O(1).
    (Tổng arr[i..j] trong O(1).)

    Formula: prefix[j+1] - prefix[i]
    """
    return prefix[j + 1] - prefix[i]


def subarray_sum_equals_k(nums, k):
    """
    Count subarrays with sum equal to k.
    (Đếm subarray có tổng bằng k.)
    
    Uses prefix sum + hash map for O(n).
    (Dùng prefix sum + hash map cho O(n).)
    
    Key insight: If prefix[j] - prefix[i] == k,
    then subarray [i..j-1] has sum k.
    (Nếu prefix[j] - prefix[i] == k, subarray [i..j-1] có tổng k.)
    """
    count = 0
    current_sum = 0
    prefix_counts = {0: 1}  # Base case: empty prefix has sum 0

    for num in nums:
        current_sum += num
        # How many previous prefixes have sum = current_sum - k?
        # (Bao nhiêu prefix trước có tổng = current_sum - k?)
        target = current_sum - k
        if target in prefix_counts:
            count += prefix_counts[target]
        
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    return count


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    arr = [2, 4, 1, 3, 5]

    print("=" * 60)
    print(f"Array: {arr}")
    print("=" * 60)

    # Build prefix sum
    prefix = build_prefix_sum(arr)
    print(f"  Prefix sum: {prefix}")
    print()

    # Visual display
    print("  Index:      ", "  ".join(f"{i:>3}" for i in range(len(arr))))
    print("  Array:      ", "  ".join(f"{v:>3}" for v in arr))
    print("  Prefix[i+1]:", "  ".join(f"{v:>3}" for v in prefix[1:]))
    print()

    # Test range queries
    queries = [(0, 4), (1, 3), (2, 4), (0, 0), (3, 4)]
    print("  Range Queries:")
    for i, j in queries:
        result = range_sum(prefix, i, j)
        actual = sum(arr[i:j+1])
        status = "✅" if result == actual else "❌"
        print(f"    sum(arr[{i}..{j}]) = {result} {status}  "
              f"(verify: {'+'.join(str(arr[x]) for x in range(i,j+1))} = {actual})")
    print()

    # Test subarray sum equals k
    print("=" * 60)
    print("Subarray Sum Equals K")
    print("=" * 60)
    nums = [1, 1, 1]
    k = 2
    count = subarray_sum_equals_k(nums, k)
    print(f"  nums={nums}, k={k} → count={count}")
    assert count == 2, f"Expected 2, got {count}"
    print(f"  ✅ Correct! (subarrays: [1,1] and [1,1])")
    print()

    nums = [1, 2, 3, -1, 2]
    k = 3
    count = subarray_sum_equals_k(nums, k)
    print(f"  nums={nums}, k={k} → count={count}")
    assert count == 2, f"Expected 2, got {count}"
    print(f"  ✅ Correct! (subarrays: [1,2] and [3] both sum to 3)")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it (Suy nghĩ thêm):")
    print("   1. Why does prefix array have length n+1, not n?")
    print("      (Tại sao mảng prefix có length n+1, không phải n?)")
    print("   2. Can prefix sum handle negative numbers?")
    print("      (Prefix sum xử lý được số âm không?)")
    print("   3. How would you compute 'prefix product'?")
    print("      (Tính 'tích tiền tố' bằng cách nào?)")
