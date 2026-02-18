"""
=============================================================
 Example 2: Merge Sort
=============================================================

Divide and Conquer. O(n log n) guaranteed. Stable.
Cons: Uses O(n) extra space.
Ideal for sorting Linked Lists.
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Extend remaining
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 100) for _ in range(20)]
    print(f"Original: {nums}")

    sorted_nums = merge_sort(nums)
    print(f"Sorted:   {sorted_nums}")

    assert sorted_nums == sorted(nums)
    print("✅ Merge sort correct!")
