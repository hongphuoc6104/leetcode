# 📖 Chapter 3: Complexity Analysis

## 1. Traversal: Always O(n)

Every traversal (DFS or BFS) visits each node **exactly once** → O(n) time. This is true for ALL traversal orders: preorder, inorder, postorder, level-order.

---

## 2. BST Operations: O(h) — Height Matters!

| Tree Shape | Height h | Search/Insert/Delete |
|-----------|----------|---------------------|
| **Balanced** (AVL, Red-Black) | O(log n) | **O(log n)** ← ideal! |
| **Skewed** (like a linked list) | O(n) | O(n) ← worst case |

```
Balanced BST (h = log n):        Skewed BST (h = n):
        4                         1
       / \                         \
      2   6                         2
     / \ / \                         \
    1  3 5  7                         3
                                       \
                                        4
```

> 🤔 **Why is balanced important?** A BST with n=1000 nodes: 
> balanced → h=10 operations. Skewed → h=1000 operations!

---

## 3. Space Complexity (Độ phức tạp không gian)

| Algorithm | Space | Explanation |
|-----------|-------|------------|
| DFS recursive | **O(h)** | Call stack depth = tree height |
| DFS iterative | **O(h)** | Explicit stack stores ancestors |
| BFS | **O(w)** | Queue stores one level; w = max width |
| Balanced tree BFS | O(n/2) ≈ **O(n)** | Last level has ~n/2 nodes |

### Worst Cases
- **DFS on skewed tree**: O(n) stack depth (effectively a linked list)
- **BFS on perfect tree**: O(n/2) queue size (last level)

---

## 4. Operations Complexity Summary

| Operation | BST (balanced) | BST (worst) | General BT |
|-----------|---------------|-------------|-----------|
| Search | O(log n) | O(n) | O(n) |
| Insert | O(log n) | O(n) | O(n)* |
| Delete | O(log n) | O(n) | O(n) |
| Min/Max | O(log n) | O(n) | O(n) |
| Inorder | O(n) | O(n) | O(n) |
| Height | O(n) | O(n) | O(n) |

\* General binary tree: insert depends on where

---

## 5. Common Mistakes (Lỗi thường gặp)

### Not handling None ⚠️
```python
# ❌ WRONG — crashes on empty tree!
def depth(root):
    return 1 + max(depth(root.left), depth(root.right))

# ✅ CORRECT — base case first!
def depth(root):
    if not root: return 0
    return 1 + max(depth(root.left), depth(root.right))
```

### BST validation with wrong bounds ⚠️
```python
# ❌ WRONG — only checks parent-child, misses grandparent violations!
#           5
#          / \
#         1   6
#            / \
#           3   7    ← 3 < 5 but passes this check!
def is_bst(node):
    if not node: return True
    if node.left and node.left.val >= node.val: return False
    if node.right and node.right.val <= node.val: return False
    return is_bst(node.left) and is_bst(node.right)

# ✅ CORRECT — passes bounds through entire subtree
def is_bst(node, lo=float('-inf'), hi=float('inf')):
    if not node: return True
    if not (lo < node.val < hi): return False
    return (is_bst(node.left, lo, node.val) and
            is_bst(node.right, node.val, hi))
```

### Confusing depth vs height ⚠️
```
Depth = distance from ROOT to node (top → down)
Height = distance from node to LEAF (bottom → up)

       1          depth=0, height=2
      / \
     2   3        depth=1, height=1
    /
   4              depth=2, height=0 (leaf)
```

---

## 6. Constraint Guide (Hướng dẫn từ constraints)

| Constraint | Approach | Expected Time |
|-----------|----------|--------------|
| n ≤ 100 | Any approach | O(n²) OK |
| n ≤ 10⁴ | DFS/BFS | O(n log n) or O(n) |
| n ≤ 10⁵ | Single-pass DFS/BFS | O(n) |
| "BST" mentioned | Use BST property | O(h) per query |

---

## ❓ Self-Check Questions

1. **What's the max stack depth for DFS on a balanced tree of 1 million nodes?** (log₂(10⁶) ≈ ?)
2. **BFS on a complete binary tree: what's the max queue size?** (max hàng đợi?)
3. **Can we improve O(n) search in a general binary tree?** How? (Cải thiện O(n) tìm kiếm?)
4. **Why is iterative inorder harder than iterative preorder?** (Tại sao inorder khó hơn preorder?)

---

**← Previous:** [Chapter 2: Patterns](./02_patterns.md)  
**Next →** [Chapter 4: Templates](./04_python_templates.md)
