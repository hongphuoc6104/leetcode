"""
=============================================================
 Example 1: Array Traversal Basics (Duyệt mảng cơ bản)
=============================================================

Demonstrates 4 ways to traverse an array in Python
and when to use each one.
(Minh họa 4 cách duyệt mảng và khi nào dùng từng cách.)

Time: O(n) for all traversal methods
Space: O(1) — no extra storage
"""


def traverse_by_index(arr):
    """Traverse using index — when you need position. (Duyệt bằng index — khi cần vị trí.)"""
    print("  Method 1: By index (range)")
    for i in range(len(arr)):
        print(f"    arr[{i}] = {arr[i]}")


def traverse_by_value(arr):
    """Traverse using value — when you only need elements. (Duyệt bằng giá trị — khi chỉ cần phần tử.)"""
    print("  Method 2: By value (for-in)")
    for val in arr:
        print(f"    value = {val}")


def traverse_enumerate(arr):
    """Traverse with enumerate — when you need BOTH index and value. (Khi cần CẢ index và giá trị.)"""
    print("  Method 3: Enumerate (index + value)")
    for i, val in enumerate(arr):
        print(f"    index={i}, value={val}")


def traverse_reverse(arr):
    """Traverse in reverse — sometimes needed for in-place operations. (Duyệt ngược — đôi khi cần cho thao tác tại chỗ.)"""
    print("  Method 4: Reverse")
    for i in range(len(arr) - 1, -1, -1):
        print(f"    arr[{i}] = {arr[i]}")


def find_max_and_index(arr):
    """
    Practical example: Find max value AND its index.
    (Ví dụ thực tế: Tìm giá trị max VÀ index của nó.)
    Uses Method 3 (enumerate) because we need both.
    """
    max_val = arr[0]
    max_idx = 0
    for i, val in enumerate(arr):
        if val > max_val:
            max_val = val
            max_idx = i
    return max_val, max_idx


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    arr = [10, 30, 20, 50, 40]

    print("=" * 50)
    print(f"Array: {arr}")
    print("=" * 50)
    print()

    traverse_by_index(arr)
    print()
    traverse_by_value(arr)
    print()
    traverse_enumerate(arr)
    print()
    traverse_reverse(arr)
    print()

    print("=" * 50)
    print("PRACTICAL: Find max value and its index")
    print("=" * 50)
    val, idx = find_max_and_index(arr)
    print(f"  Max value = {val} at index {idx}")
    assert val == 50 and idx == 3
    print("  ✅ Correct!")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it (Suy nghĩ thêm):")
    print("   1. Which method is best for 'reverse array in-place'?")
    print("      (Phương pháp nào tốt nhất để đảo mảng tại chỗ?)")
    print("   2. When would you prefer Method 1 over Method 3?")
    print("      (Khi nào chọn Method 1 thay vì Method 3?)")
