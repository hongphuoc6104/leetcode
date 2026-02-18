"""
=============================================================
 Example 4: Level-Order Traversal (BFS on Trees)
=============================================================

Demonstrates:
  - Level Order (LC 102)
  - Zigzag Level Order (LC 103)
  - Right Side View (LC 199)

Time:  O(n)
Space: O(w) — max width of tree
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


def level_order(root):
    """Standard BFS level-order."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def zigzag_order(root):
    """Zigzag level-order: alternate left-right, right-left."""
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not left_to_right:
            level.reverse()
        result.append(level)
        left_to_right = not left_to_right
    return result


def right_side_view(root):
    """Binary tree right side view — last node per level."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0:
                result.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
    return result


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root = build_tree([3, 9, 20, None, None, 15, 7])

    print("=" * 60)
    print("TEST 1: Level Order")
    print("=" * 60)
    result = level_order(root)
    print(f"  Levels: {result}")
    assert result == [[3], [9, 20], [15, 7]]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 2: Zigzag Level Order")
    print("=" * 60)
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root2 = build_tree([1, 2, 3, 4, 5, None, 6])
    result = zigzag_order(root2)
    print(f"  Zigzag: {result}")
    assert result == [[1], [3, 2], [4, 5, 6]]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 3: Right Side View")
    print("=" * 60)
    result = right_side_view(root)
    print(f"  Right view: {result}")
    assert result == [3, 20, 7]
    print("  ✅ Passed!")

    root3 = build_tree([1, 2, 3, None, 5, None, 4])
    result = right_side_view(root3)
    print(f"  Right view: {result}")
    assert result == [1, 3, 4]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 4: Edge Cases")
    print("=" * 60)
    assert level_order(None) == []
    print("  None → [] ✅")
    single = TreeNode(1)
    assert level_order(single) == [[1]]
    print("  Single → [[1]] ✅")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. BFS = deque + process len(queue) per level")
    print("   2. Zigzag = BFS + reverse every other level")
    print("   3. Right view = first node per level (right-first BFS)")
