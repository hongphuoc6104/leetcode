# 📖 Chapter 1: Introduction to Trees

## 1. What is a Tree? (Cây là gì?)

A tree is a **hierarchical, non-linear** data structure with **nodes** connected by **edges**. Unlike arrays and linked lists (linear), trees branch out — perfect for modeling hierarchical data like file systems, HTML DOM, and organizational charts.

> 🤔 **Socratic Question:** Why can't an array represent a file system well? What advantages does a tree have?

```
        1          ← Root (Gốc) — the topmost node
       / \
      2   3        ← Internal nodes (children of root)
     / \   \
    4   5   6      ← Leaf nodes (Lá) — no children
```

### Binary Tree Node — Python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left      # Left child (con trái)
        self.right = right    # Right child (con phải)
```

**Analogy (Ví dụ):** Think of a family tree — the root is the oldest ancestor. Each person has at most 2 children. You can trace any path from ancestor to descendant.

---

## 2. Key Terminology (Thuật ngữ quan trọng)

| Term | Vietnamese | Definition |
|------|-----------|-----------|
| **Root** | Gốc | Top node, no parent |
| **Leaf** | Lá | Node with no children |
| **Depth** | Độ sâu | Distance from root to this node |
| **Height** | Chiều cao | Longest path from this node to a leaf |
| **Subtree** | Cây con | A node and all its descendants |
| **Parent** | Cha | Node directly above |
| **Sibling** | Anh em | Nodes with same parent |
| **BST** | Cây tìm kiếm nhị phân | Left < Root < Right for ALL nodes |
| **Complete** | Cây đầy đủ | All levels filled except possibly last |
| **Balanced** | Cây cân bằng | Height difference between L/R ≤ 1 |

### Tree Properties
- A tree with **n nodes** has exactly **n-1 edges** (Cây n node có n-1 cạnh)
- There is exactly **one path** between any two nodes
- **Binary tree**: each node has at most 2 children
- **Max nodes at level k**: 2^k (level 0 = root)
- **Max nodes in tree of height h**: 2^(h+1) - 1

---

## 3. Types of Binary Trees (Các loại cây nhị phân)

```
Full Binary Tree:        Complete Binary Tree:    Perfect Binary Tree:
Every node has 0          All levels full           Full + Complete
or 2 children             except last (left-fill)

      1                       1                       1
     / \                    / \                    / \
    2   3                  2   3                  2   3
   / \                    / \ /                  / \ / \
  4   5                  4  5 6                 4  5 6  7
```

### BST (Binary Search Tree) — Key Property

```
        8
       / \
      3   10
     / \    \
    1   6   14
   
For EVERY node:
  - ALL nodes in left subtree < current node
  - ALL nodes in right subtree > current node
  
Inorder traversal = SORTED: [1, 3, 6, 8, 10, 14]
```

> 🤔 Why does inorder traversal of BST give sorted output? 
> (Tại sao duyệt inorder BST cho kết quả sorted?)

---

## 4. Tree Traversals (Duyệt cây) — THE Core Skill

### DFS — Depth First Search (Tìm kiếm theo chiều sâu)

There are 3 DFS orders. The name tells you WHEN to visit the ROOT:

```
        1
       / \
      2   3
     / \
    4   5

Preorder  (Root FIRST):  1, 2, 4, 5, 3    ← "Visit, go left, go right"
Inorder   (Root MIDDLE): 4, 2, 5, 1, 3    ← "Go left, visit, go right"
Postorder (Root LAST):   4, 5, 2, 3, 1    ← "Go left, go right, visit"
```

**Memory trick (Mẹo nhớ):**
- **Pre**order = root **Pre**cedes children
- **In**order = root **In** between children
- **Post**order = root after (**Post**) children

### BFS — Breadth First Search (Tìm kiếm theo chiều rộng)

```
Level-order: visit level by level, left to right
Result: [[1], [2, 3], [4, 5]]
```

Uses a **Queue** — process nodes layer by layer.

---

## 5. The Recursive Pattern — Master This!

Almost ALL tree problems follow this template (Hầu hết bài cây theo mẫu này):

```python
def solve(node):
    # Base case: empty tree
    if not node:
        return base_case
    
    # Recursive step: solve left and right subtrees
    left_result = solve(node.left)
    right_result = solve(node.right)
    
    # Combine results
    return combine(node.val, left_result, right_result)
```

### Examples of this pattern:
```python
# Max depth
def max_depth(node):
    if not node: return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))

# Count nodes
def count(node):
    if not node: return 0
    return 1 + count(node.left) + count(node.right)

# Sum of all values
def tree_sum(node):
    if not node: return 0
    return node.val + tree_sum(node.left) + tree_sum(node.right)
```

> 🤔 Can you write `is_same_tree(p, q)` using this pattern?

---

## 6. When to Use DFS vs BFS?

| Use Case | Choose | Why |
|----------|--------|-----|
| Max depth, path sum | **DFS** | Need to reach leaves |
| Level-order output | **BFS** | Process level by level |
| Validate BST | **DFS (Inorder)** | Inorder gives sorted seq |
| Shortest path in tree | **BFS** | Level = distance from root |
| Serialize/deserialize | Either | BFS is more intuitive |

---

## ❓ Self-Check Questions

1. **What's the difference between Depth and Height?** (Depth: top→node, Height: node→leaf)
2. **Inorder traversal of a BST gives what?** (Duyệt inorder BST cho gì?)
3. **A tree with n nodes has how many edges?** (n node → bao nhiêu edge?)
4. **What's the max height of a binary tree with 7 nodes?** Min height?
5. **Can a tree have cycles?** What would that be called? (Cây có vòng lặp không?)

---

**Next →** [Chapter 2: Patterns](./02_patterns.md)
