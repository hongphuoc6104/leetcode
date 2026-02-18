"""
=============================================================
 Example 4: Partition Labels (LC 763)
=============================================================

Greedy: A partition must include the LAST occurrence of all characters inside it.
Extend 'end' as we iterate.

Time:  O(n)
Space: O(1) (map size capped at 26 chars)
"""


def partition_labels(s):
    # Pass 1: find last index of each char
    last = {c: i for i, c in enumerate(s)}

    j = anchor = 0
    result = []

    # Pass 2: iterate
    for i, c in enumerate(s):
        j = max(j, last[c])
        if i == j:
            result.append(i - anchor + 1)
            anchor = i + 1

    return result


if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Partition Labels")
    print("=" * 60)
    s = "ababcbacadefegdehijhklij"
    result = partition_labels(s)
    expected = [9, 7, 8]  # "ababcbaca", "defegde", "hijhklij"
    assert result == expected
    print(f"  {s} → {result} ✅")

    print("=" * 60)
    print("TEST 2: Single Partition")
    print("=" * 60)
    s2 = "eccbbbbdec"
    result = partition_labels(s2)
    assert result == [10]
    print(f"  {s2} → {result} ✅")
    print()

    print("✅ All tests passed!")
