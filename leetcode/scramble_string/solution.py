class Solution:
    # Time: O(n^4) substring pairs times O(n) split points, memoized
    # Space: O(n^2) memo entries over substring pairs

    def is_scramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        memo: dict[tuple[str, str], bool] = {}
        return self.solve(s1, s2, memo)

    def solve(self, s1: str, s2: str, memo: dict[tuple[str, str], bool]) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        key = (s1, s2)
        cached = memo.get(key)
        if cached is not None:
            return cached
        n = len(s1)
        result = False
        for i in range(1, n):
            if self.solve(s1[:i], s2[:i], memo) and self.solve(s1[i:], s2[i:], memo):
                result = True
                break
            if self.solve(s1[:i], s2[n - i :], memo) and self.solve(s1[i:], s2[: n - i], memo):
                result = True
                break
        memo[key] = result
        return result
