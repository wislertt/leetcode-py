class LogSystem:
    # Time: retrieve O(n), put O(1)
    # Space: O(n)
    def __init__(self) -> None:
        self.logs: list[tuple[int, str]] = []
        self.gran_len = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19,
        }

    def put(self, log_id: int, timestamp: str) -> None:
        self.logs.append((log_id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> list[int]:
        size = self.gran_len[granularity]
        lo = start[:size]
        hi = end[:size]
        return [log_id for log_id, ts in self.logs if lo <= ts[:size] <= hi]
