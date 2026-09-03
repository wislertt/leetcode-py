class Solution:
    # Time: O(24 * 60 * 4) = O(1)
    # Space: O(1)
    def next_closest_time(self, time: str) -> str:
        allowed = {c for c in time if c != ":"}
        current = int(time[:2]) * 60 + int(time[3:])
        while True:
            current = (current + 1) % (24 * 60)
            candidate = f"{current // 60:02d}:{current % 60:02d}"
            if all(c in allowed for c in candidate if c != ":"):
                return candidate
