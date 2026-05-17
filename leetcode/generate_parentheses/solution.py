class Solution:
    # Time: O(4^n / sqrt(n))
    # Space: O(4^n / sqrt(n))
    def generate_parenthesis(self, n: int) -> list[str]:
        result: list[str] = []

        def backtrack(s: str, open_count: int, close_count: int) -> None:
            if len(s) == 2 * n:
                result.append(s)
                return
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
