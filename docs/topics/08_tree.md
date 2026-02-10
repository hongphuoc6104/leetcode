# 📖 Chủ đề 8: Tree (Binary Tree, BST)

## Lý thuyết cơ bản

**Binary Tree**: Mỗi node có tối đa 2 con. **BST**: Con trái < Node < Con phải.

### Duyệt cây
```python
# DFS - Preorder (Root → Left → Right)
def preorder(root):
    if not root: return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# DFS - Inorder (Left → Root → Right) → BST sorted!
def inorder(root):
    if not root: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# DFS - Postorder (Left → Right → Root)
def postorder(root):
    if not root: return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

# BFS - Level Order
from collections import deque
def level_order(root):
    if not root: return []
    queue = deque([root])
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

---

## Danh sách 30 bài LeetCode

### 🟢 Easy (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Inorder Traversal | [LC 94](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Recursive hoặc stack |
| 2 | Same Tree | [LC 100](https://leetcode.com/problems/same-tree/) | Recursive compare |
| 3 | Symmetric Tree | [LC 101](https://leetcode.com/problems/symmetric-tree/) | Mirror compare |
| 4 | Max Depth | [LC 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | DFS return height |
| 5 | Sorted Array to BST | [LC 108](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | Mid → root, recursion |
| 6 | Balanced Tree | [LC 110](https://leetcode.com/problems/balanced-binary-tree/) | DFS check height diff |
| 7 | Path Sum | [LC 112](https://leetcode.com/problems/path-sum/) | DFS, trừ dần target |
| 8 | Invert Tree | [LC 226](https://leetcode.com/problems/invert-binary-tree/) | Swap left/right |
| 9 | Diameter | [LC 543](https://leetcode.com/problems/diameter-of-binary-tree/) | Max(left+right) at each node |
| 10 | Subtree of Another | [LC 572](https://leetcode.com/problems/subtree-of-another-tree/) | DFS + same tree check |

### 🟡 Medium (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Validate BST | [LC 98](https://leetcode.com/problems/validate-binary-search-tree/) | Inorder hoặc range check |
| 2 | Level Order | [LC 102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | BFS |
| 3 | Construct from Pre+In | [LC 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Recursive build |
| 4 | Flatten to LL | [LC 114](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | Preorder, modify in-place |
| 5 | Right Side View | [LC 199](https://leetcode.com/problems/binary-tree-right-side-view/) | BFS, last of each level |
| 6 | Kth Smallest BST | [LC 230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Inorder, count k |
| 7 | LCA | [LC 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | DFS postorder |
| 8 | House Robber III | [LC 337](https://leetcode.com/problems/house-robber-iii/) | DFS + DP (rob/notRob) |
| 9 | Delete Node BST | [LC 450](https://leetcode.com/problems/delete-node-in-a-bst/) | Find successor/predecessor |
| 10 | Max Width | [LC 662](https://leetcode.com/problems/maximum-width-of-binary-tree/) | BFS + position index |

### 🔴 Hard (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Max Path Sum | [LC 124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | DFS, track global max |
| 2 | Postorder Traversal | [LC 145](https://leetcode.com/problems/binary-tree-postorder-traversal/) | Iterative with stack |
| 3 | Serialize/Deserialize | [LC 297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | BFS or preorder |
| 4 | Burst Balloons | [LC 312](https://leetcode.com/problems/burst-balloons/) | Interval DP |
| 5 | Binary Tree Cameras | [LC 968](https://leetcode.com/problems/binary-tree-cameras/) | Greedy DFS |
| 6 | Vertical Order | [LC 987](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | BFS + sort |
| 7 | Recover from Preorder | [LC 1028](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/) | Stack + parsing |
| 8 | Max Sum BST | [LC 1373](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/) | Postorder + validate |
| 9 | Reorder to Get Same BST | [LC 1569](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/) | Combinatorics + recursion |
| 10 | Longest Different Path | [LC 2246](https://leetcode.com/problems/longest-path-with-different-adjacent-characters/) | DFS on tree |

---

## Tips
- Hầu hết bài Tree giải bằng **recursion** (DFS)
- **Inorder** trên BST luôn cho kết quả **sorted**
- BFS dùng cho **level-order** problems
