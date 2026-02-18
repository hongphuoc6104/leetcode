"""
=============================================================
 Example 4: Counting Sort
=============================================================

Non-comparison sort. O(n + k) where k is range of values.
Great for small integer ranges (ages, test scores).
"""


def counting_sort(nums):
    if not nums: return []
    _min = min(nums)
    _max = max(nums)
    range_val = _max - _min + 1

    count = [0] * range_val
    output = [0] * len(nums)

    # 1. Count frequencies
    for num in nums:
        count[num - _min] += 1

    # 2. Cumulative sums (for stable sorting position)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 3. Build output array (reverse to preserve stability)
    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        output[count[num - _min] - 1] = num
        count[num - _min] -= 1

    return output


if __name__ == "__main__":
    nums = [4, 2, 2, 8, 3, 3, 1]
    print(f"Original: {nums}")

    sorted_nums = counting_sort(nums)
    print(f"Sorted:   {sorted_nums}")

    assert sorted_nums == sorted(nums)
    print("✅ Counting sort correct!")
    
    # Negative numbers test
    neg = [-5, -10, 0, -3, 8, 5, -1, 10]
    sorted_neg = counting_sort(neg)
    print(f"Negative: {sorted_neg}")
    assert sorted_neg == sorted(neg)
    print("✅ Negative numbers handled!")
