"""
=============================================================
 Example 2: Max Depth & Related Problems
=============================================================

Demonstrates the core recursive DFS pattern:
  - Max Depth (LC 104)
  - Is Balanced (LC 110)
  - Diameter (LC 543)

Time:  O(n)
Space: O(h) — recursion stack
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def max_depth(root):
    """Max depth of binary tree: O(n)."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def is_balanced(root):
    """Check if tree is height-balanced: O(n)."""
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        right = check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1


def diameter(root):
    """
    Diameter = longest path between any two nodes: O(n).
    Path goes through some node: left_depth + right_depth.
    """
    best = [0]

    def depth(node):
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        best[0] = max(best[0], left + right)
        return 1 + max(left, right)

    depth(root)
    return best[0]


def invert_tree(root):
    """Invert (mirror) binary tree: O(n)."""
    if not root:
        return None
    root.left, root.right = (invert_tree(root.right),
                              invert_tree(root.left))
    return root


def tree_values(root):
    """Get level-order values for easy comparison."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Max Depth")
    print("=" * 60)
    cases = [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
        ([1], 1),
    ]
    for vals, expected in cases:
        root = build_tree(vals)
        result = max_depth(root)
        status = "✅" if result == expected else "❌"
        print(f"  {vals} → depth={result} {status}")
    print()

    print("=" * 60)
    print("TEST 2: Is Balanced")
    print("=" * 60)
    balanced = build_tree([3, 9, 20, None, None, 15, 7])
    unbalanced = build_tree([1, 2, None, 3, None, None, None, 4])
    assert is_balanced(balanced) is True
    print(f"  [3,9,20,15,7] → balanced=True ✅")
    assert is_balanced(unbalanced) is False
    print(f"  [1,2,3,4] (skewed) → balanced=False ✅")
    print()

    print("=" * 60)
    print("TEST 3: Diameter")
    print("=" * 60)
    root = build_tree([1, 2, 3, 4, 5])
    d = diameter(root)
    assert d == 3  # 4→2→1→3 or 5→2→1→3
    print(f"  [1,2,3,4,5] → diameter={d} ✅")

    root = build_tree([1, 2])
    d = diameter(root)
    assert d == 1
    print(f"  [1,2] → diameter={d} ✅")
    print()

    print("=" * 60)
    print("TEST 4: Invert Tree")
    print("=" * 60)
    root = build_tree([4, 2, 7, 1, 3, 6, 9])
    print(f"  Before: {tree_values(root)}")
    inverted = invert_tree(root)
    vals = tree_values(inverted)
    print(f"  After:  {vals}")
    assert vals == [4, 7, 2, 9, 6, 3, 1]
    print("  ✅ Passed!")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. max_depth = 1 + max(left, right) — THE pattern")
    print("   2. Diameter passes through a node: L_depth + R_depth")
    print("   3. Return -1 early for efficient balanced check")
