"""
=============================================================
 Example 4: Find Median from Data Stream (LC 295)
=============================================================

Two-heap approach:
  - lo (max-heap): stores smaller half
  - hi (min-heap): stores larger half
  - Median is at the tops of the heaps

Time:  O(log n) per add, O(1) for median
Space: O(n)
"""
import heapq


class MedianFinder:
    def __init__(self):
        self.lo = []  # max-heap (negate values)
        self.hi = []  # min-heap

    def addNum(self, num):
        # Always push to lo first (as max-heap)
        heapq.heappush(self.lo, -num)
        # Move lo's max to hi
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        # Balance: lo should have >= elements
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Median from Stream")
    print("=" * 60)
    mf = MedianFinder()
    stream = [2, 3, 4]
    expected = [2.0, 2.5, 3.0]
    for num, exp in zip(stream, expected):
        mf.addNum(num)
        med = mf.findMedian()
        status = "✅" if med == exp else "❌"
        print(f"  Add {num} → median={med} {status}")
    print()

    print("=" * 60)
    print("TEST 2: Larger Stream")
    print("=" * 60)
    mf2 = MedianFinder()
    nums = [5, 15, 1, 3, 8, 7, 9, 2]
    for num in nums:
        mf2.addNum(num)
        med = mf2.findMedian()
        lo_vals = sorted([-x for x in mf2.lo])
        hi_vals = sorted(mf2.hi)
        print(f"  Add {num:>2}: lo={lo_vals} | hi={hi_vals} → "
              f"median={med}")
    # After all: sorted = [1,2,3,5,7,8,9,15], median = (5+7)/2 = 6.0
    assert mf2.findMedian() == 6.0
    print("  ✅ Final median = 6.0!")
    print()

    print("=" * 60)
    print("TEST 3: Single Element")
    print("=" * 60)
    mf3 = MedianFinder()
    mf3.addNum(42)
    assert mf3.findMedian() == 42
    print("  Single 42 → median=42 ✅")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. lo (max-heap) stores SMALLER half")
    print("   2. hi (min-heap) stores LARGER half")
    print("   3. Balance: len(lo) == len(hi) or len(lo) == len(hi)+1")
    print("   4. Median: top of lo, or average of both tops")
