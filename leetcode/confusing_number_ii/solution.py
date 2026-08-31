class Solution:
    # Time: O(5^d) for d digits of n
    # Space: O(d)
    def confusing_number_ii(self, n: int) -> int:
        rotate = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]
        digits = str(n)

        def check(x: int) -> bool:
            y, t = 0, x
            while t:
                t, v = divmod(t, 10)
                y = y * 10 + rotate[v]
            return x != y

        def dfs(pos: int, bounded: bool, x: int) -> int:
            if pos == len(digits):
                return int(check(x))
            up = int(digits[pos]) if bounded else 9
            total = 0
            for i in range(up + 1):
                if rotate[i] != -1:
                    total += dfs(pos + 1, bounded and i == up, x * 10 + i)
            return total

        return dfs(0, True, 0)
