class Solution:
    # Time: O(n)
    # Space: O(n)
    def get_happy_string(self, n: int, k: int) -> str:
        total = 3 << (n - 1)
        if k > total:
            return ""
        k -= 1
        result: list[str] = []
        for i in range(n):
            block = 1 << (n - 1 - i)
            prev = result[-1] if result else ""
            candidates = [c for c in "abc" if c != prev]
            index, k = divmod(k, block)
            result.append(candidates[index])
        return "".join(result)
