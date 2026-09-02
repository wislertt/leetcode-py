class Solution:
    # Time: O(4^n / sqrt(n)) operator placements, each O(n) to extend
    # Space: O(n) recursion depth plus the output
    def add_operators(self, num: str, target: int) -> list[str]:
        results: list[str] = []
        n = len(num)

        def backtrack(index: int, expr: list[str], value: int, prev_operand: int) -> None:
            if index == n:
                if value == target:
                    results.append("".join(expr))
                return

            for end in range(index + 1, n + 1):
                operand_str = num[index:end]
                # Reject operands with leading zeros ("05", "00"), allow plain "0"
                if len(operand_str) > 1 and operand_str[0] == "0":
                    break
                operand = int(operand_str)

                if index == 0:
                    expr.append(operand_str)
                    backtrack(end, expr, operand, operand)
                    expr.pop()
                    continue

                expr.append("+")
                expr.append(operand_str)
                backtrack(end, expr, value + operand, operand)
                expr.pop()
                expr.pop()

                expr.append("-")
                expr.append(operand_str)
                backtrack(end, expr, value - operand, -operand)
                expr.pop()
                expr.pop()

                multiplied = prev_operand * operand
                expr.append("*")
                expr.append(operand_str)
                backtrack(end, expr, value - prev_operand + multiplied, multiplied)
                expr.pop()
                expr.pop()

        backtrack(0, [], 0, 0)
        return results
