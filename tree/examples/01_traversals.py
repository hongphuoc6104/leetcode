"""
=============================================================
 Example 1: Tree Traversals (Duyệt cây)
=============================================================

All 4 traversals: Preorder, Inorder, Postorder, Level-order.
Both recursive and iterative versions.

Time:  O(n) — visit every node once
Space: O(h) DFS, O(w) BFS
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Build tree from level-order list (None = no node)."""
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


# DFS — Recursive
def preorder(root):
    """Root → Left → Right."""
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
    """Left → Root → Right."""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    """Left → Right → Root."""
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


# DFS — Iterative
def preorder_iter(root):
    """Iterative preorder using stack."""
    if not root:
        return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def inorder_iter(root):
    """Iterative inorder using stack."""
    stack, result = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result


# BFS
def level_order(root):
    """Level-order traversal (BFS)."""
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


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = build_tree([1, 2, 3, 4, 5, None, 6])

    print("=" * 60)
    print("TEST 1: DFS Traversals")
    print("=" * 60)
    print(f"  Preorder:  {preorder(root)}")
    print(f"  Inorder:   {inorder(root)}")
    print(f"  Postorder: {postorder(root)}")
    assert preorder(root) == [1, 2, 4, 5, 3, 6]
    assert inorder(root) == [4, 2, 5, 1, 3, 6]
    assert postorder(root) == [4, 5, 2, 6, 3, 1]
    print("  ✅ All passed!")
    print()

    print("=" * 60)
    print("TEST 2: Iterative == Recursive")
    print("=" * 60)
    assert preorder_iter(root) == preorder(root)
    print(f"  Preorder iter: {preorder_iter(root)} ✅")
    assert inorder_iter(root) == inorder(root)
    print(f"  Inorder iter:  {inorder_iter(root)} ✅")
    print()

    print("=" * 60)
    print("TEST 3: Level-Order (BFS)")
    print("=" * 60)
    levels = level_order(root)
    print(f"  Levels: {levels}")
    assert levels == [[1], [2, 3], [4, 5, 6]]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 4: Edge Cases")
    print("=" * 60)
    assert preorder(None) == []
    print("  Empty tree → [] ✅")
    single = TreeNode(42)
    assert preorder(single) == [42]
    print("  Single node → [42] ✅")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it:")
    print("   1. Preorder: Root FIRST. Inorder: Root MIDDLE.")
    print("   2. Inorder of BST = sorted! Why?")
    print("   3. Iterative inorder is the trickiest — practice it!")
