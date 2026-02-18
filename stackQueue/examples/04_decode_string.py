"""
=============================================================
 Example 4: Decode String (LC 394)
=============================================================

Pattern: "k[encoded_string]" → repeat encoded_string k times.
Uses Stack to handle nested brackets.

Examples:
  "3[a]" → "aaa"
  "2[a3[b]]" → "abbbabbb"

Time:  O(output length)
Space: O(depth of nesting)
"""


def decode_string(s):
    """Stack-based decode."""
    stack = []
    curr_str = ""
    curr_num = 0

    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        elif c == '[':
            stack.append((curr_str, curr_num))
            curr_str = ""
            curr_num = 0
        elif c == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + curr_str * num
        else:
            curr_str += c

    return curr_str


def decode_trace(s):
    """Decode with step trace."""
    stack = []
    curr_str = ""
    curr_num = 0

    print(f'  Input: "{s}"')

    for i, c in enumerate(s):
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
            print(f'    [{i}] "{c}": num={curr_num}')
        elif c == '[':
            stack.append((curr_str, curr_num))
            print(f'    [{i}] "[": push ("{curr_str}", {curr_num}) '
                  f'stack_depth={len(stack)}')
            curr_str = ""
            curr_num = 0
        elif c == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + curr_str * num
            print(f'    [{i}] "]": pop, '
                  f'"{prev_str}" + "{curr_str}"×... '
                  f'→ "{curr_str}"')
        else:
            curr_str += c
            print(f'    [{i}] "{c}": curr="{curr_str}"')

    return curr_str


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Decode String — Trace")
    print("=" * 60)
    result = decode_trace("3[a2[c]]")
    assert result == "accaccacc"
    print(f'\n  Result: "{result}" ✅')
    print()

    print("=" * 60)
    print("TEST 2: More Cases")
    print("=" * 60)
    cases = [
        ("3[a]", "aaa"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc3[cd]xyz", "abccdcdcdxyz"),
        ("10[a]", "aaaaaaaaaa"),
    ]
    for s, expected in cases:
        result = decode_string(s)
        status = "✅" if result == expected else "❌"
        print(f'  "{s}" → "{result}" {status}')
    print()

    print("=" * 60)
    print("TEST 3: Nested Decoding — Trace")
    print("=" * 60)
    result = decode_trace("2[a3[b]]")
    assert result == "abbbabbb"
    print(f'\n  Result: "{result}" ✅')
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print('   1. "[" → save state to stack, reset')
    print('   2. "]" → pop state, build string')
    print("   3. Stack handles nesting naturally!")
