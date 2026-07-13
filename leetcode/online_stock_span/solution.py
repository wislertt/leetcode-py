class StockSpanner:
    # Time: O(1) amortized per next call
    # Space: O(n)
    def __init__(self) -> None:
        # Monotonic decreasing stack of (price, span) pairs.
        self.stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
