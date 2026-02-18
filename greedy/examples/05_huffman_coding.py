"""
=============================================================
 Example 5: Huffman Coding (Concept)
=============================================================

Build a Huffman Tree using a Min-Heap.
Combined frequencies are pushed back. Smallest always merged first.

Time:  O(n log n)
"""
import heapq
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Less-than for heap comparison
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    if not text:
        return None
    counts = Counter(text)
    heap = [Node(char, freq) for char, freq in counts.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Pop two smallest
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Merge
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]  # Root


def generate_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
    if not node:
        return
    if node.char is not None:
        code_map[node.char] = prefix
    else:
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)
    return code_map


if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Huffman Coding")
    print("=" * 60)
    text = "this is an example for huffman encoding"
    print(f"  Text: {text}")

    root = build_huffman_tree(text)
    code_map = {}
    generate_codes(root, "", code_map)

    print("  Codes:")
    for char, code in sorted(code_map.items()):
        print(f"    '{char}': {code}")

    # Validation: frequent chars should have shorter codes
    # ' ' (space) is very frequent, usually 2-3 bits
    space_len = len(code_map.get(' ', '000000'))
    f_len = len(code_map.get('f', '0'))

    print(f"  Space length: {space_len}, 'f' length: {f_len}")
    
    # Simple check: tree built correctly
    assert root.freq == len(text)
    print("  ✅ Root frequency matches total length!")
    print()
    
    print("✅ All tests passed!")
