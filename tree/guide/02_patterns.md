# 📖 Chapter 2: Tree Patterns

Five patterns that cover 90% of tree problems in interviews (5 pattern bao phủ 90% bài cây trong phỏng vấn).

---

## Pattern 1: DFS Recursive — The Foundation

### 🔍 Signal (Dấu hiệu)
- "max depth", "min depth", "same tree", "symmetric", "invert"
- ANY problem asking about properties of the whole tree

### 💡 Key Insight
Trees are recursive by nature: a tree = root + left subtree + right subtree. So most solutions are recursive too!

### 💻 Code — Max Depth (LC 104)
```python
def max_depth(root):
    if not root:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return 1 + max(left, right)
```

### 💻 Code — Is Same Tree (LC 100)
```python
def is_same(p, q):
    if not p and not q: return True
    if not p or not q: return False
    return (p.val == q.val and
            is_same(p.left, q.left) and
            is_same(p.right, q.right))
```

### 💻 Code — Invert Tree (LC 226)
```python
def invert(root):
    if not root: return None
    root.left, root.right = invert(root.right), invert(root.left)
    return root
```

### 📌 Related: LC 104, LC 100, LC 101, LC 226, LC 110, LC 543

---

## Pattern 2: BFS Level-Order — Queue-based

### 🔍 Signal
- "level order", "zigzag", "right side view", "average of levels"
- Anything requiring **level-by-level** processing

### 💡 Key Insight
Use a Queue. Process all nodes at current level before moving to next. `len(queue)` gives the size of each level.

### 💻 Code — Level Order (LC 102)
```python
from collections import deque

def level_order(root):
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):   # Process ENTIRE level
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

### 💻 Code — Right Side View (LC 199)
```python
def right_side_view(root):
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(node.val)  # Last node of each level!
    return result
```

### 📌 Related: LC 102, LC 103, LC 199, LC 637, LC 515

---

## Pattern 3: BST Operations — Use the Property!

### 🔍 Signal
- "BST", "validate BST", "search in BST", "kth smallest", "successor"

### 💡 Key Insight
BST property: `left < root < right`. This means:
- Search is O(h) — go left or right based on comparison
- Inorder = sorted sequence → kth smallest = kth in inorder
- Validate by passing (lower_bound, upper_bound) down

### 💻 Code — Search BST (LC 700)
```python
def search_bst(root, val):
    while root:
        if val < root.val:
            root = root.left
        elif val > root.val:
            root = root.right
        else:
            return root
    return None
```

### 💻 Code — Validate BST (LC 98)
```python
def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    if not root: return True
    if not (lo < root.val < hi):
        return False
    return (is_valid_bst(root.left, lo, root.val) and
            is_valid_bst(root.right, root.val, hi))
```

> ⚠️ **Common Bug (Lỗi thường gặp):** Only checking parent-child relationship is WRONG! Must check entire subtree range. See complexity guide for details.

### 💻 Code — Kth Smallest (LC 230)
```python
def kth_smallest(root, k):
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
```

### 📌 Related: LC 700, LC 98, LC 701, LC 450, LC 230, LC 235

---

## Pattern 4: Path Problems — Track State Down the Tree

### 🔍 Signal
- "path sum", "root-to-leaf", "max path sum", "diameter"
- Problems that track a **running total** or **running state**

### 💡 Key Insight
Two types of paths:
1. **Root-to-leaf**: pass remaining target down
2. **Any-to-any**: use each node as potential "turning point"

### 💻 Code — Path Sum (LC 112)
```python
def has_path_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right:  # Leaf!
        return root.val == target
    target -= root.val
    return (has_path_sum(root.left, target) or
            has_path_sum(root.right, target))
```

### 💻 Code — Diameter (LC 543)
```python
def diameter(root):
    best = [0]
    def depth(node):
        if not node: return 0
        L = depth(node.left)
        R = depth(node.right)
        best[0] = max(best[0], L + R)  # Path through this node
        return 1 + max(L, R)
    depth(root)
    return best[0]
```

### 💻 Code — Max Path Sum (LC 124, Hard)
```python
def max_path_sum(root):
    best = [float('-inf')]
    def helper(node):
        if not node: return 0
        L = max(helper(node.left), 0)    # Ignore negative paths!
        R = max(helper(node.right), 0)
        best[0] = max(best[0], L + R + node.val)
        return max(L, R) + node.val
    helper(root)
    return best[0]
```

### 📌 Related: LC 112, LC 113, LC 124, LC 543, LC 257, LC 129

---

## Pattern 5: Tree Construction & Transformation

### 🔍 Signal
- "construct tree from traversals", "serialize/deserialize", "flatten"

### 💡 Key Insight
- Preorder first element = root
- Find root in inorder → split into left/right subtrees
- Recursively build subtrees

### 💻 Code — Build from Preorder + Inorder (LC 105)
```python
def build_tree(preorder, inorder):
    if not inorder:
        return None
    root_val = preorder.pop(0)
    root = TreeNode(root_val)
    mid = inorder.index(root_val)
    root.left = build_tree(preorder, inorder[:mid])
    root.right = build_tree(preorder, inorder[mid+1:])
    return root
```

### 💻 Code — LCA (LC 236) — Lowest Common Ancestor
```python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root       # p and q on different sides!
    return left or right  # Both on same side
```

### 📌 Related: LC 105, LC 106, LC 297, LC 236, LC 114

---

## 📊 Pattern Decision Table

| Signal | Pattern | Key Template |
|--------|---------|-------------|
| "depth/height/count" | DFS Recursive | `1 + max(left, right)` |
| "level-by-level" | BFS Queue | `for _ in range(len(queue))` |
| "BST search/validate" | BST Property | Go left/right by comparison |
| "path sum/diameter" | Path Tracking | Pass state or use nonlocal |
| "construct from arrays" | Construction | Find root, split, recurse |

---

## ❓ Self-Check Questions

1. **When would you use BFS over DFS for a tree problem?** Give 2 examples. (Khi nào dùng BFS thay DFS?)
2. **"Max depth" uses DFS. Can you also solve it with BFS?** How? (Giải max depth bằng BFS?)
3. **In LCA, why does `root == p` return `root` immediately?**
4. **Diameter doesn't need to pass through root.** How does the algorithm handle this?

---

**← Previous:** [Chapter 1: Introduction](./01_introduction.md)  
**Next →** [Chapter 3: Complexity](./03_complexity.md)
