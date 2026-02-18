"""
=============================================================
 Example 4: Binary Search on Answer (BS trên đáp án)
=============================================================

The MOST IMPORTANT advanced BS pattern.
(Pattern BS nâng cao QUAN TRỌNG NHẤT.)

Instead of searching IN the array, search for the ANSWER itself.

Demonstrates:
  - Koko Eating Bananas (LC 875)
  - Ship Packages in D Days (LC 1011)

Time:  O(n × log(range))
Space: O(1)
"""
import math


def koko_brute(piles, h):
    """BF: try every speed from 1 to max(piles)."""
    for speed in range(1, max(piles) + 1):
        hours = sum(math.ceil(p / speed) for p in piles)
        if hours <= h:
            return speed
    return max(piles)


def koko_bs(piles, h):
    """
    BS on Answer: binary search for minimum speed.
    Search space: [1, max(piles)]
    Feasible: can finish in <= h hours?
    """
    def can_finish(speed):
        return sum(math.ceil(p / speed) for p in piles) <= h

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if can_finish(mid):
            hi = mid           # Can finish → try slower
        else:
            lo = mid + 1       # Too slow → need faster
    return lo


def koko_trace(piles, h):
    """Koko with BS trace."""
    def can_finish(speed):
        return sum(math.ceil(p / speed) for p in piles) <= h

    lo, hi = 1, max(piles)
    step = 0

    print(f"  Piles: {piles}, hours: {h}")
    print(f"  Search space: [{lo}, {hi}]")
    print()

    while lo < hi:
        step += 1
        mid = lo + (hi - lo) // 2
        hours = sum(math.ceil(p / mid) for p in piles)
        feasible = hours <= h
        action = "hi=mid" if feasible else "lo=mid+1"
        icon = "✅" if feasible else "❌"

        print(f"    Step {step}: lo={lo} mid={mid} hi={hi} "
              f"→ speed={mid}, hours={hours} "
              f"{'<=' if feasible else '>'} {h} "
              f"{icon} → {action}")

        if feasible:
            hi = mid
        else:
            lo = mid + 1

    return lo


def ship_packages(weights, days):
    """
    Ship Packages in D Days (LC 1011).
    BS on Answer: binary search for minimum capacity.
    Search space: [max(weights), sum(weights)]
    """
    def can_ship(capacity):
        ship_days = 1
        current_load = 0
        for w in weights:
            if current_load + w > capacity:
                ship_days += 1
                current_load = 0
            current_load += w
        return ship_days <= days

    lo = max(weights)
    hi = sum(weights)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if can_ship(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Koko Eating Bananas — Trace")
    print("=" * 60)
    result = koko_trace([3, 6, 7, 11], 8)
    assert result == 4
    print(f"\n  Min speed = {result} ✅")
    print()

    print("=" * 60)
    print("TEST 2: Koko — BF vs BS")
    print("=" * 60)
    cases = [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    ]
    for piles, h, expected in cases:
        bf = koko_brute(piles, h)
        bs = koko_bs(piles, h)
        match = bf == bs == expected
        status = "✅" if match else "❌"
        print(f"  piles={piles}, h={h} → "
              f"BF={bf} BS={bs} expected={expected} {status}")
    print()

    print("=" * 60)
    print("TEST 3: Ship Packages in D Days")
    print("=" * 60)
    cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
        ([3, 2, 2, 4, 1, 4], 3, 6),
        ([1, 2, 3, 1, 1], 4, 3),
    ]
    for weights, days, expected in cases:
        result = ship_packages(weights, days)
        status = "✅" if result == expected else "❌"
        print(f"  weights={weights}, days={days} "
              f"→ capacity={result} {status}")
    print()

    print("=" * 60)
    print("TEST 4: Performance — BS on Answer")
    print("=" * 60)
    import time
    import random

    for n in [100, 1000, 5000]:
        piles = [random.randint(1, 10**6) for _ in range(n)]
        h = n * 2

        start = time.perf_counter()
        result = koko_bs(piles, h)
        t = time.perf_counter() - start

        search_range = max(piles)
        print(f"  n={n:>5}, range=[1,{search_range}]: "
              f"answer={result}, time={t*1000:.2f}ms, "
              f"steps≈{math.log2(search_range):.0f}")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. BS on Answer: search for the VALUE, not the INDEX")
    print("   2. Define: search space [lo, hi] + feasibility check")
    print("   3. Total: O(n × log(range)) — very efficient!")
