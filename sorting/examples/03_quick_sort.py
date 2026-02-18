"""
=============================================================
 Example 3: Quick Sort
=============================================================

Divide and Conquer. Pivot-based partitioning.
Avg O(n log n), Worst O(n^2).
Space O(log n) stack. Unstable.
Typically faster than MergeSort in practice due to locality.
"""


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]  # Choosing last element as pivot
    i = low - 1        # Pointer for smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap pivot into correct place
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 100) for _ in range(20)]
    print(f"Original: {nums}")

    q_copy = nums[:]
    quick_sort(q_copy, 0, len(q_copy) - 1)
    print(f"Sorted:   {q_copy}")

    assert q_copy == sorted(nums)
    print("✅ Quick sort correct!")
