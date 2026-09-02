class Logger:
    # Time: O(1) per call
    # Space: O(m) for m distinct messages
    def __init__(self) -> None:
        self.ok_until: dict[str, int] = {}

    def should_print_message(self, timestamp: int, message: str) -> bool:
        if timestamp < self.ok_until.get(message, 0):
            return False
        self.ok_until[message] = timestamp + 10
        return True
