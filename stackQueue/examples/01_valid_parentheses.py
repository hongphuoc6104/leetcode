"""
=============================================================
 Example 1: Valid Parentheses (LC 20)
=============================================================

THE classic Stack problem.
(Bài Stack KINH ĐIỂN.)

Strategy: Open bracket → push. Close bracket → pop and match.

Time:  O(n)
Space: O(n)
"""


def is_valid(s):
    """Check if parentheses are valid using stack."""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0


def is_valid_trace(s):
    """Valid parens with step trace."""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    print(f'  Input: "{s}"')

    for i, char in enumerate(s):
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                print(f"    [{i}] '{char}': ❌ Mismatch! "
                      f"stack={stack}")
                return False
            popped = stack.pop()
            print(f"    [{i}] '{char}': pop '{popped}' ✓ "
                  f"stack={stack}")
        else:
            stack.append(char)
            print(f"    [{i}] '{char}': push      "
                  f"stack={stack}")

    result = len(stack) == 0
    if not result:
        print(f"    ❌ Unmatched remaining: {stack}")
    return result


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Valid Parens — Trace")
    print("=" * 60)
    result = is_valid_trace("({[]})")
    assert result is True
    print(f"  Result: {result} ✅")
    print()

    result = is_valid_trace("([)]")
    assert result is False
    print(f"  Result: {result} ✅")
    print()

    print("=" * 60)
    print("TEST 2: More Cases")
    print("=" * 60)
    cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("((()))", True),
    ]
    for s, expected in cases:
        result = is_valid(s)
        status = "✅" if result == expected else "❌"
        print(f'  "{s}" → {result} {status}')
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it:")
    print("   1. What is the MAX stack size for a valid string?")
    print("   2. Can you solve this without a stack? (Hint: counter)")
    print("   3. What about nested: '((()))' vs interleaved: '()()()'?")
