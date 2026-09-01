class Solution:
    # Time: O(n + m)
    # Space: O(n)
    def shifting_letters(self, s: str, shifts: list[list[int]]) -> str:
        diff = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            offset = 1 if direction == 1 else -1
            diff[start] += offset
            diff[end + 1] -= offset

        result: list[str] = []
        running = 0
        for i, char in enumerate(s):
            running += diff[i]
            result.append(chr((ord(char) - ord("a") + running) % 26 + ord("a")))
        return "".join(result)
