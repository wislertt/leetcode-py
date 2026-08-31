class Solution:
    # Time: O(n)
    # Space: O(n)
    def parse_bool_expr(self, expression: str) -> bool:
        stack: list[str] = []
        for ch in expression:
            if ch == ",":
                continue
            if ch != ")":
                stack.append(ch)
                continue
            seen: list[bool] = []
            while stack[-1] in ("t", "f"):
                seen.append(stack.pop() == "t")
            stack.pop()
            op = stack.pop()
            if op == "!":
                stack.append("t" if not seen[0] else "f")
            elif op == "&":
                stack.append("t" if all(seen) else "f")
            else:
                stack.append("t" if any(seen) else "f")
        return stack[-1] == "t"
