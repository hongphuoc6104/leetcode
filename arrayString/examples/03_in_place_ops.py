"""
=============================================================
 Example 3: In-Place Operations (Thao tác tại chỗ)
=============================================================

Demonstrates array modification WITHOUT extra space.
(Minh họa sửa mảng KHÔNG dùng bộ nhớ thêm.)

Key techniques:
  1. Write Pointer — overwrite from left (Con trỏ ghi — ghi đè từ trái)
  2. Two-Pointer Swap — process from both ends (Hai con trỏ hoán đổi — xử lý từ 2 đầu)

Time:  O(n)
Space: O(1) — in-place!
"""


def remove_element(arr, val):
    """
    Remove all occurrences of val from arr IN-PLACE.
    Return the new length. (Xóa tất cả val từ mảng TẠI CHỖ.)

    Uses Write Pointer pattern.
    (Dùng pattern Con trỏ ghi.)
    """
    write = 0  # Position to write next valid element (Vị trí ghi phần tử hợp lệ tiếp)

    print(f"  Removing val={val} from {arr}")
    for read in range(len(arr)):
        if arr[read] != val:
            print(f"    read={read}, arr[{read}]={arr[read]} ≠ {val} → write to position {write}")
            arr[write] = arr[read]
            write += 1
        else:
            print(f"    read={read}, arr[{read}]={arr[read]} == {val} → skip (bỏ qua)")

    print(f"  Result: {arr[:write]} (length={write})")
    return write


def move_zeroes(arr):
    """
    Move all zeroes to end, maintain order of non-zeroes.
    (Di chuyển tất cả 0 ra cuối, giữ thứ tự phần tử khác 0.)

    IN-PLACE, O(n) time, O(1) space.
    """
    write = 0  # Write pointer for non-zero elements

    # Pass 1: Move all non-zero elements to front (Chuyển phần tử ≠ 0 ra trước)
    for read in range(len(arr)):
        if arr[read] != 0:
            arr[write] = arr[read]
            write += 1

    # Pass 2: Fill rest with zeroes (Điền phần còn lại bằng 0)
    while write < len(arr):
        arr[write] = 0
        write += 1

    return arr


def reverse_array(arr):
    """
    Reverse array in-place using two pointers.
    (Đảo mảng tại chỗ bằng hai con trỏ.)
    """
    left, right = 0, len(arr) - 1
    steps = 0

    print(f"  Reversing {arr}")
    while left < right:
        steps += 1
        print(f"    Step {steps}: swap arr[{left}]={arr[left]} ↔ arr[{right}]={arr[right]}")
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    print(f"  Result: {arr} (in {steps} swaps)")
    return arr


def dutch_flag_partition(arr):
    """
    Sort array containing only 0, 1, 2 in-place (Dutch National Flag).
    (Sắp xếp mảng chỉ chứa 0, 1, 2 tại chỗ — Bài toán Cờ Hà Lan.)

    Uses 3 pointers: low, mid, high.
    - [0..low-1] = all 0s
    - [low..mid-1] = all 1s
    - [high+1..n-1] = all 2s
    """
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Remove Element")
    print("=" * 60)
    arr = [3, 2, 2, 3, 4, 2, 5]
    new_len = remove_element(arr, 2)
    assert new_len == 4
    assert arr[:new_len] == [3, 3, 4, 5]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 2: Move Zeroes")
    print("=" * 60)
    arr = [0, 1, 0, 3, 12]
    print(f"  Before: {arr}")
    move_zeroes(arr)
    print(f"  After:  {arr}")
    assert arr == [1, 3, 12, 0, 0]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 3: Reverse Array In-Place")
    print("=" * 60)
    arr = [1, 2, 3, 4, 5]
    reverse_array(arr)
    assert arr == [5, 4, 3, 2, 1]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 4: Dutch Flag (Sort 0,1,2)")
    print("=" * 60)
    arr = [2, 0, 2, 1, 1, 0]
    print(f"  Before: {arr}")
    dutch_flag_partition(arr)
    print(f"  After:  {arr}")
    assert arr == [0, 0, 1, 1, 2, 2]
    print("  ✅ Passed!")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it (Suy nghĩ thêm):")
    print("   1. In remove_element, what happens if write == read?")
    print("      (Điều gì xảy ra khi write == read?)")
    print("   2. Can you combine move_zeroes into a single pass with swaps?")
    print("      (Có thể gộp move_zeroes thành 1 pass với swap không?)")
    print("   3. Why does Dutch Flag need 3 pointers, not 2?")
    print("      (Tại sao Dutch Flag cần 3 con trỏ, không phải 2?)")
