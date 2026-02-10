# 📖 Chủ đề 5: Linked List

## Lý thuyết cơ bản

**Linked List** là CTDL tuyến tính, mỗi node chứa giá trị và con trỏ đến node tiếp theo.

### Đặc điểm
- Thêm/xóa đầu: **O(1)**
- Thêm/xóa giữa (có pointer): **O(1)**
- Truy cập phần tử: **O(n)** (không random access)
- Tìm kiếm: **O(n)**

### Khai báo trong Python
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Dummy head pattern (rất hữu ích!)
dummy = ListNode(0)
dummy.next = head
# ... xử lý ...
return dummy.next
```

### Các kỹ thuật quan trọng
```python
# 1. Reverse Linked List
def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# 2. Fast & Slow (tìm giữa)
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# 3. Detect cycle
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

## Danh sách 30 bài LeetCode

### 🟢 Easy (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Merge Two Sorted Lists | [LC 21](https://leetcode.com/problems/merge-two-sorted-lists/) | Dummy head + merge |
| 2 | Remove Duplicates | [LC 83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | Skip duplicates |
| 3 | Linked List Cycle | [LC 141](https://leetcode.com/problems/linked-list-cycle/) | Fast & Slow |
| 4 | Intersection of Two Lists | [LC 160](https://leetcode.com/problems/intersection-of-two-linked-lists/) | Two pointers, switch head |
| 5 | Remove Elements | [LC 203](https://leetcode.com/problems/remove-linked-list-elements/) | Dummy head |
| 6 | Reverse Linked List | [LC 206](https://leetcode.com/problems/reverse-linked-list/) | Iterative hoặc recursive |
| 7 | Palindrome Linked List | [LC 234](https://leetcode.com/problems/palindrome-linked-list/) | Reverse nửa sau |
| 8 | Delete Node | [LC 237](https://leetcode.com/problems/delete-node-in-a-linked-list/) | Copy val từ next |
| 9 | Middle of List | [LC 876](https://leetcode.com/problems/middle-of-the-linked-list/) | Fast & Slow |
| 10 | Convert Binary to Int | [LC 1290](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) | Duyệt, shift bit |

### 🟡 Medium (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Add Two Numbers | [LC 2](https://leetcode.com/problems/add-two-numbers/) | Carry, dummy head |
| 2 | Remove Nth From End | [LC 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Two pointers, gap = n |
| 3 | Swap Nodes in Pairs | [LC 24](https://leetcode.com/problems/swap-nodes-in-pairs/) | Recursive hoặc iterative |
| 4 | Rotate List | [LC 61](https://leetcode.com/problems/rotate-list/) | Nối vòng, cắt |
| 5 | Remove Duplicates II | [LC 82](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | Dummy + skip all dups |
| 6 | Partition List | [LC 86](https://leetcode.com/problems/partition-list/) | 2 lists, merge |
| 7 | Reverse List II | [LC 92](https://leetcode.com/problems/reverse-linked-list-ii/) | Reverse đoạn [m,n] |
| 8 | Copy Random Pointer | [LC 138](https://leetcode.com/problems/copy-list-with-random-pointer/) | Hash map hoặc interleave |
| 9 | Cycle II | [LC 142](https://leetcode.com/problems/linked-list-cycle-ii/) | Floyd's algorithm |
| 10 | Sort List | [LC 148](https://leetcode.com/problems/sort-list/) | Merge sort O(n log n) |

### 🔴 Hard (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Merge k Sorted Lists | [LC 23](https://leetcode.com/problems/merge-k-sorted-lists/) | Heap hoặc divide & conquer |
| 2 | Reverse k-Group | [LC 25](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Reverse từng group k |
| 3 | LRU Cache | [LC 146](https://leetcode.com/problems/lru-cache/) | Hash map + doubly LL |
| 4 | Design Twitter | [LC 355](https://leetcode.com/problems/design-twitter/) | Hash map + heap |
| 5 | All O'one DS | [LC 432](https://leetcode.com/problems/all-oone-data-structure/) | Doubly LL + hash |
| 6 | LFU Cache | [LC 460](https://leetcode.com/problems/lfu-cache/) | Hash maps + doubly LL |
| 7 | Design Skiplist | [LC 1206](https://leetcode.com/problems/design-skiplist/) | Multi-level LL |
| 8 | Number of Ships | [LC 1274](https://leetcode.com/problems/number-of-ships-in-a-rectangle/) | Divide & conquer |
| 9 | Kth Smallest Sum | [LC 1439](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) | Heap + BFS |
| 10 | Double a Number | [LC 2816](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/) | Reverse, double, reverse |

---

## Tips
- **Dummy head** giải quyết edge cases khi head thay đổi
- **Fast & Slow** là pattern #1 cho Linked List
- Luôn vẽ hình trước khi code, đặc biệt với reverse và swap
