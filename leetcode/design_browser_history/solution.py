class BrowserHistory:
    # Time: __init__ O(1), visit O(n), back O(steps), forward O(steps)
    # Space: O(n)
    def __init__(self, homepage: str) -> None:
        self.history: list[str] = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        del self.history[self.cur + 1 :]
        self.history.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(len(self.history) - 1, self.cur + steps)
        return self.history[self.cur]
