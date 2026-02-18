"""
=============================================================
 Example 5: Custom Sort (Comparators)
=============================================================

Python 3 uses `key` functions instead of `cmp`.
Use `functools.cmp_to_key` for complex comparison logic.

Example: Largest Number (LC 179)
"""
from functools import cmp_to_key


def largest_number(nums):
    """Given [3, 30, 34, 5, 9], return "9534330"."""
    
    # Custom comparator: a+b vs b+a
    def compare(x, y):
        x, y = str(x), str(y)
        # Determine which order creates larger number
        if x + y > y + x:
            return -1  # x comes first (return -1 for < in sort)
        elif x + y < y + x:
            return 1
        else:
            return 0

    # Convert to strings and sort using key
    strs = [str(num) for num in nums]
    strs.sort(key=cmp_to_key(compare))
    
    # Helper for "00" case
    result = "".join(strs)
    return "0" if result[0] == "0" else result


if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    # "9" > "5" > "34" > "3" > "30"
    result = largest_number(nums)
    print(f"Largest Number from {nums}: {result}")
    
    assert result == "9534330"
    print("✅ Test 1 Passed")
    
    assert largest_number([10, 2]) == "210"
    print("✅ Test 2 Passed")
    
    # Simple Length Sort
    words = ["apple", "bat", "code", "atom"]
    # Sort by length, then by alpha
    words.sort(key=lambda w: (len(w), w))
    print(f"Sorted words: {words}")
    assert words == ['bat', 'atom', 'code', 'apple']
    print("✅ Lambda Sort Passed")
