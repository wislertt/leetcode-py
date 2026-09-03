class Solution:
    # Time: O(log_x(target)^2 * x)
    # Space: O(log_x(target))
    def least_ops_express_target(self, x: int, target: int) -> int:
        # An expression is a signed sum of blocks, where a block is a power x^k
        # written as x * x * ... * x (k-1 inner operators, k >= 1) or x / x for 1
        # (1 inner operator). Each block after the first also costs its leading +/-.
        # Counting that leading operator in the block cost gives cost(k) = k for
        # k >= 1 and cost(0) = 2, and the answer is the minimum total cost minus 1.
        # Choosing a_i copies (negative for subtraction) of each x^i means
        # sum(a_i * x^i) == target, so a_i is fixed modulo x by the remainder:
        # walk the base-x digits keeping the cheapest carry per position.
        costs: dict[tuple[int, int], int] = {(0, target): 0}
        while costs:
            (exp, remaining), total = min(costs.items(), key=lambda item: item[1])
            del costs[(exp, remaining)]
            if remaining == 0:
                return total - 1
            digit = remaining % x
            block_cost = 2 if exp == 0 else exp
            for offset in range(-3, 4):
                # Carry up to 2 units into the next digit, in either direction.
                amount = digit + offset * x
                key = (exp + 1, (remaining - amount) // x)
                candidate = total + abs(amount) * block_cost
                if key not in costs or candidate < costs[key]:
                    costs[key] = candidate
        raise ValueError("unreachable")
