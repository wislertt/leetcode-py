class Solution:
    # Time: O(n * m log n) where n = len(logs), m = max log length
    # Space: O(n * m)
    def reorder_log_files(self, logs: list[str]) -> list[str]:
        letters: list[str] = []
        digits: list[str] = []
        for log in logs:
            rest = log.split(" ", 1)[1]
            if rest[0].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda log: (log.split(" ", 1)[1], log.split(" ", 1)[0]))
        return letters + digits
