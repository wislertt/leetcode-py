class Solution:
    # Time: O(n), each token is consumed exactly once
    # Space: O(n), recursion depth plus scope frames
    def evaluate(self, expression: str) -> int:
        tokens = expression.replace("(", " ( ").replace(")", " ) ").split()

        def group_end(p: int) -> int:
            if tokens[p] != "(":
                return p + 1
            depth = 0
            while p < len(tokens):
                if tokens[p] == "(":
                    depth += 1
                elif tokens[p] == ")":
                    depth -= 1
                    if depth == 0:
                        return p + 1
                p += 1
            raise ValueError("unbalanced parentheses")

        def lookup(name: str, scope: list[dict[str, int]]) -> int:
            for frame in reversed(scope):
                if name in frame:
                    return frame[name]
            raise ValueError(f"unbound variable: {name}")

        def parse(p: int, scope: list[dict[str, int]]) -> tuple[int, int]:
            tok = tokens[p]
            if tok == "(":
                close = group_end(p) - 1
                keyword = tokens[p + 1]
                if keyword == "let":
                    scope.append({})
                    q = p + 2
                    while group_end(q) != close:
                        name = tokens[q]
                        value, q = parse(q + 1, scope)
                        scope[-1][name] = value
                    value, q = parse(q, scope)
                    scope.pop()
                    return value, close + 1
                a, q = parse(p + 2, scope)
                b, q = parse(q, scope)
                return (a + b if keyword == "add" else a * b), close + 1
            if tok == ")":
                raise ValueError("unexpected )")
            if tok[0].isdigit() or tok[0] == "-":
                return int(tok), p + 1
            return lookup(tok, scope), p + 1

        value, _ = parse(0, [])
        return value
