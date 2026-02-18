"""
=============================================================
 Example 2: Interval Scheduling (LC 435, 452)
=============================================================

Classic Greedy: Sort by END time.

LC 435: Remove min intervals to make rest non-overlapping.
LC 452: Min arrows to burst balloons (same logic).

Time:  O(n log n) for sort
Space: O(1) or O(log n) stack
"""


def erase_overlap_intervals(intervals):
    """Min removals to make non-overlapping (LC 435)."""
    if not intervals:
        return 0
    # Sort by end time
    intervals.sort(key=lambda x: x[1])

    end = intervals[0][1]
    count = 0

    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            # Overlap! Remove the one that ends later (heuristic = sort)
            # Since we sorted by end, current one ends >= prev end.
            # So we effectively "remove" current by incrementing count
            # and keeping 'end' same (prev).
            count += 1
        else:
            # No overlap, update end
            end = intervals[i][1]

    return count


def find_min_arrows(points):
    """Min arrows to burst balloons (LC 452)."""
    if not points:
        return 0
    # Sort by end coordinate
    points.sort(key=lambda x: x[1])

    arrows = 1
    end = points[0][1]

    for start, e in points:
        if start > end:
            # Original arrow can't hit this, need new one
            arrows += 1
            end = e

    return arrows


if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Non-overlapping Intervals (LC 435)")
    print("=" * 60)
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    result = erase_overlap_intervals(intervals)
    assert result == 1  # Remove [1,3]
    print(f"  {intervals} → remove {result} ✅")

    intervals2 = [[1, 2], [1, 2], [1, 2]]
    result = erase_overlap_intervals(intervals2)
    assert result == 2
    print(f"  {intervals2} → remove {result} ✅")
    print()

    print("=" * 60)
    print("TEST 2: Min Arrows (LC 452)")
    print("=" * 60)
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    result = find_min_arrows(points)
    assert result == 2
    print(f"  {points} → {result} arrows ✅")
    print()

    print("✅ All tests passed!")
