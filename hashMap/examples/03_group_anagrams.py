"""
=============================================================
 Example 3: Group Anagrams (LC 49)
=============================================================

Group strings that are anagrams of each other.
Key insight: sorted string is the grouping key.

Time:  O(n × k log k) where k = max string length
Space: O(n × k)
"""
from collections import defaultdict


def group_anagrams_sort(strs):
    """Group by sorted string key."""
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())


def group_anagrams_count(strs):
    """
    Group by character count key: O(n × k).
    Avoids sorting — better when k is large.
    """
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)
        groups[key].append(s)
    return list(groups.values())


def group_trace(strs):
    """Group anagrams with trace."""
    groups = defaultdict(list)

    print(f"  Input: {strs}")

    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
        print(f'    "{s}" → key={"".join(sorted(s)):>5} '
              f'→ group size {len(groups[key])}')

    print(f"\n  Groups:")
    for key, group in groups.items():
        print(f'    {"".join(key)} → {group}')

    return list(groups.values())


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Group Anagrams — Trace")
    print("=" * 60)
    result = group_trace(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Verify: 3 groups
    assert len(result) == 3
    # Verify all anagram groups
    sets = [set(g) for g in result]
    assert {"eat", "tea", "ate"} in sets
    assert {"tan", "nat"} in sets
    assert {"bat"} in sets
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 2: Sort Key vs Count Key — Same Result")
    print("=" * 60)
    inputs = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["abc", "bca", "cab", "def", "fed"],
    ]
    for strs in inputs:
        r1 = group_anagrams_sort(strs)
        r2 = group_anagrams_count(strs)
        # Compare as sets of frozen sets
        s1 = {frozenset(g) for g in r1}
        s2 = {frozenset(g) for g in r2}
        match = s1 == s2
        status = "✅" if match else "❌"
        print(f"  {strs[:3]}... → {len(r1)} groups {status}")
    print()

    print("=" * 60)
    print("TEST 3: Performance")
    print("=" * 60)
    import time
    import random
    import string

    for n in [1000, 5000, 10000]:
        strs = [''.join(random.choices(string.ascii_lowercase, k=5))
                for _ in range(n)]

        start = time.perf_counter()
        r1 = group_anagrams_sort(strs)
        t1 = time.perf_counter() - start

        start = time.perf_counter()
        r2 = group_anagrams_count(strs)
        t2 = time.perf_counter() - start

        print(f"  n={n:>5}: sort_key={t1*1000:.2f}ms | "
              f"count_key={t2*1000:.2f}ms")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. sorted(s) → anagram key (O(k log k))")
    print("   2. char count tuple → anagram key (O(k))")
    print("   3. defaultdict(list) makes grouping clean")
