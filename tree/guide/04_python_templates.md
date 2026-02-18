# 📖 Chapter 4: Python Templates

Copy-paste these templates and adapt. Each one solves a category of problems.
(Copy-paste các template này và chỉnh sửa. Mỗi template giải quyết một nhóm bài.)

---

## Template 1: DFS Recursive — The Universal Pattern

```python
def dfs(root):
    """Most tree problems follow this pattern."""
    if not root:
        return base_case   # 0, True, [], None...
    
    left = dfs(root.left)
    right = dfs(root.right)
    
    return combine(root.val, left, right)
```

### Variants:
```python
# Max depth: combine = 1 + max(left, right), base = 0
# Count nodes: combine = 1 + left + right, base = 0
# Sum values: combine = val + left + right, base = 0
# Is same: combine = val_match and left and right, base = True
```

---

## Template 2: DFS Iterative — Preorder (Stack)

```python
def preorder_iterative(root):
    """Root → Left → Right using explicit stack."""
    if not root:
        return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)
        # Push RIGHT first so LEFT is popped first!
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
```

---

## Template 3: DFS Iterative — Inorder (Stack + Pointer)

```python
def inorder_iterative(root):
    """Left → Root → Right — the trickiest iterative traversal."""
    stack, result = [], []
    curr = root
    while curr or stack:
        # Go as far left as possible
        while curr:
            stack.append(curr)
            curr = curr.left
        # Process node
        curr = stack.pop()
        result.append(curr.val)
        # Move to right subtree
        curr = curr.right
    return result
```

> 💡 **Tip:** Inorder iterative is the hardest to memorize. Practice it!

---

## Template 4: BFS Level-Order (Queue)

```python
from collections import deque

def level_order(root):
    """Process tree level by level using queue."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):  # Process entire level
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

---

## Template 5: BST Search (Iterative)

```python
def search_bst(root, target):
    """O(h) search — go left or right based on comparison."""
    while root:
        if target < root.val:
            root = root.left
        elif target > root.val:
            root = root.right
        else:
            return root  # Found!
    return None  # Not found
```

---

## Template 6: Validate BST (Recursive bounds)

```python
def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    """Pass bounds down to check entire subtree range."""
    if not root:
        return True
    if not (lo < root.val < hi):
        return False
    return (is_valid_bst(root.left, lo, root.val) and
            is_valid_bst(root.right, root.val, hi))
```

---

## Template 7: LCA — Lowest Common Ancestor

```python
def lca(root, p, q):
    """Find lowest common ancestor of p and q."""
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root       # p, q on different sides → root is LCA
    return left or right  # Both on same side
```

---

## Template 8: Path Sum — Track State

```python
def has_path_sum(root, target):
    """Check if root-to-leaf path equals target."""
    if not root:
        return False
    if not root.left and not root.right:  # Leaf check!
        return root.val == target
    target -= root.val
    return (has_path_sum(root.left, target) or
            has_path_sum(root.right, target))
```

---

## Utility: Build Tree from Level-Order List

```python
from collections import deque

def build_tree(values):
    """Build tree from list like [1, 2, 3, None, 4].
    None = no node at that position."""
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
```

---

## 📋 Pre-Coding Checklist (Kiểm tra trước khi code)

1. ✅ **Base case?** `if not root: return ...`
2. ✅ **Leaf check needed?** `if not root.left and not root.right`
3. ✅ **DFS or BFS?** Depth-related → DFS. Level-related → BFS.
4. ✅ **BST property?** Can I eliminate half the tree?
5. ✅ **Need global state?** Use `nonlocal` or list `[var]`
6. ✅ **Return value?** What does each recursive call return?

---

**← Previous:** [Chapter 3: Complexity](./03_complexity.md)  
**Next →** [Examples](../examples/) 🚀
