class Solution:
    # Time: O(log(x, bound) * log(y, bound))
    # Space: O(log(x, bound) * log(y, bound))
    def powerful_integers(self, x: int, y: int, bound: int) -> list[int]:
        def powers(base: int) -> list[int]:
            if base == 1:
                return [1] if bound >= 1 else []
            vals: list[int] = []
            val = 1
            while val <= bound:
                vals.append(val)
                val *= base
            return vals

        found: set[int] = set()
        for xi in powers(x):
            for yj in powers(y):
                total = xi + yj
                if total <= bound:
                    found.add(total)
        return list(found)
