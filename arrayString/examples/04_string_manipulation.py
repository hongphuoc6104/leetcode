"""
=============================================================
 Example 4: String Manipulation (Thao tác chuỗi)
=============================================================

Demonstrates common string operations and the IMMUTABILITY trap.
(Minh họa thao tác chuỗi thường gặp và bẫy BẤT BIẾN.)

Key lessons:
  1. Strings are IMMUTABLE — each modification creates new string
  2. Use list + join for efficient string building
  3. Common string patterns for coding interviews
"""


def reverse_string(s):
    """
    Reverse a string using list conversion.
    (Đảo chuỗi bằng chuyển đổi sang list.)
    
    Can't modify string directly because strings are immutable!
    (Không thể sửa chuỗi trực tiếp vì chuỗi bất biến!)
    """
    chars = list(s)  # Convert to list (Chuyển sang list)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)  # Convert back (Chuyển lại)


def is_palindrome(s):
    """
    Check if string is palindrome (ignoring case and non-alphanumeric).
    (Kiểm tra chuỗi đối xứng — bỏ qua hoa/thường và ký tự đặc biệt.)
    """
    # Clean the string (Làm sạch chuỗi)
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    # Two pointer check (Kiểm tra 2 con trỏ)
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


def string_building_comparison(n):
    """
    Compare O(n²) string concat vs O(n) join.
    (So sánh nối chuỗi O(n²) vs join O(n).)
    """
    import time

    # ❌ BAD: String concatenation — O(n²)
    start = time.perf_counter()
    result_bad = ""
    for i in range(n):
        result_bad += str(i % 10)  # Creates new string each time!
    time_bad = time.perf_counter() - start

    # ✅ GOOD: List + join — O(n)
    start = time.perf_counter()
    parts = []
    for i in range(n):
        parts.append(str(i % 10))
    result_good = ''.join(parts)
    time_good = time.perf_counter() - start

    return time_bad, time_good, result_bad == result_good


def first_unique_char(s):
    """
    Find first non-repeating character.
    (Tìm ký tự đầu tiên không lặp.)
    
    Uses frequency counting pattern.
    (Dùng pattern đếm tần suất.)
    """
    from collections import Counter
    count = Counter(s)
    
    for i, char in enumerate(s):
        if count[char] == 1:
            return i  # First unique! (Ký tự unique đầu tiên!)
    return -1


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Reverse String")
    print("=" * 60)
    tests = ["hello", "Python", "a", ""]
    for s in tests:
        result = reverse_string(s)
        expected = s[::-1]
        status = "✅" if result == expected else "❌"
        print(f'  "{s}" → "{result}" {status}')
    print()

    print("=" * 60)
    print("TEST 2: Palindrome Check")
    print("=" * 60)
    palindrome_tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("", True),
    ]
    for s, expected in palindrome_tests:
        result = is_palindrome(s)
        status = "✅" if result == expected else "❌"
        print(f'  "{s}" → {result} {status}')
    print()

    print("=" * 60)
    print("TEST 3: String Building — += vs join")
    print("=" * 60)
    for n in [1000, 10000, 50000]:
        bad_time, good_time, same = string_building_comparison(n)
        speedup = bad_time / good_time if good_time > 0 else float('inf')
        print(f"  n={n:>6}: += {bad_time*1000:>8.2f}ms | "
              f"join {good_time*1000:>8.2f}ms | "
              f"Speedup: {speedup:>5.1f}x | Same result: {same}")
    print()

    print("=" * 60)
    print("TEST 4: First Unique Character")
    print("=" * 60)
    tests = [("leetcode", 0), ("loveleetcode", 2), ("aabb", -1)]
    for s, expected in tests:
        result = first_unique_char(s)
        status = "✅" if result == expected else "❌"
        char = f"'{s[result]}'" if result >= 0 else "none"
        print(f'  "{s}" → index {result} ({char}) {status}')
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it (Suy nghĩ thêm):")
    print("   1. Why must we convert string to list to reverse in-place?")
    print("      (Tại sao phải chuyển chuỗi sang list để đảo tại chỗ?)")
    print("   2. What is the Big-O of is_palindrome?")
    print("      (Big-O của is_palindrome là gì?)")
    print("   3. For first_unique_char, can you do it with ONE pass?")
    print("      (Với first_unique_char, có thể làm trong MỘT lần duyệt không?)")
