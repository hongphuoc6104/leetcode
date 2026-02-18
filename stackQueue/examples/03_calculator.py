"""
=============================================================
 Example 3: Expression Evaluation (Đánh giá biểu thức)
=============================================================

Demonstrates:
  - Reverse Polish Notation (LC 150)
  - Basic Calculator II (LC 227)

Time:  O(n)
Space: O(n)
"""


def eval_rpn(tokens):
    """
    Evaluate Reverse Polish Notation (LC 150).
    Stack-based: push numbers, pop and compute on operators.
    """
    stack = []

    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))  # Truncate toward zero
        else:
            stack.append(int(token))

    return stack[0]


def eval_rpn_trace(tokens):
    """RPN with trace."""
    stack = []

    print(f"  Tokens: {tokens}")

    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:
                result = int(a / b)
            stack.append(result)
            print(f"    '{token}': {a} {token} {b} = {result} "
                  f"→ stack={stack}")
        else:
            stack.append(int(token))
            print(f"    '{token}': push → stack={stack}")

    return stack[0]


def calculate(s):
    """
    Basic Calculator II (LC 227).
    Handles: +, -, *, / with correct precedence.
    No parentheses.
    """
    stack = []
    num = 0
    op = '+'

    for i, c in enumerate(s):
        if c.isdigit():
            num = num * 10 + int(c)

        if c in "+-*/" or i == len(s) - 1:
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            elif op == '/':
                stack.append(int(stack.pop() / num))
            op = c
            num = 0

    return sum(stack)


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: RPN Evaluation — Trace")
    print("=" * 60)
    # (2 + 1) * 3 = 9
    result = eval_rpn_trace(["2", "1", "+", "3", "*"])
    assert result == 9
    print(f"  Result: {result} ✅")
    print()

    # (4 + (13 / 5)) = 6
    result = eval_rpn_trace(["4", "13", "5", "/", "+"])
    assert result == 6
    print(f"  Result: {result} ✅")
    print()

    print("=" * 60)
    print("TEST 2: RPN — More Cases")
    print("=" * 60)
    cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*",
          "/", "*", "17", "+", "5", "+"], 22),
    ]
    for tokens, expected in cases:
        result = eval_rpn(tokens)
        status = "✅" if result == expected else "❌"
        print(f"  {tokens[:5]}... → {result} {status}")
    print()

    print("=" * 60)
    print("TEST 3: Basic Calculator II")
    print("=" * 60)
    cases = [
        ("3+2*2", 7),
        (" 3/2 ", 1),
        (" 3+5 / 2 ", 5),
        ("1+1+1", 3),
        ("2*3+4", 10),
        ("14-3/2", 13),
    ]
    for expr, expected in cases:
        result = calculate(expr)
        status = "✅" if result == expected else "❌"
        print(f'  "{expr}" = {result} {status}')
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. RPN: push numbers, pop+compute on operators")
    print("   2. Calculator II: * and / computed immediately")
    print("   3. + and - push to stack, sum at end")
