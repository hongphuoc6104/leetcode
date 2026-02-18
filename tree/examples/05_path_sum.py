"""
=============================================================
 Example 5: Path Sum & LCA
=============================================================

Demonstrates:
  - Path Sum (LC 112)
  - All Root-to-Leaf Paths (LC 257)
  - Lowest Common Ancestor (LC 236)

Time:  O(n)
Space: O(h)
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


def find_node(root, val):
    """Find node by value."""
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


def has_path_sum(root, target):
    """Check if root-to-leaf path sums to target."""
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target
    target -= root.val
    return (has_path_sum(root.left, target) or
            has_path_sum(root.right, target))


def all_paths(root):
    """Return all root-to-leaf paths."""
    if not root:
        return []
    if not root.left and not root.right:
        return [[root.val]]
    paths = []
    for path in all_paths(root.left):
        paths.append([root.val] + path)
    for path in all_paths(root.right):
        paths.append([root.val] + path)
    return paths


def lca(root, p, q):
    """Lowest Common Ancestor: O(n)."""
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left or right


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  / \       \
    # 7   2       1
    root = build_tree([5, 4, 8, 11, None, 13, 4,
                       7, 2, None, None, None, 1])

    print("=" * 60)
    print("TEST 1: Has Path Sum")
    print("=" * 60)
    assert has_path_sum(root, 22) is True   # 5→4→11→2
    print(f"  target=22 → True  (5→4→11→2) ✅")
    assert has_path_sum(root, 26) is True   # 5→8→13
    print(f"  target=26 → True  (5→8→13) ✅")
    assert has_path_sum(root, 100) is False
    print(f"  target=100 → False ✅")
    print()

    print("=" * 60)
    print("TEST 2: All Root-to-Leaf Paths")
    print("=" * 60)
    paths = all_paths(root)
    for p in paths:
        total = sum(p)
        print(f"  {'→'.join(map(str, p))} = {total}")
    assert len(paths) == 4
    print(f"  Total paths: {len(paths)} ✅")
    print()

    print("=" * 60)
    print("TEST 3: Lowest Common Ancestor")
    print("=" * 60)
    #       3
    #      / \
    #     5   1
    #    / \   \
    #   6   2   8
    root2 = build_tree([3, 5, 1, 6, 2, None, 8])
    p = find_node(root2, 5)
    q = find_node(root2, 1)
    result = lca(root2, p, q)
    assert result.val == 3
    print(f"  LCA(5, 1) = {result.val} ✅")

    p = find_node(root2, 5)
    q = find_node(root2, 6)
    result = lca(root2, p, q)
    assert result.val == 5
    print(f"  LCA(5, 6) = {result.val} ✅")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Path Sum: subtract val, check leaf == 0")
    print("   2. All paths: collect at leaves, build upward")
    print("   3. LCA: found on both sides → current node = LCA")
