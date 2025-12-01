class Solution:
    # Time: O(N * 2^N)
    # Space: O(N)
    def partition(self, s: str) -> list[list[str]]:
        result: list[list[str]] = []
        self._backtrack(s, 0, [], result)
        return result

    def _backtrack(self, s: str, start: int, path: list[str], result: list[list[str]]) -> None:
        if start == len(s):
            result.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if self._is_palindrome(substring):
                path.append(substring)
                self._backtrack(s, end, path, result)
                path.pop()

    def _is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
