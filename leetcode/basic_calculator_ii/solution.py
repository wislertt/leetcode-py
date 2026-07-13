class Solution:
    # Time: O(n) — single pass
    # Space: O(n) — stack of operands
    def calculate(self, s: str) -> int:
        stack: list[int] = []
        current = 0
        op = "+"

        def apply(value: int) -> None:
            nonlocal stack
            if op == "+":
                stack.append(value)
            elif op == "-":
                stack.append(-value)
            elif op == "*":
                stack.append(stack.pop() * value)
            else:  # "/"
                prev = stack.pop()
                # Truncate toward zero
                stack.append(int(prev / value))

        for ch in s:
            if ch.isdigit():
                current = current * 10 + int(ch)
            elif ch in "+-*/":
                apply(current)
                op = ch
                current = 0

        apply(current)  # last operand
        return sum(stack)
