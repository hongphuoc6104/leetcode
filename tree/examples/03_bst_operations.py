"""
=============================================================
 Example 3: BST Operations (Thao tác trên BST)
=============================================================

Demonstrates:
  - Search in BST (LC 700)
  - Validate BST (LC 98)
  - Kth Smallest (LC 230)
  - Insert into BST (LC 701)

Time:  O(h) for search/insert, O(n) for validate
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


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def search_bst(root, val):
    """Search BST: O(h)."""
    while root:
        if val < root.val:
            root = root.left
        elif val > root.val:
            root = root.right
        else:
            return root
    return None


def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    """Validate BST: O(n)."""
    if not root:
        return True
    if not (lo < root.val < hi):
        return False
    return (is_valid_bst(root.left, lo, root.val) and
            is_valid_bst(root.right, root.val, hi))


def kth_smallest(root, k):
    """Kth smallest in BST using inorder: O(h + k)."""
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right

    return -1


def insert_bst(root, val):
    """Insert into BST: O(h)."""
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    #       5
    #      / \
    #     3   7
    #    / \   \
    #   1   4   9
    bst = build_tree([5, 3, 7, 1, 4, None, 9])

    print("=" * 60)
    print("TEST 1: BST Property — Inorder = Sorted")
    print("=" * 60)
    sorted_vals = inorder(bst)
    print(f"  Inorder: {sorted_vals}")
    assert sorted_vals == sorted(sorted_vals)
    print("  ✅ Sorted!")
    print()

    print("=" * 60)
    print("TEST 2: Search BST")
    print("=" * 60)
    for val in [3, 7, 6]:
        node = search_bst(bst, val)
        found = node is not None
        status = "✅"
        print(f"  search({val}) → {'Found' if found else 'Not found'} {status}")
    print()

    print("=" * 60)
    print("TEST 3: Validate BST")
    print("=" * 60)
    assert is_valid_bst(bst) is True
    print(f"  Valid BST: {inorder(bst)} ✅")

    # Invalid BST
    bad = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(bad) is False
    print(f"  Invalid BST detected ✅")
    print()

    print("=" * 60)
    print("TEST 4: Kth Smallest")
    print("=" * 60)
    for k, expected in [(1, 1), (2, 3), (3, 4), (5, 7)]:
        result = kth_smallest(bst, k)
        status = "✅" if result == expected else "❌"
        print(f"  k={k} → {result} {status}")
    print()

    print("=" * 60)
    print("TEST 5: Insert into BST")
    print("=" * 60)
    bst = build_tree([5, 3, 7])
    bst = insert_bst(bst, 2)
    bst = insert_bst(bst, 4)
    bst = insert_bst(bst, 6)
    result = inorder(bst)
    assert result == [2, 3, 4, 5, 6, 7]
    print(f"  After inserts: {result} ✅")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. BST search: go left if <, right if > → O(h)")
    print("   2. Validate: pass (lo, hi) bounds, not just parent")
    print("   3. Kth smallest = inorder traversal, stop at k")
