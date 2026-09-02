class Solution:
    # Time: O(log^2 n) -- ~60 digit counts, each a binary search over bases
    # Space: O(1)
    def smallest_good_base(self, n: str) -> str:
        num = int(n)
        for m in range(num.bit_length(), 1, -1):
            # candidates for base k with m+1 digits of 1: k ~ num^(1/m)
            lo, hi = 2, round(num ** (1.0 / m)) + 2
            while lo < hi:
                mid = (lo + hi) // 2
                total, power = 0, 1
                overflow = False
                for _ in range(m + 1):
                    total += power
                    if total > num:
                        overflow = True
                        break
                    power *= mid
                if overflow:
                    hi = mid
                elif total == num:
                    return str(mid)
                else:
                    lo = mid + 1
        return str(num - 1)
