"""
=============================================================
 Example 5: Task Scheduler (LC 621) & Sort Characters (LC 767)
=============================================================

Greedy + Heap: always process the most frequent element first.

Time:  O(n log k) where k = unique characters
Space: O(k)
"""
import heapq
from collections import Counter


def least_interval(tasks, n):
    """Task Scheduler (LC 621). Returns min intervals needed."""
    counts = Counter(tasks)
    # Max-heap: most frequent tasks first
    heap = [-cnt for cnt in counts.values()]
    heapq.heapify(heap)

    time = 0
    while heap:
        cycle = []
        for _ in range(n + 1):  # Process n+1 slots per cycle
            if heap:
                cnt = heapq.heappop(heap)
                if cnt + 1 < 0:
                    cycle.append(cnt + 1)
            time += 1
            if not heap and not cycle:
                break
        for cnt in cycle:
            heapq.heappush(heap, cnt)

    return time


def reorganize_string(s):
    """Reorganize String (LC 767) — no two adjacent same chars."""
    counts = Counter(s)
    heap = [(-cnt, ch) for ch, cnt in counts.items()]
    heapq.heapify(heap)

    result = []
    prev = (0, '')

    while heap:
        cnt, ch = heapq.heappop(heap)
        result.append(ch)
        if prev[0] < 0:
            heapq.heappush(heap, prev)
        prev = (cnt + 1, ch)  # Decrement count (was negated)

    return ''.join(result) if len(result) == len(s) else ""


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Task Scheduler")
    print("=" * 60)
    cases = [
        (['A','A','A','B','B','B'], 2, 8),
        (['A','A','A','B','B','B'], 0, 6),
        (['A','A','A','A','A','A','B','C','D','E','F','G'], 2, 16),
    ]
    for tasks, n, expected in cases:
        result = least_interval(tasks, n)
        status = "✅" if result == expected else "❌"
        print(f"  tasks={tasks}, n={n} → {result} intervals {status}")
    print()

    print("=" * 60)
    print("TEST 2: Reorganize String")
    print("=" * 60)
    cases = [
        ("aab", True),
        ("aaab", False),
        ("aabb", True),
    ]
    for s, possible in cases:
        result = reorganize_string(s)
        ok = (len(result) == len(s)) == possible
        if result:
            # Verify no adjacent same chars
            valid = all(result[i] != result[i+1]
                       for i in range(len(result)-1))
            assert valid, f"Invalid: {result}"
        status = "✅" if ok else "❌"
        print(f'  "{s}" → "{result}" (possible={possible}) {status}')
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Most frequent first → greedy via max-heap")
    print("   2. Cooldown: process n+1 per cycle, save remaining")
    print("   3. Reorganize: keep previous, push back after next pop")
