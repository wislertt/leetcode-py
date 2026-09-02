class Solution:
    # Time: O(n)
    # Space: O(n)
    def maximum_gain(self, s: str, x: int, y: int) -> int:
        hi_first, hi_second, hi = "a", "b", x
        lo_first, lo_second, lo = "b", "a", y
        if x < y:
            hi_first, hi_second, hi = "b", "a", y
            lo_first, lo_second, lo = "a", "b", x

        total = 0
        stack: list[str] = []
        for ch in s:
            if stack and stack[-1] == hi_first and ch == hi_second:
                stack.pop()
                total += hi
            else:
                stack.append(ch)

        leftover: list[str] = []
        for ch in stack:
            if leftover and leftover[-1] == lo_first and ch == lo_second:
                leftover.pop()
                total += lo
            else:
                leftover.append(ch)
        return total
