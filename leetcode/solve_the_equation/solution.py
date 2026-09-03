class Solution:
    # Time: O(n)
    # Space: O(1)
    def solve_equation(self, equation: str) -> str:
        left, right = equation.split("=")
        x_left, c_left = self._parse(left)
        x_right, c_right = self._parse(right)

        x_coeff = x_left - x_right
        const = c_right - c_left
        if x_coeff == 0:
            return "Infinite solutions" if const == 0 else "No solution"
        assert const % x_coeff == 0
        return f"x={const // x_coeff}"

    def _parse(self, side: str) -> tuple[int, int]:
        coeff = 0
        const = 0
        sign = 1
        num: int | None = None
        for ch in side:
            if ch.isdigit():
                num = (num if num is not None else 0) * 10 + int(ch)
            elif ch == "x":
                coeff += sign * (num if num is not None else 1)
                num = None
            else:
                if num is not None:
                    const += sign * num
                    num = None
                sign = -1 if ch == "-" else 1
        if num is not None:
            const += sign * num
        return coeff, const
