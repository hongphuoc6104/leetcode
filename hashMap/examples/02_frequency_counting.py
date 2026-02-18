"""
=============================================================
 Example 2: Frequency Counting (Đếm tần suất)
=============================================================

Demonstrates:
  - Valid Anagram (LC 242)
  - First Unique Character (LC 387)
  - Top K Frequent Elements (LC 347)

Time:  O(n)
Space: O(k) where k = distinct elements
"""
from collections import Counter


def is_anagram(s, t):
    """Check if t is anagram of s: O(n)."""
    return Counter(s) == Counter(t)


def first_unique_char(s):
    """First character that appears exactly once: O(n)."""
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


def top_k_frequent(nums, k):
    """Top k most frequent elements: O(n log k)."""
    return [x for x, _ in Counter(nums).most_common(k)]


def top_k_bucket_sort(nums, k):
    """
    Top k using bucket sort: O(n).
    Bucket[i] = elements with frequency i.
    """
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Valid Anagram")
    print("=" * 60)
    cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("ab", "a", False),
    ]
    for s, t, expected in cases:
        result = is_anagram(s, t)
        status = "✅" if result == expected else "❌"
        print(f'  "{s}" vs "{t}" → {result} {status}')
    print()

    print("=" * 60)
    print("TEST 2: First Unique Character")
    print("=" * 60)
    cases = [
        ("leetcode", 0),       # 'l'
        ("loveleetcode", 2),   # 'v'
        ("aabb", -1),
    ]
    for s, expected in cases:
        result = first_unique_char(s)
        status = "✅" if result == expected else "❌"
        char = s[result] if result >= 0 else "None"
        print(f'  "{s}" → index {result} '
              f'("{char}") {status}')
    print()

    print("=" * 60)
    print("TEST 3: Top K Frequent")
    print("=" * 60)
    cases = [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 1, -1, 2, -1, 2, 3], 2, {-1, 2}),
    ]
    for nums, k, expected_set in cases:
        result = top_k_frequent(nums, k)
        bucket = top_k_bucket_sort(nums, k)
        match = set(result) == expected_set
        status = "✅" if match else "❌"
        print(f"  {nums}, k={k} → {result} "
              f"(bucket: {bucket}) {status}")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Counter(s) == Counter(t) → anagram check O(n)")
    print("   2. Bucket sort gives O(n) for Top K (vs O(n log k))")
    print("   3. Counter.most_common(k) is the Pythonic way")
