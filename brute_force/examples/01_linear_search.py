"""
=============================================================
 Example 1: Linear Search (Tìm kiếm tuyến tính)
=============================================================

Problem: Find the index of a target value in an unsorted array.
         (Tìm index của giá trị target trong mảng không sắp xếp.)

Variant: Linear Search — Brute Force Variant 1
Time:    O(n) — scan every element once
Space:   O(1) — no extra data structures

How it works (Cách hoạt động):
  Step 1: Start from index 0 (Bắt đầu từ index 0)
  Step 2: Check if current element equals target (Kiểm tra phần tử hiện tại = target?)
  Step 3: If yes → return index. If no → move to next. (Đúng → trả về. Sai → tiếp)
  Step 4: If end of array → return -1 (not found) (Hết mảng → trả -1)
"""


def linear_search(arr, target):
    """
    Search for target in arr by checking every element.
    (Tìm target trong arr bằng cách duyệt từng phần tử.)

    Args:
        arr: list of elements (danh sách phần tử)
        target: value to find (giá trị cần tìm)

    Returns:
        index of target, or -1 if not found
        (index của target, hoặc -1 nếu không tìm thấy)
    """
    for i in range(len(arr)):
        print(f"  Step {i+1}: Check arr[{i}] = {arr[i]} ... ", end="")
        if arr[i] == target:
            print(f"✅ FOUND at index {i}!")
            return i
        else:
            print("✗ not a match, continue (tiếp)")
    
    print("  ❌ Reached end of array — target not found (Không tìm thấy)")
    return -1


def linear_search_min(arr):
    """
    Find the minimum element by checking every element.
    (Tìm phần tử nhỏ nhất bằng cách duyệt từng phần tử.)

    This shows that BF applies to more than just "find target".
    (BF không chỉ dùng để "tìm target" — còn dùng cho nhiều bài khác.)
    """
    if not arr:
        return None

    min_val = arr[0]  # Assume first is min (Giả sử phần tử đầu là nhỏ nhất)
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]  # Update min (Cập nhật min)
    return min_val


# ============================================================
# Test Cases (Các trường hợp kiểm tra)
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("TEST 1: Find target = 9 in [3, 7, 2, 9, 5]")
    print("=" * 50)
    result = linear_search([3, 7, 2, 9, 5], 9)
    assert result == 3, f"Expected 3, got {result}"
    print()

    print("=" * 50)
    print("TEST 2: Find target = 10 in [3, 7, 2, 9, 5]")
    print("=" * 50)
    result = linear_search([3, 7, 2, 9, 5], 10)
    assert result == -1, f"Expected -1, got {result}"
    print()

    print("=" * 50)
    print("TEST 3: Find minimum in [5, 3, 8, 1, 9]")
    print("=" * 50)
    result = linear_search_min([5, 3, 8, 1, 9])
    assert result == 1, f"Expected 1, got {result}"
    print(f"  Minimum value = {result} ✅")
    print()

    print("=" * 50)
    print("✅ All tests passed!")
    print("=" * 50)
    print()
    print("🤔 Think about it (Suy nghĩ thêm):")
    print("   1. If the array was SORTED, how could you find target faster?")
    print("      (Nếu mảng ĐÃ SẮP XẾP, tìm target nhanh hơn bằng cách nào?)")
    print("   2. If you need to search MANY TIMES, what data structure helps?")
    print("      (Nếu cần tìm NHIỀU LẦN, cấu trúc dữ liệu nào giúp ích?)")
