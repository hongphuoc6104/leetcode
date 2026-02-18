"""
=============================================================
 Example 3: Gas Station (LC 134)
=============================================================

Greedy: If we can't reach B from A, we can't reach B from ANY station between A and B.
Start over from B+1.

Time:  O(n)
Space: O(1)
"""


def can_complete_circuit(gas, cost):
    """Return starting index or -1."""
    if sum(gas) < sum(cost):
        return -1

    total_tank = 0
    start_index = 0

    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        if total_tank < 0:
            # Failed at i. Start from i + 1.
            start_index = i + 1
            total_tank = 0

    return start_index


if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Gas Station")
    print("=" * 60)
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    # Sum gas=15, cost=15. Possible.
    result = can_complete_circuit(gas, cost)
    assert result == 3  # Start at index 3 (val 4)
    print(f"  gas={gas}, cost={cost} → start {result} ✅")

    print("=" * 60)
    print("TEST 2: Impossible Case")
    print("=" * 60)
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    # Sum gas=9, cost=10. Impossible.
    result = can_complete_circuit(gas, cost)
    assert result == -1
    print(f"  gas={gas}, cost={cost} → {result} ✅")
    print()

    print("✅ All tests passed!")
