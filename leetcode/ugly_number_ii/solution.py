class Solution:
    # Time: O(n)
    # Space: O(n)
    def nth_ugly_number(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        for i in range(1, n):
            next2, next3, next5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            nxt = min(next2, next3, next5)
            ugly[i] = nxt
            if nxt == next2:
                i2 += 1
            if nxt == next3:
                i3 += 1
            if nxt == next5:
                i5 += 1
        return ugly[n - 1]
