"""
=============================================================
 Example 1: Basic Sorts (Bubble & Insertion)
=============================================================

Demonstrates O(n^2) sorts. 
Use only for education or very small arrays (n < 50).

Insertion Sort is fast (O(n)) for nearly sorted data.
"""


def bubble_sort(arr):
    n = len(arr)
    # Optimized: stop if no swaps
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements > key one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {nums}")
    
    # Test Bubble
    b_copy = nums[:]
    bubble_sort(b_copy)
    print(f"Bubble:   {b_copy}")
    assert b_copy == sorted(nums)
    
    # Test Insertion
    i_copy = nums[:]
    insertion_sort(i_copy)
    print(f"Insertion:{i_copy}")
    assert i_copy == sorted(nums)
    
    print("✅ All tests passed!")
