from collections import deque

Poly = dict[tuple[str, ...], int]


class Solution:
    # Time: O(n * m) where n is the expression length and m the term count
    # Space: O(n + m)
    def basic_calculator_iv(
        self, expression: str, evalvars: list[str], evalints: list[int]
    ) -> list[str]:
        sub = dict(zip(evalvars, evalints, strict=True))
        tokens = deque(self._tokenize(expression))
        poly = self._expression(tokens, sub)
        return self._format(poly)

    @staticmethod
    def _tokenize(expression: str) -> list[str]:
        tokens: list[str] = []
        for chunk in expression.split(" "):
            opens = 0
            while chunk.startswith("("):
                opens += 1
                chunk = chunk[1:]
            closes = 0
            while chunk.endswith(")"):
                closes += 1
                chunk = chunk[:-1]
            tokens.extend(["("] * opens)
            if chunk:
                tokens.append(chunk)
            tokens.extend([")"] * closes)
        return tokens

    @staticmethod
    def _add(left: Poly, right: Poly, sign: int) -> Poly:
        result = dict(left)
        for term, coeff in right.items():
            updated = result.get(term, 0) + sign * coeff
            if updated:
                result[term] = updated
            else:
                result.pop(term, None)
        return result

    @staticmethod
    def _mul(left: Poly, right: Poly) -> Poly:
        result: Poly = {}
        for left_term, left_coeff in left.items():
            for right_term, right_coeff in right.items():
                term = tuple(sorted(left_term + right_term))
                result[term] = result.get(term, 0) + left_coeff * right_coeff
        return {term: coeff for term, coeff in result.items() if coeff}

    def _expression(self, tokens: deque[str], sub: dict[str, int]) -> Poly:
        poly = self._term(tokens, sub)
        while tokens and tokens[0] in ("+", "-"):
            sign = 1 if tokens.popleft() == "+" else -1
            poly = self._add(poly, self._term(tokens, sub), sign)
        return poly

    def _term(self, tokens: deque[str], sub: dict[str, int]) -> Poly:
        poly = self._factor(tokens, sub)
        while tokens and tokens[0] == "*":
            tokens.popleft()
            poly = self._mul(poly, self._factor(tokens, sub))
        return poly

    def _factor(self, tokens: deque[str], sub: dict[str, int]) -> Poly:
        token = tokens.popleft()
        if token == "(":
            poly = self._expression(tokens, sub)
            tokens.popleft()  # matching closing paren
            return poly
        if token.isdigit():
            return {(): int(token)} if int(token) else {}
        if token in sub:
            return {(): sub[token]} if sub[token] else {}
        return {(token,): 1}

    @staticmethod
    def _format(poly: Poly) -> list[str]:
        ordered = sorted(poly.items(), key=lambda item: (-len(item[0]), item[0]))
        return [str(coeff) + ("*" + "*".join(term) if term else "") for term, coeff in ordered]
